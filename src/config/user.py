from dataclasses import dataclass

from src.config.marks import MarksConfig
from src.config.homeworks import HomeworksConfig


@dataclass
class UserConfig:
	marks: MarksConfig
	homeworks: HomeworksConfig
