import psycopg2
from psycopg2 import Error

conn_user = 'postgres'
conn_passw = 'JHEQWR2ZUASDasdgASd98x'
conn_host = '155.138.253.162'
conn_port = '5432'
conn_db = 'test'

"postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName";
  
#Function for creating table
def create_table(table_def):
  try:
    conn = psycopg2.connect(
      user=conn_user,
      password=conn_passw,
      host=conn_host,
      port=conn_port,
      database=conn_db
    )
    cursor = conn.cursor()
    cursor.execute(table_def)
    conn.commit()
    print("Table created")
  except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
  finally:
    if (conn):
      cursor.close()
      conn.close()
      print("PostgreSQL connection is closed\n")

#Function for inserting data
def insert_data(table_name, data):
  try:
    conn = psycopg2.connect(
      user=conn_user,
      password=conn_passw,
      host=conn_host,
      port=conn_port,
      database=conn_db
    )
    cursor = conn.cursor()
    cursor.executemany(table_name, data)
    conn.commit()
    print("Data inserted in db")
  except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
  finally:
    if (conn):
      cursor.close()
      conn.close()
      print("PostgreSQL connection is closed\n")

#Function 
def create_function():
  try:
    conn = psycopg2.connect(
      user=conn_user,
      password=conn_passw,
      host=conn_host,
      port=conn_port,
      database=conn_db
    )
    cursor = conn.cursor()
    cursor.execute("""
      CREATE OR REPLACE FUNCTION get_cedula_by_name (name)
      RETURNS integer
      AS $$
      declare
      result integer;
      BEGIN
        SELECT cedula into result FROM clients WHERE name ILIKE name;
        RETURN result;
      END;
      $$ LANGUAGE plpgsql;
    """)
    conn.commit()
    print("Function created")
  except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
  finally:
    if (conn):
      cursor.close()
      conn.close()
      print("PostgreSQL connection is closed\n")
      
def execute_function(function_name, parameters):
  try:
    conn = psycopg2.connect(
      user=conn_user,
      password=conn_passw,
      host=conn_host,
      port=conn_port,
      database=conn_db
    )
    cursor = conn.cursor()
    cursor.callproc(function_name, parameters)
    row = cursor.fetchone()
    while row is not None:
      print(row)
      row = cursor.fetchone()
    print("Function executed")
  except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
  finally:
    if (conn):
      cursor.close()
      conn.close()
      print("PostgreSQL connection is closed\n")

def run():
  command = """
    CREATE TABLE clients (
      id SERIAL PRIMARY KEY,
      name VARCHAR(255) not null,
      cedula INT,
      address VARCHAR(255),
      phone INT
    );
    """
  # create_table(command)

  data = [
    ('Pedro', 171995, 'calle principal y calle secundaria', 9929),
    ('Carlos', 18051, '22 de Julio y Flores', 994568229),
    ('Kevin', 191997, 'vicente leon y rios', 992934589),
    ('Bryan', 131998, '3 de marzo  y los rios ', 985734213)
  ]
  # insert_data('INSERT INTO clients (name, cedula, address, phone) VALUES (%s,%s,%s,%s)', data)
  create_table(data)
  #create_function()

  #execute_function('get_cedula_by_name', ('%pedro%',))