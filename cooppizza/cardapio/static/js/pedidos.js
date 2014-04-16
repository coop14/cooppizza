$(function() {
  $('.pedido_pizza_quantidade').find('option').each(function() {
    if ($(this).text() == $(this).parent().data('quantidade')) {
      $(this).attr('selected', 'selected');
    }
  });
});
