# Python GCP Automated Deployment

A complete CI/CD pipeline for a Flask web application with automated testing, Docker containerization, and continuous delivery to Google Cloud Registry (GCR).

## Project Overview

This repository demonstrates best practices for automated software delivery to Google Cloud Platform. It includes:

- **Flask Web Application**: Simple Python web server with a welcome page
- **Unit Testing**: Automated tests for code quality assurance
- **Docker Containerization**: Application packaged in lightweight containers
- **GitHub Actions CI/CD**: Automated pipelines for testing and deployment
- **Google Cloud Integration**: Seamless deployment to GCP services

## Features

- **Continuous Integration**: Automatic testing on pull requests
- **Automated Merging**: PRs auto-merge when tests pass
- **Continuous Delivery**: Automatic Docker image builds and pushes to GCR
- **Container Registry**: Images stored in Google Artifact Registry
- **Git Metadata**: Build args include commit SHA and branch reference

## Project Structure

```
python-gcp-automated-deployment/
├── README.md                      # Project documentation
├── app/
│   ├── main.py                    # Flask web application
│   ├── test_main.py               # Unit tests
│   ├── requirements.txt           # Python dependencies
│   └── dockerfile                 # Docker configuration
└── .github/
    └── workflows/
        ├── ci.yml                 # Continuous Integration workflow
        └── cd.yml                 # Continuous Delivery workflow
```

## Requirements

### Local Development

- Python 3.8 or later
- pip (Python package manager)
- Docker and Docker CLI
- Git

### GCP Setup

- Active GCP project with billing enabled
- Google Cloud Registry enabled
- Service account with permissions:
  - Container Registry Service Agent
  - Storage Admin (for GCR)

### GitHub Setup

- GitHub repository secrets configured:
  - `GCP_PROJECT`: Your GCP project ID
  - `GCP_CREDENTIALS`: GCP service account JSON key
  - `PAT`: Personal Access Token for auto-merge (for CI workflow)

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/python-gcp-automated-deployment.git
cd python-gcp-automated-deployment
```

### 2. Install Dependencies

```bash
cd app
pip install -r requirements.txt
```

### 3. Run Application Locally

```bash
python main.py
```

The application runs on `http://localhost:8080`

### 4. Run Tests

```bash
python test_main.py
```

## Docker

### Build Docker Image

```bash
cd app
docker build --tag python-app:latest .
```

### Run Docker Container

```bash
docker run -p 8080:8080 python-app:latest
```

Access the application at `http://localhost:8080`

### Build and Run with Dockerfile

```bash
docker build -t python-app .
docker run -it python-app
```

## CI/CD Pipelines

### Continuous Integration (CI)

**File**: `.github/workflows/ci.yml`

Runs automatically on pull requests to the main branch.

**Workflow**:

1. Checkout code
2. Build Docker image with tests
3. Run unit tests in container
4. Auto-merge PR if tests pass (exit code 0)

**Trigger**: Pull request to `main` branch

**Output**: Merged PR or test failure notification

### Continuous Delivery (CD)

**File**: `.github/workflows/cd.yml`

Runs automatically on push to the main branch (after successful merge).

**Workflow**:

1. Checkout code
2. Authenticate with Google Cloud
3. Configure Docker for GCR
4. Build Docker image with git metadata:
   - GITHUB_SHA: Commit hash
   - GITHUB_REF: Branch name
5. Push image to Google Container Registry

**Trigger**: Push to `main` branch

**Output**: Docker image in GCR at `eu.gcr.io/YOUR_PROJECT_ID/welcome-page:latest`

## Application Details

### Flask Application (main.py)

A simple Flask web server that:

- Listens on `0.0.0.0:8080`
- Serves a welcome page on the root path (`/`)
- Displays a centered message with DevOps theme

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_page():
    message = "Hello CGI!!! Welcome to the world of DevOps :)"
    return page(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### Testing (test_main.py)

Unit tests validate application functionality and ensure the Flask app runs correctly.

### Dependencies (requirements.txt)

```
Flask==1.1.2
```

## GitHub Secrets Configuration

### For CI Workflow

1. Go to **Settings -> Secrets and variables -> Actions**
2. Add the following secrets:
   - `PAT`: GitHub Personal Access Token with repo access

### For CD Workflow

1. Create a GCP service account with GCR permissions
2. Go to **Settings -> Secrets and variables -> Actions**
3. Add the following secrets:
   - `GCP_PROJECT`: Your GCP project ID (e.g., `my-project-123456`)
   - `GCP_CREDENTIALS`: Service account JSON key (full file contents)

## Usage Workflow

### Development

1. Create a feature branch: `git checkout -b feature/new-feature`
2. Make changes to the code
3. Test locally: `python test_main.py`
4. Commit and push: `git push origin feature/new-feature`
5. Create a Pull Request to `main`

### Automated Testing & Merge

1. GitHub Actions CI workflow triggers automatically
2. Docker image built and tests executed
3. If tests pass, PR auto-merges to main
4. If tests fail, PR review is required

### Automated Deployment

1. After PR merge, CD workflow triggers
2. Docker image built with git metadata
3. Image pushed to Google Container Registry
4. Image available for deployment to GCP services (GKE, Cloud Run, etc.)

## Accessing Deployed Images

View images in Google Container Registry:

```bash
gcloud container images list --project=YOUR_PROJECT_ID
```

List all tags for the image:

```bash
gcloud container images list-tags eu.gcr.io/YOUR_PROJECT_ID/welcome-page
```

Pull an image locally:

```bash
docker pull eu.gcr.io/YOUR_PROJECT_ID/welcome-page:latest
```

## Troubleshooting

### CI Workflow Fails

**Issue**: "Could not understand audio"

- **Cause**: Tests are failing in Docker container
- **Solution**:
  - Check `test_main.py` for test errors
  - Run tests locally: `python test_main.py`
  - Review test output in GitHub Actions logs

### CD Workflow Fails

**Issue**: "Error: UNAUTHENTICATED"

- **Cause**: GCP authentication failed
- **Solution**:
  - Verify `GCP_CREDENTIALS` secret is valid JSON
  - Ensure service account has Container Registry permissions
  - Check service account hasn't been deleted

**Issue**: "Failed to push image"

- **Cause**: GCR authentication or permissions issue
- **Solution**:
  - Run `gcloud auth configure-docker` locally
  - Verify project ID is correct in workflow
  - Check service account has Storage Admin role

### Image Not Appearing in GCR

- Verify CD workflow completed successfully
- Check GCR settings are enabled in GCP project
- Ensure image tag matches the pattern: `eu.gcr.io/PROJECT_ID/welcome-page`

## Environment Variables

### Docker Build Arguments

- `GITHUB_SHA`: Commit hash (set by GitHub Actions)
- `GITHUB_REF`: Branch name (set by GitHub Actions)

### Flask Application

- `PORT`: Server port (default: 8080)
- `HOST`: Server host (default: 0.0.0.0)

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Google Cloud Registry Documentation](https://cloud.google.com/container-registry/docs)
- [Google Cloud Platform Documentation](https://cloud.google.com/docs)
