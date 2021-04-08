import pandas as pd
import pyodbc
import psycopg2
import psycopg2.extras
import datetime, time

# Connect to SQL Server
conn = psycopg2.connect(dbname = 'central_teste', user='douglas', password='gese123', host='200.135.184.210',port='5432', sslmode='prefer')
cursor = conn.cursor()


# Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute("INSERT INTO ONI (id, year, month, total, climAdjust, anom) VALUES (" + str(row.id) + ", " + str(row.year) + ", " + str(row.month) + ", " + str(row.total) + ", " + str(row.climAdjust) + ", " + str(row.anom) + ")")

#Logica que implementa o INSERT no banco
def insert_into_CPC_SST(sst_data):
    #Cada linha de dado será upada

    try:
        for row in sst_data.itertuples():     
            #Trasformar data em  formato padrão aaaa-mm-dd
            date = row[0]
            
            cursor.execute("INSERT INTO CPC_SST (deck_date, anomalia_R0, anomalia_R1, anomalia_R2, anomalia_R3, anomalia_R4) VALUES ('{date}', {anomalia_R0}, {anomalia_R1}, {anomalia_R2}, {anomalia_R3}, {anomalia_R4})".format(date=date, anomalia_R0=row.r0, anomalia_R1=row.r1, anomalia_R2=row.r2, anomalia_R3=row.r3, anomalia_R4=row.r4))
        
        conn.commit()
    except e:
        print("Problema na Inserção de dados CPC_SST")