from dataclasses import dataclass

from src.config.user import UserConfig
from src.config.program import ProgramConfig


@dataclass
class Config:
	user: UserConfig
	program: ProgramConfig
