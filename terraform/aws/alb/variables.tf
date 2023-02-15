# --- alb/variables.tf ---

variable "public_sg" {}
variable "public_subnets" {}

# --- aws_lb_target_group ---

variable "tg_port" {}
variable "tg_protocol" {}
variable "vpc_id" {}
variable "lb_healthy_threshold" {}
variable "lb_unhealthy_threshold" {}
variable "lb_timeout" {}
variable "lb_interval" {}

# --- aws_lb_listener ---

variable "listener_port" {}
variable "listener_protocol" {}


