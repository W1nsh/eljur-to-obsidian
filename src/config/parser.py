from pathlib import Path
from typing import Any
import json

from src.config.config import Config


class ConfigParser:
	"""

	"""

	def __init__(
		self,
		encoding: str,
		config: Path,
	) -> None:
		self._encoding = encoding
		self._config = config


	def load_config(
		self,
	) -> Config:
		...


	def _load_json(
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
