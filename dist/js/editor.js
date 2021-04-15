// Retrieve Elements
const executeCodeButton = document.querySelector(".editor-run");
const resetCodeButton = document.querySelector(".editor-reset");

// Setup Ace
let codeEditor = ace.edit("editorCode");
let defaultCode = 'console.log("Hello World!")';

let editorLib = {
    init() {
        // Configure Ace

        // Theme
        codeEditor.setTheme("ace/theme/dracula");

        // Set language
        codeEditor.session.setMode("ace/mode/javascript");

        // Set Options
        codeEditor.setOptions({
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
        });

        // Set default Code
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
    // Clear ace editor
    codeEditor.setValue(defaultCode);
});

editorLib.init();
