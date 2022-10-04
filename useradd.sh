#!/bin/bash
echo "Please enter the username you want to add:"
read username

if id "$username" &>/dev/null; then
    echo 'user found'
    exit 1
else
    sudo useradd -m $username
    if cat /etc/passwd | grep home/$username &>/dev/null; then
        echo -n 'The home directory of the user is created and it is /home/'
        echo $username
        exit 0
    else
	 echo 'There is something wrong when creating the user, please check!'
	 exit 2
    fi
fi
