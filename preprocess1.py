import csv
import mysql.connector
from mysql.connector import Error
import os
import pandas as pd

# MySQL database connection settings
host = "localhost"
user = "root"
password = "123456"
database = "pfragments2"


# Path to the output CSV file
AA_csv_file = 'E:/file_name-Copy1.csv'
#read the AA csv file
data_import = pd.read_csv(AA_csv_file, index_col=False)

# Function to determine aa_number based on protein name
def get_aa_number(protein_name):
    # Perform boolean indexing to filter rows where the second column matches the name
    filtered_rows = data_import.loc[data_import.iloc[:, 1] == protein_name]

    # Extract the values from the third column for the filtered rows
    third_column_values = filtered_rows.iloc[:, 2].tolist()

    # Create a new DataFrame with the extracted values
    new_df = pd.DataFrame(third_column_values, columns=['ThirdColumn'])

    return len(new_df)


# Function to import CSV files and insert rows into MySQL
def import_csv_to_mysql(csv_files, txt_df):
    try:
        cnx = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cursor = cnx.cursor()

        for csv_file in csv_files:
            with open(csv_file, 'r') as file:
                csv_data = csv.reader(file)
                next(csv_data)  # Skip the header row

                bulk_data = []  # List to store rows for bulk insert

                for row in csv_data:
                    pdb_name = row[1]  # 
                    protein_name = row[2]  # 
                    aa_number = get_aa_number(protein_name)  # Determine the aa_number based on protein_name
                    aa = txt_df.loc[txt_df['Protein Name'] == protein_name, 'Chunk'].values[0]  # Retrieve the corresponding chunk from txt_df
                    s_structure = row[3]  # 
                    distance = round(float(row[4]), 6)  # 
                    polarity = row[5]  # 
                    surface_location = row[6][:40]  # 

                    table_name = f"table_{aa_number}"  # Determine the table name based on aa_number

                    insert_data = (pdb_name, protein_name, aa_number, aa, s_structure, distance, polarity, surface_location)
                    bulk_data.append(insert_data)

                insert_query = f"INSERT INTO {table_name} (pdb_name, protein_name, aa_number, AA, S_STRUCTURE, distance, polarity, surface_location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.executemany(insert_query, bulk_data)
                cnx.commit()

                print(f"Data imported from {csv_file} to {table_name} successfully.")

            os.remove(csv_file)  # Delete the processed CSV file
            txt_df = txt_df[~txt_df['Protein Name'].isin([protein_name])]  # Remove the processed lines from txt_df

        cursor.close()
        cnx.close()

    except Error as e:
        print("Error connecting to MySQL:", e)

# Main code
folder_path = r"C:\Users\pentium\Desktop\New_folder"  # Update with your folder path
txt_file = r"C:\Users\pentium\Desktop\protein_info.txt"  # Update with your text file path

# Read protein information from text file and create DataFrame
with open(txt_file, 'r') as txt_file:
    protein_lines = txt_file.read().split('\n')
    protein_data = [line.split('|') for line in protein_lines if line.startswith('>') and '|' in line]
    txt_df = pd.DataFrame(protein_data, columns=['Protein Name', 'Chunk'])

csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".csv")]

import_csv_to_mysql(csv_files, txt_df)
