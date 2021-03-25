// Hide all elements with specific ID outside of home page.
$(function(){
    console.log(window.location.pathname)
    if (window.location.pathname != "/dist/index.html" && window.location.pathname != "/dist/") {
          $('#hideOutsideHomePage').hide();
    } else {
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
