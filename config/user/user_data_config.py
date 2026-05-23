from dataclasses import dataclass

from config.user.marks_config import MarksConfig
from config.user.homeworks_config import HomeworksConfig


@dataclass
class UserDataConfig:
	"""
	Dataclass for storing all user configuration parameters.

	Attributes:
		marks (MarksConfig):
			Dataclass for storing all user parameters about marks.
		homeworks (HomeworksConfig):
			Dataclass for storing all user parameters about homeworks.
	"""
	marks: MarksConfig
	homeworks: HomeworksConfig
	