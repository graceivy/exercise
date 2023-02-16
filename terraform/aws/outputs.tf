# --- root/outputs.tf ---

output "load_balancer_endpoint" {
  value = module.alb.lb_endpoint
}

output "instances" {
  # value = {for i in range(length(module.compute.instance)): module.compute.instance[i].tags.Name => "${module.compute.instance[i].public_ip}: ${module.compute.port[i]}"}
  value     = { for i in module.compute.instance : i.tags.Name => "${i.public_ip}:${module.compute.instance_port}" }
  sensitive = true
}

output "kubeconfig" {
  value = [ for i in module.compute.instance : "export KUBECONFIG=../k3s-${i.tags.Name}.yaml"]
  sensitive = true
}
