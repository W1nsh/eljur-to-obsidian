from dataclasses import dataclass


@dataclass
class SecretsConfig:
	login: str
	password: str
	school_class: str
	vendor: str
	devkey: str
	auth_token: str
