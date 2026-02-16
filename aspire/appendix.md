## Appendix

This appendix serves as a quick reference for the tools, components, and concepts discussed throughout the book. Use it to look up details about Aspire components, troubleshoot common issues, and understand key terminology.

---

### A. Aspire Component Reference

.NET Aspire components are NuGet packages that simplify connecting to popular services. Below is a reference table of the most commonly used components, their hosting packages (for the AppHost), and their client packages (for the services).

| Service / Technology | Hosting Package (AppHost) | Client Package (Service) | Description |
|----------------------|----------------------------|---------------------------|-------------|
| **PostgreSQL** | `Aspire.Hosting.PostgreSQL` | `Aspire.Npgsql` or `Aspire.Npgsql.EntityFrameworkCore.PostgreSQL` | Adds a PostgreSQL container; client registers `NpgsqlDataSource` and adds health checks, tracing, metrics. |
| **Redis** | `Aspire.Hosting.Redis` | `Aspire.StackExchange.Redis` | Adds a Redis container; client registers `IConnectionMultiplexer`. |
| **RabbitMQ** | `Aspire.Hosting.RabbitMQ` | `Aspire.RabbitMQ.Client` | Adds a RabbitMQ container; client registers `IConnection` and `IChannel`. |
| **Azure Service Bus** | `Aspire.Hosting.Azure.ServiceBus` | `Aspire.Azure.Messaging.ServiceBus` | Adds an Azure Service Bus resource (can use emulator); client registers `ServiceBusClient`. |
| **Azure Storage (Blobs)** | `Aspire.Hosting.Azure.Storage` | `Aspire.Azure.Storage.Blobs` | Adds Azure Storage (with emulator); client registers `BlobServiceClient`. |
| **Azure Storage (Queues)** | `Aspire.Hosting.Azure.Storage` | `Aspire.Azure.Storage.Queues` | Adds queue storage; client registers `QueueServiceClient`. |
| **Azure Storage (Tables)** | `Aspire.Hosting.Azure.Storage` | `Aspire.Azure.Storage.Tables` | Adds table storage; client registers `TableServiceClient`. |
| **Azure Key Vault** | `Aspire.Hosting.Azure.KeyVault` | `Aspire.Azure.Security.KeyVault` | Adds Key Vault resource (no emulator); client registers `SecretClient` and `KeyClient`. |
| **Azure App Configuration** | `Aspire.Hosting.Azure.AppConfiguration` | `Aspire.Azure.Data.AppConfiguration` | Adds App Configuration resource; client registers `ConfigurationClient`. |
| **Keycloak** | `Aspire.Hosting.Keycloak` | (No official client; use standard OpenID Connect) | Adds Keycloak container. |
| **MongoDB** | `Aspire.Hosting.MongoDB` | `Aspire.MongoDB.Driver` | Adds MongoDB container; client registers `IMongoClient`. |
| **SQL Server** | `Aspire.Hosting.SqlServer` | `Aspire.Microsoft.Data.SqlClient` or `Aspire.EntityFrameworkCore.SqlServer` | Adds SQL Server container; client registers `SqlConnection`. |
| **MySQL** | `Aspire.Hosting.MySql` | `Aspire.MySqlConnector` or `Aspire.EntityFrameworkCore.MySql` | Adds MySQL container; client registers `MySqlConnection`. |
| **Oracle** | `Aspire.Hosting.Oracle` | `Aspire.Oracle.ManagedDataAccess` | Adds Oracle Free container; client registers `OracleConnection`. |

#### A.1 How to Use a Component

1. **In the AppHost**: Add the hosting package, then create the resource using the appropriate extension method (e.g., `builder.AddPostgres("mydb")`). Optionally, call `WithDataVolume()` for persistence, and reference it from your services using `WithReference()`.
2. **In the Service**: Add the client package, then in `Program.cs` call the extension method (e.g., `builder.AddNpgsqlDataSource("mydb")`). This registers the client and adds health checks, telemetry, etc.
3. **Configure** via code or `appsettings.json` using the options pattern.

Example for PostgreSQL:

```csharp
// AppHost
var postgres = builder.AddPostgres("postgres").WithDataVolume();
var productsDb = postgres.AddDatabase("productsdb");

var apiService = builder.AddProject<Projects.Api>("api")
    .WithReference(productsDb);

// In ApiService Program.cs
builder.AddNpgsqlDataSource("productsdb");
```

#### A.2 Component Configuration Keys

Each component can be configured using the `Aspire:{ComponentName}:{ResourceName}` section in `appsettings.json`. For example, for the PostgreSQL component named "productsdb":

```json
{
  "Aspire": {
    "Npgsql": {
      "Productsdb": {
        "ConnectionString": "Host=...",
        "HealthChecks": true,
        "Tracing": true,
        "Metrics": true,
        "Retry": {
          "MaxRetryCount": 3
        }
      }
    }
  }
}
```

Refer to the documentation of each component for available options.

---

### B. Troubleshooting Common Docker and Networking Issues

When running Aspire applications locally, you may encounter issues related to Docker containers or networking. This section provides solutions to common problems.

#### B.1 Docker Desktop Not Running

**Symptom**: When you run the AppHost, you see errors like "Cannot connect to Docker" or containers fail to start.

**Solution**:
- Ensure Docker Desktop is installed and running. Look for the Docker icon in the system tray.
- If Docker is running, try restarting it.
- Verify that the Docker daemon is accessible by running `docker ps` in a terminal.

#### B.2 Port Conflicts

**Symptom**: A container fails to start because the port it wants to use is already in use.

