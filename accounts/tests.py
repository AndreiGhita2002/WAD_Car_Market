import os
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from cars.models import Car
from accounts.models import UserProfile

# Create your tests here.
#This is test for register and its view
class RegisterFormTest(TestCase):

    #This is all the invalid form response

    #Test to see if form is invalid as the password wasnt given
    def test_sign_up_raises_error_not_given_password(self):

        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("This field is required." in str(test.content), "Error message not found in the response!")

    #Test to see if form is invalid if wrong format email is given
    def test_sign_up_raises_error_not_given_email(self):

        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'testgmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("Enter a valid email address." in str(test.content), "Error message not found in the response!")

    #Test to see if form is invalid if the 2 password dont match
    def test_sign_up_raises_error_not_matching_password(self):

        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat1234', 'password2':'sat123'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("The two password fields dont match." in str(test.content), "Error message not found in the response!")

     #Test to see if form is invalid if username is not unique
    
    #Test to see if username is not unique
    def test_sign_up_raises_error_username_exist(self):
        user = User.objects.create_user(username='user', password='12345')

        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("A user with that username already exists." in str(test.content), "Error message not found in the response!")

    #Test to see if form is invalid if email is not unique
    def test_sign_up_raises_error_email_exist(self):
        user = User.objects.create_user(username='testuser', password='12345', email="test27@gmail.com")

        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("User with this Email address already exists." in str(test.content), "Error message not found in the response!")


    #This is all the valid form response

    #Check if the username was added
    def test_sign_up_works_correctly(self):
        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})

        
        
        # filter by all the users with that username
        users = User.objects.filter(username="user")
        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual(len(users), 1, "The user wasn't saved")
    
    #Check if userprofile is automatically created
    def test_sign_up_works_correctly_user_profile_save_user(self):
        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})
        
        users = User.objects.filter(username="user")
        userprofiles = UserProfile.objects.filter(user=users[0])
        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual(len(userprofiles), 1, "The userprofile wasn't saved")

    #Check if userprofile has a automatic default pic stored
    def test_sign_up_works_correctly_user_profile_has_default_pic(self):
        test = self.client.post(reverse("accounts:register"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'password1':'sat123', 'password2':'sat123'})
        
        users = User.objects.filter(username="user")
        userprofiles = UserProfile.objects.filter(user=users[0])
        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual('profile1.jpg', userprofiles[0].profilePicture, "The userprofile does not have default profile pic")


#User register form test has all been done!

#Here we are going to set up a user for future test in login
def setup_user():
    """
    Sets up a user
    """
    user = User(username='testuser')
    user.set_password('test123')
    user.save()

    userprofile = UserProfile(user=user)
    userprofile.save()


#This is test for login form and its views
class SignInFormTestCase(TestCase):
     
    #Setting up the user here
    def setUp(self):
        setup_user()
    
    #Test weather there will be an error if either username or password is incorrect
    def test_sign_in_raises_error(self):

        test = self.client.post(reverse('accounts:login'), {'username': 'testuser1', 'password': 'test12345'})
        
        self.assertEqual(type(test), TemplateResponse, "The response isn't a template!")

        #The error message is not needed, as the above test will fail if incorrect details are able to login
        self.assertTrue("Please enter a correct username and password" in str(test.content), "Response was correct but details were wrong")

    #Test weather user will be redirected to the home after login
    def test_sign_in_works_correctly(self):
        
        test = self.client.post(reverse('accounts:login'), {'username': 'testuser', 'password': 'test123'})

        self.assertEqual(type(test),  HttpResponseRedirect, "The response isn't a redirect!")
        self.assertEqual(test.url, reverse('accounts:profile'), "The redirected URL isn't the account profile!")

#User login test are now done!


