# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123mainstreet",
    database="productInfo"
)

mycursor = mydb.cursor()

# sqlFormula = "INSERT INTO products (productName, productID, local, plantBased, packaging, meatRating, seasonal) VALUES(%s, %s, %s, %s, %s, %s, %s)"

# product1 = ("Boneless Skinless Chicken Breasts", 9314778, 1, 0, "Plastic Styrofoam", "White", 0)
# product2 = ("Dempster’s® 100% Whole Wheat Bread", 8103403, 1, 1, "Plastic", "-", 0)
# product3 = ("Apple, Gala", 30449004, 1, 1, "-", "-", 1)
# product4 = ("Banana", 30895821, 0, 1, "-", "-", 0)
# product5 = ("Tostitios Spinach Dip", 9263624, 0, 1, "Glass", "-", 0)
# product6 = ("Your Fresh Market Lean Ground Beef", 30231908, 1, 0, "Plastic Styrofoam", "Red", 0)
# product7 = ("Pork Loin Center & Rib End Chops Boneless Fast Fry", 31108465, 1, 0, "Plastic Styrofoam", "Red", 0)
# product8 = ("Avocado", 9444412, 0, 1, "-", "-", 1)

# products = [("Boneless Skinless Chicken Breasts", 9314778, 1, 0, "Plastic Styrofoam", "White", 0),
#             ("Dempster’s® 100% Whole Wheat Bread", 8103403, 1, 1, "Plastic", "-", 0),
#             ("Apple, Gala", 30449004, 1, 1, "-", "-", 1),
#             ("Banana", 30895821, 0, 1, "-", "-", 0),
#             ("Tostitios Spinach Dip", 9263624, 0, 1, "Glass", "-", 0),
#             ("Your Fresh Market Lean Ground Beef", 30231908, 1, 0, "Plastic Styrofoam", "Red", 0),
#             ("Pork Loin Center & Rib End Chops Boneless Fast Fry", 31108465, 1, 0, "Plastic Styrofoam", "Red", 0),
#             ("Avocado", 9444412, 0, 1, "-", "-", 1)]

# mycursor.executemany(sqlFormula, products)
# mydb.commit()

mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)
    for i in row:
        print(i)

mydb.close()