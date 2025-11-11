import sqlite3
import csv

def csv_to_sql(csv_content, database, table_name):
    CSV_reader = csv.reader(csv_content)
    CSV_headers = next(CSV_reader)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # filling database

    cursor.execute("BEGIN") # tell cursor not to comit untill cursor.commit()
        
    columns = ', '.join([f'"{header}" TEXT' for header in CSV_headers]) #fill columns
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})" # make a request
    cursor.execute(create_table_sql) # create table with filled columns

    # Insert data rows
    placeholders = ', '.join(['?' for _ in CSV_headers])
    insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    
    for row in CSV_reader:
        cursor.execute(insert_sql, row)
    
    cursor.execute("COMMIT") # Commit the transaction
    connection.close()