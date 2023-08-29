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