#!/bin/bash

case ${1,,} in
	lucas | administrator)
		echo "Hello, you're the boss here!"
		;;
	help)
		echo "Just enter your username!"
		;;
	*)
		echo "Enter a valid username."
esac

		
