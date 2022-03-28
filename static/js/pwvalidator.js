$(document).ready(function () {
    // Assign password id input to variable
    let password = document.getElementById("password");
    // Assign pconfirm id input to variable
    let pconfirm = document.getElementById("pconfirm");

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
});