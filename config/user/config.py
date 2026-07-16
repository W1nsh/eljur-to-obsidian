from dataclasses import dataclass

from config.paths.paths import Paths
from config.user.user_data_config import UserDataConfig
from config.user.user_eljur_config import UserEljurConfig


@dataclass
class Config:
	"""
	Dataclass for storing main configuration parameters.

	Attributes:
		paths (Paths):
			Paths to all files and directories used in the project.
		user_data (UserDataConfig):
			User data configuration.
		user_eljur (UserEljurConfig):
			User Eljur configuration.
			Data for logging in Eljur.
	"""
	paths: Paths
	user_data: UserDataConfig
	user_eljur: UserEljurConfig
