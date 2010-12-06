$().ready( function() {
	
	
	/* simulate html5 placeholder attribute in unsupported browsers */
    $("input, textarea").placehold();
	
	$("form#press-nav-form").submit(function(ev) {
		var form = $(this);
		ev.preventDefault();
		window.location = '/press/' +
			form.find('input[name=pub_type]').val() + '/' + 
			form.find('select[name=year]').val() + '/' + 
			form.find('select[name=month]').val() + '/';
	});
	
	
	/*
	 * carousel stuff
	 */
	var slideWidth = 478;
	var carouselUserIntervention = false;
	$('.carousel ul').css({'width': $('.carousel li').length * slideWidth});
	$('.carousel ul').prepend($('.carousel li:last'));
	
	var carouselNext = function() {
		$('.carousel li:first').animate(
			{width: 0},
			{queue: false, duration: 300, complete: function() {
				$('.carousel ul').append($(this).css({'width': slideWidth}));
			}}
		);
	};
	
	var carouselPrevious = function() {
		$('.carousel ul').prepend($('.carousel li:last').css({'width': 0}));
		$('.carousel li:first').animate(
			{width: slideWidth},
			{queue: false, duration: 300}
		);
	};
	
	var carouselAutoAdvance = function() {
		if (carouselUserIntervention) return;
		carouselNext();
		setTimeout(carouselAutoAdvance, 10000);
	};

	$('a.carousel-next').click(function(ev) {
		carouselNext();
		carouselUserIntervention = true;
		ev.preventDefault();
	});
	
	$('a.carousel-previous').click(function(ev) {
		carouselPrevious();
		carouselUserIntervention = true;
		ev.preventDefault();
	});
	
	if ($('.carousel').attr('data-autoadvance') == 'autoadvance') {
		setTimeout(carouselAutoAdvance, 10000);
	}
	
	$('#mailinglistform').submit(function(ev) {
		var btn = $(this).find('#joinBtn');
		if (btn.hasClass('disabled')) {
			ev.preventDefault();
		} else {
			btn.addClass('disabled').attr('disabled', 'disabled');
		}
	});
	
});

