#!/bin/bash
clear
source ./face_recognition_env/bin/activate

shopt -s nullglob
array=(/dev/video*)
shopt -u nullglob


x="${array[@]}"

if ((${#array[@]} == 0)) 
then
	echo "No camera found"
else
	if (($? > 0))
	then
		echo $1
		echo ${x:10:-1}
		#python3 main.py ${$1:1}

		#echo $x

	else
		x = ${array[0]}
		echo "${array[@]}"
		#python3 main.py ${array[0]}
	fi
fi


