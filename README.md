# 🚀 DevOps Projects Portfolio  

Welcome to my **DevOps Projects Portfolio**!  
This repository demonstrates my hands-on experience with **multi-cloud DevOps practices** across **AWS, Azure, and Google Cloud (GCP)**.  

Each project folder contains:  
- Source code / configuration files  
- Infrastructure-as-Code (Terraform / CloudFormation / ARM/Bicep)  
- Step-by-step deployment guide in README.md  

---

## 📂 Project List  

### 🌐 AWS Projects  
1. **Static Website Hosting on S3 + CloudFront**  
   Host a personal portfolio site on Amazon S3 with CloudFront and Route 53.  
   *Skills: Storage, Networking, CDN*  

2. **CI/CD Pipeline with CodePipeline + CodeBuild**  
   Automate builds and deployments to Elastic Beanstalk.  
   *Skills: CI/CD*  

3. **EC2 Web Server Setup**  
   Launch an EC2 instance with Apache/Nginx using User Data.  
   *Skills: Compute, Networking, IAM*  

4. **IAM Roles & Policies**  
   Define least privilege IAM roles (Admin, Developer, Auditor).  
   *Skills: Security, Governance*  

5. **CloudWatch Monitoring & Alerts**  
   Monitor EC2 instance health with CloudWatch dashboards and alarms.  
   *Skills: Monitoring, Reliability*  

6. **AWS Backup & Disaster Recovery**  
   Automate EBS snapshots and enable S3 cross-region replication.  
   *Skills: High Availability*  

7. **AWS Budgets & Cost Explorer**  
   Set up budgets and tagging for cost tracking.  
   *Skills: Cost Management*  

8. **Resource Tagging & Organization**  
   Apply tags for environments (Dev, Test, Prod).  
   *Skills: Governance, Optimization*  

9. **Serverless App with Lambda + API Gateway**  
   CRUD REST API using API Gateway + Lambda + DynamoDB.  
   *Skills: Serverless, NoSQL*  

10. **Event-Driven Notifications with SNS & SQS**  
    Build an event-driven notification system.  
    *Skills: Messaging, Decoupling*  

11. **Auto Scaling Group + Load Balancer**  
    Deploy a scalable web app with Auto Scaling + ALB.  
    *Skills: Scalability, HA*  

12. **VPC Setup with Public/Private Subnets**  
    Secure networking with NAT, Security Groups, and subnetting.  
    *Skills: Networking, Security*  

---

### ☁️ Google Cloud Projects  
13. **CI/CD Pipeline on GCP with GKE**  
    Microservices app with Docker, Terraform, and GitHub Actions CI/CD.  
    *Skills: Kubernetes, Terraform, CI/CD*  

14. **GitOps with ArgoCD on GCP**  
    Manage GKE deployments using GitOps workflows.  
    *Skills: GitOps, Helm, Kubernetes*  

15. **Monitoring & Logging with Prometheus + Grafana**  
    System metrics and logging dashboards for GKE apps.  
    *Skills: Observability, Monitoring*  

16. **DevSecOps Pipeline on GCP**  
    Secure CI/CD with SonarQube + Trivy scans before GKE deployment.  
    *Skills: DevSecOps, Security Automation*  

---

### 🔷 Microsoft Azure Projects  
17. **Azure CI/CD Pipeline with AKS**  
    GitHub Actions → Build & Push Docker images → Deploy to AKS.  
    Secrets managed with Azure Key Vault.  
    *Skills: CI/CD, Kubernetes, Security*  

18. **Infrastructure as Code (Terraform + AzureRM)**  
    Provision a 3-tier application architecture (frontend, backend, database) in Azure.  
    *Skills: IaC, Networking, Cloud Architecture*  

19. **Azure Monitor + Application Insights**  
    Deploy a web app instrumented with Application Insights for observability.  
    *Skills: Monitoring, Distributed Tracing*  

20. **Azure Arc Multi-Cloud Management**  
    Manage Kubernetes clusters on AWS/GCP from Azure Arc.  
    *Skills: Multi-cloud, Governance, Policy Enforcement*  

21. **Serverless DevOps with Azure Functions + Event Grid**  
    Build an event-driven serverless app (Blob Storage trigger → Function → Event Grid).  
    *Skills: Serverless, Event-Driven Architecture*  

22. **GitOps with FluxCD/ArgoCD on AKS**  
    Implement GitOps workflows for AKS using FluxCD/ArgoCD.  
    *Skills: GitOps, Kubernetes, Continuous Delivery*  

23. **Security-First DevSecOps Pipeline**  
    CI/CD pipeline with static code analysis, container scanning, Key Vault integration, and Azure Policy compliance.  
    *Skills: DevSecOps, Compliance, Security Automation*  

---

## 🛠️ Tech Stack  

**AWS Services**: S3, EC2, VPC, IAM, CloudWatch, CloudFront, Route53, DynamoDB, Lambda, SNS, SQS, Auto Scaling, ALB, Elastic Beanstalk, CodePipeline, CodeBuild.  
**Azure Services**: AKS, Azure Functions, Event Grid, Application Insights, Key Vault, Azure Arc, Azure Policy, Azure Monitor.  
**Google Cloud Services**: GKE, Artifact Registry, Cloud SQL, Cloud Monitoring, IAM, Cloud Load Balancing.  
**Infrastructure as Code**: Terraform, AWS CloudFormation, ARM/Bicep.  
**DevOps Tools**: Docker, Kubernetes, Helm, FluxCD, ArgoCD, GitHub Actions, Jenkins, Prometheus, Grafana, SonarQube, Trivy.  
**Languages & Tools**: Python, Bash, YAML, JSON.  

---

## 📖 How to Use  

```bash
# Clone this repo
git clone https://github.com/Phionanamugga/DevOps_Projects_Portfolio.git
cd DevOps_Projects_Portfolio

# Navigate to a project folder (AWS, Azure, GCP)
cd azure-ci-cd-aks
Follow the instructions in the project’s README.md to deploy resources.
⚠️ Note: Some projects may incur cloud costs if deployed. Remember to delete resources after testing.

👩🏽‍💻 Author
Phiona Namugga
🌍 Based in Germany 🇩🇪
🎓 MSc Data Science, AI & Digital Business
📌 Career: AI & DevOps
⭐ Contribution
This is a learning-focused repository.
Feel free to fork, explore, and suggest improvements via Pull Requests!
If you find these projects useful, don’t forget to ⭐ the repo!

