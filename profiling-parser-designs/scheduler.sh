#!/bin/bash 
: '
Uncomment to profile the modules outputs.
'

COUNTER=0
while [ $COUNTER -lt 10 ]; do
    echo "Hitting endpoints for the $COUNTER time"
    make p_lxml
    time
    let COUNTER=COUNTER+1 
    sleep 6
done