$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        items: 1,
        loop: true,
        margin: 10,
        dots: false,
        nav: true,
        autoplay: true,
        autoplaySpeed: 1000,
        smartSpeed: 1500,
        autoplayHoverPause: true,
  });
});

/* $(document).ready(function () {
  $('.nav__link').click(function (e) {
    e.preventDefault();
    $('.nav__link').removeClass('nav__link--active');
    $(this).addClass('nav__link--active')
  })
}); */

$(document).ready(function () {
  $('.menu__item').click(function (e) {
    e.preventDefault();
    $('.menu__item').removeClass('menu__item--active');
    $(this).addClass('menu__item--active')
  })
});