from dataclasses import dataclass
from pathlib import Path

from config.dates import DatesConfig
from src.config.templates import TemplatesConfig


@dataclass
class HomeworksConfig:
	need: bool
	path: Path
	dates: DatesConfig
	templates: TemplatesConfig
