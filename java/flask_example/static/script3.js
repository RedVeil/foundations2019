document.addEventListener("DOMContentLoaded", function() {
  var counter = 0

  function createParagraph() {
      counter +=1
      if(counter<2){
      var paragraphEl = document.createElement('p');
      paragraphEl.textContent = 'You clicked the button!'
      paragraphEl.setAttribute("id","element");
      document.getElementById("main").appendChild(paragraphEl);
      x = document.getElementById("element");
    } else {
      alert('You can only create one paragraph'); 
    }
  }
    var buttonEl = document.querySelector('button')
    buttonEl.addEventListener('click', createParagraph); 
});

