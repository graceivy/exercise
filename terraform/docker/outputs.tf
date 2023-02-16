# output "IP_Address_port" {
#   value       = flatten(module.container[*].IP_Address_port)
#   description = "IP address and the external port of the container"
# }

# output "container_name" {
#   value       = module.container[*].container_name
#   description = "Name of the container"
# }

output "application_access" {
  value = module.container[*]
  # value = [for x in module.container[*]: x]
  description = "The name and socket for each application."
}