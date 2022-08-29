#!/bin/bash

read -p "what file path: "  t

read -p "what is the file: " file

for i in $t:

do

    if  [ -f $file  ]

    then

        echo 'Check'

    else

        echo "file not found"

    fi

done
