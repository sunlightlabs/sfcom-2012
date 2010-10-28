
(function($) {
	
	var defaults = {
		slideWidth: null
	}

	$.carousel = function(e, o) {
		
	};
	
	$.carousel.fn = $.carousel.prototype = {
		carousel: '0.1.0'
	};

	$.carousel.fn.extend = $.carousel.extend = $.extend;
	
	$.carousel.fn.extend({
		
		this.list = $(e).find('ul').first();
		
		next: function() {
			var list = this.list;
			list.find('li:first').animate(
				{width: 0},
				{queue: false, duration: 300, complete: function() {
					list.append(
						$(this).css({'width': slideWidth})
					);
				}}
			);
		},
		
		previous: function() {
			var list = this.list;
			list.prepend(list.find('li:last').css({'width': 0}));
			list.find('li:first').animate(
				{width: slideWidth},
				{queue: false, duration: 300}
			);
		}
		
	});
	
	$.fn.carousel = function(o) {
		if (typeof o == 'string') {
			var instance = $(this).data('carousel'), args = Array.prototype.slice.call(arguments, 1);
			return instance[o].apply(instance, args);
		} else {
			return this.each(function() {
				$(this).data('carousel', new $.carousel(this, o));
			});
		}
	};

})(this.jQuery);




window.log = function(){
  log.history = log.history || [];   
  log.history.push(arguments);
  if(this.console){
    console.log( Array.prototype.slice.call(arguments) );
  }
};
(function(doc){
  var write = doc.write;
  doc.write = function(q){ 
    log('document.write(): ',arguments); 
    if (/docwriteregexwhitelist/.test(q)) write.apply(doc,arguments);  
  };
})(document);


