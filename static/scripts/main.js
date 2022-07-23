function logRedirect(id) {
  location.assign("/logs/" + id);
}

var navController = document.getElementById("side-change");
var sideBar = document.getElementById("side-bar");
var main = document.getElementById("main");
var body = document.getElementsByTagName("body")[0];
var modeIcon = document.getElementById("mode-icon");

navController.addEventListener("click", () => {
  sideBar.classList.toggle("hidden");
  navController.classList.toggle("to-right");
  main.classList.toggle("full");
  //
  if (sideBar.classList.contains("hidden")) {
    localStorage.setItem("sideBarHidden", "yes");
  } else {
    localStorage.setItem("sideBarHidden", "no");
  }
  //
  console.log(localStorage);
});

if (localStorage.getItem("sideBarHidden") == "yes") {
  sideBar.classList.toggle("hidden");
  navController.classList.toggle("to-right");
  main.classList.toggle("full");
}

// Dark Light Modde
function iconTransform() {
  modeIcon.classList.toggle("fa-moon");
  modeIcon.classList.toggle("fa-sun");
}
function nightDayMode() {
  document.body.classList.toggle("dark-theme");

  if (body.classList.contains("dark-theme")) {
    localStorage.setItem("darkMode", "yes");
  } else {
    localStorage.setItem("darkMode", "no");
  }

  iconTransform();
}

if (localStorage.getItem("darkMode") == "yes") {
  body.classList.toggle("dark-theme");
  iconTransform();
}
