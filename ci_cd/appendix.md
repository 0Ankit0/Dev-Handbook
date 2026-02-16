# Appendix A: Quick Reference

## A.1 Docker Commands Cheat Sheet

**Image Operations:**
```bash
# Build with context
docker build -t myapp:v1.0.0 -f Dockerfile.prod .

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest --push .

# Tag and push
docker tag myapp:v1.0.0 registry.io/myapp:v1.0.0
docker push registry.io/myapp:v1.0.0

# Pull and inspect
docker pull myapp:v1.0.0
docker inspect myapp:v1.0.0 --format='{{.Os}}'

# Layer analysis
docker history myapp:v1.0.0
dive myapp:v1.0.0  # Interactive layer browser

# Cleanup
docker system prune -af --volumes
docker images -f "dangling=true" -q | xargs docker rmi
```

**Container Lifecycle:**
```bash
# Run with resource limits
docker run -d \
  --name webapp \
  --memory=512m \
  --memory-swap=512m \
  --cpus=1.0 \
  --read-only \
  --tmpfs /tmp \
  -p 8080:80 \
  myapp:v1.0.0

# Execute in running container
docker exec -it webapp /bin/sh

# View logs and metrics
docker logs -f --tail 100 webapp
docker stats webapp --no-stream

# Copy files
docker cp webapp:/app/logs ./local-logs
docker cp ./config.json webapp:/app/config/
```

**Network & Volumes:**
```bash
# Create network
docker network create --driver bridge app-network

# Volume operations
docker volume create pgdata
docker run -v pgdata:/var/lib/postgresql/data postgres:15

# Bind mount (development)
docker run -v $(pwd)/src:/app/src:ro node:18
```

## A.2 Kubernetes Commands Cheat Sheet

**Cluster Information:**
```bash
# Context and cluster management
kubectl config current-context
kubectl config get-contexts
kubectl config use-context production
kubectl cluster-info

# Node operations
kubectl get nodes -o wide
kubectl describe node worker-1
kubectl top nodes
kubectl cordon node-1
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data
```

**Resource Management:**
```bash
# Pods
kubectl get pods -n production -o wide
kubectl get pods --show-labels
kubectl describe pod webapp-7d9f4b8c5-x2v4n
kubectl logs webapp-7d9f4b8c5-x2v4n -f --previous
kubectl exec -it webapp-7d9f4b8c5-x2v4n -- /bin/sh

# Deployments
kubectl get deployments
kubectl rollout status deployment/webapp
kubectl rollout history deployment/webapp
kubectl rollout undo deployment/webapp --to-revision=2
kubectl scale deployment webapp --replicas=5

# Services & Networking
kubectl get svc -o wide
kubectl port-forward svc/webapp 8080:80
kubectl get endpoints webapp

# ConfigMaps & Secrets
kubectl create configmap app-config --from-file=config.json
kubectl create secret generic db-creds \
  --from-literal=username=admin \
  --from-literal=password=secret123
kubectl get secret db-creds -o jsonpath='{.data.password}' | base64 -d
```

**Advanced Operations:**
```bash
# Resource quotas and limits
kubectl get resourcequota
kubectl describe limitranges

# RBAC
kubectl get roles
kubectl get rolebindings
kubectl auth can-i create pods --as=developer-user

# Debugging
kubectl debug node/node-1 -it --image=busybox
kubectl debug pod/webapp-xxx --copy-to=webapp-debug --container=app --image=nicolaka/netshoot -- /bin/bash
kubectl events --sort-by='.lastTimestamp' -n production

# Apply with dry-run
kubectl apply -f deployment.yaml --dry-run=server
kubectl diff -f k8s/
```

## A.3 Helm Commands Cheat Sheet

**Chart Management:**
```bash
# Create and package
helm create mychart
helm package mychart --sign --key 'My Key' --keyring ~/.gnupg/secring.gpg
helm lint mychart --values values-production.yaml

# Search and install
helm search hub postgresql
helm search repo bitnami/postgresql
helm install postgres bitnami/postgresql --version 13.2.0 -f values.yaml --namespace db --create-namespace

# Upgrade and rollback
helm upgrade --install webapp ./mychart --set image.tag=v2.0.0 --wait --timeout 5m
helm rollback webapp 3
helm history webapp

# Uninstall and cleanup
helm uninstall webapp --keep-history
helm delete webapp --purge
```

