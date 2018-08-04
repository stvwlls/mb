$( document ).ready(function() {
  $('.splash__readmore-link').on('click', function (e) {
    e.preventDefault();

    $('html, body').animate({
      scrollTop: $($(this).attr('href')).offset().top
    }, 500);
  });
});
