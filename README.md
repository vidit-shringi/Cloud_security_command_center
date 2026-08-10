<div align="center">

<img src="assets/internshield-iam-banner.png" alt="InternShield AI-Powered IAM Security Auditor" width="100%">
# 🛡️ InternShield CSCC

### Cloud Security Command Center

> **Cloud Security. Intelligence. Visibility.**

<p align="center">
  <strong>AI-Assisted • Read-Only • Modular • DevSecOps-Oriented</strong>
</p>

<p align="center">
  A unified security assessment platform for AWS, Docker, Trivy, and AI-assisted security analysis.
</p>

---

## ✦ Overview

**InternShield CSCC** is a modular, AI-assisted **Cloud Security Command Center** designed to bring multiple cloud and container security assessment capabilities into a single professional command-line interface.

Instead of managing separate scripts for AWS auditing, Docker scanning, risk analysis, AI interpretation, and reporting, InternShield provides a centralized workflow for authorized security assessments.

The platform is designed around a **read-only and least-privilege security model**, with human approval required before any remediation action.

### Core Security Domains

```text
AWS Security
     │
     ├── S3 Security Assessment
     └── IAM Security Review

Container Security
     │
     └── Docker + Trivy Scanning

AI Security Analysis
     │
     ├── Shell-GPT
     ├── OpenAI-compatible Providers
     └── Extensible AI Provider Layer

Security Intelligence
     │
     ├── Finding Normalization
     ├── Risk Analysis
     └── Security Recommendations

Reporting
     │
     ├── JSON
     ├── HTML
     ├── Markdown
     └── TXT
```

---

# ✦ Why InternShield?

Modern security assessments often involve multiple tools, consoles, scripts, and reporting workflows.

InternShield aims to bring these capabilities together:

| Capability         | Purpose                                               |
| ------------------ | ----------------------------------------------------- |
| ☁️ AWS S3 Audit    | Review storage security configuration                 |
| 👤 AWS IAM Review  | Identify identity and permission risks                |
| 🐳 Docker Security | Assess locally available container images             |
| 🔎 Trivy           | Detect vulnerabilities, secrets and misconfigurations |
| 🧠 AI Analysis     | Interpret findings and generate recommendations       |
| ⚠️ Risk Engine     | Normalize and prioritize findings                     |
| 📊 Reporting       | Generate structured security reports                  |
| 🖥️ CLI Dashboard  | Provide a unified analyst experience                  |

The overall architecture is designed to behave more like a **security operations utility** than a collection of independent shell commands.

---

# ✦ Architecture

```text
                         ┌───────────────────────┐
                         │       SECURITY        │
                         │        ANALYST        │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   INTERN SHIELD CSCC  │
                         │     CLI COMMAND CENTER│
                         └───────────┬───────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
       ┌─────────────┐        ┌─────────────┐       ┌─────────────┐
       │ AWS SECURITY│        │   DOCKER    │       │ AI ANALYSIS │
       │             │        │  SECURITY   │       │             │
       │ S3 / IAM    │        │   Trivy     │       │ SGPT / LLMs │
       └──────┬──────┘        └──────┬──────┘       └──────┬──────┘
              │                      │                     │
              └──────────────────────┼─────────────────────┘
                                     ▼
                         ┌───────────────────────┐
                         │    FINDING ENGINE     │
                         └───────────┬───────────┘
                                     ▼
                         ┌───────────────────────┐
                         │      RISK ENGINE      │
                         └───────────┬───────────┘
                                     ▼
                         ┌───────────────────────┐
                         │    REPORT ENGINE      │
                         └───────────┬───────────┘
                                     │
                     ┌───────────────┼───────────────┐
                     ▼               ▼               ▼
                  JSON/MD          HTML             TXT
```

The project specification defines AWS APIs, Trivy, an LLM gateway, finding normalization, risk analysis, and report generation as the major architectural layers.

---

# ✦ Security Philosophy

InternShield is designed with **defensive security first**.

### 🔐 Default Principles

* **Read-only by default**
* **Least-privilege access**
* **Human oversight**
* **Credential protection**
* **Structured logging**
* **Input validation**
* **Output sanitization**
* **Timeout-controlled external commands**
* **No arbitrary LLM command execution**
* **No credential extraction**
* **No persistence**
* **No stealth mechanisms**
* **No destructive actions**

The platform is intended for AWS resources and assessment targets for which the operator has authorization.

---

# ✦ Modules

## ☁️ 01 — AWS S3 Security Auditor

The S3 module performs a defensive configuration assessment of accessible S3 resources.

### Assessment Areas

* S3 bucket enumeration
* Public Access Block configuration
* Bucket policies
* ACL-related configuration
* Encryption configuration
* Versioning
* Logging configuration
* Lifecycle configuration
* Risky configuration indicators

### Design

```text
AWS Identity
     │
     ▼
S3 Enumeration
     │
     ▼
Configuration Inspection
     │
     ▼
Finding Generation
     │
     ▼
Risk Analysis
```

The module is intended to inspect configuration rather than download arbitrary bucket contents or automatically modify resources.

---

# 👤 02 — AWS IAM Security Review

The IAM module provides a read-only review of identity and permission configuration.

### Assessment Areas

* IAM users
* IAM groups
* IAM roles
* Access-key metadata
* MFA status
* Attached policies
* Inline policies
* Permission-risk indicators
* Stale credential metadata
* Excessive permission indicators
* Root-account security indicators where available

The design specifically excludes retrieving passwords, secret access keys, credential dumping, account deletion, and automatic policy modification.

---

# 🐳 03 — Docker & Trivy Security

InternShield integrates **Trivy** for local container security assessment.

### Detection Areas

* Vulnerabilities
* Secrets where supported
* Misconfigurations
* SBOM information where supported
* Severity classification
* JSON output
* Human-readable reporting

### Pipeline

```text
Docker Image
     │
     ▼
   Trivy
     │
     ▼
Raw Findings
     │
     ▼
Normalization
     │
     ▼
Risk Engine
     │
     ▼
AI Analysis
     │
     ▼
Security Report
```

The planned implementation uses Python subprocess execution with timeouts and structured JSON parsing rather than unsafe shell invocation.

---

# 🧠 04 — AI Security Analysis

InternShield is designed around an **AI Provider abstraction layer** instead of being permanently coupled to a single AI service.

### Provider Architecture

```text
                  AIProvider
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Shell-GPT       OpenAI       Other LLMs
```

Planned provider options include:

* Shell-GPT
* OpenAI-compatible APIs
* Anthropic
* Gemini
* Local LLM
* AI disabled mode

The provider abstraction allows additional models to be integrated without redesigning the rest of the application.

---

# ⚠️ AI Safety Model

AI is treated as an **analysis assistant**, not an autonomous security operator.

```text
Security Findings
       │
       ▼
      AI
       │
       ▼
Structured Recommendation
       │
       ▼
Safety Validation
       │
       ▼
Human Review
       │
       ▼
Optional Approved Action
```

InternShield must never blindly execute arbitrary commands generated by an LLM.

---

# 📊 Risk Engine

All security findings are normalized into a common finding model.

### Finding Structure

```text
Finding ID
Title
Category
Resource
Severity
Confidence
Evidence
Impact
Recommendation
Source Tool
Timestamp
```

### Severity Model

```text
CRITICAL
   │
 HIGH
   │
MEDIUM
   │
 LOW
   │
 INFO
```

The final severity is intended to use deterministic security logic, while AI analysis can provide additional context rather than becoming the sole authority for risk classification.

---

# 📑 Reporting Engine

InternShield is designed to transform assessment results into structured reports.

### Supported Formats

```text
JSON
HTML
Markdown
TXT
```

PDF generation can be added as an optional reporting capability.

### Report Contents

* Assessment ID
* Assessment date
* AWS account information where applicable
* Environment
* Tools used
* Executive summary
* Risk summary
* Critical findings
* High findings
* Medium findings
* Low findings
* Detailed findings
* Recommendations
* Tool-output references
* AI analysis
* Assessment limitations

Sensitive credentials must never be included in generated reports.

---

# 🖥️ CLI Experience

InternShield is designed around a professional terminal interface using technologies such as:

* **Rich**
* **Questionary**
* **Typer**

### Main Menu

```text
╔══════════════════════════════════════════════════╗
║                 INTERN SHIELD                     ║
║          CLOUD SECURITY COMMAND CENTER            ║
╚══════════════════════════════════════════════════╝

[1] AWS S3 Security Audit
[2] AWS IAM Security Review
[3] Docker Image Security Scan
[4] AWS Security Overview
[5] AI Security Analysis
[6] Run Combined Security Assessment
[7] View Previous Reports
[8] Configuration
[9] System Health Check
[0] Exit
```

The CLI design specification calls for tables, panels, progress indicators, status badges, and a restrained black/white/neon-green visual identity.

---

# ⚡ CLI Usage

### Interactive Mode

```bash
python main.py
```

### Direct Commands

```bash
python main.py s3
```

```bash
python main.py iam
```

```bash
python main.py docker
```

```bash
python main.py ai
```

```bash
python main.py full-audit
```

```bash
python main.py health
```

```bash
python main.py reports
```

### Help

```bash
python main.py --help
```

The command-oriented interface is intended to complement the interactive dashboard.

---

# 🚀 Combined Security Assessment

The combined assessment provides a unified workflow:

```text
Preflight
   │
   ▼
AWS Identity Verification
   │
   ▼
S3 Assessment
   │
   ▼
IAM Assessment
   │
   ▼
Docker Assessment
   │
   ▼
Finding Normalization
   │
   ▼
Risk Calculation
   │
   ▼
AI Analysis
   │
   ▼
Report Generation
   │
   ▼
Assessment Summary
```

Individual module failures should not unnecessarily terminate the entire assessment pipeline.

---

# 📁 Project Structure

```text
InternShield-CSCC/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── config.example.yaml
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── models.py
│   ├── risk_engine.py
│   └── validators.py
│
├── modules/
│   ├── __init__.py
│   │
│   ├── s3/
│   │   ├── __init__.py
│   │   └── scanner.py
│   │
│   ├── iam/
│   │   ├── __init__.py
│   │   └── scanner.py
│   │
│   └── docker/
│       ├── __init__.py
│       └── scanner.py
│
├── ai/
│   ├── __init__.py
│   ├── base.py
│   ├── shellgpt.py
│   ├── openai_provider.py
│   └── prompts/
│       └── templates.py
│
├── reporting/
│   ├── __init__.py
│   ├── json_report.py
│   ├── markdown_report.py
│   ├── html_report.py
│   └── txt_report.py
│
├── cli/
│   ├── __init__.py
│   ├── commands.py
│   ├── dashboard.py
│   └── menu.py
│
├── tests/
│   ├── __init__.py
│   └── test_risk_engine.py
│
├── reports/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
└── docs/
    ├── architecture.md
    ├── aws-permissions.md
    ├── ai-integration.md
    ├── reporting.md
    ├── security-model.md
    └── development.md
```

This structure follows the modular architecture specified for the project.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd InternShield-CSCC
```

## 2. Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment

```bash
cp .env.example .env
```

Configure only the providers you intend to use.

---

# 🔐 Credential Security

**Never commit credentials to GitHub.**

Do not commit:

```text
.env
AWS access keys
AWS secret keys
API keys
Tokens
Passwords
Sensitive reports
Sensitive logs
```

Use environment variables, AWS-supported credential mechanisms, or appropriate operating-system credential stores.

Example:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
```

The repository should contain only safe configuration templates such as:

```text
.env.example
config.example.yaml
```

The project specification explicitly requires secrets to remain outside the repository.

---

# ☁️ AWS Requirements

InternShield is designed around **least-privilege AWS access**.

The project should use only the permissions required by the enabled assessment modules.

### Principle

```text
❌ AdministratorAccess
        │
        ▼
     Avoid

✅ Minimum Required
       Read-Only
       Permissions
```

AWS permissions should be documented per module and should not unnecessarily request administrative privileges.

---

# 🩺 System Health Check

InternShield includes a health-check concept for validating required tooling.

Expected checks include:

```text
[✓] Python
[✓] AWS CLI
[✓] AWS Identity
[✓] Docker
[✓] Trivy
[✓] Shell-GPT
[!] Optional AI Provider
```

The health check should provide installation/configuration guidance rather than silently installing system packages.

---

# 🧪 Testing

The project is designed to include unit tests for:

