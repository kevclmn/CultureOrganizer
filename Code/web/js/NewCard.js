function RequestCardInfo() {
  let Title;
  const InfoForm = document.createElemente("form");

  //Name question of form
  const CardNameQuestion = document.createElement("label");
  const NameInput = document.createElement("input");
  InfoForm.id = "Card-data";
  CardNameQuestion.textContent = "Name: ";
  NameInput.type = "text";
  NameInput.name = "name";
  CardNameQuestion.appendChild(NameInput);
  InfoForm.appendChild(CardNameQuestion);

  //Radio question of form
  const RadioQuestion = document.createElement("div"); //Contains Each Radio Option
  const RadioHeader = document.createElement("p");

  RadioQuestion.id = "Radio-questions";
  RadioHeader.textContent = "Card Type";
  InfoForm.appendChild(RadioHeader);

  //---- Firs option ----

  const RadioFilmContainter = document.createElement("div");
  const RadioFilmLabel = document.createElement("label");
  const RadioFilmInput = document.createElement("input");
  RadioFilmInput.type = "radio";
  RadioFilmInput.id = "Type-film-selector";
  RadioFilmInput.name = "card-type-selector";
  RadioFilmInput.value = "Film";
  RadioFilmLabel.for = "child";
  RadioFilmLabel.textContent = "Film";
  RadioFilmContainter.appendChild(RadioFilmInput, RadioFilmLabel);
  RadioQuestion.appendChild(RadioFilmContainter);

  //---- Second option ----

  const RadioBookContainter = document.createElement("div");
  const RadioBookLabel = document.createElement("label");
  const RadioBookInput = document.createElement("input");
  RadioBookInput.type = "radio";
  RadioBookInput.id = "Type-Book-selector";
  RadioBookInput.name = "card-type-selector";
  RadioBookInput.value = "Book";
  RadioBookLabel.for = "child";
  RadioBookLabel.textContent = "Film";
  RadioBookContainter.appendChild(RadioBookInput, RadioBookLabel);
  RadioQuestion.appendChild(RadioBookContainter);

  //---- Third option ----

  const RadioTheaterContainter = document.createElement("div");
  const RadioTheaterLabel = document.createElement("label");
  const RadioTheaterInput = document.createElement("input");
  RadioTheaterInput.type = "radio";
  RadioTheaterInput.id = "Type-Theater-selector";
  RadioTheaterInput.name = "card-type-selector";
  RadioTheaterInput.value = "Theater";
  RadioTheaterLabel.for = "child";
  RadioTheaterLabel.textContent = "Film";
  RadioTheaterContainter.appendChild(RadioTheaterInput, RadioTheaterLabel);
  RadioQuestion.appendChild(RadioTheaterContainter);

  //---- Fourth option ----

  const RadioPaintingContainter = document.createElement("div");
  const RadioPaintingLabel = document.createElement("label");
  const RadioPaintingInput = document.createElement("input");
  RadioPaintingInput.type = "radio";
  RadioPaintingInput.id = "Type-Painting-selector";
  RadioPaintingInput.name = "card-type-selector";
  RadioPaintingInput.value = "Painting";
  RadioPaintingLabel.for = "child";
  RadioPaintingLabel.textContent = "Painting";
  RadioPaintingContainter.appendChild(RadioPaintingInput, RadioPaintingLabel);
  RadioQuestion.appendChild(RadioPaintingContainter);
  //---- Final commit ----
  InfoForm.appendChild(RadioQuestion);

  //File question of form
  const FileQuestion = document.createElement("label");
  const FileInput = document.createElement("input");
  FileInput.type = "name";
  FileInput.name = "name";
  FileQuestion.textContent = "File:";
  FileQuestion.appendChild(FileInput);
  InfoForm.appendChild(FileQuestion);
}
function CreateNewCard() {
  const NewCard = document.createElement("div");
  const Img = document.createElement("img");
  const BentoGrid = document.getElementById("bento-grid");
  BentoGrid.appendChild(NewCard);
  NewCard.classList.add("bento-card", "card");
  NewCard.appendChild(Img);
  Img.src = "Files/Images/Icons/file-error-svgrepo-com.svg";
}
