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

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const likeBtns = document.querySelectorAll('.card__slider_like');
likeBtns?.forEach(btn => {
  btn.addEventListener('click', function (e) {
    e.preventDefault();
    const id = btn.getAttribute('data-id');
    fetch('/like', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({id: id})
    })
    .then((res) => {
      if (res.status === 403) {
        window.location.href = '/accounts/login'
      }
    })
    btn.classList.toggle('card__slider_like_active')
  })
})

const likeBtn = document.querySelector('.product__fav_btn');
if (likeBtn) {
  likeBtn.addEventListener('click', function () {
    const id = likeBtn.getAttribute('data-id');
    fetch('/like', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({id: id})
    })
    .then((res) => {
      if (res.status === 403) {
        window.location.href = '/accounts/login'
      }
    })
    if (likeBtn.classList.contains('product__fav_btn_active')) {
      likeBtn.textContent = 'В избранное'
      likeBtn.classList.remove('product__fav_btn_active');
    } else {
      likeBtn.textContent = 'Удалить из избранного'
      likeBtn.classList.add('product__fav_btn_active');
    }
  })
}