$ ->
  $('nav .icon').on 'click', (e) ->
    e.preventDefault()
    if $(this).parents('nav').hasClass 'open'
      $(this).parents('nav').removeClass 'open'
    else
      $(this).parents('nav').addClass 'open'

  return