**Template Debugging:**
```bash
# Render templates locally
helm template mychart --values values.yaml --debug
helm get values webapp --all
helm get manifest webapp

# Test releases
helm test webapp --logs
```

## A.4 Git Commands Cheat Sheet

**Branching & Merging:**
```bash
# Feature branch workflow
git checkout -b feature/new-login main
git commit -m "feat: add OAuth2 login"
git push -u origin feature/new-login

# Interactive rebase
git rebase -i HEAD~5
git rebase --continue
git rebase --abort

# Merge strategies
git merge --no-ff feature/new-login
git merge --squash feature/quick-fix
git cherry-pick abc1234
```

**CI/CD Specific:**
```bash
# Shallow clone for CI (faster)
git clone --depth 1 --branch main https://github.com/org/repo.git

# Get changed files
git diff --name-only HEAD~1 HEAD
git log --oneline --graph -10

# Tags for releases
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0
git push --delete origin v1.1.0  # Delete remote tag
```

## A.5 kubectl常用命令 (Common kubectl Commands)

```bash
# 查看所有命名空间资源
kubectl get all -n production

# 导出资源定义
kubectl get deployment webapp -o yaml --export > webapp.yaml

# 强制删除Pod
kubectl delete pod webapp-xxx --grace-period=0 --force

# 查看资源使用
kubectl top pod -n production --sort-by=cpu

# 进入容器调试
kubectl exec -it pod-name -- /bin/bash

# 端口转发到本地
kubectl port-forward svc/mysql 3306:3306
```

## A.6 YAML Syntax Reference

**Basic Structure:**
```yaml
apiVersion: v1          # API版本
kind: Pod              # 资源类型
metadata:
  name: example        # 名称（DNS子域名）
  namespace: default   # 命名空间
  labels:              # 标签（查询用）
    app: web
    version: v1
  annotations:         # 注解（非标识性元数据）
    description: "Web application pod"
spec:                  # 规格说明
  containers:
  - name: app          # 容器名称（唯一）
    image: nginx:1.25  # 镜像
    ports:
    - containerPort: 80
      protocol: TCP
    resources:         # 资源限制
      requests:
        memory: "128Mi"
        cpu: "100m"
      limits:
        memory: "256Mi"
        cpu: "200m"
    env:               # 环境变量
    - name: ENV
      value: "production"
    volumeMounts:      # 卷挂载
    - name: data
      mountPath: /data
  volumes:             # 卷定义
  - name: data
    emptyDir: {}
```

**Multi-document Files:**
```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-1
data:
  key: value
---
apiVersion: v1
kind: Secret
metadata:
  name: secret-1
stringData:
  password: secret123
```

## A.7 Regular Expressions Reference

**CI/CD Patterns:**
```regex
# Semantic Versioning matching
^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$

# Docker image tag validation
^[a-z0-9]+((\.|_|-)[a-z0-9]+)*$

# Kubernetes resource names
^[a-z0-9]([-a-z0-9]*[a-z0-9])?$

# Git commit SHA (short)
^[a-f0-9]{7,8}$

# Branch name validation (no special chars)
^(feature|bugfix|hotfix|release)\/[a-z0-9-]+$
```

## A.8 JSON Path Reference

**kubectl JSONPath Examples:**
```bash
# Get specific fields
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.capacity.cpu}{"\n"}{end}'

# Complex queries
kubectl get pod webapp -o jsonpath='{.spec.containers[0].image}'
kubectl get pods -o jsonpath='{..image}' | tr ' ' '\n' | sort | uniq

# Custom columns
kubectl get pods -o custom-columns='NAME:.metadata.name,IMAGE:.spec.containers[0].image,STATUS:.status.phase'
```

---

# Appendix B: Troubleshooting Guide

This appendix provides diagnostic procedures and solutions for common CI/CD and Kubernetes failures. Follow the structured approach: identify symptoms, check logs, verify configuration, apply fix.

## B.1 Common Docker Issues

