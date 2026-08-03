from pathlib import Path

from src.config.secrets.main import SecretsConfig


class SecretsWriter:
	"""

	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		self._encoding = encoding


	def secrets(
		self,
		secrets: SecretsConfig,
		env_file: Path,
	) -> None:
		secrets_content = self._generate_secrets(
			secrets=secrets,
		)
		env_file.write_text(
			data=secrets_content,
			encoding=self._encoding,
		)


	def _generate_secrets(
		self,
		secrets: SecretsConfig,
	) -> str:
		content = f'ELJUR_LOGIN = {secrets.login}\n'
		content += f'ELJUR_PASSWORD = {secrets.password}\n'
		content += f'ELJUR_SCHOOL_CLASS = {secrets.school_class}\n'
		content += f'ELJUR_VENDOR = {secrets.vendor}\n'
		content += f'ELJUR_DEVKEY = {secrets.devkey}\n'
		content += f'ELJUR_AUTH_TOKEN = {secrets.auth_token}\n'
		return content
