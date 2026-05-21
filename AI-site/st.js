const navbar = document.getElementById('navbar');

// ვუსმენთ სქროლს
window.addEventListener('scroll', () => {
    // თუ 50 პიქსელზე მეტით ჩამოვსქროლეთ
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        // თუ ისევ ზევით ვართ
        navbar.classList.remove('scrolled');
    }
});