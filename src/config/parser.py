from pathlib import Path
from typing import Any
import json

from src.config.responses_paths import ResponsesPaths
from src.config.templates import TemplatesConfig
from src.config.dates import DatesConfig
from src.config.homeworks import HomeworksConfig
from src.config.marks import MarksConfig
from src.config.program import ProgramConfig
from src.config.user import UserConfig
from src.config.main import Config


class ConfigParser:
	"""

	"""

	def __init__(
		self,
		encoding: str,
		base_path: Path,
		config: Path,
	) -> None:
		self._encoding = encoding
		self._config = config
		self._base_path = base_path


	def config(
		self,
	) -> Config:
		json = self._json(
			self._config,
		)
		user = self._user(
			json['user'],
		)
		program = self._program(
			json['program'],
		)
		return Config(
			user=user,
			program=program,
		)


	def _json(
		self,
		file: Path,
	) -> dict[str, Any]:
		"""
		Loads json file and returns it as a dictionary.

		Args:
			path (Path): Absolute path to the json file.

		Returns:
			dict[str, Any]: Content of the json file as a dictionary.
		"""
		json_string = file.read_text(encoding=self._encoding)
		json_dict = json.loads(json_string)
		return json_dict


	def _user(
		self,
		user: dict[str, Any],
	) -> UserConfig:
		marks = self._marks(
			user['marks'],
		)
		homeworks = self._homeworks(
			user['homeworks'],
		)
		return UserConfig(
			marks=marks,
			homeworks=homeworks,
		)


	def _homeworks(
		self,
		homeworks: dict[str, Any],
	) -> HomeworksConfig:
		need = homeworks['need']
		path = Path(homeworks['path'])
		dates = self._dates(
			homeworks['date'],
		)
		templates = self._templates(
			homeworks['template'],
		)
		return HomeworksConfig(
			need=need,
			path=path,
			dates=dates,
			templates=templates,
		)


	def _marks(
		self,
		marks: dict[str, Any],
	) -> MarksConfig:
		homeworks = self._homeworks(
			marks,
		)
		desired = marks['desired']
		return MarksConfig(
			need=homeworks.need,
			path=homeworks.path,
			dates=homeworks.dates,
			templates=homeworks.templates,
			desired=desired,
		)


	def _dates(
		self,
		dates: dict[str, Any],
	) -> DatesConfig:
		start = dates['start']
		end = dates['end']
		return DatesConfig(
			start=start,
			end=end,
		)


	def _templates(
		self,
		templates: dict[str, Any],
	) -> TemplatesConfig:
		starts_with = self._base_path / templates['starts_with']
		ends_with = self._base_path / templates['ends_with']
		return TemplatesConfig(
			starts_with=starts_with,
			ends_with=ends_with,
		)


	def _program(
		self,
		program: dict[str, Any],
	) -> ProgramConfig:
		encoding = program['encoding']
		env = self._base_path / program['env']
		responses = self._responses(
			program['responses'],
		)
		return ProgramConfig(
			encoding=encoding,
			env=env,
			responses=responses,
		)


	def _responses(
		self,
		responses: dict[str, Any],
	) -> ResponsesPaths:
		assessments = self._base_path / responses['assessments']
		diary = self._base_path / responses['diary']
		homeworks = self._base_path / responses['homeworks']
		marks = self._base_path / responses['marks']
		periods = self._base_path / responses['periods']
		rules = self._base_path / responses['rules']
		schedule = self._base_path / responses['schedule']
		return ResponsesPaths(
			assessments=assessments,
			diary=diary,
			homeworks=homeworks,
			marks=marks,
			periods=periods,
			rules=rules,
			schedule=schedule,
		)
