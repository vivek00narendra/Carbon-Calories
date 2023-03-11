# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123mainstreet",
    database="productInfo"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM products")
products = mycursor.fetchall()

columnWeights = [0.3, 0.2, 0.1, 0.2, 0.2]

def calculateRating(productID):
    score = 0
    i = 0

    while i < len(products):
        val = products[i][1]
        if val == productID:
            break
        else:
            i += 1

    score1=0
    score2=0
    score3=100
    score4=100
    score5=0

    # Local Calculation
    if products[i][2] == 1:
        score1 = 100
    else:
        score1 = 0
    
    # Plant Based Calculation
    if products[i][3] == 1:
        score2 = 100
    else:
        score2 = 0
    
    # Packaging Calculation
    packaging = products[i][4].split()
    j = 0
    while j < len(packaging):
        if packaging[j] == 'Plastic':
            score3 = score3 - 30
            j = j+1
        elif packaging[j] == 'Paper':
            score3 = score3 - 10
            j = j+1
        elif packaging[j] == 'Styrofoam':
            score3 = score3 - 15
            j = j+1
        elif packaging[j] == 'Glass':
            score3 = score3 - 20
            j = j+1
        elif packaging[j] == 'Metal':
            score3 = score3 - 25
            j = j+1
        else:
            j = j+1
    
    # Meat Calculation
    if products[i][5] == 'red':
        score4 = score4 - 70
    elif products[i][5] == 'white':
        score4 = score4 - 30
    
    # Seasonal Calculation
    if products[i][6] == 1:
        score5 = 0
    elif products[i][6] == 0:
        score5 = 100

    print(score1)
    print(score2)
    print(score3)
    print(score4)
    print(score5)

    score = ((score1 * columnWeights[0]) + (score2 * columnWeights[1]) + (score3 * columnWeights[2]) + (score4 * columnWeights[3]) + (score5 * columnWeights[4])) / 10
    return score

print(calculateRating(8103403))

mydb.close()