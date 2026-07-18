from dataclasses import dataclass
from pathlib import Path


@dataclass
class TemplatesConfig:
	starts_with: Path
	ends_with: Path
