// Retrieve Elements
const executeCodeButton = document.querySelector(".editor-run");
const resetCodeButton = document.querySelector(".editor-reset");

// Setup Ace
let codeEditor = ace.edit("editorCode");
let defaultCode = 'console.log("Hello World!", true, 100)';
let consoleMessages = [];

let editorLib = {
    init() {
        // Configure Ace

        // Theme
        codeEditor.setTheme("");

        // Set Language
        codeEditor.session.setMode("ace/mode/javascript");

        // Set Options
        codeEditor.setOptions({
            fontSize: '14pt',
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
        });

        // Set Default Code
        codeEditor.setValue(defaultCode)
    }
}

// Events
executeCodeButton.addEventListener('click', () => {
    // Get input from the code editor
    const userCode = codeEditor.getValue();

    // Run the user code
    try {
        new Function(userCode)();
    } catch (err) {
        console.error(err);
    }
});

resetCodeButton.addEventListener('click', () => {
    // Clear Ace Editor
    codeEditor.setValue(defaultCode);
});

editorLib.init();
