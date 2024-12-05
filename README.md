# mlops_US_visa_approved_proj 

# MLOps Production-Ready Machine Learning Project

### 🎥 YouTube Playlist: *"MLOPs for Machine Learning"*  

## 📚 Tools and Resources

Tools Used in the Project
Anaconda – Environment management
VS Code – Code editor
Git – Version control
Whimsical – Flowchart creation
Evidently AI – MLOps monitoring tool
MongoDB – Database
Kaggle – Dataset source
Docker – Containerization
GitHub Actions – CI/CD pipeline
AWS – Cloud deployment (EC2, ECR)

## 🚀 Git Commands
```bash
git add .
git commit -m "Updated"
git push origin main



# Create and activate environment
conda create -n visa python=3.8 -y
conda activate visa

# Install dependencies
pip install -r requirements.txt


export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net"
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> 


AWS CI/CD Deployment with GitHub Actions
Steps:
Login to AWS Console.

Create IAM User with:

EC2 Access (Virtual Machine)
ECR Access (Elastic Container Registry)
Deployment Process:

Build Docker image.
Push Docker image to ECR.
Launch EC2 instance.
Pull and run Docker image in EC2.
Required Policies:
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
Docker Setup on EC2: 


sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker






Configure EC2 as Self-Hosted Runner:
GitHub:
Settings > Actions > Runners > New Self-Hosted Runner
Follow on-screen commands.
GitHub Secrets Setup:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO