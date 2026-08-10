#!/bin/bash

# ================================================================
# INTERNSHIELD CLOUD SECURITY COMMAND CENTER - BOOTSTRAPPER
# ================================================================

echo -e "\033[0;32m[+] Initializing InternShield CSCC Project Structure...\033[0m"

# Main project directory
PROJECT_DIR="internshield-cloud-security"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR" || exit

# Create directory tree
mkdir -p core modules/{s3,iam,docker,system} ai/prompts reporting cli utils tests reports logs docs

# Create root files
touch main.py requirements.txt README.md LICENSE .gitignore .env.example config.example.yaml

# Create core files
touch core/__init__.py core/config.py core/logger.py core/models.py core/risk_engine.py core/exceptions.py core/validators.py

# Create module inits
touch modules/__init__.py modules/s3/__init__.py modules/iam/__init__.py modules/docker/__init__.py modules/system/__init__.py

# Create ai files
touch ai/__init__.py ai/base.py ai/shellgpt.py ai/openai_provider.py ai/anthropic_provider.py ai/gemini_provider.py ai/local_provider.py

# Create reporting files
touch reporting/__init__.py reporting/json_report.py reporting/markdown_report.py reporting/html_report.py reporting/txt_report.py

# Create cli files
touch cli/__init__.py cli/menu.py cli/dashboard.py cli/commands.py

# Create utils files
touch utils/__init__.py utils/subprocess_runner.py utils/security.py utils/filesystem.py

# Create docs
touch docs/architecture.md docs/aws-permissions.md docs/ai-integration.md docs/reporting.md docs/security-model.md docs/development.md

# Populate .gitignore
cat << 'EOF' > .gitignore
# Environments
.env
.venv
env/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Output and Logs
logs/*.log
reports/*.json
reports/*.html
reports/*.md
reports/*.txt
!logs/.gitkeep
!reports/.gitkeep

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
EOF

# Ensure empty directories are tracked in git initially
touch logs/.gitkeep reports/.gitkeep

# Populate requirements.txt
cat << 'EOF' > requirements.txt
rich>=13.0.0
typer>=0.9.0
questionary>=2.0.0
pydantic>=2.0.0
pyyaml>=6.0
python-dotenv>=1.0.0
boto3>=1.28.0
EOF

# Populate config.example.yaml
cat << 'EOF' > config.example.yaml
# InternShield Cloud Security Command Center Configuration
app:
  name: "InternShield CSCC"
  version: "1.0"
  log_level: "INFO"
  
aws:
  default_region: "us-east-1"
  max_retries: 3
  
ai:
  default_provider: "shellgpt"
  # Options: shellgpt, openai, anthropic, gemini, local, disabled
  require_human_confirmation: true
  
reporting:
  output_dir: "reports"
  default_formats: 
    - json
    - html
EOF

# Populate .env.example
cat << 'EOF' > .env.example
# ==========================================
# INTERNSHIELD SECURE ENVIRONMENT VARIABLES
# ==========================================
# DO NOT COMMIT ACTUAL SECRETS TO VERSION CONTROL

# AI Provider Keys (Uncomment and fill as needed)
# OPENAI_API_KEY="sk-..."
# ANTHROPIC_API_KEY="sk-ant-..."
# GEMINI_API_KEY="AIza..."

# AWS Overrides (Usually handled by ~/.aws/credentials)
# AWS_PROFILE="default"
EOF

echo -e "\033[0;32m[+] Project structure successfully created at ./${PROJECT_DIR}\033[0m"
echo -e "\033[1;37mRun the following to begin:\033[0m"
echo -e "cd ${PROJECT_DIR}"
echo -e "ls -la"