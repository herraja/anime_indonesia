console.log(`Coba scrollbar`);

$(window).scroll(function () {
  var scroll = $(window).scrollTop();
  if (scroll >= 290) {
    $("#myNav").addClass("bg-dark");
  } else {
    $("#myNav").removeClass("bg-dark");
  }
});
