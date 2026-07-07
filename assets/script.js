function togglePassword()   {
    
    let password = document.getElementById("password");

    if(password.type==="password") {
        password.type = "text";
    }
    else {
        password.type = "password";
    }
}

function copyPassword() {
    let generated = document.getElementById("generatedPassword");

    generated.select();
    generated.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(generated.value);
    alert("Password copied successfully!")
}