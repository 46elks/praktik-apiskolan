function showQuizResult(quizname) {
    let quiz = document.getElementsByName(quizname)[0]
    let value = quiz.question.value;

    if (value==quiz.getAttribute("data-answer"))
        alert("Rätt svar!");
    else
        alert("Fel svar.");
}
