# --- compute/variables.tf ---

variable "instance_count" {}
variable "instance_type" {}
variable "public_sg" {}
variable "public_subnets" {}
variable "vol_size" {}

# --- key pair ---
variable "key_name" {}
variable "public_key_path" {}

# --- userdata ---
variable "user_data_path" {}
variable "db_endpoint" {}
variable "dbuser" {}
variable "dbpassword" {}
variable "dbname" {}


# --- target group attachment ---
variable "lb_target_group_arn" {}
variable "tg_port" {}

# --- provisioner ---
variable "private_key_path" {}
