# APIskolan - Internship Version
APIskolan.se - a resource for developers by developers.

## Installing Dependencies (Linux)

When working with this repository, run this command in your terminal to ensure that everything will work as intended:

```bash
sudo apt-get install jq
```
## Remote Validation for HTML and CSS Documents

In the **tests** folder found in the root of this repository is a file called **run_validators.sh** and a folder called **validators** containing a remote HTML validator and a remote CSS validator. These files are able to automatically scan specified folders for HTML and CSS files and then send those scanned files as API requests to online validators. They then parse the response from the API before printing it in the terminal. These files are also compatible with *Continuos Integration systems*, since they purposefully exit themselves with different exit codes depending on the validation result.

The files **css_validator.sh** and **html_validator.sh** function in the same way. They take one argument containing the directory which to scan for files. The file **run_validators.sh** runs both of these two remote validators and specifies the folder for them. Because of this, make sure that you are in the same directory as **run_validators.sh** when you run the file.

If you are using Linux, these files can easily be run locally. From the root folder of the repository, run this command:

```bash
cd tests && ./run_validators.sh
```

## Definition of Done

- All team members should **understand the code** and be capable to make changes to it.
- Code should be **commented**.
- **Automated tests** should be written for each feature if applicable.
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

## Languages

- HTML5
- CSS3
