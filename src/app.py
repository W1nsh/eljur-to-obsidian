from pathlib import Path

from src.config import ConfigParser


class App:
	"""
	Main class of the EtO.
	"""

	def __init__(
		self,
		encoding: str,
		eto: Path,
		config: Path,
	) -> None:
		self._encoding = encoding
		self._eto = eto
		self._config_parser = ConfigParser(
			encoding=encoding,
			eto=eto,
		)
		self._config = self._config_parser.load_config(
			config
		)


	def parse(
		self,
	) -> None:
		pass
