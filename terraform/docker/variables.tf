variable "image" {
  type        = map(any)
  description = "Image for container"
  default = {
    nodered = {
      dev  = "nodered/node-red:latest"
      prod = "nodered/node-red:latest-minimal"
    }
    influxdb = {
      dev  = "quay.io/influxdb/influxdb:v2.0.2"
      prod = "quay.io/influxdb/influxdb:v2.0.2"
    }
    grafana = {
      dev  = "grafana/grafana"
      prod = "grafana/grafana"
    }
  }
}

variable "ext_port" {
  type = map(any)

  # validation {
  #   condition     = max(var.ext_port["nodered"]["dev"]...) <= 65535 && min(var.ext_port["dev"]...) >= 1980
  #   error_message = "The ext_port must be in the valid port range from 0 to 65535."
  # }

  # validation {
  #   condition     = max(var.ext_port["nodered"]["prod"]...) < 1980 && min(var.ext_port["prod"]...) >= 1880
  #   error_message = "The prod ext_port must be in the valid port range from 1880 to 1979."
  # }
}

# variable "int_port" {
#   type    = number
#   default = 1880

#   validation {
#     condition     = var.int_port == 1880
#     error_message = "The int_port must be 1880."
#   }
# }
