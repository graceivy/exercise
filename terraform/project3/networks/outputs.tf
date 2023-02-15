output "vpc_id" {
  value = aws_vpc.my_vpc.id
}

output "subnet_ids" {
  value = aws_subnet.my_subnets.*.id
}

output "db_subnet_group_name" {
  value = aws_db_subnet_group.my_rds_subnetgroup.name
}