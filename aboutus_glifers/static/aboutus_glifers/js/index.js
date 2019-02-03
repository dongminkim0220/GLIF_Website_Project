function activeThis(element){
    var current = document.getElementsByClassName("breadcrumb-item active")[0];
    current.classList.remove("active");
    element.classList.add("active");
}