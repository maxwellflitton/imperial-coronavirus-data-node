const loginButton = document.getElementById('loginButton');
const username = document.getElementById('defaultLoginFormEmail');
const password = document.getElementById('defaultLoginFormPassword');
const message = document.getElementById("loginMessage");


loginButton.addEventListener("click", () => {

    let xhr = new XMLHttpRequest();
    let url = "/users/login";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {

        if (xhr.readyState === 4 && xhr.status === 200) {
            let json = JSON.parse(xhr.responseText);
            if (json.success === false) {
                message.textContent = "username or password is incorrect";
                username.value = null;
                password.value = null;
            }
            if (json.success === true) {
                window.location.replace(window.location.href + "users/dashboard");
            }
        }
    };
    let data = JSON.stringify({"username": username.value, "password": password.value});
    xhr.send(data);
});
