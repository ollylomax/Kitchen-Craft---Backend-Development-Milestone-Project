$(document).ready(function () {
  $('.sidenav').sidenav({
    edge: 'right'
  });
  $(".dropdown-trigger").dropdown();
  // Get current year in footer copyright by assigning new date object to year id
  document.getElementById("year").innerHTML = new Date().getFullYear();
  $('.collapsible').collapsible();
  $('.tooltipped').tooltip();
  $('select').formSelect();
  $('textarea').characterCounter();
  $('.modal').modal();

  // Assign password id input to variable
  let password = document.getElementById("password")
  // Assign pconfirm id input to variable
  let pconfirm = document.getElementById("pconfirm")

  // Function to check password against pconfirm
  function confirmPassword() {
    if (password.value != pconfirm.value) { // Conditional statement to check if passwords do not match
      pconfirm.setCustomValidity("Your Password does not match"); // Method to display custom validity error
    } else { // If they do match
      pconfirm.setCustomValidity(''); // Empty string meaning no validity error
    }
  }
  // Function is called if password input is changed
  password.onchange = confirmPassword;
  // Function called after every keystroke
  pconfirm.onkeyup = confirmPassword;

  // Code Institute Materialize Select Validator from task manager walkthrough lessons
  validateMaterializeSelect();

  function validateMaterializeSelect() {
    let classValid = {
      "border-bottom": "1px solid #4caf50",
      "box-shadow": "0 1px 0 0 #4caf50"
    };
    let classInvalid = {
      "border-bottom": "1px solid #f44336",
      "box-shadow": "0 1px 0 0 #f44336"
    };
    if ($("select.validate").prop("required")) {
      $("select.validate").css({
        "display": "block",
        "height": "0",
        "padding": "0",
        "width": "0",
        "position": "absolute"
      });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
      $(this).parent(".select-wrapper").on("change", function () {
        if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
          $(this).children("input").css(classValid);
        }
      });
    }).on("click", function () {
      if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
        $(this).parent(".select-wrapper").children("input").css(classValid);
      } else {
        $(".select-wrapper input.select-dropdown").on("focusout", function () {
          if ($(this).parent(".select-wrapper").children("select").prop("required")) {
            if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
              $(this).parent(".select-wrapper").children("input").css(classInvalid);
            }
          }
        });
      }
    });
  }
});