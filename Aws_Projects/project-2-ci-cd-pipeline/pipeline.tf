terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}
provider "aws" { region = "eu-central-1" }
# Simplified CodePipeline skeleton (user must fill in GitHub details)
resource "aws_codepipeline" "demo" {
  name     = "demo-pipeline"
  role_arn = "REPLACE_WITH_IAM_ROLE_ARN"
  artifact_store {
    location = "REPLACE_WITH_S3_BUCKET"
    type     = "S3"
  }
  # Stages omitted for brevity
}
