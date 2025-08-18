🚀 DevOps Projects Portfolio
Welcome to my DevOps Projects Portfolio!
This repository demonstrates my hands-on experience with Cloud Practitioner knowledge and end-to-end DevOps practices across AWS and Google Cloud (GCP).

Each project folder contains:
Source code / configuration files
Infrastructure-as-Code (Terraform / CloudFormation templates)
Step-by-step deployment guide in README.md

📂 Project List

🌐 AWS Projects
1. Static Website Hosting on S3 + CloudFront
Host a personal portfolio site on Amazon S3.
Use CloudFront for global distribution and Route 53 for DNS.
Skills: Storage, Networking, CDN.
2. CI/CD Pipeline with CodePipeline + CodeBuild
Automate builds and deployments from GitHub → CodePipeline → CodeBuild → Elastic Beanstalk.
Skills: Continuous Integration, Continuous Deployment.
3. EC2 Web Server Setup
Launch an EC2 instance with Apache/Nginx using User Data scripts.
Secure with Security Groups.
Skills: Compute, Networking, IAM.
4. IAM Roles & Policies
Define multiple IAM roles (Admin, Developer, Auditor) with least privilege policies.
Skills: Security, Governance.
5. CloudWatch Monitoring & Alerts
Monitor EC2 instance health with CloudWatch metrics, dashboards, and alarms.
Skills: Monitoring, Reliability.
6. AWS Backup & Disaster Recovery
Enable EBS snapshots and S3 cross-region replication.
Skills: High Availability, Reliability.
7. AWS Budgets & Cost Explorer
Set up budgets and cost alerts for services.
Use tagging to track project spend.
Skills: Cost Management.
8. Resource Tagging & Organization
Apply tags for environments (Dev, Test, Prod).
Generate reports in Cost Explorer.
Skills: Governance, Cost Optimization.
9. Serverless App with Lambda + API Gateway
Build a CRUD REST API using API Gateway + Lambda + DynamoDB.
Skills: Serverless, NoSQL, Event-driven architecture.
10. Event-Driven Notifications with SNS & SQS
Create a notification system using SNS for alerts and SQS + Lambda for processing.
Skills: Messaging, Decoupling.
11. Auto Scaling Group + Load Balancer
Deploy a scalable web app using EC2 Auto Scaling and Application Load Balancer.
Skills: Scalability, High Availability.
12. VPC Setup with Public/Private Subnets
Create a VPC with secure networking (public/private subnets, NAT Gateway, Security Groups).
Deploy a DB in private subnet and web server in public subnet.
Skills: Networking, Security.

☁️ Google Cloud Projects
13. CI/CD Pipeline on GCP with GKE
Build a microservices app (frontend + backend) with Docker.
Use Terraform to provision Google Kubernetes Engine (GKE) and Artifact Registry.
Implement GitHub Actions pipeline → Build → Push → Deploy to GKE.
Skills: Kubernetes, Terraform, CI/CD, Cloud-native deployment.
14. GitOps with ArgoCD on GCP
Set up ArgoCD on GKE to enable GitOps workflows.
Manage deployments using Helm charts synced automatically from GitHub.
Skills: GitOps, Helm, Kubernetes, Continuous Delivery.
15. Monitoring & Logging with Prometheus + Grafana
Deploy Prometheus and Grafana on GKE for system metrics.
Use Fluentbit to forward logs.
Build dashboards and set up alerts for CPU/memory usage.
Skills: Observability, Monitoring, Logging.
16. DevSecOps Pipeline on GCP
Implement a secure CI/CD pipeline with GitHub Actions.
Run unit tests, scan code with SonarQube, and scan containers with Trivy.
Deploy to GKE only if all checks pass.
Skills: DevSecOps, Security Automation, Kubernetes.
🛠️ Tech Stack
AWS Services: S3, EC2, VPC, IAM, CloudWatch, CloudFront, Route53, DynamoDB, Lambda, SNS, SQS, Auto Scaling, ALB, Elastic Beanstalk, CodePipeline, CodeBuild.
Google Cloud Services: GKE, Artifact Registry, Cloud SQL, Cloud Monitoring, IAM, Cloud Load Balancing.
Infrastructure as Code: Terraform, AWS CloudFormation.
DevOps Tools: Docker, Kubernetes, Helm, ArgoCD, GitHub Actions, Jenkins, Prometheus, Grafana, SonarQube, Trivy.
Languages & Tools: Python, Bash, YAML, JSON.

📖 How to Use
Clone this repo:
git clone https://github.com/Phionanamugga/DevOps_Projects_Portfolio.git
cd DevOps_Projects_Portfolio
Navigate to a project folder (AWS or GCP).
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