**Issue: ImagePullBackOff / ErrImagePull**
```bash
# Symptoms: Pod status shows ImagePullBackOff
# Diagnosis:
kubectl describe pod <pod-name> | grep -A 5 Events
# Look for: "repository not found", "unauthorized", "manifest unknown"

# Solutions:
# 1. Check image tag exists
docker pull registry.io/app:v1.0.0  # Verify locally

# 2. Verify pull secrets
kubectl get secret regcred -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d

# 3. Check node disk space
docker system df
df -h /var/lib/docker

# 4. For private registries, ensure imagePullSecrets is configured
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "regcred"}]}'
```

**Issue: Container Creating / Stuck**
```bash
# Check volume mount issues
kubectl describe pod <pod-name>
# Look for: "MountVolume.SetUp failed", "volume not found"

# Common fixes:
# - Verify PVC exists and is Bound
kubectl get pvc
# - Check storage class availability
kubectl get storageclass
# - For ConfigMap/Secret mounts, verify resource exists
```

## B.2 Common Kubernetes Issues

**Issue: CrashLoopBackOff**
```bash
# Diagnosis chain:
kubectl logs <pod-name> --previous  # Crashed container logs
kubectl get events --field-selector involvedObject.name=<pod-name>

# Common causes:
# 1. Application error (check logs)
# 2. Resource limits (OOMKilled)
kubectl describe pod <pod-name> | grep -A 5 "Last State"
# Fix: Increase memory limits or optimize application

# 3. Liveness probe failing
kubectl get pod <pod-name> -o yaml | grep -A 10 livenessProbe
# Fix: Adjust initialDelaySeconds or probe path

# 4. Missing environment variables or secrets
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].env}' | jq .
```

**Issue: Pending Pods**
```bash
# Check why pod is pending
kubectl describe pod <pod-name> | grep -A 10 Events

# Common causes:
# 1. Insufficient resources
kubectl describe node | grep -A 5 "Allocated resources"

# 2. Taints/Tolerations mismatch
kubectl get nodes -o json | jq '.items[].spec.taints'

# 3. PVC not bound
kubectl get pvc
# If Pending: Check StorageClass, provisioner, or cloud quota

# 4. Node selector/affinity not matching
kubectl get nodes --show-labels
```

**Issue: Service Not Accessible**
```bash
# Diagnosis:
kubectl get endpoints <service-name>
# If empty: Check label selector matches pods
kubectl get pods --selector=app=<label>

# Check DNS resolution
kubectl run -it --rm debug --image=busybox:1.28 --restart=Never -- nslookup <service-name>

# Check network policies
kubectl get networkpolicies -n <namespace>
# Temporarily allow all for testing (SECURITY RISK - remove after):
kubectl create networkpolicy allow-all --namespace=<ns> --pod-selector={} --ingress={} --egress={}
```

## B.3 Common CI Pipeline Issues

**Issue: Pipeline Fails Intermittently (Flaky Tests)**
```yaml
# Strategy 1: Retry logic (GitHub Actions)
- name: Test
  run: npm test
  id: test
  continue-on-error: true

- name: Retry on failure
  if: steps.test.outcome == 'failure'
  run: npm test

# Strategy 2: Parallelism reduction (resource contention)
strategy:
  max-parallel: 2  # Reduce from default

# Strategy 3: Test isolation
# Use unique databases per test run
services:
  postgres:
    env:
      POSTGRES_DB: test_${{ github.run_id }}
```

**Issue: Slow Builds (Cache not working)**
```bash
# Verify cache keys
# Docker layer caching - ensure RUN commands are ordered correctly
# Bad (changes every build):
COPY . /app
RUN npm install

# Good (cache friendly):
COPY package*.json /app/
RUN npm install
COPY . /app

# For GitHub Actions cache action:
# Check cache hit in logs
# Verify key matches: actions/cache@v3 with key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

**Issue: Permission Denied in CI**
```bash
# Docker-in-Docker scenarios
# Fix: Add user to docker group or use root (less secure)
sudo chmod 666 /var/run/docker.sock

# Kubernetes: Security contexts
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
```

## B.4 Common CD Pipeline Issues

**Issue: ArgoCD Sync Failures**
```bash
# Check application status
argocd app get <app-name>
argocd app wait <app-name> --health

# Common issues:
# 1. Resource already exists (not managed by Argo)
argocd app sync <app-name> --force  # Caution: deletes orphaned resources

