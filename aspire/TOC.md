

---

 **Building Cloud-Native Apps with .NET Aspire: The Definitive Guide from Start to Production**

---

## Part I: Laying the Foundation (Beginner)

**[Chapter 1: Welcome to the Distributed World](1.%20laying_the_foundation/1.%20welcome_to_the_distributed_world.ipynb)**
- The Problem: The complexity of modern cloud-native development (service discovery, configuration, health checks, orchestration).
- The Solution: What is .NET Aspire?
- Core Concepts: Orchestrator, App Model, Components.
- The Developer's Inner Loop: How Aspire simplifies local development.
- Setting up the Development Environment: Installing the latest .NET SDK, Docker Desktop, and the Aspire workload.

**[Chapter 2: Your First .NET Aspire Application](1.%20laying_the_foundation/2.%20your_first_net_aspire_application.ipynb)**
- Creating a new Aspire project from a template (`aspire-starter`).
- Anatomy of an Aspire Solution: Understanding the four projects (AppHost, ServiceDefaults, ApiService, Web).
- Running the AppHost: Seeing the Aspire Dashboard for the first time.
- The Aspire Dashboard Deep Dive: Exploring logs, traces, and metrics in real-time.
- **Hands-on:** Run the starter template and navigate the dashboard.

**[Chapter 3: The Service Defaults Project](1.%20laying_the_foundation/3.%20the_service_defaults_project.ipynb)**
- What is `ServiceDefaults` and why is it crucial?
- OpenTelemetry Deep Dive: Metrics, Logs, and Traces (The pillars of observability).
- Health Checks HTTP endpoints and standard health checks.
- Resilience: Adding default resilience patterns (timeouts, retries) with Polly.
- Service Discovery: How the defaults enable service-to-service communication.
- **Hands-on:** Modify the defaults to add a custom health check.

**[Chapter 4: The AppHost Project & Application Modeling](1.%20laying_the_foundation/4.%20the_apphost_project_application_modeling.ipynb)**
- The `IDistributedApplicationBuilder`: The heart of the orchestrator.
- Adding Resources: `.AddProject<T>`, `.AddContainer`, `.AddExecutable`.
- Resource Relationships: Connecting a frontend to a backend API using `.WithReference()`.
- Environment Variables and Configuration: Passing settings between services.
- **Hands-on:** Add a new .NET project to the solution and connect it to the existing API.

---

## Part II: Integrating with Data and Services (Intermediate)

**[Chapter 5: .NET Aspire Components](2.%20integrating_with_data_and_services/5.%20net_aspire_components.ipynb)**
- What are Components? Opinionated, cloud-ready clients for popular services.
- The "Connection String" Abstraction: How Aspire manages connections.
- Working with Databases:
    - Using the `Aspire.Npgsql` component for PostgreSQL.
    - Using the `Aspire.StackExchange.Redis` component for caching.
    - Adding and configuring a database container in the AppHost.
- **Hands-on:** Integrate a PostgreSQL database into the API project using its corresponding component.

**[Chapter 6: Messaging and Event-Driven Architecture](2.%20integrating_with_data_and_services/6.%20messaging_and_event_driven_architecture.ipynb)**
- Integrating with Message Brokers:
    - Using the `Aspire.RabbitMQ.Client` component.
    - Using the `Aspire.Azure.Messaging.ServiceBus` component.
- Adding a message queue container to the AppHost.
- Publishing and consuming messages in your services.
- **Hands-on:** Implement an order-processing workflow using RabbitMQ between two services.

**[Chapter 7: Externalizing Configuration with Aspire](2.%20integrating_with_data_and_services/7.%20externalizing_configuration_with_aspire.ipynb)**
- The limits of `appsettings.json`.
- Using the Aspire Configuration components:
    - `Aspire.Azure.Data.AppConfiguration` (Azure App Configuration).
    - `Aspire.Azure.KeyVault` (for secrets).
- Setting up these resources in the AppHost (using emulators or connection strings).
- Dynamic configuration reloading.
- **Hands-on:** Move a feature flag into Azure App Configuration and consume it in a service.

**[Chapter 8: Storage and Blobs](2.%20integrating_with_data_and_services/8.%20storage_and_blobs.ipynb)**
- Integrating with Azure Storage:
    - Using the `Aspire.Azure.Storage.Blobs` component.
    - Using the `Aspire.Azure.Storage.Queues` component.
- Adding Azurite (Azure Storage emulator) as a container resource in the AppHost.
- Uploading and processing files.
- **Hands-on:** Add a product image upload feature that stores images in Azure Blob Storage.

---

## Part III: Advanced Orchestration and Patterns (Advanced)

