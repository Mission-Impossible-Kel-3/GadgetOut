function setUsername()
{
    var username;
    username = document.getElementById("username").value;
    localStorage.setItem('username', username);
}

function loader()
{
    if (localStorage.getItem("username") !== null)
    {
        document.getElementById("loggedIn").innerHTML = localStorage.getItem("username");
        document.getElementById("loggedIn").innerHTML += ' <button type="button" onclick="logout()"><a href="index.html">Logout</a></button>';
    }
    else
    {
        document.getElementById("loggedIn").innerHTML = ' <a href="login.html">Login</a>';
    }
}

function logout()
{
    localStorage.removeItem("username");
}