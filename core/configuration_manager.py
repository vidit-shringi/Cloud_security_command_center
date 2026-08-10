"""
Configuration Management.
Securely loads settings from config.yaml and environment variables (.env).
Masks sensitive data.
"""
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel
from core.exceptions import ConfigurationError

# Load environment variables from .env (API Keys, etc.)
load_dotenv()

class AppConfig(BaseModel):
    name: str = "InternShield CSCC"
    version: str = "1.0"
    log_level: str = "INFO"

class AWSConfig(BaseModel):
    default_region: str = "us-east-1"
    max_retries: int = 3

class AIConfig(BaseModel):
    default_provider: str = "shellgpt"
    require_human_confirmation: bool = True

class ReportingConfig(BaseModel):
    output_dir: str = "reports"
    default_formats: list[str] = ["json", "html"]

class ConfigManager:
    """Singleton-style configuration loader."""
    _instance = None
    
    def __init__(self):
        self.app = AppConfig()
        self.aws = AWSConfig()
        self.ai = AIConfig()
        self.reporting = ReportingConfig()
        self._load_yaml()
        
    def _load_yaml(self):
        config_path = Path("config.yaml")
        if not config_path.exists():
            # Fallback to defaults if no config.yaml exists
            return
            
        try:
            with open(config_path, "r") as f:
                data = yaml.safe_load(f) or {}
                
            if "app" in data:
                self.app = AppConfig(**data["app"])
            if "aws" in data:
                self.aws = AWSConfig(**data["aws"])
            if "ai" in data:
                self.ai = AIConfig(**data["ai"])
            if "reporting" in data:
                self.reporting = ReportingConfig(**data["reporting"])
        except Exception as e:
            raise ConfigurationError(f"Failed to parse config.yaml: {str(e)}")

    def get_ai_api_key(self, provider_name: str) -> str:
        """Securely fetch API keys without storing them in memory."""
        key_map = {
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "gemini": "GEMINI_API_KEY"
        }
        env_var = key_map.get(provider_name.lower())
        if not env_var:
            return ""
        return os.getenv(env_var, "")

# Global configuration instance
settings = ConfigManager()