# start the container

resource "random_string" "random" {
  count   = var.count_in
  length  = 4
  special = false
  upper   = false
}

resource "docker_container" "app_container" {
  count = var.count_in
  name  = join("_", [var.name_in, terraform.workspace, random_string.random[count.index].result])
  image = var.image_in
  ports {
    internal = var.int_port_in
    external = var.ext_port_in[count.index]
  }
  dynamic "volumes" {
    for_each = var.volumes_in
    content {
      container_path = volumes.value["container_path"]
      volume_name    = module.volume[count.index].volume_output[volumes.key]
    }

    # host_path = var.host_path_in
  }
  provisioner "local-exec" {
    # command = "echo ${self.name}: ${self.network_data[0].ip_address}:${self.ports[0].external})} >> container.txt"
    command = "echo ${self.name}: ${self.network_data[0].ip_address}:${join("", [for x in self.ports[*]["external"] : x])} >> container.txt"
    # on_failure = continue
  }

  provisioner "local-exec" {
    when    = destroy
    command = "rm -f container.txt"
    # on_failure = continue
  }
}

module "volume" {
  source       = "./volume"
  count        = var.count_in
  volume_count = length(var.volumes_in)
  volume_name  = "${var.name_in}-${terraform.workspace}-${random_string.random[count.index].result}-volume"
}