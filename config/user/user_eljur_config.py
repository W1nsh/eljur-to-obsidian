from dataclasses import dataclass


@dataclass
class UserEljurConfig:
	"""
	Dataclass for storing all user parameters for eljur data parse.

	Attributes:
		login (str): User's eljur login.
		password (str): User's eljur password.
		school_class (str): User's eljur school class.
		vendor (str): User's eljur vendor.
			Part of the eljur school domen, where wrote only school name.
		devkey (str): User's eljur devkey.
		auth_token (str): User's authentication token.
	"""
	login: str
	password: str
	school_class: str
	vendor: str
	devkey: str
	auth_token: str