# 2. CRD not installed
kubectl apply -f crds/  # Apply CRDs first

# 3. Hook failure
argocd app get <app-name> -o yaml | grep -A 10 hook

# 4. OutOfSync due to mutation
# Add ignoreDifferences to Application spec:
ignoreDifferences:
- group: apps
  kind: Deployment
  jsonPointers:
  - /spec/replicas
```

**Issue: Helm Upgrade Fails**
```bash
# Check release status
helm history <release-name>
helm get values <release-name> --revision 2

# Common fixes:
# 1. CRD already exists
helm upgrade --install <name> <chart> --skip-tests

# 2. Previous release stuck in pending
kubectl get secrets -l owner=helm,name=<release-name>
# Delete stuck release secret if safe (causes data loss if DB):
kubectl delete secret sh.helm.release.v1.<release-name>.v3

# 3. Immutable field errors (re-create required)
helm uninstall <release-name>
helm install <release-name> ./chart
```

## B.5 Network Issues

**Issue: Inter-Service Communication Timeout**
```bash
# Debug steps:
# 1. Check service exists and has endpoints
kubectl get svc <service-name>
kubectl get endpoints <service-name>

# 2. Test connectivity from within cluster
kubectl run -it --rm debug --image=curlimages/curl --restart=Never -- \
  curl -v http://<service-name>:<port>/health

# 3. Check Istio/Service Mesh sidecar
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}'
# Should include istio-proxy or linkerd-proxy

# 4. Check mTLS strict mode causing blocks
kubectl get peerauthentication -A
# Temporarily disable for testing:
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: <ns>
spec:
  mtls:
    mode: PERMISSIVE
EOF
```

## B.6 Performance Issues

**Issue: High Memory Usage in Pods**
```bash
# Diagnosis:
kubectl top pod <pod-name>
kubectl logs <pod-name> | grep -i "out of memory\|OOM"

# Solutions:
# 1. Java applications - set heap size
env:
- name: JAVA_OPTS
  value: "-Xmx512m -Xms512m"

# 2. Node.js - set max old space
env:
- name: NODE_OPTIONS
  value: "--max-old-space-size=512"

# 3. Check for memory leaks
# Enable pprof for Go, heap snapshots for Node
```

**Issue: Slow Database Queries**
```bash
# Enable slow query log (PostgreSQL)
kubectl exec -it <postgres-pod> -- psql -c "ALTER SYSTEM SET log_min_duration_statement = '1000';"
kubectl exec -it <postgres-pod> -- psql -c "SELECT pg_reload_conf();"

# Check connection pooling
kubectl exec -it <app-pod> -- netstat -an | grep :5432 | wc -l
# If close to max_connections, increase pool size or add PgBouncer
```

## B.7 Security Issues

**Issue: Pod Security Policy Violations**
```bash
# Check for violations
kubectl get events --field-selector reason=FailedCreate

# Common fixes:
# 1. Run as non-root
securityContext:
  runAsNonRoot: true
  runAsUser: 1000

# 2. Read-only root filesystem
securityContext:
  readOnlyRootFilesystem: true
volumeMounts:
- name: tmp
  mountPath: /tmp
volumes:
- name: tmp
  emptyDir: {}

# 3. Drop capabilities
securityContext:
  capabilities:
    drop:
    - ALL
    add:
    - NET_BIND_SERVICE  # If binding low ports
```

## B.8 Where to Get Help

**Community Resources:**
- **Kubernetes Slack**: https://kubernetes.slack.com (channels: #kubernetes-novice, #troubleshooting)
- **Stack Overflow**: Tag with `kubernetes`, `docker`, `cicd`
- **GitHub Issues**: Check repository issues (kubernetes/kubernetes, argoproj/argo-cd)
- **Reddit**: r/kubernetes, r/devops

**Diagnostic Tools:**
```bash
# k9s - Terminal UI for K8s
k9s

# stern - Multi-pod log tailing
stern <pod-name-pattern>

# kubectl-debug - Ephemeral debug containers
kubectl debug pod/<pod-name> -it --image=nicolaka/netshoot -- /bin/bash

