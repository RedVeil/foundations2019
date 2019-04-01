document.addEventListener("DOMContentLoaded", function() {

  var button = document.findElementByID("button");
  var pokemon = document.findElementByID("pokemon");

  function updateName () {
    if (pokemon.style.display === "none") {
      pokemon.style.display = "block";
    } else {
      pokemon.style.display = "none";
    }
  }

  button.addEventListener('click', updateName);

});
