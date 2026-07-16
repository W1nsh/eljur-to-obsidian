from pathlib import Path

# from src.app import App


BASE_DIR = Path(__file__).parent
PATHS_PATH = BASE_DIR / 'config' / 'paths' / 'paths.json'
ENCODING = 'utf-8'
TAB_SIZE = 4 # ???

app = ... # BASE_DIR, PATHS_PATH, ENCODING, TAB_SIZE

if __name__ == '__main__':
	# app.run()
	pass
