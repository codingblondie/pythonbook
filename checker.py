from flask import session
from functools import wraps

#декоратор функции func
#*args и **kwargs означает что ф-ия принимает любое кол-во любых аргументов
def check_logged_in(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'logged_in' in session:
			return func(*args, **kwargs)
		return "You are NOT logged in"
	return wrapper