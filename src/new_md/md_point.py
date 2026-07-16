from dataclasses import dataclass, field

from src.new_md.md_point_types import MdPointTypes


@dataclass
class MdPoint:
	"""
	
	"""
	text: str
	type: MdPointTypes
	children: list['MdPoint'] = field(default_factory=list)
