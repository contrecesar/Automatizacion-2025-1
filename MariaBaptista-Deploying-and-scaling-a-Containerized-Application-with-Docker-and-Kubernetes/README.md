# Deploying and scaling a Containerized Application with-Docker and Kubernetes
This repository contains a simple Node.js application deployed in a Kubernetes cluster using Docker. The application responds with a greeting message and the pod's hostname.

## Prerequisites
- Docker installed
- kubectl installed
- Access to a Kubernetes cluster (local options like Kind/K3s, or cloud services like EKS/GKE/AKS)
- A Docker Hub account

## Instructions
1. Build and push your Docker image to Docker Hub.
```
docker build -t yourdockerhubusername/simple-node-app:latest
docker login
docker push yourdockerhubusername/simple-node-app:latest
```
2. Connect kubectl to cluster.
3. Apply Kubernetes manifests. Edit the deployment.yaml file so that the Docker Hub username matches the one used when building the Docker image before applying it.
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
4. Verify deployment
```
kubectl get deployments
kubectl get pods -w
kubectl get services -w
```
5. Access the application once the service has an EXTERNAL-IP.
```
curl http://<EXTERNAL-IP>
```
