# --- root/locals.tf ---

locals {
  vpc_cidr = "10.0.0.0/16"
}

locals {
  security_groups = {
    public = {
      name        = "public_sg"
      description = "Security Group for Public Access"
      ingress = {
        ssh = {
          from_port   = "22"
          to_port     = "22"
          protocol    = "tcp"
          cidr_blocks = [var.access_ip]
        }

        http = {
          from_port   = "80"
          to_port     = "80"
          protocol    = "tcp"
          cidr_blocks = [var.access_ip]
        }

        nginx = {
          from_port   = "8000"
          to_port     = "8000"
          protocol    = "tcp"
          cidr_blocks = [var.access_ip]
        }

      }
    }

    rds = {
      name        = "rds_sg"
      description = "Security Group for RDS Access"
      ingress = {
        ssh = {
          from_port   = "3306"
          to_port     = "3306"
          protocol    = "tcp"
          cidr_blocks = [local.vpc_cidr]
        }

      }
    }

  }
}