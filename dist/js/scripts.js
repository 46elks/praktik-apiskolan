function showQuizResult(quizName) {
    const quiz = document.getElementsByName(quizName)[0];
    const quizValue = quiz.quizOption.value;
    const quizAnswer = quiz.getAttribute("data-answer")
    const quizAnswerText = quiz.querySelector('[value="' + quizAnswer + '"]').parentElement.textContent.trim();

    if (quizValue==quizAnswer)
        alert("Rätt svar, bra jobbat!");
    else
        alert('Nästan! Rätt svar är "' + quizAnswerText + '".');
}
