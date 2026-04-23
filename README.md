# DevOps Health Checker

A high-scale, distributed health monitoring system featuring a FastAPI web service, Nginx load balancing, asynchronous task processing via Celery, and real-time observability.

## 🚀 Features
- **FastAPI Interface:** High-performance asynchronous API for health monitoring.
- **Reverse Proxy & Load Balancing:** Nginx manages incoming traffic and scales across multiple API replicas.
- **Asynchronous Task Queue:** Heavy processing offloaded to Celery Workers to keep the API responsive.
- **Persistence:** Tracks success/failure metrics using a **Redis 8** backend.
- **Real-time Monitoring:** Flower dashboard for visualizing task queues and worker health.
- **Dynamic Probes:** Check any system path via query parameters.
- **Orchestration:** Seamless multi-container management via Docker Compose.
- **CI/CD:** Automated linting and container builds via GitHub Actions.

## 🏗 Architecture
The system follows a modern **Distributed Microservices** pattern:
1. **Entry Point:** Nginx (Port 80) acting as a Reverse Proxy.
2. **Application Tier:** Replicated **FastAPI** services handling logic.
3. **Task Tier: Celery Workers** processing background jobs (e.g., long-running system checks).
4. **Broker/Data Tier: Redis** acting as both a metrics store and a message broker.
5. **Observability Tier: Flower** (Port 5555) for monitoring background tasks.

## 🛠 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/gixorian/app-health-checker
cd app-health-checker
```

### 2. Configure Environment
Update `.env` with your `USER_ID` and `GROUP_ID` to ensure container permissions match your host.
```bash
cp .env.example .env
```
> [!NOTE]
> Run ```id -u``` and ```id -g``` in your terminal to find your IDs and update the ```.env``` file.

### 3. Launch the Stack
```bash
docker compose up -d --build
```

### 4. Scaling the Workers (Optional)
To handle massive background task volume, scale the worker tier horizontally:
```bash
docker compose up -d --scale worker=3
```
> [!NOTE]
> Every worker will handle as many tasks as your CPU has cores concurrently.

## 📊 API & Dashboards

### Endpoints
- **Health Check:** `GET /health?path=/etc/passwd` (Immediate file probe)
- **Stats:** `GET /stats` (Retrieve Redis metrics)
- **Background Process:** `GET /process` (Triggers a 10s background task)

### Dashboards
- **API Traffic:** `http://localhost/` (via Nginx)
- **Task Monitor:** `http://localhost:5555/` (Flower Dashboard)

## 💾 Persistence
This project uses a named Docker volume (```redis_data```). This means your statistics will survive a ```docker compose down```. To completely wipe the database, run:
```bash 
docker compose down -v
```
## 🤖 CI/CD Architecture

On every push to main, GitHub Actions will:

1. Install dependencies from requirements.txt.
2. Lint the code using flake8 with custom linting rules defined in ```.flake8```.
3. Build and push a new Docker image to GHCR (GitHub Container Registry).
