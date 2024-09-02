
# Flask and MongoDB with Kubernetes

A Flask web application connected to a MongoDB database, deployed on a Kubernetes cluster. The application supports basic CRUD operations with data persistence and uses Kubernetes for deployment and scaling.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [State Management](#state-management)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Basic CRUD Operations**: Create, read, and manage data via RESTful endpoints.
- **Data Persistence**: Data is stored in MongoDB and persists across application restarts.
- **Kubernetes Deployment**: Deploys the application and MongoDB using Kubernetes for scaling and management.
- **Service Discovery**: Utilizes Kubernetes services to manage inter-service communication.
- **Logging**: Provides basic logging for troubleshooting and debugging.

## Getting Started

To get started with this project, follow the installation and deployment instructions.

### Prerequisites

- Docker
- Kubernetes (Minikube or a managed Kubernetes service)
- `kubectl` CLI
- Docker Hub account (for pushing images)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nihalbagul/flaskdevops.git
   cd flaskdevops
   ```

2. Build Docker images:

   **For Flask Application:**
   ```bash
   cd src
   docker build -t <your-dockerhub-username>/flask-app .
   ```

3. Push Docker images to Docker Hub:
   ```bash
   docker push <your-dockerhub-username>/flask-app
   ```

4. Create Kubernetes resources:

   **MongoDB StatefulSet and Service:**
   ```bash
   kubectl apply -f k8s-config/mongo-statefulset.yaml
   kubectl apply -f k8s-config/mongo-service.yaml
   ```

   **Flask Deployment and Service:**
   ```bash
   kubectl apply -f k8s-config/deployment.yaml
   kubectl apply -f k8s-config/flask-service.yaml
   ```

### Usage

#### Accessing the Application

Use the following commands to access the Flask application:

**Minikube:**
```bash
minikube service flask-service
```

**For other Kubernetes environments:**
```bash
kubectl port-forward svc/flask-service 5000:5000
```

#### API Endpoints

- **GET /**: Returns a welcome message with the current time.
- **POST /data**: Inserts new data into the MongoDB collection.
- **GET /data**: Retrieves all data from the MongoDB collection.

## Folder Structure

```markdown
flask-mongodb-kubernetes/
├── k8s-config/
│   ├── deployment.yaml          # Kubernetes Deployment configuration for Flask
│   ├── flask-service.yaml       # Kubernetes Service configuration for Flask
│   ├── mongo-service.yaml       # Kubernetes Service configuration for MongoDB
│   └── mongo-statefulset.yaml   # Kubernetes StatefulSet configuration for MongoDB
├── src/
│   ├── app.py                   # Main Flask application
│   └── requirements.txt         # Python dependencies
├── Dockerfile                   # Dockerfile for Flask application
└── README.md                    # Project documentation
```

## Dependencies

- **Flask**: Web framework for Python.
- **pymongo**: MongoDB driver for Python.
- **Docker**: For containerizing the application.
- **Kubernetes**: For deploying and managing containerized applications.

## State Management

The application does not use state management in the traditional sense as it relies on MongoDB for data storage. The MongoDB connection is managed through environment variables in the Kubernetes deployment configuration.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

