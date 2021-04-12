![build](https://github.com/46elks/praktik-apiskolan/actions/workflows/main.yml/badge.svg)


# APIskolan - Internship Version
A swedish learning platform on what APIs are and how to use them.

# Getting Started

## Installing Dependencies

If you are using Debian Linux, run this command **from the root folder of the repository** in your terminal to install all dependencies at once:

```bash
sudo apt-get install jq python3 python3-pip firefox nodejs npm && pip3 install -r requirements.txt && npm install
```

If you are not using Debian Linux, or if you wish to install these dependencies in a different way, here is a more easily read list of them:

#### apt packages:

- jq
- Python 3
- pip 3
- Firefox
- Node.js
- npm

#### pip packages:

- Selenium 3.141.0

#### npm packages:

- pug-cli 1.0.0-alpha6

Make sure you install all dependencies before working with this repository to ensure that everything will work as intended.

## Working with Pug

To automatically compile .pug files into .html files when saving your changes, run this command **from the root folder of the repository**:

```bash
pug -w ./src/pug/pug_example.pug -o ./dist -P
```

Make sure you replace "pug_example" with the name of the .pug file you want Pug to compile. The reason we specify a single file, instead of letting Pug watch the entire folder, is to avoid the files in the **/includes** folder being compiled into **/dist**.

## Working with SCSS

For compiling SCSS files, we use the Visual Studio Code extension *Live Sass Compiler*. To set up this extension correctly for working with this project, add these lines to the bottom of your Visual Studio Code **settings.json** file:

```json
"liveSassCompile.settings.formats": [
    {
        "format": "expanded",
        "extensionName": ".css",
        "savePath": "/dist"
    }
],
```
```json
"liveSassCompile.settings.generateMap": false,
```

Make sure these lines are added within the main curly brackets of the json file with **one step of indentation**, like the rest of the settings in **settings.json**.

This setup can also be achieved more simply by going to *Live Sass Compiler's* extension settings and clicking both the "Generate Map" setting and the "Formats" setting. This will automatically add these lines to your **settings.json** file. However, if you do it this way, make sure you **manually change** the "savePath" value from null to "/dist", like in the code block above.

## Live Server

To view a preview of your website live as you're making changes to it, we recommend the *Live Server* extension for Visual Studio Code. 

After installing the extension, navigate to the .html file you want a preview of. This would be **dist/index.html** for previewing the home page of the website. With the .html file of your choice open in the editor, click the "Go Live" button in the bottom right. This will open a live preview of the website in your default browser. 

This preview page will automatically refresh to display any new changes as they are saved.

## Remote Validation for HTML and CSS Documents

In the **tests** folder found in the root of this repository is a file called **run_validators.sh** and a folder called **validators** containing a remote HTML validator and a remote CSS validator. These files are able to automatically scan specified folders for HTML and CSS files and then send those scanned files as API requests to online validators. They then parse the response from the API before printing it in the terminal. These files are also compatible with *Continuous Integration systems*, since they purposefully exit themselves with different exit codes depending on the validation result.

The files **css_validator.sh** and **html_validator.sh** function in the same way. They take one argument representing the directory which to scan for files. The file **run_validators.sh** runs both of these two remote validators and specifies the folder for them. Because of this, make sure that you are in the same directory as **run_validators.sh** when you run the file.

If you are using Linux, these files can easily be run locally. From the root folder of the repository, run this command:

```bash
cd tests && ./run_validators.sh
```

## Automated Testing

To run all created automated tests manually, navigate to **tests/webtests** using the **cd** command in your terminal. Then, run this command:

```bash
python3 -m unittest
```

If you want to run a specific test, just add the file name at the end of the command like this:

```bash
python3 -m unittest test_example.py
```

For automated tests, we use *Selenium 3* for Python combined with Python's *unittest* module.

To create a new automated test in the same format as the others, follow these instructions:

- First, create a new Python file in the **tests/webtests** folder. The file name needs to start with "test_".
- Then, copy and paste this into the file:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestExample(WebTestBase):
    
    def test_example(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
```

- Replace every instance of the word "example" with test names of your choice. These do not have match the file name.

Now you're ready to start writing tests as you normally would in Selenium 3 for Python! Use classes for grouping tests within a file, and functions within classes for specific tests. The other automated tests should contain some hints as to how to structure this kind of code.

Keep in mind that using ```driver.get(self.WEBSITE_URL)``` will start the test environment on the home page (**index.html**). If you want the test environment to start on a different page, you can use the custom **get_url_to()** function. Here is an example:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestExample(WebTestBase):
    
    def test_example(self):
        driver = self.driver
        driver.get(self.get_url_to("my_page_name"))
```

This code will start the test on **my_page_name.html** instead, saving you the effort of manually navigating your way there using Selenium.

*geckodriver v0.29.0 is currently used for running these tests. If you find that the tests won't run, you may need to replace this geckodriver with a more recent version. Specific versions of geckodriver only function properly with specific versions of Firefox.*

## GitHub Workflows/Actions (CI)

This repository uses GitHub's system for *Continuous Integration*. This means that all static validation and automated tests run automatically on an online, GitHub provided, installation of Ubuntu every time there has been a push or pull request in the repository. There should be a **green check mark** or a **red cross** next to all your commits in the GitHub commit history, indicating if your commit has or hasn't passed all tests. Go to the **Actions** tab to view the output and status of these tests as they run.

Since the CI setup in this repository runs Python Unittest, any tests that are added in the **tests/webtests** folder will automatically be added to CI as well without additional setup. If you want to edit CI for any reason however, the YAML (.yml) file containing all instructions for CI are located in **.github/workflows**.

# Workflow

## Definition of Done

- All HTML and CSS code should pass **validation** with no errors.
- **Automated tests** should be written for each feature if applicable.
- All **automated tests** should pass.
- All team members should **understand the code** and be capable to make changes to it.
- Code should be **commented**.
- Proper **documentation** should be written if necessary.
- Code should be **pushed** to GitHub repository.

## Git Conventions

- **Feature Branches**.
- Everyone on site should **read through** each pull request before merging with the main branch.
- **Small commits**.
- If there's been more changes in a commit than what can fit in **under 50 characters**, extended commit descriptions should be used.
- **Feature branch naming conventions:**
    - Dashes in place of spaces.
    - No capital letters.
    - Short and concise branch names.
    - **Example:** my-feature-branch. 

## Coding Conventions

### General

- **Comments:** English, first letter capitalized. Space between comment symbol and comment.
- **Spaces:** 4
- **End of Line Sequence:** LF

### Naming Conventions

#### All

- **File Names:** snake_case

#### Python

- **Class Names:** PascalCase
- **Function Names:** snake_case
- **Function Arguments:** snake_case
- **Variable Names:** snake_case

#### HTML/CSS

- **Class Names:** kebab-case
- **ID Names:** camelCase
- **Variable Names:** kebab-case

#### JavaScript

- **Class Names:** camelCase
- **Variable Names:** camelCase

## Development Environment

- Visual Studio Code
    - Extensions:
        - Live Server
        - Code Spell Checker
        - Live Sass Compiler

## Coding Languages

- HTML 5
- CSS 3
- Python 3
- JavaScript

## Libraries, Frameworks, Language Extensions and Template Engines

- JQuery (JavaScript Library)
- Bootstrap 5 (CSS Framework)
- SCSS (CSS Language Extension)
- Pug (HTML Template Engine)
