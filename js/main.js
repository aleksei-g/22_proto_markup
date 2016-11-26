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
  template:
  '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
      '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
      '<span data-notify="icon"></span> ' +
      '<span data-notify="title">{1}</span> ' +
      '<span data-notify="message">{2}</span>' +
      '<div class="text-center">'+
        '<a class="btn btn-info btn-sm" data-notify="dismiss">ДА</a>' +
        '<a class="btn btn-info btn-sm" data-notify="dismiss" id="button_error_region">НЕТ</a>' +
      '</div>'+
      '<div class="progress" data-notify="progressbar">' +
          '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0;"></div>' +
      '</div>' +
      '<a href="{3}" target="{4}" data-notify="url"></a>' +
  '</div>'
  });
}

if ( NeedToShowNotifyMessage == 1) {
  ShowNotifyMessage();
}
