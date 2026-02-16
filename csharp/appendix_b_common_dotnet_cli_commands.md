# Appendix B: Common .NET CLI Commands

The .NET Command‑Line Interface (CLI) is a cross‑platform tool for developing, building, running, and publishing .NET applications. This appendix lists the most frequently used commands, with examples and explanations. All commands assume you have the .NET SDK installed and are run from a terminal/command prompt.

---

## B.1 Getting Help and Version Information

| Command | Description |
|---------|-------------|
| `dotnet --version` | Displays the installed .NET SDK version. |
| `dotnet --info` | Shows detailed .NET installation information (SDKs, runtimes, environment). |
| `dotnet --list-sdks` | Lists all installed .NET SDKs. |
| `dotnet --list-runtimes` | Lists all installed .NET runtimes. |
| `dotnet help` | Shows general help. Append a command for specific help (e.g., `dotnet help new`). |

---

## B.2 Creating New Projects and Solutions

| Command | Description |
|---------|-------------|
| `dotnet new` | Lists all available templates. |
| `dotnet new console -n MyApp` | Creates a new console application named MyApp. |
| `dotnet new webapi -n MyApi` | Creates a new Web API project. |
| `dotnet new mvc -n MyMvcApp` | Creates a new MVC project. |
| `dotnet new classlib -n MyLib` | Creates a new class library. |
| `dotnet new xunit -n MyTests` | Creates a new xUnit test project. |
| `dotnet new sln -n MySolution` | Creates a new empty solution file. |
| `dotnet sln add MyApp/MyApp.csproj` | Adds a project to the solution. |
| `dotnet sln list` | Lists all projects in the solution. |

**Examples:**
```bash
dotnet new console -n HelloWorld
cd HelloWorld
dotnet run
```

---

## B.3 Building and Running

| Command | Description |
|---------|-------------|
| `dotnet build` | Builds the project and its dependencies. |
| `dotnet build -c Release` | Builds in Release configuration. |
| `dotnet run` | Runs the application (builds first if needed). |
| `dotnet run -- --arg1 value` | Passes arguments to the application (after `--`). |
| `dotnet clean` | Cleans the output of a project. |
| `dotnet restore` | Restores NuGet packages (implicit in most commands). |

**Examples:**
```bash
dotnet build MyApp.csproj
dotnet run --project MyApp
```

---

## B.4 Testing

| Command | Description |
|---------|-------------|
| `dotnet test` | Runs tests in the current project or solution. |
| `dotnet test --filter "Category=Unit"` | Runs tests matching a filter expression. |
| `dotnet test --logger "trx;LogFileName=results.trx"` | Runs tests and saves results in a TRX file. |
| `dotnet test --collect:"XPlat Code Coverage"` | Runs tests and collects code coverage (requires coverlet). |

**Examples:**
```bash
cd MyTests
dotnet test
dotnet test --filter "FullyQualifiedName~CalculatorTests"
```

---

## B.5 Managing NuGet Packages

| Command | Description |
|---------|-------------|
| `dotnet add package Newtonsoft.Json` | Adds a NuGet package reference to the project. |
| `dotnet add package Microsoft.EntityFrameworkCore -v 6.0.0` | Adds a specific version. |
| `dotnet remove package Newtonsoft.Json` | Removes a package reference. |
| `dotnet list package` | Lists all package references in the project. |
| `dotnet list package --outdated` | Lists outdated packages with available updates. |
| `dotnet restore` | Restores packages (automatically run by most commands). |

**Examples:**
```bash
dotnet add package Dapper
dotnet list package --outdated
```

---

## B.6 Publishing and Deploying

| Command | Description |
|---------|-------------|
| `dotnet publish -c Release` | Publishes the app in Release mode (framework‑dependent). |
| `dotnet publish -c Release -r win-x64 --self-contained true` | Publishes a self‑contained deployment for Windows x64. |
| `dotnet publish -c Release -o ./publish` | Publishes to a specific output folder. |

**Examples:**
```bash
dotnet publish -c Release -r linux-x64 --self-contained true
```

The output can be deployed to the target machine.

---

## B.7 Managing Solutions and Projects

| Command | Description |
|---------|-------------|
| `dotnet sln add **/*.csproj` | Adds all projects matching pattern to solution. |
| `dotnet sln remove MyLib/MyLib.csproj` | Removes a project from the solution. |
| `dotnet new globaljson` | Creates a `global.json` file to pin SDK version. |
| `dotnet new tool-manifest` | Creates a local tool manifest. |
| `dotnet tool install dotnet-ef` | Installs a local tool (adds to manifest). |
| `dotnet tool run dotnet-ef` | Runs a local tool. |

**Examples:**
```bash
dotnet new globaljson --sdk-version 8.0.100
dotnet tool install dotnet-ef
```

---

## B.8 Entity Framework Core Commands

If the `dotnet ef` tool is installed (globally or locally):

| Command | Description |
|---------|-------------|
| `dotnet ef migrations add InitialCreate` | Creates a new migration. |
| `dotnet ef migrations list` | Lists all migrations. |
| `dotnet ef database update` | Applies pending migrations to the database. |
| `dotnet ef database drop` | Drops the database. |
| `dotnet ef dbcontext scaffold` | Reverse engineers a DbContext from an existing database. |

**Examples:**
```bash
dotnet ef migrations add AddCustomerTable
dotnet ef database update
```

---

## B.9 Working with Templates

| Command | Description |
|---------|-------------|
| `dotnet new --list` | Lists installed templates. |
| `dotnet new --search web` | Searches for templates on NuGet.org. |
| `dotnet new --install Microsoft.AspNetCore.SpaTemplates` | Installs a template package. |
| `dotnet new --uninstall Microsoft.AspNetCore.SpaTemplates` | Uninstalls a template package. |

---

## B.10 Global Options

| Option | Description |
|--------|-------------|
| `-v|--verbosity <LEVEL>` | Sets verbosity level: q[uiet], m[inimal], n[ormal], d[etailed], diag[nostic]. |
| `-h|--help` | Shows help for a command. |
| `--version` | Shows version information. |

**Example:**
```bash
dotnet build --verbosity diag
```

---

## B.11 Summary

This appendix covered the essential .NET CLI commands for everyday development. For a complete reference, run `dotnet help` or visit the [official .NET CLI documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/).

---

**Next:** Appendix C: Recommended Tools and Libraries – a curated list of tools and NuGet packages that enhance productivity and code quality in C# development.