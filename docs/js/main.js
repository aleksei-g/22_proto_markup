$(function(){
  $(".phone-mask").mask("+7(999) 999-9999");
  $('#button_error_region').click(function(open_select_region){
    open_select_region.stopPropagation();
    $('#button_navbar_toggle').click();
    $('#region').dropdown('toggle');
  });
});

function ShowNotifyMessage() {
  $.notify({
  // options
  message: document.getElementById("message-notify").innerText
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
  template: document.getElementById("template-notify").innerText
  });
}

if ( NeedToShowNotifyMessage == 1) {
  ShowNotifyMessage();
}
