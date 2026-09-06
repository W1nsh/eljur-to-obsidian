from dataclasses import dataclass

from src.config.homeworks import HomeworksConfig


@dataclass
class MarksConfig(HomeworksConfig):
	desired: dict[str, int]
