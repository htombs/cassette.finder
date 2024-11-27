import sqlite3
from .database import connect_database, response

def createTenSpeedTable():
    connect = connect_database()
    cursor = connect.cursor()
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
    connect.commit()
    connect.commit()

def insertTenSpeedData():
    connect = connect_database()
    cursor = connect.cursor()
    data = [
        ("Shimano", "5700", "21590", 10, "11-28", "Bob-Elliot", 54.99, 1),
        ("Shimano", "M4100", "25269", 10, "11-46", "Bob-Elliot", 59.99, 1),
        ("Shimano", "M4100", "25206", 10, "11-42", "Bob-Elliot", 49.99, 1),
        ("Shimano", "HG50", "25253", 10, "11-36", "Bob-Elliot", 45.99, 1),
        ("Shimano", "HG500", "25238", 10, "11-28", "Bob-Elliot", 34.99, 1),
        ("Sunrace", "M1", "50374", 10, "11-36", "Bob-Elliot", 46.99, 1),
        ("Sunrace", "MS1", "50236", 10, "11-36", "Bob-Elliot", 46.99, 1),
        ("Sunrace", "MS3", "50237", 10, "11-40", "Bob-Elliot", 64.99, 1),
        ("Sunrace", "MS3", "50238", 10, "11-40", "Bob-Elliot", 64.99, 1),
        ("Sunrace", "MS3", "50239", 10, "11-42", "Bob-Elliot", 64.99, 1),
        ("Sunrace", "MS3", "50240", 10, "11-42", "Bob-Elliot", 64.99, 1),
        ("Sunrace", "MS3", "50341", 10, "11-46", "Bob-Elliot", 72.99, 1),
        ("Sunrace", "MS3", "50342", 10, "11-46", "Bob-Elliot", 72.99, 1),
        ("Sunrace", "MX0", "50249", 10, "11-36", "Bob-Elliot", 81.99, 1),
        ("Sunrace", "MX0", "50250", 10, "11-36", "Bob-Elliot", 68.99, 1),
        ("Sunrace", "MX3", "50253", 10, "11-42", "Bob-Elliot", 99.99, 1),
        ("Sunrace", "MX3", "50254", 10, "11-42", "Bob-Elliot", 86.99, 1),
        ("Sunrace", "MX3", "50255", 10, "11-46", "Bob-Elliot", 107.99, 1),
        ("Sunrace", "MX3", "50256", 10, "11-46", "Bob-Elliot", 95.99, 1),
        ("Sunrace", "RS0", "50270", 10, "11-25", "Bob-Elliot", 54.99, 1),
        ("Sunrace", "RS0", "50271", 10, "11-28", "Bob-Elliot", 54.99, 1),
        ("Sunrace", "RS0", "50272", 10, "11-32", "Bob-Elliot", 54.99, 1),
        ("Sunrace", "RS1", "50275", 10, "11-28", "Bob-Elliot", 35.99, 1),
        ("Sunrace", "RS1", "50276", 10, "11-32", "Bob-Elliot", 35.99, 1),
        ("Sunrace", "RX0", "50345", 10, "11-28", "Bob-Elliot", 73.99, 1),
        ("Sunrace", "RX0", "50348", 10, "11-32", "Bob-Elliot", 60.99, 1),
        ("Sunrace", "RX0", "50346", 10, "11-28", "Bob-Elliot", 60.99, 1),
        ("Sunrace", "RX0", "50347", 10, "11-32", "Bob-Elliot", 73.99, 1),
        ("Campagnolo", "Centuar", "CPB528A", 10, "14-23", "Chicken Cyclekit", 98.99, 2),
        ("Campagnsolo", "Veloce", "CPB533", 10, "11-25", "Chicken Cyclekit", 71.24, 2),
        ("Campagnolo", "Veloce", "CPB539", 10, "12-23", "Chicken Cyclekit", 52.99, 2),
        ("Campagnolo", "Veloce", "CPB535", 10, "12-25", "Chicken Cyclekit", 52.99, 2),
        ("Campagnolo", "Veloce", "CPB536", 10, "13-26", "Chicken Cyclekit", 52.99, 2),
        ("Campagnolo", "Veloce", "CPB537", 10, "13-29", "Chicken Cyclekit", 52.99, 2),
        ("Miche", "Primato", "MCX23", 10, "12-23", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX20", 10, "12-25", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primate", "MCX21", 10, "12-27", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX22", 10, "12-29", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX19", 10, "13-26", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX24", 10, "13-30", "Chicken Cyclekit", 64.99, 2),
        ("Miche", "Primato", "MCX18", 10, "16-23", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX25", 10, "12-25", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX250", 10, "11-30", "Chicken Cyclekit", 54.99, 2),
        ("Miche", "Primato", "MCX251", 10, "12-30", "Chicken Cyclekit", 51.99, 2),
        ("Miche", "Primato", "MCX252", 10, "13-30", "Chicken Cyclekit", 64.99, 2),
        ("Miche", "Primato", "MCX253", 10, "11-27", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX254", 10, "14-28", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX26", 10, "12-27", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX27", 10, "12-29", "Chicken Cyclekit", 48.99, 2),
        ("Miche", "Primato", "MCX956A", 10, "16-27", "Chicken Cyclekit", 48.99, 2),
        ("KMC", "REACT", "KX40", 10, "11-36", "Chicken Cyclekit", 45.99, 2),
        ("KMC", "REACT", "KX41", 10, "11-42", "Chicken Cyclekit", 49.99, 2),
        ("Tifosi", "10x", "TIF710A", 10, "11-34", "Chicken Cyclekit", 31.99, 2),
        ("Tifosi", "10x", "TIF710B", 10, "11-36", "Chicken Cyclekit", 32.99, 2),
        ("Clarks", "", "C-10SC-UKS", 10, "11-36", "Greyville", 31.96, 3),
        ("Sunrace", "MS1", "CSMS1TAWM", 10, "11-36", "Greyville", 29.95, 3),
        ("Sunrace", "MS3", "CSMS3M", 10, "11-42", "Greyville", 59.95, 3),
        ("Sunrace", "MX3", "CSMX3", 10, "11-42", "Greyville", 69.95, 3),
        ("GTB", "", "ESP1036N", 10, "11-36", "Greyville", 69.95, 3),
        ("Geardrive", "", "GD1025", 10, "11-25", "Greyville", 32.95, 3),
        ("Geardrive", "", "GD1028", 10, "11-28", "Greyville", 32.95, 3),
        ("Geardrive", "", "GD1032", 10, "11-32", "Greyville", 32.95, 3),
        ("Geardrive", "", "GD1036", 10, "11-36", "Greyville", 34.96, 3),
        ("Geardrive", "", "GD1040", 10, "11-40", "Greyville", 35.95, 3),
        ("Geardrive", "", "GD1042", 10, "11-42", "Greyville", 47.95, 3),
        ("Driven", "RZ", "CSDV1123", 10, "11-23", "Ison Distribution", 249.99, 4),
        ("Microshift", "Sword", "CSMSH10138", 10, "11-38", "Ison Distribution", 54.99, 4),
        ("Microshift", "Advent", "CSMSH10148", 10, "11-48", "Ison Distribution", 54.99, 4),
        ("N/A", "N/A", "CSESP1036", 10, "11-36", "Mackadams", 31.99, 5),
        ("S-Ride", "M400", "590848", 10, "11-36", "Mackadams", 59.99, 5),
        ("SRAM", "PG1030", "FWS131126", 10, "11-26", "Mackadams", 61.99, 5),
        ("SRAM", "PG1030", "FWS131128", 10, "11-28", "Mackadams", 61.99, 5),
        ("SRAM", "PG1030", "FWS131132", 10, "11-32", "Mackadams", 61.99, 5),
        ("SRAM", "PG1030", "FWS131136", 10, "11-36", "Mackadams", 61.99, 5),
        ("SRAM", "PG1050", "FWS151123", 10, "11-23", "Mackadams", 75.99, 5),
        ("SRAM", "PG1050", "FWS151126", 10, "11-26", "Mackadams", 75.99, 5),
        ("SRAM", "PG1050", "FWS151128", 10, "11-28", "Mackadams", 75.99, 5),
        ("SRAM", "PG1050", "FWS151132", 10, "11-32", "Mackadams", 75.99, 5),
        ("SRAM", "PG1050", "FWS151136", 10, "11-36", "Mackadams", 75.99, 5),
        ("Sunrace", "MS1", "CSMS1TAWM", 10, "11-36", "Mackadams", 46.99, 5),
        ("Sunrace", "MS1", "CSMS1TAWB", 10, "11-36", "Mackadams", 46.99, 5),
        ("Sunrace", "MS3", "CSMS3TAXM", 10, "11-40", "Mackadams", 64.99, 5),
        ("Sunrace", "MS3", "CSMS3TAYM", 10, "11-42", "Mackadams", 64.99, 5),
        ("Sunrace", "MS3", "CSMS3TAXB", 10, "11-40", "Mackadams", 64.99, 5),
        ("Sunrace", "MS3", "CSMS3TAYB", 10, "11-42", "Mackadams", 64.99, 5),
        ("Sunrace", "MX0", "CSMX0TAWM", 10, "11-36", "Mackadams", 68.99, 5),
        ("Sunrace", "MX0", "CSMX0TAWB", 10, "11-36", "Mackadams", 68.99, 5),
        ("Sunrace", "MX3", "CSMX3TAXM", 10, "11-40", "Mackadams", 69.99, 5),
        ("Sunrace", "MX3", "CSMX3TAYM", 10, "11-42", "Mackadams", 69.99, 5),
        ("Sunrace", "MX3", "CSMX3TAZM", 10, "11-46", "Mackadams", 69.99, 5),
        ("Sunrace", "MX3", "CSMX3TAXB", 10, "11-40", "Mackadams", 69.99, 5),
        ("Sunrace", "MX3", "CSMX3TAYB", 10, "11-42", "Mackadams", 69.99, 5),
        ("Sunrace", "MX3", "CSMX3TAZB", 10, "11-46", "Mackadams", 69.99, 5),
        ("Sunrace", "RS1", "CSRS1TAS", 10, "11-28", "Mackadams", 35.99, 5),
        ("Sunrace", "RS1", "CSRS1TAU", 10, "11-32", "Mackadams", 35.99, 5),
        ("Sunrace", "RS0", "CSRS0TAQ", 10, "11-25", "Mackadams", 54.99, 5),
        ("Sunrace", "RS0", "CSRS0TAS", 10, "11-28", "Mackadams", 54.99, 5),
        ("Sunrace", "RS0", "CSRS0TAU", 10, "11-32", "Mackadams", 54.99, 5),
        ("Sunrace", "RX0", "CSRX0TAQM", 10, "11-25", "Mackadams", 63.99, 5),
        ("Sunrace", "RX0", "CSRX0TASM", 10, "11-28", "Mackadams", 63.99, 5),
        ("Sunrace", "RX0", "CSRX0TAUM", 10, "11-32", "Mackadams", 63.99, 5),
        ("Sunrace", "RX0", "CSRX0TAQB", 10, "11-25", "Mackadams", 73.99, 5),
        ("Sunrace", "RX0", "CSRX0TASB", 10, "11-28", "Mackadams", 73.99, 5),
        ("Sunrace", "RX0", "CSRX0TAUB", 10, "11-32", "Mackadams", 73.99, 5),
        ("Shimano", "6700", "CS670010128", 10, "11-28", "Madison", 74.99, 6),
        ("Shimano", "6700", "CS670010225", 10, "12-25", "Madison", 74.99, 6),
        ("Shimano", "6700", "CS670010230", 10, "12-30", "Madison", 74.99, 6),
        ("Shimano", "M771", "CSM771132", 10, "11-32", "Madison", 74.99, 6),
        ("Shimano", "M771", "CSM771134", 10, "11-34", "Madison", 74.99, 6),
        ("Shimano", "M771", "CSM771136", 10, "11-36", "Madison", 74.99, 6),
        ("Shimano", "LG400", "CSLG40010139", 10, "11-39", "Madison", 49.99, 6),
        ("Shimano", "LG400", "CSLG40010143", 10, "11-43", "Madison", 59.99, 6),
        ("Shimano", "LG400", "CSLG40010148", 10, "11-48", "Madison", 59.99, 6),
        ("Shimano", "M4100", "CSM4100142", 10, "11-42", "Madison", 49.99, 6),
        ("Shimano", "M4100", "CSM4100146", 10, "11-46", "Madison", 59.99, 6),
        ("Shimano", "HG50", "CSHG5010136", 10, "11-36", "Madison", 44.99, 6),
        ("Shimano", "LG300", "CSLG30010139", 10, "11-39", "Madison", 44.99, 6),
        ("Shimano", "LG300", "CSLG30010148", 10, "11-48", "Madison", 54.99, 6),
        ("Shimano", "HG500", "CSHG50010125", 10, "11-25", "Madison", 34.99, 6),
        ("Shimano", "HG500", "CSHG50010132", 10, "11-32", "Madison", 39.99, 6),
        ("Shimano", "HG500", "CSHG50010134", 10, "11-34", "Madison", 39.99, 6),
        ("Shimano", "HG500", "CSHG50010228", 10, "12-28", "Madison", 34.99, 6),
        ("SRAM", "PG1030", "FWS131128", 10, "11-28", "ZyroFisher", 62.00, 7),
        ("SRAM", "PG1030", "FWS131132", 10, "11-32", "ZyroFisher", 62.00, 7),
        ("SRAM", "PG1030", "FWS131136", 10, "11-36", "ZyroFisher", 62.00, 7),
        ("SRAM", "PG1050", "FWS151128", 10, "11-28", "ZyroFisher", 76.00, 7),
        ("SRAM", "PG1050", "FWS151132", 10, "11-32", "ZyroFisher", 76.00, 7),
        ("SRAM", "PG1050", "FWS151136", 10, "11-36", "ZyroFisher", 76.00, 7),
        ("SRAM", "PG1050", "FWS151232", 10, "12-32", "ZyroFisher", 76.00, 7),
        ("SRAM", "PG1050", "FWS151236", 10, "12-36", "ZyroFisher", 76.00, 7),
        ("SRAM", "PG1070", "FWS171125", 10, "11-25", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171126", 10, "11-26", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171128", 10, "11-28", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171136", 10, "11-36", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171225", 10, "12-25", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171232", 10, "12-32", "ZyroFisher", 91.00, 7),
        ("SRAM", "PG1070", "FWS171236", 10, "12-36", "ZyroFisher", 91.00, 7),
        ("Clarks", "", "C-10SC", 10, "11-36", "ZyroFisher", 39.99, 7),
        ("Microshift", "Advent", "CSMSG10148", 10, "11-48", "Ison Distribution", 74.99, 4),
        ("Microshift", "Sword", "CSMSG10138", 10, "11-38", "Ison Distribution", 79.99, 4)]
    
    cursor.executemany("INSERT INTO cassettes (brand, model, partNumber, speed, ratio, distributor, rrp, distributor_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)

    connect.commit()
    connect.close()

tenspdSQL = '''SELECT cassettes.brand, cassettes.model, cassettes.partNumber, cassettes.speed, cassettes.ratio, distributor_table.distributor_name, cassettes.rrp, distributor_table.distributor_link_url 
        FROM cassettes, distributor_table WHERE cassettes.distributor_id = distributor_table.distributor_id '''

def get_10spd(speed: str, ratio: str, brand: str):
    query = tenspdSQL
    parameter = []
    if speed != "all":
        query += "AND speed=?"
        parameter.append(speed)
    
    if ratio != "all":
        query += "AND ratio=?"
        parameter.append(ratio)

    if brand != "all":
        query += "AND brand=?"
        parameter.append(brand)

    connect = connect_database()
    cursor = connect.cursor()
    result = cursor.execute(query, parameter)

    rows = result.fetchall()
    connect.close()
    return response(rows)