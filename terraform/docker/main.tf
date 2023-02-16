module "image" {
  source   = "./images"
  for_each = local.deployment
  image_in = each.value.image
}

# start the container

module "container" {
  source = "./container"
  # depends_on = [null_resource.dockervol]
  for_each = local.deployment
  count_in = each.value.container_count
  name_in  = each.key
  image_in = module.image[each.key].image_out

  int_port_in = each.value.int
  ext_port_in = each.value.ext
  volumes_in  = each.value.volumes
  # container_path_in = each.value.container_path
  # host_path_in = "${path.cwd}/dockervol"
}




