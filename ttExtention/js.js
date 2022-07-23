function scrapHref(str) {
  arr = str.split("/");
  return arr[8];
}
function getTable() {
  table = document.getElementsByClassName("table-rows");
  //   console.log(table.length);
  data = [];
  if (table.length != 0) {
    clearInterval(interval);
    table = table[0].children;
    for (let i = 0; i < table.length; i++) {
      data.push(scrapHref(table[i].children[0].getElementsByTagName("a")[0].href));
      data.push(table[i].children[1].getElementsByTagName("a")[0].innerText);
    }

    console.log(data);
  }
}
const interval = setInterval(getTable, 1000);
///
function get() {
  fetch("https://www.dragons.uz/samsara/get-data/")
    .then((res) => res.json())
    .then((data) => {
      console.log("json data: ", data);
    });
}
get();
