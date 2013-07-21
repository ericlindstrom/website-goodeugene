$(function() {
  $('#header a[href="/info/"]').on('click', function(e) {
    e.preventDefault();
    var info = $('meta[name="info"]').attr('content').replace(/\|/gi, '<br/>');
    $('#header').after(['<div class="info_block block border_bottom"><div class="position"><div class="container">', info, '</div></div></div>'].join(''));

    if ($('body').hasClass('info_open')) {
      $('.info_block').remove();
      $('body').removeClass('info_open');
    } else {
      $('body').addClass('info_open');
    }
  });
});
