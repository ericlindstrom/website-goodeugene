/**
 * jQuery Unveil
 * A very lightweight jQuery plugin to lazy load images
 * http://luis-almeida.github.com/unveil
 *
 * Licensed under the MIT license.
 * Copyright 2013 Luís Almeida
 * https://github.com/luis-almeida
 */

;(function($){$.fn.unveil=function(threshold){var $w=$(window),th=threshold||0,retina=window.devicePixelRatio>1,attrib=retina?"data-src-retina":"data-src",images=this,loaded,inview,source;this.one("unveil",function(){source=this.getAttribute(attrib);source=source||this.getAttribute("data-src");if(source)this.setAttribute("src",source);});function unveil(){inview=images.filter(function(){var $e=$(this),wt=$w.scrollTop(),wb=wt+$w.height(),et=$e.offset().top,eb=et+$e.height();return eb>=wt-th&&et<=wb+th;});loaded=inview.trigger("unveil");images=images.not(loaded);}$w.scroll(unveil);$w.resize(unveil);unveil();return this;};})(window.jQuery||window.Zepto);


$(function() {
  $('#header a[href="/info/"]').on('click', function(e) {
    e.preventDefault();
    var info = $('meta[name="info"]').attr('content').replace(/\|/gi, '<br/>');
    $('.content_wrap').prepend(['<div class="info_block block border_bottom"><div class="position"><div class="container">', info, '<a class="close" href="#"> × </a></div></div></div>'].join(''));

    $('.info_block .close').on('click', function(e) {
      e.preventDefault();
      $('.info_block').remove();
    });

    if ($('body').hasClass('info_open')) {
      $('.info_block').remove();
      $('body').removeClass('info_open');
    } else {
      $('body').addClass('info_open');
      window.scrollTo(0);
    }
  });


  $('img').unveil(200);
});
