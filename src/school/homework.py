from dataclasses import dataclass, field

from src.school.homework_file import HomeworkFile


@dataclass
class Homework:
	date: str
	homework: str
	files: list[HomeworkFile] = field(default_factory=list)
