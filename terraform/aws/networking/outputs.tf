# --- networking/output.tf ---

output "vpc_security_group_ids" {
  # value = [for sg in aws_security_group.mtc_sg: sg.id]
  value = [aws_security_group.mtc_sg["rds"].id]
}

output "public_security_group_ids" {
  # value = [for sg in aws_security_group.mtc_sg: sg.id]
  value = [aws_security_group.mtc_sg["public"].id]
}

output "db_subnet_group_name" {
  value = aws_db_subnet_group.mtc_rds_subnetgroup[0].name
}

output "vpc_id" {
  value = aws_vpc.mtc_vpc.id
}

output "public_subnet_id" {
  value = aws_subnet.mtc_public_subnet.*.id
}

