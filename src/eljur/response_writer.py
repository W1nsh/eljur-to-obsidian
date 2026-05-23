import json
from pathlib import Path
from typing import Any


class ResponseWriter:
	"""
	Class for writing responses of the Eljur API (from EljurParser).
	Write data as json file.

	Attributes:
		_encoding (str): Encoding for writing responses files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		Initilazes ResponsesWriter object.

		Args:
			encoding (str): Encoding for writing responses files.
		"""
		self._encoding = encoding


	def write_response(
		self,
		response: dict[str, Any],
		file: Path,
	) -> None:
		"""
		Writes eljur api reponse as json file.

		Args:
			response (dict[str, Any]): Reponse data for writing.
			file (Path): Path to the reponse file.
		"""
		json_response = json.dumps(
			response,
			ensure_ascii=False,
			indent=4
		)
		file.write_text(
			json_response,
			encoding=self._encoding,
		)
