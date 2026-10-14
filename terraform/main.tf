terraform {
  required_version = ">= 1.0.0"
}

# This represents your multi-environment configuration logic
resource "terraform_data" "environment_check" {
  input = var.environment
}

output "deployment_summary" {
  value = "Environment: ${var.environment} | Scale: ${var.instance_count} instances"
}