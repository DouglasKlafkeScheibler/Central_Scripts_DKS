import argparse
import psycopg2
import psycopg2.extras
import os


INSERT = 'INSERT INTO {} ({}) VALUES {};'
secrets = '../config/secretsDbCentral.json'


def _parseSecrets(path):
    import json

    result = None
    with open(path,'r') as f:
        result = json.loads(f.read())

    return result['db_host'], result['db_port'], result['db_name'], result['db_user'], result['db_password']

def _getPlaceholders(columns):

    placeholders = ''
    sep = ''
    for _ in range(len(columns)):
        placeholders = placeholders + sep + '%s'
        sep = ', '
    return '({})'.format(placeholders)

def _parseData(rawData, hasHeader = True):

    data = []
    lines = []
    if os.path.isfile(rawData):
        with open(rawData, 'r') as f:
            lines = f.readlines()
    else:
        lines = rawData.split('\\n')

    if hasHeader:
        lines = lines[1:]

    for line in lines:
        data.append(line.strip().split(';'))

    return data

def _getConnection():
    host, port, dbname, user, password = _parseSecrets(secrets)
    return psycopg2.connect(dbname = dbname, user=user, password=password, host=host,port=port, sslmode='prefer')

def sendToDb(columns, data, table):

    try:
        connection = _getConnection()
        cursor = connection.cursor()
        placeholders = _getPlaceholders(columns)
    
        values = ', '.join(cursor.mogrify(placeholders, row).decode() for row in data)

        statement = INSERT.format(table, ', '.join(columns), values )

        cursor.execute(statement)

        connection.commit()

    except Exception as e:
        print(e)
        raise
    else:
        cursor.close()
        connection.close()
    

def uploadDB(table,columns,data):
    
    data = _parseData(data)

    sendToDb(columns, data, table)

