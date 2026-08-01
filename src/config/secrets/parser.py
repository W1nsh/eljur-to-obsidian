from pathlib import Path
from os import getenv

from dotenv import load_dotenv

from src.config.secrets.main import SecretsConfig


class SecretsParser:
	def __init__(
		self,
		encoding: str,
		env: Path,
	) -> None:
		self._encoding = encoding
		self._env = env


	def secrets(
		self,
	) -> SecretsConfig:
		load_dotenv(
			dotenv_path=self._env,
			encoding=self._encoding,
		)
		login = getenv('ELJUR_LOGIN', '')
		password = getenv('ELJUR_PASSWORD', '')
		school_class = getenv('ELJUR_SCHOOL_CLASS', '')
		vendor = getenv('ELJUR_VENDOR', '')
		devkey = getenv('ELJUR_DEVKEY', '')
		auth_token = getenv('ELJUR_AUTH_TOKEN', '')
		return SecretsConfig(
			login=login,
			password=password,
			school_class=school_class,
			vendor=vendor,
			devkey=devkey,
			auth_token=auth_token,
		)