# kubectx/kubens - Context/namespace switching
kubectx production
kubens monitoring
```

---

# Appendix C: Configuration Templates

Production-ready YAML templates for common CI/CD scenarios. Copy and customize for your environment.

## C.1 Dockerfile Templates

**Multi-stage Node.js Production:**
```dockerfile
# syntax=docker/dockerfile:1
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

FROM node:18-alpine AS production
RUN apk add --no-cache dumb-init ca-certificates
USER node
WORKDIR /app
COPY --from=builder --chown=node:node /app/node_modules ./node_modules
COPY --chown=node:node ./src ./src
ENV NODE_ENV=production
ENV PORT=3000
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => r.statusCode === 200 ? process.exit(0) : process.exit(1))"
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "src/index.js"]
```

**Python FastAPI:**
```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
RUN pip install --user --no-cache-dir poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim
WORKDIR /app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
USER appuser
COPY ./app ./app
EXPOSE 8000
HEALTHCHECK CMD python -c "import requests; requests.get('http://localhost:8000/health')"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Go Microservice:**
```dockerfile
FROM golang:1.21-alpine AS builder
WORKDIR /build
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o app cmd/main.go

FROM gcr.io/distroless/static:nonroot
COPY --from=builder /build/app /app
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/app"]
```

## C.2 docker-compose.yml Templates

**Development Environment:**
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DB_HOST=postgres
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: devdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U devuser -d devdb"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## C.3 Kubernetes Deployment Templates

**Production Deployment with HPA:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  labels:
    app: webapp
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: webapp-sa
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: webapp
        image: webapp:v1.0.0
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          protocol: TCP
        envFrom:
        - configMapRef:
            name: webapp-config
        - secretRef:
            name: webapp-secret
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 2
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsUser: 1000
          capabilities:
            drop:
            - ALL
        volumeMounts:
        - name: tmp
          mountPath: /tmp
      volumes:
      - name: tmp
        emptyDir: {}
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - webapp
              topologyKey: kubernetes.io/hostname
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: webapp
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
```

## C.4 Helm Chart Templates

**Standard Chart Structure:**
```yaml
# Chart.yaml
apiVersion: v2
name: microservice
description: Generic microservice Helm chart
type: application
version: 1.0.0
appVersion: "1.0.0"
dependencies:
- name: postgresql
  version: 13.x.x
  repository: https://charts.bitnami.com/bitnami
  condition: postgresql.enabled
```

```yaml
# values.yaml
replicaCount: 2

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: ""

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

serviceAccount:
  create: true
  annotations: {}
  name: ""

podAnnotations: {}
podSecurityContext: {}
  # fsGroup: 2000

securityContext: {}
  # capabilities:
  #   drop:
  #   - ALL
  # readOnlyRootFilesystem: true
  # runAsNonRoot: true
  # runAsUser: 1000

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false
  className: ""
  annotations: {}
  hosts:
  - host: chart-example.local
    paths:
    - path: /
      pathType: ImplementationSpecific
  tls: []

resources: {}
  # limits:
  #   cpu: 100m
  #   memory: 128Mi
  # requests:
  #   cpu: 100m
  #   memory: 128Mi

autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 100
  targetCPUUtilizationPercentage: 80

nodeSelector: {}
tolerations: []
affinity: {}
```

## C.5 Jenkins Pipeline Templates

**Declarative Pipeline:**
```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: node
    image: node:18-alpine
    command: ['cat']
    tty: true
  - name: docker
    image: docker:24-dind
    securityContext:
      privileged: true
    volumeMounts:
    - name: docker-graph-storage
      mountPath: /var/lib/docker
  volumes:
  - name: docker-graph-storage
    emptyDir: {}
