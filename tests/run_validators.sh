#!/bin/bash

folder=".."

exit_code=0

echo "VALIDATING ALL HTML FILES"
echo
./validators/html_validator.sh $folder

if [ $? != 0 ]; then
    exit_code=1
fi

echo
echo

echo "VALIDATING ALL CSS FILES"
echo
./validators/css_validator.sh $folder

if [ $? != 0 ]; then
    exit_code=1
fi

echo
echo

echo "VALIDATION COMPLETE"

exit $exit_code
