document.addEventListener("DOMContentLoaded", () => {
  // main slider 
  const swiper = new Swiper(".mainSlider", {
    loop: true,
  
    pagination: {
      el: ".swiper-pagination",
    },

    keyboard: {
        enabled: true,
    },
  
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    effect: "fade",
  })

  let tl = gsap.timeline()
  tl.fromTo(".slideImage", {opacity:0,scale:0, duration:.5}, {scale:1, opacity:1, duration:.5})
  tl.fromTo(".slideTitle", {opacity:0, x:200, duration:.5}, {x:0, opacity:1, duration:.3})
  tl.fromTo(".slideBody", {opacity:0, height:0, duration:.5}, {height:"auto", opacity:1, duration:.5})
  
  swiper.on("slideChange", () => {
    tl.fromTo(".slideImage", {opacity:0, scale:0, duration:.5}, {scale:1, opacity:1, duration:.5})
    tl.fromTo(".slideTitle", {opacity:0, x:200, duration:.5}, {x:0, opacity:1, duration:.3})
    tl.fromTo(".slideBody", {opacity:0, height:0, duration:.5}, {height:"auto", opacity:1, duration:.5})  
  })


  // Cards spotlight
class Spotlight {
  constructor(containerElement) {
    this.container = containerElement;
    this.cards = Array.from(this.container.children);
    this.mouse = {
      x: 0,
      y: 0,
    };
    this.containerSize = {
      w: 0,
      h: 0,
    };
    this.initContainer = this.initContainer.bind(this);
    this.onMouseMove = this.onMouseMove.bind(this);
    this.init();
  }

  initContainer() {
    this.containerSize.w = this.container.offsetWidth;
    this.containerSize.h = this.container.offsetHeight;
  }

  onMouseMove(event) {
    const { clientX, clientY } = event;
    const rect = this.container.getBoundingClientRect();
    const { w, h } = this.containerSize;
    const x = clientX - rect.left;
    const y = clientY - rect.top;
    const inside = x < w && x > 0 && y < h && y > 0;
    if (inside) {
      this.mouse.x = x;
      this.mouse.y = y;
      this.cards.forEach((card) => {
        const cardX = -(card.getBoundingClientRect().left - rect.left) + this.mouse.x;
        const cardY = -(card.getBoundingClientRect().top - rect.top) + this.mouse.y;
        card.style.setProperty('--mouse-x', `${cardX}px`);
        card.style.setProperty('--mouse-y', `${cardY}px`);
      });
    }
  }

  init() {
    this.initContainer();
    window.addEventListener('resize', this.initContainer);
    window.addEventListener('mousemove', this.onMouseMove);
  }
}

// Init Spotlight
const spotlights = document.querySelectorAll('[data-spotlight]');
spotlights.forEach((spotlight) => {
  new Spotlight(spotlight);
});


  const slider1 = new Swiper(".slider1", {
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 40
      },
      1536: {
        slidesPerView: 4,
        spaceBetween: 40
      },
    },

    centerInsufficientSlides:true
  })
})