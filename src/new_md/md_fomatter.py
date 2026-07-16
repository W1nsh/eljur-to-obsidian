from src.new_md.md_point import MdPoint
from src.new_md.md_point_types import MdPointTypes
from src.school.subject import Subject


class MdFormatter:
	"""
	
	"""
	SUBJECT_POINT = MdPointTypes.ITEM
	DATE_POINT = MdPointTypes.CHECKBOX
	HOMEWORK_POINT = MdPointTypes.CHECKBOX
	FILE_POINT = MdPointTypes.ITEM
	
	def __init__(
		self,
		tab_size: int,
	) -> None:
		"""
		
		"""
		self._tab_size = tab_size


	def add_starts_with(
		self,
		starts_with: str,
		md: str,
	) -> str:
		"""
		
		"""
		return starts_with + md


	def add_ends_with(
		self,
		ends_with: str,
		md: str,
	) -> str:
		"""
		
		"""
		return md + ends_with
	

	def del_starts_with(
		self,
		starts_with: str,
		md: str,
	) -> str:
		"""
		
		"""
		pass


	def del_ends_with(
		self,
		ends_with: str,
		md: str,
	) -> str:
		"""
		
		"""
		pass


	def generate_homeworks_ast(
		self,
		subject_list: list[Subject],
	) -> list[MdPoint]:
		"""
		
		"""
		subject_points: list[MdPoint] = []
		for subject in subject_list:
			subject_point = MdPoint(
				subject.name,
				type=self.SUBJECT_POINT,
			)
			date_points: list[MdPoint] = []
			for homework in subject.homeworks:
				file_points: list[MdPoint] = []
				for file in homework.files:
					file_point = MdPoint(
						f'[{file.filename}]({file.file_link})',
						type=self.FILE_POINT,
					)
					file_points.append(file_point)
				homework_point = MdPoint(
					homework.value,
					type=self.HOMEWORK_POINT,
				)
				for date_point in date_points:
					if date_point.text == homework.date:
						break
				else:
					date_point = MdPoint(
						homework.date,
						type=self.DATE_POINT,
					)
					date_points.append(date_point)
				homework_point.children.extend(file_points)
				date_point.children.append(homework_point)
			subject_point.children.extend(date_points)
			subject_points.append(subject_point)
		return subject_points


	def generate_marks_ast(
		self,
	) -> None:
		"""
		
		"""
		pass


	def merge_homeworks_asts(
		self,
	) -> None:
		"""
		
		"""
		pass


	def md_to_ast(
		self,
	) -> None:
		"""
		
		"""
		pass


	def ast_to_md(
		self,
		points: list[MdPoint],
		current_indent: int = 0,
		md: str = '',
	) -> str:
		"""
		
		"""
		for point in points:
			md += '\n'
			md += current_indent * self._tab_size * ' '
			md += self._get_point_symbol(
				point.type,
			)
			md += point.text
			if point.children:
				md += self.ast_to_md(
					point.children,
					current_indent + 1,
				)
		return md
	

	def _get_point_symbol(
		self,
		type: MdPointTypes,
	) -> str:
		match type:
			case MdPointTypes.ITEM:
				symbol = '- '
			case MdPointTypes.CHECKBOX:
				symbol = '- [ ] '
			case MdPointTypes.DONE_CHECKBOX:
				symbol = '- [x] '
		return symbol
