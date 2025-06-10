


# Adome SaaS Project

Welcome to the SaaS Project! This repository contains the source code and configuration for running the application locally using Docker, Minikube, and Skaffold.

---

## 📑 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## ✅ Prerequisites

Ensure the following tools are installed on your system:

- **Docker** (v20.10 or later)
- **Minikube** (v1.25 or later)
- **Skaffold** (v2.0 or later)

---

## ⚙️ Installation

Follow these steps to set up the development environment.

### 1. Install Docker

Docker is used to containerize the application.

- **Windows/Mac:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Linux:**

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
````

* **Verify Installation:**

```bash
docker --version
```

---

### 2. Install Minikube

Minikube runs a local Kubernetes cluster.

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

* **Start Minikube:**

```bash
minikube start
```

* **Verify Installation:**

```bash
minikube version
```

---

### 3. Install Skaffold

Skaffold streamlines the development workflow.

```bash
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
sudo install skaffold /usr/local/bin/
```

* **Verify Installation:**

```bash
skaffold version
```

---

## 🚀 Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/codewithjoe-tech/Backend-Adome.git
cd BackendAdome
```

### 2. Start Minikube (if not already running)

```bash
minikube start
```

### 3. Run the Application

Use Skaffold to build, deploy, and watch for changes:

```bash
skaffold dev
```

### 4. Access the Application

* Skaffold will display the application URL (e.g., `http://localhost:<port>`).
* Alternatively, find the service URL:

```bash
minikube service <service-name> --url
```

> Replace `<service-name>` with the name defined in your Kubernetes manifests.

---

## 🛠️ Troubleshooting

* **Docker issues:** Ensure Docker is running → `docker info`
* **Minikube issues:** Check with → `minikube status`
  Restart if needed → `minikube stop && minikube start`
* **Skaffold issues:** Validate `skaffold.yaml`, Dockerfiles, and Kubernetes manifests.
* **Resource constraints:** Allocate more CPU/memory to Docker and Minikube.

For verbose logs:

```bash
skaffold dev --verbosity=debug
```

To stop the application:

```bash
Ctrl + C
minikube stop
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add your feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature
   ```

5. Open a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```

Let me know if you want this customized for your actual GitHub repo name, service names, or have CI/CD instructions too.
```
