import mysql.connector
from mysql.connector import Error
import pandas as pd

# 1. Create a table named "employees" in MySQL with the following columns: columns: id (integer), name (text), department (text), salary (integer), and join_date (date).
def crt_table_employees(hostname, databasename, username, password):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='hostname', 
            database='databasename', 
            user='username',  
            password='password'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL query to create the "employees" table
            create_table_query = """
            CREATE TABLE employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary INT NOT NULL,
                join_date DATE NOT NULL
            )
            """
            
            # Execute the query
            cursor.execute(create_table_query)
            print("Table 'employees' created successfully.")

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# 2. Extract data from the JSON file, clean and remove unnecessary fields
def transform_json_to_data(json_file_path):
    try:
        # Turn json file into DataFrame
        df = pd.read_json(json_file_path)
        
        # Change the data type of join_date column from string to datetime
        df['join_date'] = pd.to_datetime(df['join_date'])
        
        # Test data type
        if not pd.api.types.is_integer_dtype(df['id']):
            raise ValueError("Column 'id' must be integer type")
        if not pd.api.types.is_string_dtype(df['name']):
            raise ValueError("Column 'name' must be string type")
        if not pd.api.types.is_string_dtype(df['department']):
            raise ValueError("Column 'department' must be string type")
        if not pd.api.types.is_integer_dtype(df['salary']):
            raise ValueError("Column 'salary' must be integer type")
        
        # Remove unneccessary fields
        required_cols = ['id', 'name', 'department', 'salary', 'join_date']
        return df[required_cols]
    
    except Exception as e:
        print("An error occured: e")
    
# 3. Insert data into the "employees" table in MySQL
def insert_data_into_table(df, hostname, databasename, username, password):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='hostname',  
            database='databasename', 
            user='username',  
            password='password'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL query to insert data into the "employees" table
            insert_query = """
            INSERT INTO employees (id, name, department, salary, join_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            # Prepare the data to be inserted into the table
            data = df.values.tolist()
            
            # Execute the query
            cursor.executemany(insert_query, data)
            print("Data inserted successfully.")
            
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("My SQL connection is closed")


def etl_process(json_file_path, hostname, databasename, username, password):
    # Step 1: Create the employees table
    crt_table_employees(hostname, databasename, username, password)
    
    # Step 2: Extract and transform data from JSON file
    df = transform_json_to_data(json_file_path)
    if df is None or df.empty:
        print("No data to insert after transformation.")
        return
    
    # Step 3: Load data into the MySQL database
    insert_data_into_table(df, hostname, databasename, username, password)
    print("ETL process completed successfully.")
