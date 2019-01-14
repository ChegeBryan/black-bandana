function toggleNavlink() {
  var x = document.getElementsByClassName('navbar--collapse');
  if (x[0].className === 'navbar--collapse') {
    x[0].className += ' navbar--collapse-show';
  }
  else {
    x[0].className = 'navbar--collapse';
  }
}

function showPassword() {
  var x = document.getElementById("pwd");
  x.type = "text";
}
function hidePassword() {
  var x = document.getElementById("pwd");
  x.type = 'password';
}