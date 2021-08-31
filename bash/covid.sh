#!/bin/bash
# This script will query covid data and display it 

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative') 

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive, $NEGATIVE negative, COVID cases" 
