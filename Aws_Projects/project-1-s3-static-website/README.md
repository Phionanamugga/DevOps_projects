# Project 1 — Static Website Hosting (S3) — Starter Template

**What this project shows (AWS Cloud Practitioner concepts):**
- AWS global infrastructure & core services (Amazon S3)
- Security & IAM (bucket policy for public website hosting)
- Pricing model (pay-per-use, storage and data transfer)
- Scalability and durability (S3 storage class basics)

**What's included**
- `index.html` — sample static website content
- `main.tf` — Terraform configuration to create an S3 website bucket and a bucket policy
- `variables.tf` — Terraform variables for customization
- `outputs.tf` — Terraform outputs
- `deploy.sh` — helper script to upload website files to the bucket using AWS CLI (local credentials required)
- `README.md` — (this file)

**Prerequisites (local machine)**
- Terraform installed (v1.0+ recommended)
- AWS CLI configured with credentials that have permission to create S3 buckets and put objects
- (Optional) An AWS account with access to create resources

**Quick usage**
1. Edit `variables.tf` to set `bucket_name` (must be globally unique).
2. Run:
   ```bash
   terraform init
   terraform apply -var="bucket_name=your-unique-bucket-name" -auto-approve
   ```
3. After Terraform finishes, run the deploy script to upload website content:
   ```bash
   ./deploy.sh your-unique-bucket-name
   ```
4. The website will be available at the S3 website endpoint printed by Terraform outputs (or at `http://<bucket-name>.s3-website-<region>.amazonaws.com`).

**Notes & extensions**
- For production, use CloudFront (CDN) + ACM certificate (requires additional steps and region-specific cert setup).
- The template uses a public bucket policy for simple demo purposes. In real projects prefer using CloudFront + Origin Access Identity (OAI) to restrict direct access to S3.
- The `deploy.sh` script expects AWS credentials configured locally (e.g., via `aws configure` or environment variables).

**Security reminder**
- Don't commit AWS credentials into source control.
- Clean up resources after testing to avoid charges: `terraform destroy -var="bucket_name=your-unique-bucket-name" -auto-approve`
