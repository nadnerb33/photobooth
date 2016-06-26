#!/bin/bash



echo "Creating directory: "$1
mkdir $1
mkdir $1/frames

for i in {0..5}; do
	SECONDS=$(date +"%s")
	#echo $SECONDS
	fswebcam -r 320x240 --no-banner -q --greyscale -S 1 $1/frames/$SECONDS.jpg 
	echo "created frame"
done


if [ $2 = 1 ]; then
    	gm convert -modulate 100,0  -delay 30 $1/frames/*.jpg $1/$1.gif
	echo "created gif"
else
	echo "not converting to gif yet"
fi


