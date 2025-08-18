# Azure CI/CD Pipeline with AKS
Skeleton project demonstrating:
- Containerized sample app (Flask)
- GitHub Actions workflow to build, test, and push image to ACR
- AKS deployment manifests
- Use Azure Key Vault (placeholder)

## Files
- app/app.py : simple Flask app
- Dockerfile : builds the app
- .github/workflows/ci-cd.yml : sample GitHub Actions workflow
- k8s/ : AKS manifests
