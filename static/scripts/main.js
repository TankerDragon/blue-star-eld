var navController = document.getElementById("side-change");
var sideBar = document.getElementById("side-bar");
var main = document.getElementById("main");

navController.addEventListener("click", () => {
  sideBar.classList.toggle("hidden");
  navController.classList.toggle("to-right");
  main.classList.toggle("full");
  //
  if (sideBar.classList.contains('hidden')) {
    localStorage.setItem("sideBarHidden", "yes");
  }
  else {
    localStorage.setItem("sideBarHidden", "no");
  }
  //
  // document.body.classList.toggle('dark-theme');
  console.log(localStorage);
});

if (localStorage.getItem("sideBarHidden") == "yes") {
  sideBar.classList.toggle("hidden");
  navController.classList.toggle("to-right");
  main.classList.toggle("full");
}
