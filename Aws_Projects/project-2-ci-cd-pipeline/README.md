# Project 2 — CI/CD Pipeline with CodePipeline & CodeBuild

**Concepts covered:**
- Developer tools (CodePipeline, CodeBuild)
- Continuous integration & delivery
- IAM roles & permissions
- Pay-per-use model for builds

**Included files:**
- `pipeline.tf` — Terraform config for CodePipeline
- `buildspec.yml` — CodeBuild build instructions
- `README.md`

**Usage:**
1. Update `pipeline.tf` with your GitHub repo info.
2. Run `terraform init && terraform apply`.
3. Push code → pipeline triggers → build → deploy.

**Cleanup:**
Run `terraform destroy` to avoid charges.
