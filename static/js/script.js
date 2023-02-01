const swiper = new Swiper('.card__slider', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1,
    spaceBetween: 20,
    wrapperClass: 'card__slider_wrapper',
    slideClass: 'card__slider_photo',
    navigation: {
      nextEl: '#mainpage_card_slider_arrow_next',
      prevEl: '#mainpage_card_slider_arrow_prev',
    }
});

const Bswiper = new Swiper('.product__slider', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1,
    spaceBetween: 20,
    wrapperClass: 'product__slider_wrapper',
    slideClass: 'product__slider_photo',
    navigation: {
      nextEl: '#mainpage_card_slider_arrow_next',
      prevEl: '#mainpage_card_slider_arrow_prev',
    }
});