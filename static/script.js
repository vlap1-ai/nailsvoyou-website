document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});

let lastScrollY = window.scrollY;
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    if (!navbar) return;

    if (window.scrollY < lastScrollY || window.scrollY < 60) {
        navbar.style.transform = "translateY(0)";
    } else {
        navbar.style.transform = "translateY(-100%)";
    }

    lastScrollY = window.scrollY;
});

document.querySelectorAll(".gallery-grid img").forEach(img => {
    img.style.cursor = "zoom-in";

    img.addEventListener("click", () => {
        const overlay = document.createElement("div");
        overlay.className = "lightbox-overlay";

        const bigImg = document.createElement("img");
        bigImg.src = img.src;

        overlay.appendChild(bigImg);
        document.body.appendChild(overlay);

        overlay.addEventListener("click", () => overlay.remove());
    });
});