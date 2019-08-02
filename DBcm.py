import psycopg2

class UseDatabase:
	def __init__(self,config: dict) -> None:
		self.configuration = config
	def __enter__(self) -> 'cursor':
		self.con = psycopg2.connect(**self.configuration)
		self.cursor = self.con.cursor()
		return self.cursor
	def __exit__(self, exc_type, exc_value, exc_trace) -> None:
		self.con.commit()
		self.cursor.close()
		self.con.close()
