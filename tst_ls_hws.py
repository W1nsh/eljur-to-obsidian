from pathlib import Path

from config.user.config_manager import ConfigManager
from src.eljur.eljur_parser import EljurParser
from src.eljur.response_writer import ResponseWriter
from src.eljur.response_parser import ResponseParser
from src.utils.date import Date
from src.new_md.md_fomatter import MdFormatter


BASE_DIR = Path(__file__).parent
PATHS_PATH = BASE_DIR / 'config' / 'paths' / 'paths.json'
ENCODING = 'UTF-8'

FROM_DATE = Date.to_eljur('06.05.2026')
TO_DATE = Date.to_eljur('06.05.2026')

MARKS_FROM_DATE = Date.to_eljur('23.03.2026')
MARKS_TO_DATE = Date.to_eljur('06.05.2026')

RULES_PATH = BASE_DIR / 'tst_ls_hws_rules.json'
MARKS_PATH = BASE_DIR / 'tst_ls_hws_marks.json'
HOMEWORKS_PATH = BASE_DIR / 'tst_ls_hws_homeworks.json'

RESULT_PATH = BASE_DIR / 'tst_ls_hws_result_ast.txt'

md_formatter = MdFormatter(
	4,
)

cm = ConfigManager(
	BASE_DIR,
	PATHS_PATH,
	ENCODING,
)

eljur_config = cm.config.user_eljur

ep = EljurParser(
	ENCODING,
	eljur_config.devkey,
	eljur_config.vendor,
	eljur_config.school_class,
	eljur_config.login,
	eljur_config.password,
	eljur_config.auth_token,
)

rw = ResponseWriter(
	ENCODING,
)

rp = ResponseParser(
	ENCODING,
)


ep.authenticate()

rules = ep.get_rules()

rw.write_response(
	rules,
	RULES_PATH,
)

student = rp.get_user_ids(
	RULES_PATH,
)[0].id

homeworks = ep.get_homeworks(
	FROM_DATE,
	TO_DATE,
	student,
)

rw.write_response(
	homeworks,
	HOMEWORKS_PATH,
)

marks = ep.get_marks(
	MARKS_FROM_DATE,
	MARKS_TO_DATE,
	student,
)

rw.write_response(
	marks,
	MARKS_PATH,
)

subject_list = rp.load_suject_list(
	MARKS_PATH,
	student,
)

subject_list = rp.load_homeworks(
	HOMEWORKS_PATH,
	student,
	subject_list,
)

subject_list_ast = md_formatter.generate_homeworks_ast(subject_list)
md_ast = md_formatter.ast_to_md(subject_list_ast)

RESULT_PATH.write_text(
	str(md_ast),
	encoding=ENCODING,
)
