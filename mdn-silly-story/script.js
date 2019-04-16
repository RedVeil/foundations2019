var names = ["Gudrun", "Big C", "the Banana King"];
var places = ["the forest", "your house", "Disneyland"];
var actions = ["suddenly imploded without making any sounds", "angels appeared and took them to heaven", "sat down"];

var story = "It was 80 fahrenheit outside, so {person} went for a walk. When they got to {place}, they stared in horror for a few moments, then {action}. Bob saw the whole thing, but was not surprised — {person} weighs 300 pounds, and it was a hot day.";
const usTemperature = 80;
const usWeight = 300;
var textClass = document.querySelector('.story');

var costumName = document.getElementById("costumname");
var randomize = document.querySelector(".randomize");

randomize.addEventListener('click', result);

function unitChange(){
    let deTemperature = Math.round((usTemperature-32)*(5/9));
    let deWeight = Math.round((usWeight /2)-(usWeight/20));
    return [deTemperature, deWeight]
};

function random(){
    car randNum = Math.floor(Math.random() * 3);
    return randNum;
};

function result(){
    let newStory = story

    if (document.getElementById("de").checked) {
        let deValues = unitChange();
        let deTemperature = deValues[0];
        let deWeight = deValues[1];
        var temperature = deTemperature.toString() + " degrees";
        var weight = deWeight.toString()+ " kilo";
        newStory = newStory.replace("80 fahrenheit", temperature);
        newStory = newStory.replace("300 pounds",weight);
    }

    if (costumName.value !== ""){
        let input = costumName.value;
        newStory = newStory.replace("Bob",input);
    }

    let person = names[random()];
    let place = places[random()];
    let action = actions[random()];

    newStory = newStory.replace(/{person}/g,person);
    newStory = newStory.replace("{place}",place);
    newStory = newStory.replace("{action}",action);

    textClass.textContent = newStory;
    textClass.style.visibility = 'visible';
};