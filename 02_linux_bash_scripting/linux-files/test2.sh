#!/bin/bash

cd /home/dgomes/iea-cohort-08/02_linux_bash_scripting

for i in 1 2 3
do

echo "Enter File Name"
read filename
    
  if [[ ! -f $filename ]]
  then
    echo "The file ${filename} does not exist!"
  fi
done
