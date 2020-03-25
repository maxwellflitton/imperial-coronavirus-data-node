const loginButton = document.getElementById('loginButton');
const username = document.getElementById('defaultLoginFormEmail');
const password = document.getElementById('defaultLoginFormPassword');


loginButton.addEventListener("click", () => {
    console.log(username.value);
    console.log(password.value);

    let xhr = new XMLHttpRequest();
    let url = "/users/login";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {

        if (xhr.readyState === 4 && xhr.status === 200) {
            let json = JSON.parse(xhr.responseText);
            console.log(json.success);
        }
    };
    let data = JSON.stringify({"username": username.value, "password": password.value});
    xhr.send(data);
});