**Solution**:
- Change the port mapping in the AppHost using `WithEndpoint` or by setting the port in the resource definition.
- Find the process using the port (e.g., `netstat -ano | findstr :5432` on Windows, `lsof -i :5432` on macOS/Linux) and stop it, or configure Aspire to use a different port.

#### B.3 Container Names Conflict

**Symptom**: You see an error like "The container name ... is already in use".

**Solution**:
- Aspire generates unique container names based on the resource name and a random suffix. If you stop and start the AppHost, old containers may still exist. Run `docker rm -f <container-name>` to remove them, or use the dashboard to stop resources properly.
- Alternatively, use `docker system prune` to clean up unused containers.

#### B.4 Persistent Data Issues

**Symptom**: After restarting the AppHost, database data is missing or corrupted.

**Solution**:
- Ensure you used `WithDataVolume()` for your database resource. This creates a Docker volume that persists data across container restarts.
- To reset the data, you can remove the volume: `docker volume ls` to find the volume name, then `docker volume rm <volume-name>`. Be careful not to remove important data.

#### B.5 Service Discovery Not Working

**Symptom**: A service cannot reach another service using its logical name (e.g., `http://apiservice`).

**Solution**:
- Verify that the `WithReference` is correctly set up in the AppHost.
- In the service, ensure you called `builder.AddServiceDefaults()` (which adds service discovery) and that the `HttpClient` base address is set to the logical name (e.g., `http://apiservice`).
- Check the environment variables of the calling service (in the dashboard) for entries like `services__apiservice__http__0`. If they are missing, the reference may not be correctly established.
- In Kubernetes or ACA, ensure that the service DNS name matches the logical name.

#### B.6 Health Checks Failing

**Symptom**: The dashboard shows a resource as unhealthy, or the `/health` endpoint returns unhealthy.

**Solution**:
- Check the logs of the service to see why the health check failed.
- For database health checks, ensure the database is reachable and the connection string is correct.
- For custom health checks, verify that they are registered correctly and that any dependencies are available.
- If you haven't mapped the health endpoint, do so with `app.MapHealthChecks("/health")`.

#### B.7 Docker Networking on macOS/Windows

**Symptom**: Containers can't communicate with each other, or the host cannot reach a container.

**Solution**:
- By default, containers run on a bridge network and are accessible via published ports. Use `localhost` with the published port to access from the host.
- For container-to-container communication, use the container name (e.g., `postgres`) as the hostname. Aspire sets up a network automatically, so this should work.
- On macOS/Windows, Docker runs in a VM; networking is generally seamless, but if you have complex setups, you may need to check Docker's network settings.

#### B.8 Resource Cleanup

After stopping the AppHost, some containers may remain. To clean up:

- Use the dashboard's stop button for each resource.
- Run `docker stop $(docker ps -q)` to stop all containers, then `docker system prune` to remove stopped containers and unused images.

---

### C. Glossary of Terms

| Term | Definition |
|------|------------|
| **.NET Aspire** | A cloud‑ready stack for building observable, production‑ready, distributed applications. |
| **AppHost** | The orchestrator project that models and runs the entire application, including services and dependencies. |
| **Resource** | Any component modeled in the AppHost: a .NET project, a container, an executable, etc. |
| **Logical Name** | The name given to a resource in the AppHost (e.g., "apiservice"). Used for service discovery and configuration. |
| **WithReference** | A method that establishes a dependency between two resources and injects connection information into the dependent resource. |
| **Service Defaults** | A shared project that configures OpenTelemetry, health checks, resilience, and service discovery for all services. |
| **Component** | A NuGet package that provides a pre‑configured client for a service (e.g., PostgreSQL, Redis) with health checks and telemetry. |
| **OpenTelemetry** | An open standard for observability (logs, metrics, traces). Aspire uses it to send telemetry to the dashboard. |
| **OTLP** | OpenTelemetry Protocol, used to export telemetry data. |
| **Health Check** | An endpoint that reports the health status of a service. Used by orchestrators for liveness and readiness probes. |
| **Resilience** | The ability of a system to handle transient failures. In Aspire, provided by Polly policies (retry, circuit breaker, timeout). |
| **Service Discovery** | The mechanism by which a service locates the network address of another service using a logical name. |
| **Parameter** | A special resource that represents a value (often a secret) that can be provided at runtime via user secrets or environment variables. |
| **Annotation** | Metadata attached to a resource, used to influence behavior (e.g., lifecycle hooks, endpoint configuration). |
| **Lifecycle Hook** | A way to execute custom code at specific points in the application startup (e.g., before resources start, after they are created). |
| **Manifest** | A JSON file generated by the AppHost that describes all resources and their relationships. Used for deployment to Kubernetes or ACA. |
| **Aspirate** | A community tool that converts the Aspire manifest into Kubernetes YAML. |
| **Azure Developer CLI (AZD)** | A command‑line tool that provisions Azure resources and deploys applications, with built‑in support for Aspire. |
| **Azure Container Apps (ACA)** | A serverless container platform that runs on Kubernetes but abstracts away the cluster management. |
| **Kubernetes** | An open‑source container orchestration platform. |
| **mTLS** | Mutual Transport Layer Security – both client and server authenticate each other using certificates. |
| **Keycloak** | An open‑source identity and access management solution supporting OpenID Connect and OAuth2. |
| **Shared Access Signature (SAS)** | A secure, time‑limited URI that grants access to a specific Azure Storage resource. |
| **Azurite** | An Azure Storage emulator that runs locally in a Docker container, simulating Blob, Queue, and Table storage. |

---

This concludes the appendix and the book. We hope you found this handbook valuable and that you are now equipped to build and deploy cloud‑native applications with .NET Aspire. Happy coding!