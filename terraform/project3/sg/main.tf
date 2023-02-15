resource "aws_security_group" "web_sg" {
  name   = "web_sg"
  vpc_id = var.vpc_id
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

locals {
  ports = [22, 80, 443]
}

resource "aws_security_group_rule" "ingress_rules" {
  count             = length(local.ports)
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.web_sg.id
  protocol          = "tcp"
  type              = "ingress"
  from_port         = local.ports[count.index]
  to_port           = local.ports[count.index]
}

resource "aws_security_group" "rds_sg" {
  name   = "rds_sg"
  vpc_id = var.vpc_id
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [var.cidr_block]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}