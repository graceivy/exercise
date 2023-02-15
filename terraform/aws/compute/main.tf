# --- compute/main.tf ---

data "aws_ami" "server_ami" {
  most_recent = true
  owners      = ["137112412989"]

  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm-*-x86_64-gp2"]
  }
}

resource "random_id" "mtc_node_id" {
  byte_length = 2
  count       = var.instance_count
  # If the key_name changes, the random_id must be destroyed and created again
  keepers = {
    key_name = var.key_name
  }
}

resource "aws_key_pair" "mtc_auth" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_instance" "mtc_node" {
  count         = var.instance_count #1
  ami           = data.aws_ami.server_ami.id
  instance_type = var.instance_type # t3.micro

  tags = {
    Name = "mtc_node-${random_id.mtc_node_id[count.index].dec}"
  }

  key_name               = aws_key_pair.mtc_auth.id
  vpc_security_group_ids = var.public_sg
  subnet_id              = var.public_subnets[count.index]
  user_data = templatefile(var.user_data_path, {
    nodename    = "mtc-${random_id.mtc_node_id[count.index].dec}"
    db_endpoint = var.db_endpoint
    dbuser      = var.dbuser
    dbpass      = var.dbpassword
    dbname      = var.dbname
  })
  root_block_device {
    volume_size = var.vol_size # 10
  }
}

resource "aws_lb_target_group_attachment" "mtc_tg_attach" {
  count = var.instance_count
  target_group_arn = var.lb_target_group_arn
  target_id        = aws_instance.mtc_node[count.index].id
  port             = var.tg_port
}

