variable "environment" {
  type        = string
  description = "The deployment environment (qa, uat, prod)"
}

variable "instance_count" {
  type        = number
  description = "Number of app instances to run"
}