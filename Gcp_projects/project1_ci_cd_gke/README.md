# CI/CD on GCP with GKE (Project 1)
This scaffold demonstrates:
- Terraform to provision GKE, Artifact Registry, and Cloud SQL (placeholder configs).
- Dockerized microservices: backend (Node.js) and frontend (React).
- Kubernetes manifests for deployments + services.
- GitHub Actions workflow to build, push to Artifact Registry, and deploy to GKE using `kubectl`.

**Warning:** Terraform files use placeholders. Review and replace with your GCP project id, region, and credentials.
