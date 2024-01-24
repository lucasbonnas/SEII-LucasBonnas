#!/bin/bash

if [ ${1,,} = lucas ]; then
	echo "Oh, you're the boos here. Welcome!"
elif [ ${1,,} = help ]; then
	echo "Just enter your username."
else 
	echo "I don't know who you are."
fi


