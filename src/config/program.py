from dataclasses import dataclass
from pathlib import Path

from src.config.responses_paths import ResponsesPaths


@dataclass
class ProgramConfig:
	encoding: str
	env: Path
	responses: ResponsesPaths
