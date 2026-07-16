from pathlib import Path


class MdParser:
	"""
	
	"""
	
	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		
		"""
		self._encoding = encoding


	def read_md(
		self,
		md: Path,
	) -> str:
		"""
		
		"""
		return md.read_text()
	

	def split_to_lines(
		self,
		text: str,
	) -> list[str]:
		"""
		
		"""
		return text.splitlines()
