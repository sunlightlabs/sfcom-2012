$().ready( function() {
	
	
	/* simulate html5 placeholder attribute in unsupported browsers */
    $("input, textarea").placehold();
	
	/* carousel */
	$('.carousel').carousel({
		autoAdvance: true,
		nextElem: $('a.carousel-next'),
		previousElem: $('a.carousel-previous')
	});
	
	$("form#press-nav-form").submit(function(ev) {
		var form = $(this);
		ev.preventDefault();
		window.location = '/press/' +
			form.find('input[name=pub_type]').val() + '/' + 
			form.find('select[name=year]').val() + '/' + 
			form.find('select[name=month]').val() + '/';
	});
	
	$('#mailinglistform').submit(function(ev) {
		var btn = $(this).find('#joinBtn');
		if (btn.hasClass('disabled')) {
			ev.preventDefault();
		} else {
			btn.addClass('disabled').attr('disabled', 'disabled');
		}
	});
	
});