* S3 parsing
* IAM parsing
* Trivy parsing
* AI parsing
* Severity/risk engine
* Configuration
* Logging
* Report generation
* Input validation

Run the available tests with:

```bash
python -m unittest discover
```

The project specification also calls for mocked AWS responses so core tests do not require a real AWS account.

---

# 🛡️ Security Engineering

InternShield emphasizes defensive engineering throughout the application.

### Built-in design goals

```text
Input Validation
       ↓
Output Sanitization
       ↓
Command Injection Prevention
       ↓
Path Traversal Protection
       ↓
Secret Masking
       ↓
Least Privilege
       ↓
Secure Temporary Files
       ↓
Structured Logging
       ↓
Timeouts
       ↓
Resource Limits
```

External commands should use argument arrays and controlled execution rather than unsafe `shell=True` usage with untrusted input.

---

# 📈 Observability

The command center is designed to surface operational information such as:

```text
Elapsed Time
Modules Executed
Success / Failure
Finding Counts
AI Status
Report Path
```

Example:

```text
╔══════════════════════════════════════════════╗
║              ASSESSMENT SUMMARY              ║
╠══════════════════════════════════════════════╣
║ S3 Findings       : 08                       ║
║ IAM Findings      : 05                       ║
║ Docker Findings   : 13                       ║
║ Critical          : 02                       ║
║ High              : 07                       ║
║ Medium            : 11                       ║
║ Low               : 06                       ║
║ AI Analysis       : COMPLETE                 ║
║ Report            : reports/audit-001.html   ║
╚══════════════════════════════════════════════╝
```

---

# 🗺️ Development Roadmap

The project is organized into progressive development phases:

```text
Phase 01  → Architecture & Project Foundation
Phase 02  → Core Models, Configuration & Logging
Phase 03  → AWS S3 Security Module
Phase 04  → AWS IAM Security Module
Phase 05  → Docker & Trivy Integration
Phase 06  → AI Provider Abstraction
Phase 07  → Shell-GPT Integration
Phase 08  → Additional AI Provider Integration
Phase 09  → Risk Engine
Phase 10  → Reporting
Phase 11  → CLI Dashboard
Phase 12  → Unit Testing
Phase 13  → Documentation
Phase 14  → Security Review
Phase 15  → Final Integration
```

The original development plan defines a phased implementation approach with verification after each stage.

---

# ⚠️ Responsible Use

InternShield is intended for:

* Authorized AWS environments
* Authorized cloud-security assessments
* Local Docker security testing
* Lab environments
* Security research
* Defensive security operations
* Educational purposes

### Do not use this project for:

* Unauthorized AWS access
* Credential theft
* Unauthorized scanning
* Destructive activity
* Persistence
* Stealth
* Security-control bypass
* Unauthorized exploitation

**Always obtain appropriate authorization before assessing systems or cloud resources.**

---

# 🤝 Contributing

Contributions are welcome.

A typical contribution workflow:

```bash
git clone <repository>
cd InternShield-CSCC
```

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Implement and test your changes:

```bash
python -m unittest discover
```

Commit:

```bash
git add .
git commit -m "Add: your feature"
```

Push:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 📜 License

This project is intended to be distributed under the license specified in the repository's `LICENSE` file.

---

# 👨‍💻 Author

### Vidit Shringi

**InternShield CSCC**

> *Your Shield in the Digital World.*

Designed as a cybersecurity R&D project focused on **cloud security, DevSecOps, security automation, AI-assisted analysis, and professional security tooling**.

---

# ⭐ Project Vision

InternShield is not intended to be just another collection of security scripts.

The long-term vision is a modular security command center where:

```text
           CLOUD
             │
             ▼
        SECURITY DATA
             │
             ▼
       NORMALIZATION
             │
             ▼
        RISK ANALYSIS
             │
             ▼
       AI ASSISTANCE
             │
             ▼
      HUMAN DECISION
             │
             ▼
       PROFESSIONAL
         REPORTING
```

The goal is to transform fragmented cloud-security checks into a **single, maintainable, observable and extensible security operations platform**.

---

<p align="center">

### 🛡️ InternShield CSCC

**Cloud Security • Intelligence • Visibility**

**Built for Security. Designed for Scale.**

</p>
