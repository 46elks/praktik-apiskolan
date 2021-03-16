function showQuizResult(quizname) {
    let quiz = document.getElementsByName(quizname)[0];
    let quizValue = quiz.quizOption.value;

    if (quizValue==quiz.getAttribute("data-answer"))
        alert("Rätt svar!");
    else
        alert("Fel svar.");
}
