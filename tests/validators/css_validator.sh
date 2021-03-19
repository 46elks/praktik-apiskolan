#!/bin/bash

# Makes sure an argument in the form of folder to validate is provided.
if [ "$1" == "" ]; then
    echo -e "Please provide the folder which to scan for files like this:\n\t$0 [FOLDER]"
    exit 1
fi

let "file_amount=0"

# Goes through all files ending in .css.
for file in $(find $1 -iname '*.css'); do
    let "file_amount++"

    # Sends a CSS validation request to the jigsaw.w3.org API. Return the data in plain text format.
    data=`curl -s -H "Content-Type: multipart/form-data" \
        -F "text=<$file;type=text/plain" \
        -F "profile=css3" \
        -F "output=json" \
        https://jigsaw.w3.org/css-validator/validator`
    json=`jq .cssvalidation <<< "$data"`
    # Checks if any errors occured.
    error_count=`echo $json | jq .result.errorcount`

    if [ -z "$error_count" ]; then
        echo "Failed getting response from CSS validation API. Try again!"
        exit 1

    elif [ "$error_count" -gt 0 ]; then
        # Prints any errors that are found.
        echo "Error(s) in $file:"
        echo
        for i in $(seq 0 `expr $error_count - 1`); do
            error=`echo $json | jq .errors[$i]`
            echo "$(echo $error | jq -r .context): L$(echo $error | jq -r .line) {type: $(echo $error | jq -r .type)}"
            echo -e "\t $(echo $error | jq -r .message)"
        done
        echo 
        exit 1
    fi
done

if [ $file_amount != 0 ]; then
    echo "No errors in CSS file(s)"
    exit 0
else
    echo "No CSS files found"
    exit 1
fi
