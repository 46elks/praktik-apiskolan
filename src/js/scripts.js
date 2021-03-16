function showQuizResult(){
    let quiz = document.quiz;
    let value = quiz.question.value;

    if (value==quiz.getAttribute("data-answer"))
        alert("Rätt");
    else
        alert("Fel");
}
