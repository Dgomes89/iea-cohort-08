#!/bin/bash
DIR=/home/dgomes/iea-cohort-08/02_linux_bash_scripting
cd /home/dgomes/iea-cohort-08/02_linux_bash_scripting
echo "type in a filename"
read filename
if [ -f "$filename" ]
then
echo "" > /dev/null
else
	echo "File is not found"
fi
