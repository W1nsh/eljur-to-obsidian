from dataclasses import dataclass
from pathlib import Path


@dataclass
class ResponsesPaths:
	assessments: Path
	diary: Path
	homeworks: Path
	marks: Path
	periods: Path
	rules: Path
	schedule: Path
