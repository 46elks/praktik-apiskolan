![CI](https://github.com/46elks/praktik-apiskolan/actions/workflows/main.yml/badge.svg)


# APIskolan - Internship Version
APIskolan.se - a resource for developers by developers.

# Getting Started

## Installing Dependencies (Linux)

When working with this repository, run this command **from the root folder of this repository** in your terminal to ensure that everything will work as intended:

```bash
sudo apt-get install jq python3 python3-pip firefox && pip3 install -r requirements.txt
```

Here is a more easily read list of all dependencies, if you wish to install them in a different way:

apt packages:

- jq
- Python 3
- pip 3
- Firefox

pip packages:

- Selenium 3

## Working with Sass/SCSS

For compiling Sass/SCSS files, we use the Visual Studio Code extension *Live Sass Compiler*. To set up this extension correctly for working with this project, add these lines to the bottom of your Visual Studio Code **settings.json** file:

```json
"liveSassCompile.settings.formats": [
    {
        "format": "expanded",
        "extensionName": ".css",
        "savePath": "/public"
    }
],
```
```json
"liveSassCompile.settings.generateMap": false,
```

Make sure these lines are added within the main curly brackets of the json file with **one step of indentation**, like the rest of the settings in **settings.json**.

This setup can also be achieved more simply by going to *Live Sass Compiler's* extension settings and clicking both the "Generate Map" setting and the "Formats" setting. This will automatically add these lines to your **settings.json** file. However, if you do it this way, make sure you **manually change** the "savePath" value from null to "/public", like in the code block above.

## Remote Validation for HTML and CSS Documents

In the **tests** folder found in the root of this repository is a file called **run_validators.sh** and a folder called **validators** containing a remote HTML validator and a remote CSS validator. These files are able to automatically scan specified folders for HTML and CSS files and then send those scanned files as API requests to online validators. They then parse the response from the API before printing it in the terminal. These files are also compatible with *Continuos Integration systems*, since they purposefully exit themselves with different exit codes depending on the validation result.

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

## GitHub Workflows/Actions (CI)

This repository uses GitHub's system for *Continuos Integration*. This means that all static validation and automated tests run automatically on an online, GitHub provided, installation of Ubuntu every time there has been a push or pull request in the repository. There should be a **green check mark** or a **red cross** next to all your commits in the GitHub commit history, indicating if your commit has or hasn't passed all tests. Go to the **Actions** tab to view the output and status of these tests as they run.

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
- **Feature branch naming conventions:**
    - Dashes in place of spaces.
    - No capital letters.
    - Short and concise branch names.
    - **Example:** my-feature-branch. 

## Coding Conventions

- **Comments:** English, first letter capitalized. Space between comment symbol and comment.
- **Spaces:** 4
- **End of Line Sequence:** LF

## Development Environment

- Visual Studio Code
    - Extensions:
        - Live Server
        - Live Sass Compiler
        - Code Spell Checker

## Languages

- HTML 5
- CSS 3
- SCSS
