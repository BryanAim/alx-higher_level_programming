#!/bin/bash
# A script POSt Header variable to the URL email, subject
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