**[Chapter 9: Custom Resources and Lifecycle Hooks](3.%20advanced_orchestration_and_patterns/9.%20custom_resources_and_lifecycle_hooks.ipynb)**
- Beyond the built-in resources: Creating custom resources.
- Using `WithAnnotation<T>` to add metadata.
- Lifecycle Hooks: `BeforeStart`, `AfterResourcesCreated`.
- Running custom setup scripts or database migrations on startup.
- **Hands-on:** Create a custom resource that runs Entity Framework migrations before the web API starts.

**[Chapter 10: Advanced Service Discovery and Resiliency](3.%20advanced_orchestration_and_patterns/10.%20advanced_service_discovery_and_resiliency.ipynb)**
- Manual vs. Automatic Service Discovery.
- Configuring service binding schemes (http, https, tcp).
- Implementing advanced retry and circuit-breaker patterns using Polly and `IHttpClientFactory` within the Aspire context.
- Traffic Splitting and Routing for testing scenarios in the local dev environment.
- **Hands-on:** Configure a backend service to have multiple instances and observe how the frontend discovers them.

**[Chapter 11: Testing Aspire Applications](3.%20advanced_orchestration_and_patterns/11.%20testing_aspire_applications.ipynb)**
- The challenge of testing distributed systems.
- Integration Testing with Aspire:
    - Using `Aspire.Hosting.Testing` to spin up the AppHost for tests.
    - Writing integration tests that interact with real (containerized) dependencies.
- End-to-End Testing: Automating the dashboard and resource checks.
- **Hands-on:** Write an integration test that verifies the API can write and read from the test PostgreSQL container.

**[Chapter 12: Security from the Start](3.%20advanced_orchestration_and_patterns/12.%20security_from_the_start.ipynb)**
- Securing service-to-service communication with mTLS (mutual TLS).
- Integrating with Identity Providers:
    - Using the `Aspire.Keycloak` component (or similar) for auth.
    - Adding an authentication container (Keycloak) to the AppHost.
- Managing secrets safely with User Secrets and Parameter resources.
- Passing connection strings and credentials securely to containers.
- **Hands-on:** Add Keycloak to the AppHost and protect the API endpoints.

---

## Part IV: From Development to Production (Expert)

**[Chapter 13: Deployment Fundamentals with Aspire](4.%20from_development_to_production/13.%20deployment_fundamentals_with_aspire.ipynb)**
- The `aspirate` (Aspir8) Tool: The community standard for generating Kubernetes manifests.
- Compiling the Aspire manifest (`manifest.json`).
- Understanding the output: How Aspire resources map to Kubernetes concepts (Deployments, Services, ConfigMaps).
- Deploying to a local Kubernetes cluster (e.g., Docker Desktop, K3s, Minikube).
- **Hands-on:** Use `aspirate` to generate manifests and deploy the e-commerce app to a local K8s cluster.

**[Chapter 14: Deploying to the Cloud - Azure Container Apps](4.%20from_development_to_production/14.%20deploying_to_the_cloud_azure_container_apps.ipynb)**
- Azure Container Apps (ACA) as the ideal production target for Aspire.
- Using the Azure Developer CLI (AZD) with Aspire (`azd init`, `azd up`).
- How `azd` automates infrastructure provisioning (Bicep) and deployment.
- Configuring ACA: Ingress, scaling rules, and secrets management in the cloud.
- **Hands-on:** Deploy the entire application to Azure Container Apps using AZD.

**[Chapter 15: Production Readiness and Day 2 Operations](4.%20from_development_to_production/15.%20production_readiness_and_day_2_operations.ipynb)**
- Logging and Monitoring in Production:
    - Shipping logs to Azure Log Analytics or Grafana.
    - Setting up distributed tracing in production (e.g., with Aspire Dashboard or Azure Monitor Application Insights).
- Scaling: Configuring auto-scaling rules for your ACA services.
- Secrets Management: Moving from developer secrets to Azure Key Vault in production.
- **Hands-on:** Configure auto-scaling for the API service based on CPU usage.

**[Chapter 16: Real-World Project Structure and Best Practices](4.%20from_development_to_production/16.%20real_world_project_structure_and_best_practices.ipynb)**
- Organizing a large-scale Aspire solution (multiple AppHosts, shared ServiceDefaults).
- Versioning strategies for Aspire applications.
- CI/CD Pipelines:
    - Building container images in GitHub Actions / Azure DevOps.
    - Running Aspire integration tests in the pipeline.
    - Deploying the validated manifest.
- Pitfalls to avoid and common troubleshooting techniques.

**Appendix**
- A. Aspire Component Reference
- B. Troubleshooting Common Docker and Networking Issues
- C. Glossary of Terms