// (UI logic like tabs and menu)
// Toggle tabs
const tablinks = document.getElementsByClassName("tab-links");
const tabcontents = document.getElementsByClassName("tab-contents");

export function opentab(tabname) {
  for (let tablink of tablinks) {
    tablink.classList.remove("active-link");
  }
  for (let tabcontent of tabcontents) {
    tabcontent.classList.remove("active-tab");
  }
  event.currentTarget.classList.add("active-link");
  document.getElementById(tabname).classList.add("active-tab");
}

// Toggle side menu
const sidemenu = document.getElementById("sidemenu");

export function openmenu() {
  sidemenu.style.right = "0";
}

export function closemenu() {
  sidemenu.style.right = "-200px";
}
