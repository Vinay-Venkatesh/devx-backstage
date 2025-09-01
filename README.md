# IDP Blueprints

A Backstage blueprint for creating applications with Kubernetes deployment and CI/CD pipeline.

## Features

- **FastAPI Application** with basic routing structure
- **Docker Configuration** with multi-stage builds
- **Kubernetes Manifests** with environment overlays
- **GitHub Actions** CI/CD pipeline
- **ArgoCD Ready** for GitOps deployment

## Structure

```
blueprints/fastapi/
├── app/                    # FastAPI application code
├── k8s/                    # Kubernetes manifests
│   ├── overlays/          # Environment-specific configs
│   └── patches/           # Production patches
├── .github/workflows/     # CI/CD workflows
├── Dockerfile             # Development container
├── Dockerfile.prod        # Production container
└── requirements.txt       # Python dependencies
```

## Template Information

This blueprint is designed to be used as a **Backstage Software Template**. When a developer selects this template:

1. **Repository Generation**: Backstage creates a new repository with the FastAPI application structure
2. **Customization**: Template variables like `{{ values.name }}` are replaced with user input
3. **Resource Naming**: All Kubernetes resources are dynamically named based on the application name
4. **Ready to Deploy**: The generated repository includes everything needed for immediate deployment

### Template Variables
- `{{ values.name }}` → Application name (used throughout manifests)

### What Gets Generated
- **FastAPI App**: Basic API structure with hello world endpoints
- **Kubernetes Resources**: Complete deployment manifests with proper naming
- **CI/CD Pipeline**: GitHub Actions workflow for automated deployment
- **Docker Images**: Multi-stage builds for development and production
- **Environment Configs**: Staging and production overlays ready to use
