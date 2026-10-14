output "current_environment" {
  value = "Successfully deployed infrastructure for: ${var.environment}"
}

output "replicas_configured" {
  value = var.instance_count
}