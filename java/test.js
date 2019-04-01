var capitalize_string = "capitalize me now";
word_list = capitalize_string.split(" ");
var text = "";
for (var i = 0; i < word_list.length; i++) {
  text += word_list[i][0].toUpperCase()+word_list[i].slice(1) + " ";
} 
console.log(text);

//string.UpperCase()