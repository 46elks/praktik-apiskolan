#!/bin/bash

# Makes sure an argument in the form of folder to validate is provided.
if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit 1
fi

# Goes through all files ending in .html.
for file in $(find $1 -iname '*.html'); do
    # Sends a HTML validation request to the validator.w3.org API. Return the data in JSON format.
    data=`curl -s -H "Content-Type: text/html" \
    --data-binary @$file \
    https://validator.w3.org/nu/?out=json \
    \;`
    if [[ $data == *"type"* ]]; then
        # If the result data contains the text "type", an error has occured.
        # In this case, print the error and return 1 as exit status.
        echo "Error(s) in $file:"
        echo $data | jq .
        exit 1
    fi
done
# No errors in validation, return 0 as exit status.
echo "No errors in HTML-document(s)"
exit 0
