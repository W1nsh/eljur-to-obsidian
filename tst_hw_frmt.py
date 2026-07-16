from pathlib import Path

from config.user.config_manager import ConfigManager
from src.eljur.eljur_parser import EljurParser
from src.eljur.response_writer import ResponseWriter
from src.eljur.response_parser import ResponseParser
from src.utils.date import Date


BASE_DIR = Path(__file__).parent
PATHS_PATH = BASE_DIR / 'config' / 'paths' / 'paths.json'
ENCODING = 'UTF-8'

FROM_DATE = Date.to_eljur('06.05.2026')
TO_DATE = Date.to_eljur('06.05.2026')

ASSESMENTS_PATH = BASE_DIR / 'responses' / 'assessments_2.json'
DIARY_PATH = BASE_DIR / 'responses' / 'diary_2.json'
HOMEWORKS_PATH = BASE_DIR / 'responses' / 'homeworks_2.json'
MARKS_PATH = BASE_DIR / 'responses' / 'marks_2.json'
PERIODS_PATH = BASE_DIR / 'responses' / 'periods_2.json'
RULES_PATH = BASE_DIR / 'responses' / 'rules_2.json'
SCHEDULE_PATH = BASE_DIR / 'responses' / 'schedule_2.json'

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

ep.authenticate()

rw = ResponseWriter(
	ENCODING,
)

rp = ResponseParser(
	ENCODING,
)


rules = ep.get_rules()

rw.write_response(
	rules,
	RULES_PATH,
)


STUDENT = rp.get_user_ids(
	RULES_PATH,
)[0]


assesments = ep.get_assessments(
	FROM_DATE,
	TO_DATE,
)

rw.write_response(
	assesments,
	ASSESMENTS_PATH,
)


diary = ep.get_diary(
	FROM_DATE,
	TO_DATE,
)

rw.write_response(
	diary,
	DIARY_PATH,
)


homeworks = ep.get_homeworks(
	FROM_DATE,
	TO_DATE,
)
rw.write_response(
	homeworks,
	HOMEWORKS_PATH,
)


marks = ep.get_marks(
	FROM_DATE,
	TO_DATE,
)

rw.write_response(
	marks,
	MARKS_PATH,
)


periods = ep.get_periods(
	STUDENT.id,
	show_disabled=True,
)

rw.write_response(
	periods,
	PERIODS_PATH,
)


schedule = ep.get_schedule(
	FROM_DATE,
	TO_DATE,
)

rw.write_response(
	schedule,
	SCHEDULE_PATH,
)
