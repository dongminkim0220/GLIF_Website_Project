function activeThis(element){
    var current = document.getElementsByClassName("breadcrumb-item active")[0];
    current.classList.remove("active");
    element.classList.add("active");
}

function seeMore(id) {
    var x = document.getElementById(id)
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}