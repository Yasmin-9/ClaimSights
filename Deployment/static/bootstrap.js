//note to self: 'document'is a global object, referring to .html

    
// Creating re-usable instances of Tooltips (Hovering over for text)

document.addEventListener('DOMContentLoaded', function () { 
  // Selecting all elements with data-bs-toggle="tooltip" (bootstrap)
    var tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');  
     
    // Iterating over all matching elements and initialize a tooltip for each
    tooltipElements.forEach(function (element) {
    new bootstrap.Tooltip(element);});
   });
  
  
   // Drop-down menu initializer (for all)
  document.addEventListener('DOMContentLoaded',function(){
  var menus = document.querySelectorAll('[data-bs-toggle="dropdown"]');
    menus.forEach(function(menu){
      new bootstrap.Dropdown(menu);
    })
  });
  
function nextPage(){
  window.location.href = 'next-page.html';
  // if path doesn't work TRY: 'templates/next-page.html'

}

if 