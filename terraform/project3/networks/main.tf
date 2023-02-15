# --- networks/main.tf ---

resource "aws_vpc" "my_vpc" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "my-vpc"
  }
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_subnet" "my_subnets" {
  count                   = var.subnet_number
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = ["10.10.2.0/24", "10.10.4.0/24", "10.10.1.0/24", "10.10.3.0/24"][count.index]
  map_public_ip_on_launch = count.index < 2 # 0,1 for public subnet, 2, 3 for private subnet
  availability_zone       = ["us-east-1a", "us-east-1b"][count.index % 2]

  tags = {
    Name = "my-subnet-${count.index + 1}"
  }
}

resource "aws_internet_gateway" "my_internet_gateway" {
  vpc_id = aws_vpc.my_vpc.id

  tags = {
    Name = "my_igw"
  }
}

resource "aws_route_table" "my_public_rt" {
  vpc_id = aws_vpc.my_vpc.id

  tags = {
    Name = "my_public"
  }
}

resource "aws_route" "default_route" {
  route_table_id         = aws_route_table.my_public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.my_internet_gateway.id
}

resource "aws_route_table_association" "my_public_assoc" {
  count          = 2
  subnet_id      = aws_subnet.my_subnets.*.id[count.index]
  route_table_id = aws_route_table.my_public_rt.id
}

resource "aws_default_route_table" "my_private_rt" {
  default_route_table_id = aws_vpc.my_vpc.default_route_table_id

  tags = {
    Name = "my_private"
  }
}

resource "aws_db_subnet_group" "my_rds_subnetgroup" {
  name       = "my_rds_subnetgroup"
  subnet_ids = slice(aws_subnet.my_subnets.*.id, 2, 4)

  tags = {
    Name = "mtc_rds_sng"
  }
}
