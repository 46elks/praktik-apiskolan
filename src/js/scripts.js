function showQuizResult(quizName) {
    let quiz = document.getElementsByName(quizName)[0];
    let quizValue = quiz.quizOption.value;

    if (quizValue==quiz.getAttribute("data-answer"))
        alert("Rätt svar!");
    else
        alert("Fel svar.");
}
