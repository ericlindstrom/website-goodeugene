require.config({
  paths: {
    jquery: ['//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min', 
      '/media/static/js/vendor/jquery-1.10.1.min'],
    unveil: '/media/static/js/vendor/unveil'
  },
  shim: {
    jquery: { exports: '$' },
    unveil: ['jquery']
  }
})

require(['jquery', 'unveil'], function($) {
  $(function() {
    $('#header a[href="/info/"]').on('click', function(e) {
      e.preventDefault();
      var info = $('meta[name="info"]').attr('content').replace(/\|/gi, '<br/>');
      $('.content_wrap').prepend(['<div class="info_block block border_bottom"><div class="position"><div class="container"><p class="infobox">', info, '</p><a class="close" href="#"> × </a></div></div></div>'].join(''));
  
      $('.info_block .close').on('click', function(e) {
        e.preventDefault();
        $('.info_block').remove();
      });
  
      if ($('body').hasClass('info_open')) {
        $('.info_block').remove();
        $('body').removeClass('info_open');
      } else {
        $('body').addClass('info_open');
        window.scrollTo(0,0);
      }
    });
  
  
    $('img').unveil(200);
  });
});
