// Retrieve Elements
const consoleLogList = document.querySelector(".editor-console-logs");
const executeCodeButton = document.querySelector(".editor-run");
const resetCodeButton = document.querySelector(".editor-reset");

// Setup Ace
let codeEditor = ace.edit("editorCode");
let defaultCode = 'console.log("Hello World!");';
let consoleMessages = [];

let editorLib = {
    clearConsoleScreen() {
        consoleMessages.length = 0;

        // Remove all elements in the log list
        while (consoleLogList.firstChild) {
            consoleLogList.removeChild(consoleLogList.firstChild);
        }

    },
    printToConsole() {
        consoleMessages.forEach(log => {
            const newLogItem = document.createElement('li');
            const newLogText = document.createElement('pre');

            newLogText.className = log.class;
            newLogText.textContent = `>  ${log.message}`;

            newLogItem.appendChild(newLogText);

            consoleLogList.appendChild(newLogItem);
        })

    },
    init() {
        // Configure Ace
        
        // Worker
        ace.config.setModuleUrl('ace/mode/javascript_worker', 'https://pagecdn.io/lib/ace/1.4.12/worker-javascript.min.js')

        // Theme
        codeEditor.setTheme("ace/theme/dreamweaver");

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
    // Clear console massages
    editorLib.clearConsoleScreen();

    // Get input from the code editor
    const userCode = codeEditor.getValue();

    // Run the user code
    try {
        new Function(userCode)();
    } catch (err) {
        console.error(err);
    }

    // Print to the console
    editorLib.printToConsole();
});

resetCodeButton.addEventListener('click', () => {
    // Clear Ace Editor
    codeEditor.setValue(defaultCode);

    // Clear console massages
    editorLib.clearConsoleScreen();
});

editorLib.init();
