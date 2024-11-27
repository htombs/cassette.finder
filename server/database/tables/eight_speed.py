import sqlite3
from .database import connect_database, response

def createEightSpeedTable():
    connect = connect_database()
    # opens a connection to the database as opened in database.py
    cursor = connect.cursor()
    # creates a cursor so we can interact with the database and write SELECT statements and other SQL statement 
    cursor.execute('''CREATE TABLE IF NOT EXISTS cassettes
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
    # cursor.excecute tells the database to perform the task in brackets, in this case the SQL statement where we create a table
    # CREATE TABLE IF NOT EXISTS is used to avoid multiple variation of cassettes being created, that's quite annoying later on if you have multiples of the same table
    # SQL is also case sensitive and when naming tables, needs to begin with a letter, not and number. The table used to be called 8_speed_cassettes, but had to be changed
    # ''' are used in python when performing complex lined SQL statements. "" can also be used but I've found them not as reliable for the big stuff
    connect.commit()
    # .commit() saves all progress. Always save within the funciton, not overall
    connect.close()
    # .close() closeds the connection to the database as we no longer need it open for this function


def insertEightSpeedData():
    connect = connect_database()
    cursor = connect.cursor()
    data = [
        ("Shimano", "HG400", "CSHG4008145", 8, "11-45", "Madison", 36.99, 6),
        ("Shimano", "HG400", "CSHG4008140", 8, "11-40", "Madison", 34.99, 6),
        ("Shimano", "HG50", "CSHG508128", 8, "11-28", "Madison", 22.99, 6),
        ("Shimano", "HG50", "CSHG508130", 8, "11-30", "Madison", 22.99, 6),
        ("Shimano", "HG50", "CSHG508132", 8, "11-32", "Madison", 22.99, 6),
        ("Shimano", "HG50", "CSHG508134", 8, "11-34", "Madison", 22.99, 6),
        ("Shimano", "HG50", "CSHG508225", 8, "12-25", "Madison", 34.99, 6),
        ("Shimano", "HG41", "CSHG418130", 8, "11-30", "Madison", 21.99, 6),
        ("Shimano", "HG41", "CSHG418132", 8, "11-32", "Madison", 21.99, 6),
        ("Shimano", "HG41", "CSHG418134", 8, "11-34", "Madison", 22.99, 6),
        ("Shimano", "HG31", "CSHG318132", 8, "11-32", "Madison", 20.99, 6),
        ("Shimano", "HG31", "CSHG318134", 8, "11-34", "Madison", 20.99, 6),
        ("SRAM", "PG820", "FW821130", 8, "11-30", "ZyroFisher", 18.00, 8),
        ("SRAM", "PG820", "FW821132", 8, "11-32", "ZyroFisher", 18.00, 8),
        ("SRAM", "PG850", "FW851128", 8, "11-28", "ZyroFisher", 26.00, 8),
        ("SRAM", "PG850", "FW851130", 8, "11-30", "ZyroFisher", 26.00, 8),
        ("SRAM", "PG850", "FW851132", 8, "11-32", "ZyroFisher", 26.00, 8),
        ("SRAM", "PG850", "FW851223", 8, "12-23", "ZyroFisher", 35.00, 8),
        ("SRAM", "PG850", "FW851226", 8, "12-26", "ZyroFisher", 35.00, 8),
        ("SRAM", "PG830", "FW831128", 8, "11-28", "ZyroFisher", 20.00, 8),
        ("SRAM", "XG", "FW075000", 8, "11-48", "ZyroFisher", 480.00, 8),
        ("Shimano", "HG41", "25113", 8, "11-34", "Bob Elliot", 22.99, 1),
        ("Shimano", "HG51", "25149", 8, "11-30", "Bob Elliot", 28.99, 1),
        ("Shimano", "HG51", "25150", 8, "11-32", "Bob Elliot", 28.99, 1),
        ("Sunrace", "M66", "50232", 8, "11-32", "Bob Elliot", 19.99, 1),
        ("Sunrace", "M66", "50340", 8, "11-34", "Bob Elliot", 20.99, 1),
        ("Sunrace", "R86", "50283", 8, "11-28", "Bob Elliot", 22.99, 1),
        ("Sunrace", "M55", "50337", 8, "11-34", "Bob Elliot", 19.99, 1),
        ("Shimano", "HG200", "25265", 8, "12-32", "Bob Elliot", 24.99, 1),
        ("Box", "FOUR", "CSBX48142K", 8, "11-42", "Ison Distribution", 59.99, 4),
        ("Box", "FOUR", "CSBX48242K", 8, "12-42", "Ison Distribution", 59.99, 4),
        ("Sunrace", "R86", "CSSR6832", 8, "11-32", "Ison Distribution", 21.99, 4),
        ("Sunrace", "R86", "CSSR8825", 8, "12-25", "Ison Distribution", 24.99, 4),
        ("GTB", "N/A", "ESP1031N", 8, "11-28", "Greyville", 25.96, 3),
        ("GTB", "N/A", "ESP1032N", 8, "11-32", "Greyville", 27.95, 3),
        ("Geardrive", "N/A", "GD0823", 8, "11-23", "Greyville", 16.96, 3),
        ("Geardrive", "N/A", "GD0825", 8, "11-25", "Greyville", 17.95, 3),
        ("Geardrive", "N/A", "GD0828", 8, "11-28", "Greyville", 18.54, 3),
        ("Geardrive", "N/A", "GD0832", 8, "11-32", "Greyville", 18.54, 3),
        ("Geardrive", "N/A", "GD0832OE", 8, "11-32", "Greyville", 16.96, 3),
        ("KMC", "REACT X8", "KX20", 8, "11-32", "Chicken Cyclekit", 26.00, 2),
        ("Miche", "PRIMATO 8X", "MCX501", 8, "11-28", "Chicken Cyclekit", 32.99, 2),
        ("Miche", "PRIMATO 8X", "MCX502", 8, "12-25", "Chicken Cyclekit", 32.99, 2),
        ("Miche", "PRIMATO 8X", "MCX503", 8, "12-27", "Chicken Cyclekit", 32.99, 2),
        ("Tifosi", "8X HG", "TIF708A", 8, "11-28", "Chicken Cyclekit", 18.99, 2),
        ("Tifosi", "8X HG", "N/A", 8, "11-32", "Chicken Cyclekit", 18.99, 2),
        ("Shimano", "HG50", "25261", 8, "11-28", "Bob Elliot", 22.99, 1),
        ("Shimano", "HG50", "25262", 8, "11-30", "Bob Elliot", 22.99, 1),
        ("Shimano", "HG50", "25263", 8, "11-32", "Bob Elliot", 22.99, 1),
        ("Shimano", "HG50", "25264", 8, "11-34", "Bob Elliot", 22.99, 1),
        ("Shimano", "HG50", "25137", 8, "12-25", "Bob Elliot", 34.99, 1),
        ("Shimano", "HG41", "25124", 8, "11-30", "Bob Elliot", 21.99, 1),
        ("Shimano", "HG41", "25122", 8, "11-32", "Bob Elliot", 21.99, 1),
        ("Shimano", "HG31", "25252", 8, "11-32", "Bob Elliot", 20.99, 1),
        ("Sunrace", "M66", "CSM668AU", 8, "11-32", "Greyville", 19.99, 3),
        ("Sunrace", "R86", "CSSR6828", 8, "11-28", "Ison Distribution", 22.99, 4),
        ("Sunrace", "R86", "CSR868AS", 8, "11-28", "Greyville", 22.99, 3),
        ("Shimano", "HG200", "HG200832", 8, "12-32", "Greyville", 24.99, 3),
        ("SRAM", "PG850", "FW851128", 8, "11-28", "Mackadams", 26.00, 5),
        ("SRAM", "PG850", "FW851130", 8, "11-30", "Mackadams", 26.00, 5),
        ("SRAM", "PG850", "FW851132", 8, "11-32", "Mackadams", 26.00, 5),
        ("SRAM", "PG850", "FW851223", 8, "12-23", "Mackadams", 35.00, 5),
        ("SRAM", "PG850", "FW851226", 8, "12-26", "Mackadams", 35.00, 5),
        ("Shimano", "HG200", "HG200832", 8, "12-32", "Mackadams", 24.99, 5),
        ("Undranded", "N/A", "CSESP1032", 8, "12-32", "Mackadams", 23.99, 5),
        ("Sunrace", "CSR86", "CSR868AO", 8, "11-23", "Mackadams", 19.99, 5),
        ("Sunrace", "CSR86", "CSR868AS", 8, "11-28", "Mackadams", 21.99, 5),
        ("Sunrace", "CSR86", "CSR868BQ", 8, "12-25", "Mackadams", 22.99, 5),
        ("Sunrace", "CSM66", "CSM668AU", 8, "11-32", "Mackadams", 22.99, 5),
        ("SRAM", "PG830", "FW831128", 8, "11-28", "Mackadams", 20.00, 5),
        ("Undranded", "N/A", "CSESP1031", 8, "11-28", "Mackadams", 20.00, 5),
        ("SRAM", "PG820", "FW821128", 8, "11-28", "Mackadams", 18.00, 5),
        ("SRAM", "PG820", "FW821130", 8, "11-30", "Mackadams", 18.00, 5),
        ("SRAM", "PG820", "FW821132", 8, "11-32", "Mackadams", 18.00, 5),
        ("Tektro", "ED-8", "TK-ABCS000001", 8, "11-42", "Upgrade", 70.00, 7),
        ("Microshift", "R8", "CSMSH8128", 8, "11-28", "Ison Distribution", 24.99, 4),
        ("Microshift", "Mezzo", "CSMSH8132", 8, "11-32", "Ison Distribution", 24.99, 4),
        ("Microshift", "Mezzo", "CSMSH8134", 8, "11-34", "Ison Distribution", 24.99, 4),
        ("Microshift", "Acolyte", "CSMSH8138", 8, "11-38", "Ison Distribution", 29.99, 4),
        ("Microshift", "Acolyte", "CSMSH8242", 8, "12-42", "Ison Distribution", 34.99, 4),
        ("Microshift", "Acolyte", "CSMSH8246", 8, "12-46", "Ison Distribution", 39.99, 4)]
    # Here we are creating all the data that will be inserted into the cassettes table in the form of a list [] named: data be sure to use the correct number of columns as stated in the CREATE TABLE statement

    cursor.executemany("INSERT INTO cassettes (brand, model, partNumber, speed, ratio, distributor, rrp, distributor_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
    # Now we use .excecutemany to insert multiple parameters, we use ? as placeholders for those parameters, and "data" to tell the statement what inforamtion to put instead of the placeholders. The ? are the same number as coloumns created and data listed above

    connect.commit()
    connect.close()

eightspdSQL = '''SELECT cassettes.brand, cassettes.model, cassettes.partNumber, cassettes.speed, cassettes.ratio, distributor_table.distributor_name, cassettes.rrp, distributor_table.distributor_link_url 
        FROM cassettes, distributor_table WHERE cassettes.distributor_id = distributor_table.distributor_id '''
    # Here we create a simple SELECT statment to pull all the relevent information taht we want to show the client

def get_8spd(speed: str, ratio: str, brand: str):
    # this funciton is listing all possible parameters (dropdown options) needed to run: speed, ratio, brand. The purpose is to add the data when it is selected from the dropdown option on the website
    query = eightspdSQL
    # to use the eightspdSQL statement created earlier, we need to assign it a new name, in this case: query
    parameter = []
    # an empty list is created called parameter that we can add to later
    if speed != "all":
    # if statement to decide what happens if "all" option is not selected (referencing script.js "const form" for "Submit" button line 82)
        query += "AND speed=?"
    # the += combines the eightspdSQL SELECT statement with "AND speed=?" at the end. A ? mark is again used as a placeholder in SQLite3
        parameter.append(speed)
    # the .append(speed) takes the selected "speed" from the dropdown option and adds it to the "parameter" list
    
    if ratio != "all":
        query += "AND ratio=?"
        parameter.append(ratio)

    if brand != "all":
        query += "AND brand=?"
        parameter.append(brand)


    # as with all other SQLite3 functions we've used, we need to close the connection to the database
    connect = connect_database()
    # opens a connection to the database
    cursor = connect.cursor()
    result = cursor.execute(query, parameter)

    rows = result.fetchall()
    connect.close()
    return response(rows)