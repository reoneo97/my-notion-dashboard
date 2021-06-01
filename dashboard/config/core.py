from pydantic import BaseModel
from pathlib import Path
import yaml
from typing import Dict, Optional

CFG_PATH = "my_config.yaml"


class NotionConfig(BaseModel):
    integration_token: str
    notion_url: str
    db_id: str
    _source: Optional[str]


def fetch_config_from_yaml(cfg_path: Path = None) -> Dict:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def parse_config(cfg_path: Path = None) -> Dict:
    if cfg_path:
        with open(cfg_path, "r") as f:
            parsed = yaml.load(f)
            return parsed


def load_config(cfg_path: Path = None) -> NotionConfig:
    parsed_config = parse_config(CFG_PATH)
    config = NotionConfig(**parsed_config["notion_config"])
    return config

config = load_config(CFG_PATH)
