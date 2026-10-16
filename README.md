# 🚀 DevOps Assessment: Multi-Tier Application Pipeline (FA1 & FA2)

A complete, production-grade DevOps implementation featuring a containerized two-tier machine learning application, multi-environment infrastructure provisioning, automated CI/CD pipelines, Kubernetes orchestration, and comprehensive system monitoring.

---

## 🎯 Project Overview & Objective
The goal of this project is to build a reliable, scalable, and automated deployment pipeline for a crop recommendation application. In modern software engineering, writing code is only half the battle; ensuring it builds automatically, scales reliably under traffic, and is monitored for failures is what **DevOps** is all about.

---

## 🏗️ Architecture & Data Flow


1. **Frontend (Streamlit - Port 8501):** The user-facing web interface where farmers input parameters.
2. **Backend (FastAPI - Port 8000):** The core API logic that processes input data and returns recommendations.

---

## 📂 Project Structure & Component Explanation

```text
/FA1-DEVOPS/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                 # Automated CI/CD pipeline
├── backend/
│   ├── Dockerfile                    # Container blueprint for FastAPI
│   ├── main.py                       # Backend API logic
│   └── requirements.txt              # Python dependencies for backend
├── frontend/
│   ├── Dockerfile                    # Container blueprint for Streamlit
│   ├── app.py                        # Frontend UI logic
│   └── requirements.txt              # Python dependencies for frontend
├── k8s/
│   ├── backend-deployment.yaml       # Kubernetes Deployment (manages backend pods)
│   ├── backend-service.yaml          # ClusterIP (secure internal routing)
│   ├── frontend-deployment.yaml      # Kubernetes Deployment (manages frontend pods)
│   └── frontend-service.yaml         # NodePort (exposes app externally)
├── monitoring/
│   ├── prometheus.yml                # Prometheus metrics scraping rules
│   └── docker-compose.monitoring.yml # Running Prometheus & Grafana stack
├── terraform/                        # Multi-environment infrastructure code
└── README.md
