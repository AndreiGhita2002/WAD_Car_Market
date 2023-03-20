document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('user_form');
    form.classList.add('opacity-0');

    setTimeout(() => {
        form.classList.remove('opacity-0');
        form.classList.add('opacity-1');
    }, 200);
});