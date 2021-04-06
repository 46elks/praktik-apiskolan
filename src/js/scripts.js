function showQuizResult(quizName) {
    let quiz = document.getElementsByName(quizName)[0];
    let quizValue = quiz.quizOption.value;
    let quizAnswer = quiz.getAttribute("data-answer")
    let quizAnswerText = quiz.querySelector('[value="' + quizAnswer + '"]').parentElement.textContent.trim();

    if (quizValue==quizAnswer)
        alert("Rätt svar. Bra jobbat!");
    else
        alert('Nästan! Rätt svar är "' + quizAnswerText + '"');
}
