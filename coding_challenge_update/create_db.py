import sqlite3

conn = sqlite3.connect("Ecommerce.db")

cur = conn.cursor()

Orders = """
	CREATE TABLE Orders_Table(
			id TEXT,
			status TEXT,
			lastUpdated TEXT,
			totalAmount REAL,
			totalCurrency TEXT,
			paymentMethod TEXT,
			purchaseDate TEXT,
			sellerId TEXT

	)"""

Financial_groups = """
	CREATE TABLE Fingroups_Table(
			id TEXT,
			groupStart TEXT,
			groupEnd TEXT,
			status TEXT,
			sellerId TEXT

	)"""

Financials = """
	CREATE TABLE Financials_Table(
			groupId TEXT,
			postedDate TEXT,
			orderId TEXT,
			type TEXT,
			subType TEXT,
			currencyAmount REAL,
			currencyCode TEXT

	)"""

cur.execute(Orders)
cur.execute(Financial_groups)
cur.execute(Financials)
print("Orders,financial groups and financials tables has been created")

conn.commit()
conn.close()