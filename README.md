Flask and MongoDB with Kubernetes
Project Overview
This project sets up a Flask web application with a MongoDB database, deployed on a Kubernetes cluster. The Flask application exposes two endpoints:

/: A welcome message with the current time.
/data: Allows inserting and retrieving data from MongoDB.
Prerequisites
Docker
Kubernetes (Minikube or a managed Kubernetes service)
kubectl CLI
helm (optional, for easier deployments)
Directory Structure
arduino
Copy code
.
├── k8s-config
│   ├── deployment.yaml
│   ├── mongo-service.yaml
│   ├── mongo-statefulset.yaml
│   └── flask-service.yaml
├── src
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
└── README.md
Setup Instructions
1. Clone the Repository
sh
Copy code
git clone <repository-url>
cd <repository-directory>
2. Build Docker Images
For Flask Application:

sh
Copy code
cd src
docker build -t <your-dockerhub-username>/flask-app .
For MongoDB:

MongoDB doesn't require a custom Dockerfile as we're using an official image from Docker Hub.

3. Create Kubernetes Resources
MongoDB StatefulSet
Create the MongoDB StatefulSet and Service:

sh
Copy code
kubectl apply -f k8s-config/mongo-statefulset.yaml
kubectl apply -f k8s-config/mongo-service.yaml
Flask Application Deployment and Service
Create the Flask Deployment and Service:

sh
Copy code
kubectl apply -f k8s-config/deployment.yaml
kubectl apply -f k8s-config/flask-service.yaml
4. Verify the Deployment
Check the status of pods, services, and deployments:

sh
Copy code
kubectl get pods
kubectl get svc
kubectl get deployments
5. Access the Application
You can access the Flask application using the Kubernetes service. If you're using Minikube, you can expose the service with:

sh
Copy code
minikube service flask-service
For other Kubernetes environments, you may need to set up an Ingress or use kubectl port-forward:

sh
Copy code
kubectl port-forward svc/flask-service 5000:5000
Environment Variables
Ensure that the Flask application has the correct environment variables set for MongoDB:

MONGODB_URI: MongoDB connection string, e.g., mongodb://mongo:27017/
Example Environment Configuration in Deployment
yaml
Copy code
env:
- name: MONGODB_URI
  value: "mongodb://mongo:27017/"
Troubleshooting
Common Issues
500 Internal Server Error: Check MongoDB logs and ensure MongoDB is running correctly. Ensure that the MONGODB_URI is correct and the Flask application is able to reach the MongoDB service.
Connection Refused Errors: Ensure that the MongoDB pod is running and the service is correctly pointing to the MongoDB pod. Check service and endpoint configurations.
Network Issues: Use kubectl exec to run commands in the Flask pod and check connectivity to MongoDB. For example, use nc to check port connectivity.
Debugging Tips
Check Logs: Check the logs of both the Flask and MongoDB pods for any errors.

sh
Copy code
kubectl logs <flask-pod-name>
kubectl logs <mongo-pod-name>
Pod Connectivity: Use a temporary pod to test connectivity between services.

sh
Copy code
kubectl run -i --tty --rm debug --image=alpine --restart=Never -- sh
apk add --no-cache nc
nc -zv mongo 27017
Service and Endpoints: Verify the service configuration and ensure the correct endpoints are exposed.

sh
Copy code
kubectl get svc mongo
kubectl get endpoints mongo
License
This project is licensed under the MIT License - see the LICENSE file for details.
