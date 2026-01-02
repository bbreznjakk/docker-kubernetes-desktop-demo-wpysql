# 1. Project
Flask CRUD Application with PostgreSQL: Containerized & Orchestrated & Clustered

# 2. Description
This repository implements a simple CRUD application for managing a book inventory, build with Flask, PostgreSQL.
Projecy structured for educational purposes, demonstrating lean-good-practice DevOps Patterns.

# 3.Technology Stack
Flask: 3.1.2
PostgreSQL: 16
Docker: 18.09
Kubectl: 1.22.1
OS: 2.0

# 4. Operations
## 4.1 With Local
psql -u postgres
CREATE USER flask-user WITH PASSWORD 'admin';
CREATE DATABASE flask_crud_db OWNER flask_user;
pqsl -U flask_user -d flask_crud_db -f database_setup.sql
set DATABASE_URL=postgresql://flask_user:admin@localhost:5432/flask_crud_db

## 4.2 With Docker
docker build -t yourdockername/flaskcrudapp:1 .
docker push  yourdockername/flaskcrudapp:1
docker-compose up

## 4.3 With Kubernetes
kubectl apply -f postgres-pv.yaml
kubectl apply -f devops-deployment.yaml
