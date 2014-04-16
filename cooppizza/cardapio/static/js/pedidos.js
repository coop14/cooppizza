$(function() {
  $('#dialog_pizza').dialog({
    modal: true,
    autoOpen: true,
    buttons: {
      Ok: function () {
        $(this).dialog("close");
      }
    }
  });
  $('#dialog_pizza').show();
});
