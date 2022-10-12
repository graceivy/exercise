#!/bin/bash
#sudo yum update -y
#sudo yum install -y httpd.x86_64
#sudo systemctl start httpd.service
#sudo systemctl enable httpd.service
#sudo chmod 777 /usr/share/httpd/noindex/index.html 
#sudo bash -c ‘echo “Greetings from Pingping! Hello my friends~” > /usr/share/httpd/noindex/index.html’
echo “Greetings from Pingping! Hello my friends~” | sudo tee /usr/share/httpd/noindex/index.html
