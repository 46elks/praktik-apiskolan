// Hide all elements with specific ID outside of home page.
$('#hideOutsideHomePage').hide()
$(function(){
    if (window.location.pathname == "/dist/index.html" || window.location.pathname == "/dist/") {
          $('#hideOutsideHomePage').show();
    }
});


// Quiz System
function showQuizResult(quizName) {
    let quiz = document.getElementsByName(quizName)[0];
    let quizValue = quiz.quizOption.value;

    if (quizValue==quiz.getAttribute("data-answer"))
        alert("Rätt svar!");
    else
        alert("Fel svar.");
}
