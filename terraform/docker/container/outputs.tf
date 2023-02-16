# output "IP_Address_port" {
#   value       = [for container in docker_container.container[*] : join(":", [container.network_data[0].ip_address, container.ports[0].external])]
#   description = "IP address and the external port of the container"

# }

# output "container_name" {
#   value       = docker_container.nodered_container.name
#   description = "Name of the container"
# }

output "application_access" {
  value = { for container in docker_container.app_container[*] : container.name => join(":", [container.network_data[0].ip_address, container.ports[0].external]) }
}