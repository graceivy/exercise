resource "aws_instance" "my_server" {
  count         = var.public_subnet_number
  ami           = var.ami_in
  instance_type = var.instance_type_in
  subnet_id     = var.subnet_id[count.index]
  tags = {
    Name = "my-ec2-${count.index + 1}"
  }
  vpc_security_group_ids = var.sg_group_in
  user_data              = <<EOF
    #!/bin/bash
  	yum update -y
  	yum install -y httpd.x86_64
  	systemctl start httpd.service
  	systemctl enable httpd.service
  	echo “Hello World from Pingping” > /var/www/html/index.html
    EOF
}