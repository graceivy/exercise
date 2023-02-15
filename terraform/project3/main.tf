module "ec2_instance" {
  ami_in               = var.ami_in
  public_subnet_number = var.public_subnet_number
  source               = "./ec2"
  instance_type_in     = var.instance_type_in
  sg_group_in          = [module.sg.web_sg_id]
  subnet_id            = module.networks.subnet_ids
}

module "sg" {
  source     = "./sg"
  vpc_id     = module.networks.vpc_id
  cidr_block = var.cidr_block
}

module "networks" {
  subnet_number = var.public_subnet_number + var.private_subnet_number
  source        = "./networks"
  cidr_block    = var.cidr_block
}

module "rds" {
  source                     = "./rds"
  db_storage                 = 10
  db_engine_version          = "5.7"
  db_instance_class          = "db.t2.micro"
  dbname                     = var.dbname
  dbuser                     = var.dbuser
  dbpassword                 = var.dbpassword
  db_subnet_group_name       = module.networks.db_subnet_group_name
  private_security_group_ids = [module.sg.rds_sg_id]
  db_identifier              = "my-db"
  skip_db_snapshot           = true
}