$(function(){
  function insertCSS(){
    var frm = frames['frame1'].document;
    var otherhead = frm.getElementsByTagName("head")[0];
    if(otherhead.length != 0){
    	var link = frm.createElement("link");
      link.setAttribute("rel", "stylesheet");
      link.setAttribute("type", "text/css");
      link.setAttribute("href", "http://development0.metatroid.com/css/frame.css");
      otherhead.appendChild(link);
      setTimeout(function(){$("#frame1").show();}, 200);
      clearInterval(cssInsertion);
    }
  }
  
  cssInsertion = setInterval(insertCSS, 500);
  //setTimeout(insertCSS, 1000);

  $(window).scroll(function() {
     if($(window).scrollTop() + $(window).height() > $(document).height() - 100 && $("#frame1").height() < 50000) {
         $("#frame1").css("height", "+=1000px");
     }
  });
});
