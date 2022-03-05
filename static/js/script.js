$(document).ready(function(){
    $('.sidenav').sidenav({edge: 'right'});
    $(".dropdown-trigger").dropdown();
    // Get current year in footer copyright by assigning new date object to year id
    document.getElementById("year").innerHTML = new Date().getFullYear();
    $('.collapsible').collapsible();
  });

  