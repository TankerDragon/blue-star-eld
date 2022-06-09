var navController = document.getElementById("side-change");
var sideBar = document.getElementById("side-bar");
var main = document.getElementById("main");

navController.addEventListener("click", () => {
  sideBar.classList.toggle("hidden");
  navController.classList.toggle("to-right");
  main.classList.toggle("full");
});
