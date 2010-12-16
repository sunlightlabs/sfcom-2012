
(function($) {


})(this.jQuery);




window.log = function(){
  log.history = log.history || [];   
  log.history.push(arguments);
  if(this.console){
    console.log( Array.prototype.slice.call(arguments) );
  }
};
// (function(doc){
//   var write = doc.write;
//   doc.write = function(q){ 
//     log('document.write(): ',arguments); 
//     if (/<script src="http:\/\/maps\.gstatic\.com\/intl\/en_us\/mapfiles\/api-3\/2\/10\/main\.js" type="text\/javascript"><\/script>/.test(q)) write.apply(doc,arguments);  
//   };
// })(document);


