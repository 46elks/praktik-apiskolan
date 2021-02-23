#!/bin/bash

folder=".."

echo "VALIDATING ALL HTML FILES"
echo
./validators/html_validator.sh $folder

echo
echo

echo "VALIDATING ALL CSS FILES"
echo
./validators/css_validator.sh $folder

echo
echo

echo "VALIDATION COMPLETE"