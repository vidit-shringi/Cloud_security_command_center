"""
InternShield Cloud Security Command Center (IS-CSCC)
Main Entry Point.

This script wires together the Typer CLI arguments with the Interactive Menu.
"""
import sys
import typer
from typing import List

from core.logger import log
from core.config import settings
from cli.menu import interactive_menu
from cli.commands import execute_audit
from cli.dashboard import print_status_dashboard
from ai.base import AIProvider
from ai import AIProviderFactory

app = typer.Typer(
    help="InternShield Cloud Security Command Center",
    add_completion=False,
    no_args_is_help=False
)

def check_system_health():
    """Performs a background health check of the underlying tools."""
    import subprocess
    
    # Check AWS CLI
    aws_ok = False
    try:
        res = subprocess.run(["aws", "sts", "get-caller-identity"], capture_output=True, timeout=5)
        aws_ok = res.returncode == 0
    except FileNotFoundError:
        pass

    # Check Docker/Trivy
    docker_ok = False
    try:
        res = subprocess.run(["trivy", "--version"], capture_output=True, timeout=5)
        docker_ok = res.returncode == 0
    except FileNotFoundError:
        pass

    # Check AI
    ai_provider_name = settings.ai.default_provider
    if ai_provider_name.lower() == "disabled":
        ai_status = None
    else:
        try:
            provider = AIProviderFactory.create(ai_provider_name)
            ai_status = ai_provider_name if provider.health_check() else None
        except Exception:
            ai_status = None

    return aws_ok, docker_ok, ai_status

@app.command()
def interactive():
    """Launch the Interactive Command Center (Default)."""
    aws_ok, docker_ok, ai_status = check_system_health()
    print_status_dashboard(aws_ok, docker_ok, ai_status)
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n[+] Assessment aborted by user. Stay Secure!\n")
        sys.exit(0)

@app.command()
def s3():
    """Run an isolated AWS S3 Security Audit."""
    execute_audit(scanners=["s3"], target_env="AWS S3")

@app.command()
def iam():
    """Run an isolated AWS IAM Security Review."""
    execute_audit(scanners=["iam"], target_env="AWS IAM")

@app.command()
def docker(image: str = typer.Argument(..., help="Docker image name to scan (e.g., nginx:latest)")):
    """Run a local Docker Container Vulnerability Scan."""
    execute_audit(scanners=["docker"], target_env="Local Container", image_name=image)

@app.command()
def full_audit():
    """Run a combined security assessment across AWS S3 and IAM."""
    execute_audit(scanners=["s3", "iam"], target_env="AWS Combined Environment")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    InternShield CSCC - Defensive Posture Management.
    """
    if ctx.invoked_subcommand is None:
        interactive()

if __name__ == "__main__":
    app()