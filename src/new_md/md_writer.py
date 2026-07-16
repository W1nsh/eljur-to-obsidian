from pathlib import Path


class MdWriter:
	"""
	
	"""
	
	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		
		"""
		self._encoding = encoding


	def write_md(
		self,
		file: Path,
		md: str,
	) -> None:
		"""
		
		"""
		file.write_text(
			md,
			self._encoding,
		)