from dataclasses import dataclass

from src.config.user import UserConfig
from src.config.program import ProgramConfig
from src.config.secrets.main import SecretsConfig


@dataclass
class Config:
	user: UserConfig
	program: ProgramConfig
	secrets: SecretsConfig