"""
        }
    }
    
    environment {
        DOCKER_REGISTRY = 'registry.company.com'
        IMAGE_NAME = 'myapp'
        GIT_COMMIT_SHORT = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
    }
    
    stages {
        stage('Test') {
            steps {
                container('node') {
                    sh 'npm ci'
                    sh 'npm test'
                }
            }
        }
        
        stage('Build') {
            steps {
                container('docker') {
                    sh """
                    docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT_SHORT} .
                    docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT_SHORT}
                    """
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                container('node') {
                    sh 'kubectl set image deployment/myapp app=${DOCKER_REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT_SHORT}'
                }
            }
        }
    }
    
    post {
        always {
            junit 'reports/**/*.xml'
            cleanWs()
        }
        failure {
            slackSend(color: 'danger', message: "Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
        }
    }
}
```

## C.6 GitHub Actions Workflow Templates

**Full CI/CD Pipeline:**
```yaml
name: Complete Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Lint
      run: npm run lint
    
    - name: Test
      run: npm run test:coverage
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'

  build:
    needs: [test, security]
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Login to Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=sha,prefix=,suffix=,format=short
    
    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy to Staging
      run: |
        echo "Deploying to staging..."
        # kubectl apply -k k8s/overlays/staging

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy to Production
      run: |
        echo "Deploying to production..."
        # kubectl apply -k k8s/overlays/production
```

## C.7 GitLab CI Templates

**Multi-stage Pipeline:**
```yaml
stages:
  - test
  - build
  - security
  - deploy

variables:
  DOCKER_HOST: tcp://docker:2376
  DOCKER_TLS_CERTDIR: "/certs"
  DOCKER_DRIVER: overlay2

services:
  - docker:24-dind

test:
  stage: test
  image: node:18-alpine
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  script:
    - npm ci
    - npm run test
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'

build:
  stage: build
  image: docker:24
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main

security_scan:
  stage: security
  image: aquasec/trivy:latest
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA -n production
  environment:
    name: production
    url: https://app.company.com
  when: manual
  only:
    - main
```

## C.8 Terraform Templates

**EKS Cluster with Managed Node Groups:**
```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "production-cluster"
  cluster_version = "1.28"

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  manage_aws_auth_configmap = true

  eks_managed_node_groups = {
    general = {
      desired_size = 3
      min_size     = 2
      max_size     = 10

      instance_types = ["m6i.xlarge"]
      capacity_type  = "ON_DEMAND"

      labels = {
        workload = "general"
      }

      update_config = {
        max_unavailable_percentage = 25
      }

      tags = {
        Environment = "production"
      }
    }

    spot = {
      desired_size = 2
      min_size     = 0
      max_size     = 20

      instance_types = ["m6i.large", "m5.large", "m5a.large"]
      capacity_type  = "SPOT"

      labels = {
        workload = "batch"
      }

      taints = [{
        key    = "spot"
        value  = "true"
        effect = "NO_SCHEDULE"
      }]
    }
  }

  cluster_addons = {
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
    aws-ebs-csi-driver = {
      most_recent = true
    }
  }

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

---

# Appendix D: Tool Installation Guides

Comprehensive installation guides for essential CI/CD tools across different platforms.

## D.1 Docker Installation

**macOS:**

Download Docker Desktop from https://docs.docker.com/desktop/setup/install/mac-install/

For Apple Silicon Macs:
```bash
# Download and install
curl -L https://desktop.docker.com/mac/main/arm64/Docker.dmg -o Docker.dmg
sudo hdiutil attach Docker.dmg
sudo /Volumes/Docker/Docker.app/Contents/MacOS/install
sudo hdiutil detach /Volumes/Docker
```

For Intel Macs:
```bash
curl -L https://desktop.docker.com/mac/main/amd64/Docker.dmg -o Docker.dmg
sudo hdiutil attach Docker.dmg
sudo /Volumes/Docker/Docker.app/Contents/MacOS/install
sudo hdiutil detach /Volumes/Docker
```

**Linux (Ubuntu/Debian):**

```bash
# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker
```

**Windows:**

Download Docker Desktop from https://docs.docker.com/desktop/setup/install/windows-install/

## D.2 Kubernetes Installation

**Minikube (Local Development):**

**macOS:**
```bash
brew install minikube
minikube start
```

**Linux:**
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
```

**Windows:**
```powershell
choco install minikube
minikube start
```

**Kind (Kubernetes in Docker):**

**macOS/Linux/Windows:**
```bash
# Install kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-$(uname)-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Create cluster
kind create cluster
```

## D.3 kubectl Installation

**macOS:**
```bash
brew install kubectl
# or
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Linux:**
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Windows:**
```powershell
curl.exe -LO "https://dl.k8s.io/release/v1.28.0/bin/windows/amd64/kubectl.exe"
# Add to PATH
```

## D.4 Helm Installation

**macOS:**
```bash
brew install helm
```

**Linux:**
```bash
curl https://get.helm.sh/helm-v3.13.0-linux-amd64.tar.gz -o helm.tar.gz
tar -zxvf helm.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm
```

**Windows:**
```powershell
choco install kubernetes-helm
```

## D.5 Jenkins Installation

**Docker (Recommended):**
```bash
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins jenkins/jenkins:lts
```

**macOS with Homebrew:**
```bash
brew install jenkins
brew services start jenkins
```

**Linux:**
```bash
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins
sudo systemctl start jenkins
```

## D.6 ArgoCD Installation

**kubectl:**
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

**Access:**
```bash
kubectl get pods -n argocd
kubectl port-forward svc/argocd-server -n argocd 8080:443
# Get initial password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## D.7 Flux Installation

**Bootstrap:**
```bash
flux bootstrap github \
  --owner=<your-github-username> \
  --repository=<your-repo-name> \
  --branch=main \
  --path=./clusters/my-cluster \
  --personal
```

## D.8 Monitoring Stack Installation

**Prometheus + Grafana with Helm:**
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
```

**Access Grafana:**
```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
# Default credentials: admin/prom-operator
```

---

# Appendix E: Best Practices Checklist

Use these checklists during code reviews, architecture reviews, and production readiness assessments.

## E.1 Docker Best Practices Checklist

**Image Construction:**
- [ ] Uses specific base image tags (not `latest`)
- [ ] Multi-stage build used to separate build/runtime dependencies
- [ ] Non-root user specified (`USER` instruction)
- [ ] `.dockerignore` file present and excludes unnecessary files
- [ ] Health check defined (`HEALTHCHECK` instruction)
- [ ] Image size < 200MB (Alpine/Distroless preferred)
- [ ] No secrets in layers (use BuildKit secrets if needed)
- [ ] Single process per container (or proper init system like dumb-init)
- [ ] Read-only root filesystem where possible

**Security:**
- [ ] No `sudo` or elevated privileges
- [ ] Minimal capabilities dropped (`--cap-drop=ALL`)
- [ ] Security scanning integrated in CI (Trivy, Clair, Snyk)
- [ ] No hardcoded credentials (environment variables only)
- [ ] Updated base images (< 30 days old)

## E.2 Kubernetes Best Practices Checklist

**Pod Specification:**
- [ ] Resource requests and limits defined for all containers
- [ ] Liveness and readiness probes configured
- [ ] Graceful termination period set (`terminationGracePeriodSeconds`)
- [ ] Security context with `runAsNonRoot: true`
- [ ] Security context with `readOnlyRootFilesystem: true` (if applicable)
- [ ] Security context with `allowPrivilegeEscalation: false`
- [ ] Security context with `capabilities: drop: - ALL`
- [ ] `imagePullPolicy: Always` or specific digest reference
- [ ] Pod Disruption Budget defined for HA workloads
- [ ] Affinity/anti-affinity rules for distribution

**Workload Management:**
- [ ] Rolling update strategy defined with appropriate `maxSurge`/`maxUnavailable`
- [ ] Horizontal Pod Autoscaler configured for variable load
- [ ] Vertical Pod Autoscaler considered for right-sizing
- [ ] Pod Security Standards (Restricted) enforced
- [ ] Service Account with minimal RBAC permissions
- [ ] Network Policies restricting ingress/egress

**Storage:**
- [ ] Persistent Volumes use appropriate StorageClass
- [ ] Backup strategy defined for stateful workloads
- [ ] Volume encryption enabled (storage class or CSI driver)

## E.3 CI Pipeline Checklist

**Code Quality:**
- [ ] Linting stage (ESLint, flake8, golint)
- [ ] Unit test coverage > 80%
- [ ] Static analysis (SonarQube, CodeClimate)
- [ ] Dependency vulnerability scanning
- [ ] Secret scanning (gitleaks, truffleHog)
- [ ] License compliance check (FOSSA, Snyk)

**Build Process:**
- [ ] Deterministic builds (same input → same output)
- [ ] Build caching configured and working
- [ ] Artifact versioning (semantic versioning or SHA)
- [ ] Multi-architecture support if needed (amd64, arm64)
- [ ] SBOM (Software Bill of Materials) generated
- [ ] Image signing (Cosign, Notary)

**Testing:**
- [ ] Integration tests against real dependencies (or TestContainers)
- [ ] Contract tests (Pact) for service boundaries
- [ ] Performance/smoke tests for critical paths
- [ ] Security tests (OWASP ZAP for web apps)

## E.4 CD Pipeline Checklist

**Deployment Strategy:**
- [ ] Blue/green or canary deployment (not recreate)
- [ ] Automated rollback on health check failure
- [ ] Database migrations run before app deployment (PreSync hooks)
- [ ] Feature flags for risky changes
- [ ] Progressive delivery with metrics analysis (Flagger)

**Environment Management:**
- [ ] Configuration externalized (ConfigMaps/Secrets, not baked in)
- [ ] Environment-specific values in Git (GitOps)
- [ ] Sealed Secrets or External Secrets for sensitive data
- [ ] Network isolation between environments

**Observability:**
- [ ] Health checks (liveness/readiness) configured
- [ ] Metrics endpoint exposed (Prometheus)
- [ ] Distributed tracing configured (OpenTelemetry)
- [ ] Log aggregation configured (structured logging)
- [ ] Alerts for deployment failures

## E.5 Security Checklist

**Supply Chain:**
- [ ] Container images scanned before deployment
- [ ] Image signatures verified at deployment
- [ ] Private registry with access controls
- [ ] SBOM stored with each release

**Runtime Security:**
- [ ] Pod Security Standards enforced
- [ ] Network Policies default-deny with explicit allows
- [ ] Secrets encrypted at rest (etcd encryption)
- [ ] Secrets rotated regularly (cert-manager for TLS)
- [ ] mTLS between services (Service Mesh)
- [ ] Audit logging enabled for API server

**Access Control:**
- [ ] RBAC least privilege (no cluster-admin for apps)
- [ ] Service accounts per workload (no default SA)
- [ ] OIDC authentication for cluster access
- [ ] Regular access reviews (quarterly)

## E.6 Monitoring Checklist

**Metrics:**
- [ ] RED method (Rate, Errors, Duration) for services
- [ ] USE method (Utilization, Saturation, Errors) for resources
- [ ] Business metrics (orders, payments) not just technical
- [ ] Alerting rules with appropriate severity levels
- [ ] Runbooks linked to alerts

**Logging:**
- [ ] Structured JSON logging
- [ ] Correlation IDs for request tracing
- [ ] Sensitive data redaction
- [ ] Log retention policy defined

**Tracing:**
- [ ] Distributed tracing for microservices
- [ ] Sampling configured (not 100% in production)
- [ ] Critical path identification

## E.7 Documentation Checklist

**Operational:**
- [ ] Architecture diagrams (C4 model recommended)
- [ ] Dependency mapping (data flow diagrams)
- [ ] Runbooks for common failures
- [ ] Disaster recovery procedures
- [ ] On-call escalation procedures

**Developer:**
- [ ] Local setup instructions
- [ ] API documentation (OpenAPI/Swagger)
- [ ] ADRs (Architecture Decision Records)
- [ ] Changelog maintenance

## E.8 Production Readiness Checklist

**Scalability:**
- [ ] Load testing results (2x expected peak load)
- [ ] Chaos engineering (fault injection) performed
- [ ] Auto-scaling tested under load
- [ ] Database connection limits verified

**Reliability:**
- [ ] SLOs defined (availability, latency)
- [ ] Error budgets calculated
- [ ] Circuit breakers configured
- [ ] Retry policies with exponential backoff
- [ ] Graceful degradation tested

**Compliance:**
- [ ] Data residency requirements met
- [ ] GDPR/CCPA compliance verified
- [ ] SOC 2 / ISO 27001 controls mapped
- [ ] Penetration testing completed (annual)
- [ ] Backup and recovery tested (quarterly)

**Go-Live:**
- [ ] Production-like environment tested
- [ ] Rollback procedure tested
- [ ] Monitoring dashboards reviewed
- [ ] Incident response team notified
- [ ] Business stakeholders signed off

---

**End of Appendix Sections**

This completes the comprehensive Dev Handbook covering CI/CD with Docker and Kubernetes from foundations to advanced topics, with practical projects and reference materials.