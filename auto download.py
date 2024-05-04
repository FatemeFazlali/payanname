import os
import requests
from tqdm import tqdm
import csv
import subprocess

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))  # Total size of the file
    
    # Start download progress visualization
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                progress_bar.update(len(chunk))  # Update the progress bar
    
    # Close the progress bar after download completes
    progress_bar.close()

def extract_sequences(filename):
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('>'):
                sequence = line.strip()[1:5]  # Extracting four letters after ">"
                sequences.append(sequence)
    return sequences

def save_to_csv(sequences, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sequence in sequences:
            writer.writerow([sequence])

def main():
    # URL of the file to download
    url = 'https://files.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz'

    # Directory where you want to save the file
    save_directory = 'downloads'
    os.makedirs(save_directory, exist_ok=True)

    # File name
    file_name = 'pdb_seqres.txt.gz'

    # Path to save the file
    save_path = os.path.join(save_directory, file_name)

    # Download the file
    download_file(url, save_path)
    
    print("File downloaded successfully.")

    # Extract sequences from the downloaded file
    sequences = extract_sequences(save_path)
    
    # Load sequences from previous_protein_name.csv
    previous_sequences = set()
    previous_filename = 'previous_protein_name.csv'
    if os.path.exists(previous_filename):
        with open(previous_filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                previous_sequences.add(row[0])
    
    # Find new sequences not in previous_protein_name.csv
    new_sequences = [sequence for sequence in sequences if sequence not in previous_sequences]
    
    # Save new sequences to new_protein.csv
    new_filename = 'new_protein.csv'
    save_to_csv(new_sequences, new_filename)
    
    print("New protein names saved successfully.")

    # Load sequences from new_protein.csv
    new_sequences = set()
    if os.path.exists(new_filename):
        with open(new_filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                new_sequences.add(row[0])

    # URL of the server address to get the new pdb files of new proteins 
    server_url = 'http://example.com/path/to/files/'

    # Directory where you want to save the files
    save_directory = 'downloaded_files'
    os.makedirs(save_directory, exist_ok=True)

    # Iterate over each sequence and download the corresponding file
    for sequence in new_sequences:
        # Construct the URL for the file based on the sequence
        file_url = f'{server_url}/{sequence}.txt'

        # Construct the path to save the file
        save_path = os.path.join(save_directory, f'{sequence}.txt')

        # Download the file
        download_file(file_url, save_path)
        
        print(f"File {sequence}.txt downloaded successfully.")
    
    # Execute process1.py for all the downloaded files
    subprocess.run(['python', 'process1.py'])

if __name__ == "__main__":
    main()
