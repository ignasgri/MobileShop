$(document).ready(function(){
    $(".flip").click(function(){
        $(this).next(".panel").slideToggle("slow");
    });
});

// link scroller
$(document).ready(function(){
    $('a[href^="#"]').on('click', function(event) {
        event.preventDefault();
  
        var target = this.hash;
        var $target = $(target);
  
        $('html, body').animate({
          'scrollTop': $target.offset().top
        }, 1000, 'swing')
          window.location.hash = target;
        });
    });
  // to top scroller
  $(document).ready(function(){
        $('body').append('<div id="toTop"</div>');
          $(window).scroll(function () {
              if ($(this).scrollTop() != 0) {
                  $('#toTop').fadeIn();
              } else {
                  $('#toTop').fadeOut();
              }
          }); 
      $('#toTop').click(function(){
          $("html, body").animate({ scrollTop: 0 }, 600);
          return false;
      });
  });
//enlarge image in modal

$(".modal-img").click(function() {
    $('.modal-img1').css('display', 'none');
  });
$(".modal-img").click(function() {
    $('.transform').toggleClass('transform-active');
    $('.modal-img').css('width', '100%!important');
    
  });