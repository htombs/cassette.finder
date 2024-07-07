import sqlite3
from .database import connect_database

connect = connect_database()

connect.execute("PRAGMA foreign_keys = 1")

cursor = connect.cursor()

def createNineSpeedTable():
    cursor.execute('''CREATE TABLE IF NOT EXISTS cassettes_9spd 
               (id INT PRIMARY KEY, 
               brand VARCHAR(255), 
               model VARCHAR(255), 
               partNumber VARCHAR(255), 
               speed INT, 
               ratio VARCHAR(10), 
               distributor VARCHAR(255), 
               rrp DECIMAL(10,2),
               distributor_id INT,
               FOREIGN KEY (distributor_id) REFERENCES distributor_table (distributor_id))''')
    connect.commit()

def insertNineSpeedData():
    data = [
        (1, "Shimano", "HG400", "25148", 9, "11-36", "Bob-Elliot", 31.99, 1),
        (2, "Shimano", "HG200", "25143", 9, "11-36", "Bob-Elliot", 27.99, 1),
        (3, "Shimano", "HG201", "25152", 9, "11-36", "Bob-Elliot", 29.99, 1),
        (4, "Shimano", "HG200", "25138", 9, "11-32", "Bob-Elliot", 27.99, 1),
        (5, "Shimano", "HG200", "25139", 9, "11-34", "Bob-Elliot", 27.99, 1),
        (6, "Shimano", "HG200", "25143", 9, "11-36", "Bob-Elliot", 27.99, 1),
        (7, "Shimano", "HG400", "25134", 9, "11-25", "Bob-Elliot", 31.99, 1),
        (8, "Shimano", "HG400", "25145", 9, "11-28", "Bob-Elliot", 31.99, 1),
        (9, "Shimano", "HG400", "25130", 9, "11-32", "Bob-Elliot", 31.99, 1),
        (10, "Shimano", "HG400", "25148", 9, "11-36", "Bob-Elliot", 31.99, 1),
        (11, "Shimano", "HG400", "25146", 9, "12-36", "Bob-Elliot", 32.99, 1),
        (12, "Shimano", "HG400", "25133", 9, "11-34", "Bob-Elliot", 31.99, 1),
        (13, "Shimano", "HG50", "251352", 9, "11-30", "Bob-Elliot", 33.99, 1),
        (14, "Sunrace", "M90", "50361", 9, "11-36", "Bob-Elliot", 24.99, 1),
        (15, "Sunrace", "M96", "50233", 9, "11-32", "Bob-Elliot", 25.99, 1),
        (16, "Sunrace", "M96", "50234", 9, "11-34", "Bob-Elliot", 25.99, 1),
        (17, "Sunrace", "M98", "50235", 9, "11-36", "Bob-Elliot", 28.99, 1),
        (18, "Sunrace", "M980", "50339", 9, "11-40", "Bob-Elliot", 36.99, 1),
        (19, "Sunrace", "M980", "50373", 9, "11-40", "Bob-Elliot", 36.99, 1),
        (20, "Sunrace", "R91", "50267", 9, "11-25", "Bob-Elliot", 31.99, 1),
        (21, "Sunrace", "R91", "50268", 9, "11-28", "Bob-Elliot", 31.99, 1),
        (22, "Sunrace", "R91", "50269", 9, "12-25", "Bob-Elliot", 31.99, 1),
        (23, "KMC", "React X9", "KX30", 9, "11-32", "Chicken Cyclekit", 31.50, 2),
        (24, "KMC", "React X9", "KX31", 9, "11-36", "Chicken Cyclekit", 34.00, 2),
        (25, "Miche", "Primato 9X", "MCX33", 9, "12-25", "Chicken Cyclekit", 38.99, 2),
        (26, "Miche", "Primato 9X", "MCX34", 9, "12-29", "Chicken Cyclekit", 38.99, 2),
        (27, "Miche", "Primato 9X", "MCX31", 9, "13-26", "Chicken Cyclekit", 38.99, 2),
        (28, "Miche", "Primato 9X", "MCX32", 9, "13-28", "Chicken Cyclekit", 38.99, 2),
        (29, "Miche", "Primato 9X", "MCX30", 9, "12-23", "Chicken Cyclekit", 38.99, 2),
        (30, "Miche", "Primato 9X", "MCX36", 9, "13-26", "Chicken Cyclekit", 38.99, 2),
        (31, "Miche", "Primato 9X", "MCX37", 9, "13-28", "Chicken Cyclekit", 38.99, 2),
        (32, "Miche", "Primato 9X", "MCX38", 9, "13-26", "Chicken Cyclekit", 38.99, 2),
        (33, "Miche", "Primato 9X", "MCX50", 9, "12-26", "Chicken Cyclekit", 38.99, 2),
        (34, "Campagnolo", "Veloce 9X", "CP530", 9, "12-23", "Chicken Cyclekit", 41.99, 2),
        (35, "Campagnolo", "Veloce 9X", "CP531", 9, "13-23", "Chicken Cyclekit", 37.99, 2),
        (36, "Campagnolo", "Veloce 9X", "CP532", 9, "13-26", "Chicken Cyclekit", 41.99, 2),
        (37, "Tifosi", "9X HG", "TIF709A", 9, "11-34", "Chicken Cyclekit", 22.99, 2),
        (38, "Clarks", "N/A", "C-9SC-UKS", 9, "11-32", "Greyville", 21.95, 3),
        (39, "Sunrace", "M96", "CSM969AU", 9, "11-32", "Greyville", 24.95, 3),
        (40, "Sunrace", "M96", "CSM969AV", 9, "11-34", "Greyville", 26.95, 3),
        (41, "Sunrace", "MX7", "CSMX79AV", 9, "11-34", "Greyville", 54.95, 3),
        (42, "Sunrace", "R91", "CSR919AS", 9, "11-28", "Greyville", 25.99, 3),
        (43, "GTB", "N/A", "ESP1037N", 9, "11-28", "Greyville", 32.95, 3),
        (44, "Geardrive", "N/A", "GD0923", 9, "11-23", "Greyville", 21.95, 3),
        (45, "Geardrive", "N/A", "GD0925", 9, "11-25", "Greyville", 21.95, 3),
        (46, "Geardrive", "N/A", "GD0928", 9, "11-28", "Greyville", 21.95, 3),
        (47, "Geardrive", "N/A", "GD0932", 9, "11-32", "Greyville", 21.54, 3),
        (48, "Geardrive", "N/A", "GD0932OE", 9, "11-32", "Greyville", 19.96, 3),
        (49, "Geardrive", "N/A", "GD0936", 9, "11-36", "Greyville", 22.96, 3),
        (50, "Geardrive", "N/A", "GD0940", 9, "11-40", "Greyville", 28.96, 3),
        (51, "Geardrive", "N/A", "GD0942", 9, "11-42", "Greyville", 29.95, 3),
        (52, "Box", "Two Prime 9", "CSBX2P9150", 9, "11-50", "Ison Distribution", 114.99, 4),
        (53, "Box", "Two Prime 9", "CSBX2P9250", 9, "12-50", "Ison Distribution", 114.99, 4),
        (54, "Box", "Three Prime 9", "CSBX3P9146", 9, "11-46", "Ison Distribution", 79.99, 4),
        (55, "Box", "Three Prime 9", "CSBX3P9150", 9, "11-50", "Ison Distribution", 89.99, 4),
        (56, "Box", "Three Prime 9", "CSBX3P9246", 9, "12-46", "Ison Distribution", 79.99, 4),
        (57, "Box", "Three Prime 9", "CSBX3P9250", 9, "12-50", "Ison Distribution", 89.99, 4),
        (58, "Sunrace", "R90", "CSSR9925", 9, "11-25", "Ison Distribution", 34.99, 4),
        (59, "Sunrace", "R91", "CSSR9928", 9, "11-28", "Ison Distribution", 34.99, 4),
        (60, "Sunrace", "M96", "CSSR9932", 9, "11-32", "Ison Distribution", 29.99, 4),
        (61, "Sunrace", "M96", "CSSR9934", 9, "11-34", "Ison Distribution", 29.99, 4),
        (62, "Sunrace", "M98", "CSSR9936", 9, "11-36", "Ison Distribution", 31.99, 4),
        (63, "Sunrace", "M980", "CSSR9940", 9, "11-40", "Ison Distribution", 39.99, 4),
        (64, "SRAM", "PG970", "FW971132", 9, "11-32", "Mackadams", 45.00, 5),
        (65, "SRAM", "PG970", "FW971134", 9, "11-34", "Mackadams", 45.00, 5),
        (66, "S-Ride", "M300", "590845", 9, "11-32", "Mackadams", 40.00, 5),
        (67, "Sunrace", "R91", "CSR919AQ", 9, "11-25", "Mackadams", 34.99, 5),
        (68, "Sunrace", "R91", "CSR919AS", 9, "11-28", "Mackadams", 34.99, 5),
        (69, "Sunrace", "R91", "CSR919BQ", 9, "12-25", "Mackadams", 31.99, 5),
        (70, "SRAM", "PG950", "FW951126", 9, "11-26", "Mackadams", 36.00, 5),
        (71, "SRAM", "PG950", "FW951128", 9, "11-28", "Mackadams", 36.00, 5),
        (72, "SRAM", "PG950", "FW951132", 9, "11-32", "Mackadams", 36.00, 5),
        (73, "SRAM", "PG950", "FW951134", 9, "11-34", "Mackadams", 36.00, 5),
        (74, "SRAM", "PG950", "FW951223", 9, "12-23", "Mackadams", 36.00, 5),
        (75, "SRAM", "PG950", "FW951226", 9, "12-26", "Mackadams", 36.00, 5),
        (76, "Sunrace", "M96", "CSM969AU", 9, "11-32", "Mackadams", 25.99, 5),
        (77, "Sunrace", "M96", "CSM969AV", 9, "11-34", "Mackadams", 26.99, 5),
        (78, "Sunrace", "M98", "CSM989AW", 9, "11-36", "Mackadams", 31.99, 5),
        (79, "Sunrace", "M980", "CSM9809AX", 9, "11-40", "Mackadams", 36.99, 5),
        (80, "Unbranded", "N/A", "CSESP1034", 9, "11-32", "Mackadams", 25.99, 5),
        (81, "Shimano", "LG300", "CSLG3009136", 9, "11-36", "Madison", 24.99, 6),
        (82, "Shimano", "LG300", "CSLG3009141", 9, "11-41", "Madison", 29.99, 6),
        (83, "Shimano", "LG300", "CSLG3009146", 9,"11-46", "Madison", 34.99, 6),
        (84, "Shimano", "HG201", "CSHG2019132", 9,"11-32", "Madison", 27.99, 6),
        (85, "Shimano", "HG201", "CSHG2019134", 9,"11-36", "Madison", 27.99, 6),
        (86, "Shimano", "LG400", "CSLG4009136", 9,"11-36", "Madison", 29.99, 6),
        (87, "Shimano", "LG400", "CSLG4009141", 9,"11-41", "Madison", 34.99, 6),
        (88, "Shimano", "LG400", "CSLG4009146", 9,"11-46", "Madison", 39.99, 6),
        (89, "Shimano", "HG400", "CSHG4009125", 9,"11-25", "Madison", 31.99, 6),
        (90, "Shimano", "HG400", "CSHG4009128", 9,"11-28", "Madison", 31.99, 6),
        (91, "Shimano", "HG400", "CSHG4009132", 9,"11-32", "Madison", 31.99, 6),
        (92, "Shimano", "HG400", "CSHG4009134", 9,"11-34", "Madison", 31.99, 6),
        (93, "Shimano", "HG400", "CSHG4009136", 9,"11-36", "Madison", 31.99, 6),
        (94, "Shimano", "HG400", "CSHG4009236", 9,"12-36", "Madison", 31.99, 6),
        (95, "Shimano", "HG50", "CSHG509225", 9,"12-25", "Madison", 34.99, 6),
        (96, "Tektro", "ED-9", "TK-ABCS000002", 9,"11-46", "Upgrade", 80.00, 7),
        (97, "SRAM", "PG950", "FW951128", 9, "11-28", "ZyroFisher", 36.00, 8),
        (98, "SRAM", "PG950", "FW951132", 9, "11-32", "ZyroFisher", 36.00, 8),
        (99, "SRAM", "PG950", "FW951134", 9, "11-34", "ZyroFisher", 36.00, 8),
        (100, "SRAM", "PG950", "FW951223", 9, "12-23", "ZyroFisher", 36.00, 8),
        (101, "SRAM", "PG950", "FW951226", 9, "12-26", "ZyroFisher", 36.00, 8),
        (102, "SRAM", "PG970", "FW971134", 9, "11-34", "ZyroFisher", 45.00, 8),
        (103, "SRAM", "PG970", "FW971226", 9, "12-26", "ZyroFisher", 68.00, 8),
        (104, "Clarks", "N/A", "C-9SC", 9, "11-32", "ZyroFisher", 28.99, 8),
        (105, "Microshift", "H092 H-series", "CSMSH9128", 9, "11-28", "Ison Distribution", 27.99, 4),
        (106, "Microshift", "H092 H-series", "CSMSH9134", 9, "11-34", "Ison Distribution", 27.99, 4),
        (107, "Microshift", "H092 H-series", "CSMSH9136", 9, "11-36", "Ison Distribution", 27.99, 4),
        (108, "Microshift", "Advent", "CSMSH9142A", 9, "11-42", "Ison Distribution", 47.99, 4),
        (109, "Microshift", "Advent", "CSMSH9138", 9, "11-38", "Ison Distribution", 39.99, 4),
        (110, "Microshift", "Advent", "CSMSH9142", 9, "11-42", "Ison Distribution", 39.99, 4),
        (111, "Microshift", "Advent", "CSMSH9146", 9, "11-46", "Ison Distribution", 47.99, 4)
    ]

    cursor.executemany("REPLACE INTO cassettes_9spd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data) 

    connect.commit()

def get_distributor_9spd(distributor: str):
    print(distributor)
    cursor = connect.cursor()
    result = cursor.execute("SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_9spd WHERE distributor=?", [distributor])

    rows = result.fetchall()
    connect.close()
    #print(rows)

    for row in rows:
        print(row)

connect.commit()

def get_brand_9spd(brand: str):
    print(brand)
    cursor = connect.cursor()
    result = cursor.execute("SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_9spd WHERE brand=?", [brand])

    rows = result.fetchall()
    connect.close()
    #print(rows)

    for row in rows:
        print(row)

connect.commit()

def get_speed_9spd(speed: int):
    print(speed)
    cursor = connect.cursor()
    result = cursor.execute("SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_9spd WHERE speed=?", [speed])

    rows = result.fetchall()
    connect.close()
    # print(rows)

    for row in rows:
        print(row)

connect.commit()

def get_ratio_9spd(ratio: str):
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute("SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_9spd WHERE ratio=?", [ratio])

    rows = result.fetchall()
    connect.close()
    # print(rows)

    for row in rows:
        print(row)

connect.commit()