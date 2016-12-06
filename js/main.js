$(function(){
  $("#f-bid-phone").mask("+7(999) 999-9999");
  $("#f-provider-phone").mask("+7(999) 999-9999");
  $("#f-company-phone").mask("+7(999) 999-9999");
  $('#button_error_region').click(function(open_select_region){
    open_select_region.stopPropagation();
    $('#button_navbar_toggle').click();
    $('#region').dropdown('toggle');
  });
});

function ShowNotifyMessage() {
  $.notify({
  // options
  message: MessageRegion
  },{
  // settings
  type: 'info',
  position: 'absolute',
  placement: {
    from: "top",
    align: "left"
  },
  offset: {
    x: 20,
    y: 52
  },
  delay: 0,
  mouse_over: 'pause',
  template: AlertTemplate
  });
}

if ( NeedToShowNotifyMessage == 1) {
  ShowNotifyMessage();
}
