variable "bucket_name" {
  description = "Unique name for the S3 bucket (must be globally unique)"
  type        = string
}

variable "region" {
  description = "AWS region for the bucket (S3 website endpoints are region specific)"
  type        = string
  default     = "eu-central-1"
}