#Test update profile form
class TestUpdateUserProfileForm(TestCase):
    
    #positive form response
    #Test weather the form updates the user email
    def test_update_email(self):

        user = User.objects.create(username='testuser', password='test123', email='dano@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        self.client.force_login(user)
     
        test = self.client.post(reverse("accounts:profile"), {'username': 'user', 'email': 'dabi@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'address':'blabla'}) 
        user.refresh_from_db()
        userprofile.refresh_from_db()

        self.assertEqual(type(test),  HttpResponse, "The response isn't a redirect!")
        self.assertEqual('dabi@gmail.com', user.email, "Email wasnt updated")


    #Test weather the form updates the user address
    def test_update_adress(self):

        user = User.objects.create(username='testuser', password='test123', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        self.client.force_login(user)
     
        test = self.client.post(reverse("accounts:profile"), {'username': 'user', 'email': 'dabi@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'address':'test'}) 
        user.refresh_from_db()
        userprofile.refresh_from_db()

        self.assertEqual(type(test),  HttpResponse, "The response isn't a redirect!")
        self.assertEqual('test', userprofile.address, "adress wasnt updated")

    
    #Test weather username will change
    def test_update_user(self):
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        self.client.force_login(user)

        test = self.client.post(reverse("accounts:profile"), {'username': 'testuser', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'address':'test'})
        user.refresh_from_db()

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual('testuser', user.username, "adress wasnt updated")

    #invalid test response
    #Test weather username will changed despite database having another user with same username
    def test_update_user_fail(self):
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        user2 = User.objects.create(username='testuser', password='test123', email='dabi1@gmail.com')
        userprofile = UserProfile.objects.create(user=user2)
        self.client.force_login(user2)

        test = self.client.post(reverse("accounts:profile"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast', 'address':'test'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("A user with that username already exists." in str(test.content), "Error message not found in the response!")

    #Test weather form will submit if adress isnt changed
    def test_update_address_fail(self):
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        self.client.force_login(user)

        test = self.client.post(reverse("accounts:profile"), {'username': 'user', 'email': 'test27@gmail.com', 'first_name': 'test',
                                                              'last_name': 'testLast'})

        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertTrue("This field is required." in str(test.content), "Error message not found in the response!")

    
#TestUpdateUserProfileForm are now done!

#Test the view for myCars
class TestMyCars(TestCase):

    #Test if you can enter my car without logging in, will redirect you to login page
    def test_my_car_fail_to_enter_if_not_log_in(self):
        response = self.client.get(reverse('accounts:mycars'))
        self.assertEqual(type(response), HttpResponseRedirect, "The response wasn't an httpResponse!")
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/mycars', 'wrong url')

    
    #Test if you can enter my car with logging in
    def test_my_car_enter_if_log_in(self):
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        cars = Car.objects.create(seller=user,unique_car_id=500)
        self.client.force_login(user)
        
        test = self.client.get(reverse('accounts:mycars'))
        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual(test.status_code, 200, 'Wrong status code')
    
    #Test to see if can delete car
    def test_my_car_if_can_delete(self):
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        cars = Car.objects.create(seller=user,unique_car_id=500)
        self.client.force_login(user)
        
        test = self.client.post(reverse('accounts:mycars'), {'car_id':'500'})
        filterCar = Car.objects.filter(unique_car_id=500)
        self.assertEqual(type(test), HttpResponse, "The response wasn't an httpResponse!")
        self.assertEqual(0,len(filterCar), 'The car wasnt deleted')
        self.assertEqual(test.status_code, 200, 'Wrong status code')

    
#Test for MyCars has been done

#Test for adding wishlist
class TestMyWishList(TestCase):

    #Test if can add to wishlist
    def test_my_car_if_can_add_to_wishlist(self): 
        user = User.objects.create_user(username='user', password='12345', email='dabi@gmail.com')
        userprofile = UserProfile.objects.create(user=user)
        cars = Car.objects.create(seller=user,unique_car_id=500,model='a3')
        self.client.force_login(user)
        test = self.client.post(reverse('accounts:add_wishlist',kwargs={'car_id': cars.unique_car_id}))
        cars.refresh_from_db
        user.refresh_from_db
        filterWishList = Car.objects.filter(user_wishlist=user)
        self.assertEqual(type(test), HttpResponseRedirect, "The response wasn't an httpResponseredirect!")
        self.assertEqual(filterWishList[0].model, 'a3', "The response didnt add proper car to wishlist")
        
#Finished test for adding cars in wishlist and the view

#The account tests have been finished
