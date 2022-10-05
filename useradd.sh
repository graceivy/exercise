#!/bin/bash
if [ $# -lt 1 ]
then
        echo "No user to be added"
else	
	for username in $@
	do
		if id "$username" &>/dev/null; then
		    echo 'user found'
		else
		    sudo useradd -m $username
		    if cat /etc/passwd | grep home/$username &>/dev/null; then
			echo -n 'The home directory of the user is created and it is /home/'
			echo $username
		    else
			 echo 'There is something wrong when creating the user, please check!'
		    fi
		fi
	done
fi
