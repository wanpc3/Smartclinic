function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const icon = passwordField.nextElementSibling;
    
    if (passwordField.type === "password") {
        passwordField.type = "text";
        icon.classList.replace("fa-eye-slash", "fa-eye");
    } else {
        passwordField.type = "password";
        icon.classList.replace("fa-eye", "fa-eye-slash");
    }
}