
// ==========================================
// FLATPICKR — Date & Time Pickers
// ==========================================

flatpickr("#appointment-date", {
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: false,
});

flatpickr("#appointment-time", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    minTime: "09:00",
    maxTime: "18:00",
    minuteIncrement: 15,
    disableMobile: false,
});


// ==========================================
// SMOOTH SCROLL for navbar links
// ==========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
});


// ==========================================
// NAVBAR — hide/show on scroll
// ==========================================

let lastScrollY = window.scrollY;
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    if (window.scrollY < lastScrollY || window.scrollY < 60) {
        navbar.style.transform = "translateY(0)";
    } else {
        navbar.style.transform = "translateY(-100%)";
    }
    lastScrollY = window.scrollY;
});


// ==========================================
// GALLERY — lightbox on click
// ==========================================

document.querySelectorAll(".gallery-grid img").forEach(img => {
    img.style.cursor = "zoom-in";
    img.addEventListener("click", () => {
        const overlay = document.createElement("div");
        overlay.className = "lightbox-overlay";

        const bigImg = document.createElement("img");
        bigImg.src = img.src;
        bigImg.alt = img.alt;

        overlay.appendChild(bigImg);
        document.body.appendChild(overlay);

        overlay.addEventListener("click", () => overlay.remove());
    });
});
