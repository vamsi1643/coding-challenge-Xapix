import sqlite3, csv

conn = sqlite3.connect("Ecommerce.db")

cur = conn.cursor()

with open("orders.csv") as file:
	for row in file:
		cur.execute("INSERT INTO Orders_Table VALUES (?,?,?,?,?,?,?,?)", row.split(','))
		conn.commit()


with open("financial_groups.csv") as file:
	for row in file:
		cur.execute("INSERT INTO Fingroups_Table VALUES (?,?,?,?,?)", row.split(','))
		conn.commit()


with open("financials.csv") as file:
	for row in file:
		cur.execute("INSERT INTO Financials_Table VALUES (?,?,?,?,?,?,?)", row.split(','))
		conn.commit()


conn.close()