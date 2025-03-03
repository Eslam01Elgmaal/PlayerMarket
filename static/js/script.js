var swiperContainer = document.getElementsByClassName("slide-container")[0];
var pagination = document.getElementsByClassName("swiper-pagination")[0];

var swiper = new swiper(swiperContainer, {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: {
    el: pagination,
    clickable: true,
  },
});
