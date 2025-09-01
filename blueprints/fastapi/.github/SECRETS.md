# GitHub Actions Secrets Required for CD Workflow

This document outlines all the secrets that need to be configured in your GitHub repository for the Continuous Deployment workflow to function properly.

## Repository Secrets

Configure these secrets in your GitHub repository: `Settings` → `Secrets and variables` → `Actions`

### 🔐 Kubernetes Configuration

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `KUBECONFIG_STAGING` | Base64 encoded kubeconfig for staging cluster | `echo "$(cat ~/.kube/config)" \| base64` |
| `KUBECONFIG_PRODUCTION` | Base64 encoded kubeconfig for production cluster | `echo "$(cat ~/.kube/config)" \| base64` |

### 🔔 Notifications

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `SLACK_WEBHOOK_URL` | Slack webhook URL for deployment notifications | `https://hooks.slack.com/services/...` |

### 🐳 Container Registry (Optional)

If using a different container registry than GitHub Container Registry:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `REGISTRY_USERNAME` | Container registry username | `your-username` |
| `REGISTRY_PASSWORD` | Container registry password/token | `your-password` |
| `REGISTRY_URL` | Container registry URL | `registry.example.com` |

## Environment Protection Rules

Set up environment protection rules for staging and production:

### Staging Environment
- **Required reviewers**: DevOps team members
- **Wait timer**: 0 minutes
- **Deployment branches**: `develop`, `feature/*`

### Production Environment
- **Required reviewers**: DevOps team leads, Tech leads
- **Wait timer**: 5 minutes
- **Deployment branches**: `main` only

## Setting Up Secrets

### 1. Kubernetes Configuration

```bash
# For staging cluster
kubectl config view --flatten --minify --context staging-context | base64

# For production cluster
kubectl config view --flatten --minify --context production-context | base64
```

### 2. Slack Webhook

1. Go to your Slack workspace
2. Create a new app or use existing one
3. Enable Incoming Webhooks
4. Create a webhook for the `#deployments` channel
5. Copy the webhook URL

### 3. Container Registry (if different from GHCR)

```bash
# For Docker Hub
REGISTRY_USERNAME=your-dockerhub-username
REGISTRY_PASSWORD=your-dockerhub-token
REGISTRY_URL=docker.io

# For AWS ECR
REGISTRY_USERNAME=AWS
REGISTRY_PASSWORD=$(aws ecr get-login-password --region us-west-2)
REGISTRY_URL=123456789012.dkr.ecr.us-west-2.amazonaws.com
```

## Security Best Practices

1. **Rotate secrets regularly** - Update secrets every 90 days
2. **Use least privilege** - Only grant necessary permissions
3. **Audit access** - Regularly review who has access to secrets
4. **Use environment secrets** - Separate staging and production secrets
5. **Monitor usage** - Set up alerts for secret access

## Troubleshooting

### Common Issues

1. **"Secret not found" error**
   - Verify secret name matches exactly (case-sensitive)
   - Check if secret is configured in the correct environment

2. **Kubernetes authentication failed**
   - Verify kubeconfig is valid and not expired
   - Check cluster access permissions
   - Ensure context is correct

3. **Container registry authentication failed**
   - Verify registry credentials
   - Check if registry allows GitHub Actions IPs
   - Ensure repository has proper permissions

### Debug Commands

```bash
# Test kubeconfig
kubectl --kubeconfig=kubeconfig.yaml get nodes

# Test registry login
docker login $REGISTRY_URL -u $REGISTRY_USERNAME -p $REGISTRY_PASSWORD

# Check secret values (in workflow)
echo "Secret length: ${#SECRET_NAME}"
```

## Alternative: Using GitHub Environments

For better security, consider using GitHub Environments:

1. **Create environments** in repository settings
2. **Configure protection rules** per environment
3. **Store secrets** at environment level
4. **Reference environments** in workflow

```yaml
# In workflow
deploy-production:
  environment: production
  # ... rest of job
```

This provides better secret isolation and access control. 