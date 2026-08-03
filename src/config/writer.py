from pathlib import Path
from typing import Any
import json

from src.config.secrets.main import SecretsConfig
from src.config.main import Config
from src.config.secrets.writer import SecretsWriter


class ConfigWriter:
	"""

	"""

	def __init__(
		self,
		encoding: str,
		base_path: Path,
	) -> None:
		self._encoding = encoding
		self._base_path = base_path
		self._secrets_writer = SecretsWriter(
			encoding=encoding,
		)


	def all(
		self,
		config: Config,
		config_file: Path,
	) -> None:
		self.config(
			config=config,
			config_file=config_file,
		)
		self._secrets_writer.secrets(
			secrets=config.secrets,
			env_file=config.program.env,
		)


	def config(
		self,
		config: Config,
		config_file: Path,
	) -> None:
		config_json = json.dumps(
			self._generate_config(config),
			ensure_ascii=False,
			indent=4,
		)
		config_file.write_text(
			config_json,
			encoding=self._encoding,
		)


	def _generate_config(
		self,
		config: Config,
	) -> dict[str, Any]:
		return {
			'user': {
				'marks': {
					'need': config.user.marks.need,
					'path': config.user.marks.path.as_posix(),
					'date': {
						'start': config.user.marks.dates.start,
						'end': config.user.marks.dates.end,
					},
					'template': {
						'starts_with': config.user.marks.templates.starts_with.relative_to(self._base_path).as_posix(),
						'ends_with': config.user.marks.templates.ends_with.relative_to(self._base_path).as_posix(),
					},
					'desired': config.user.marks.desired,
				},
				'homeworks': {
					'need': config.user.homeworks.need,
					'path': config.user.homeworks.path.as_posix(),
					'date': {
						'start': config.user.homeworks.dates.start,
						'end': config.user.homeworks.dates.end,
					},
					'template': {
						'starts_with': config.user.homeworks.templates.starts_with.relative_to(self._base_path).as_posix(),
						'ends_with': config.user.homeworks.templates.ends_with.relative_to(self._base_path).as_posix(),
					},
				},
			},
			'program': {
				'env': config.program.env.relative_to(self._base_path).as_posix(),
				'responses': {
					'assessments': config.program.responses.assessments.relative_to(self._base_path).as_posix(),
					'diary': config.program.responses.diary.relative_to(self._base_path).as_posix(),
					'homeworks': config.program.responses.homeworks.relative_to(self._base_path).as_posix(),
					'marks': config.program.responses.marks.relative_to(self._base_path).as_posix(),
					'periods': config.program.responses.periods.relative_to(self._base_path).as_posix(),
					'rules': config.program.responses.rules.relative_to(self._base_path).as_posix(),
					'schedule': config.program.responses.schedule.relative_to(self._base_path).as_posix(),
				},
			},
		}
