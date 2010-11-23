$().ready( function() {
	
	/* simulate html5 placeholder attribute in unsupported browsers */
    $("input, textarea").placehold();
	
	var slideWidth = 420;
	$('.carousel ul').css({'width': $('.carousel li').length * slideWidth});
	$('.carousel ul').prepend($('.carousel li:last'));

	$('a.carousel-next').click(function(ev) {
		$('.carousel li:first').animate(
			{width: 0},
			{queue: false, duration: 300, complete: function() {
				$('.carousel ul').append($(this).css({'width': slideWidth}));
			}}
		);
		ev.preventDefault();
	});
	
	$('a.carousel-previous').click(function(ev) {
		$('.carousel ul').prepend($('.carousel li:last').css({'width': 0}));
		$('.carousel li:first').animate(
			{width: slideWidth},
			{queue: false, duration: 300}
		);
		ev.preventDefault();
	});
	
});

