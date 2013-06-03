function getPhotos(target, paramString){
	$.ajax({
		url: "http://api.tumblr.com/v2/blog/iambradleymanning.tumblr.com/posts?api_key=3L0eVSusQgAxs5XPAeqz55XxylQpOGUVedFh2I02UC8dusC5jS&limit=10"+paramString,
		dataType: 'jsonp',
		success: function(results){
			results.response.posts.forEach(function(post){
		    if(post.type == "photo"){
		      post["photos"].forEach(function(photo){
  		    	$("#photo-feed .feed ."+target).html("");
            $("#photo-feed .feed ."+target).append("<div class='box'><img src='"+photo.alt_sizes[0].url+"'></div>");
  		    });	
		    }
			});
			$("#photo-feed .feed ."+target).siblings().hide();
			$("#photo-feed .feed ."+target).show();
			$("#photo-feed .feed ."+target).imagesLoaded(function(){
		    $("#photo-feed .feed ."+target).masonry({
		      itemSelector: '.box'
		    });
      });
		}
	});
}


$(function(){

  getPhotos("featured", "&tag=notables");
  

  $("#photo-feed .nav-links li a").click(function(e){
    var option = $(this).data("option");
    $("#photo-feed .nav-links .selected").removeClass("selected");
    $(this).addClass("selected");
    switch(option){
    	case "recent":
        getPhotos("recent", "");
        break;
      case "featured":
        getPhotos("featured", "&tag=notables");
        break;
      case "veterans":
        getPhotos("veterans", "&tag=veterans");
        break;
    }
    return false;
	});	

});

