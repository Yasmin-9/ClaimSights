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
  
  // Go to next page via button click function
function nextPage(){
  window.location.href = '/diagnosis-page.html';}

// Updating the 3 interactive parameter buttons for model searching
function updateButtonText (buttonId, ClickedOption){
  document.getElementById(buttonId).innerText = ClickedOption;
}

//fixing function, ignore for now
function userSelectedOptions (buttonId1,buttonId2,buttonId3){
  document.getElementById();
}


function homePage(){
  window.location.href = '/';

}

function searchFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.querySelector("table");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function homePage(){
  window.location.href = '/';

}


function searchFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.querySelector("table");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
