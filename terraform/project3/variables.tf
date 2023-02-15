# --- root/variables.tf ---

variable "ami_in" {
  type    = string
  default = "ami-0aa7d40eeae50c9a9"
}

variable "instance_type_in" {
  type    = string
  default = "t2.micro"
}

variable "aws_region" {
  default = "us-east-1"
}

# --- database variables ---

variable "dbname" {
  type = string
}

variable "dbuser" {
  type      = string
  sensitive = true
}

variable "dbpassword" {
  type      = string
  sensitive = true
}

variable "public_subnet_number" {
  type    = number
  default = 2
}

variable "private_subnet_number" {
  type    = number
  default = 2
}

variable "cidr_block" {
  type    = string
  default = "10.10.0.0/16"
}
