


import sqlite3


__all__ = ['init']


class init:
	def __init__(self):
		self.conn = sqlite3.connect('db/drugstore.db')
		self.cursor = self.conn.cursor()

	def query(self, q, v):
		res = self.cursor.execute(q, v)
		self.conn.commit()
		return res

	def close(self):
		self.conn.close()