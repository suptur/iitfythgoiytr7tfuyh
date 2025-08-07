import requests
import os
import logging
from tqdm import tqdm
import re
import threading

# Configure logging
logging.basicConfig(filename='script.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# List of URLs to download
urls = [


"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/in/ipv6-aggregated.txt",
"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/il/ipv6-aggregated.txt",
"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/cn/ipv6-aggregated.txt",
"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/in/ipv4-aggregated.txt",
"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/il/ipv4-aggregated.txt",
"https://raw.githubusercontent.com/ipverse/rir-ip/refs/heads/master/country/cn/ipv4-aggregated.txt",

    # Add more URLs here
]

# Function to download a file and show progress
def download_file(url, dest_folder):
    try:
        filename = url.split("/")[-1]
        filepath = os.path.join(dest_folder, filename)
        with open(filepath, "wb") as file, requests.get(url, stream=True) as response:
            total_size = int(response.headers.get("content-length", 0))
            progress_bar = tqdm(total=total_size, unit="B", unit_scale=True, desc=f"Downloading {filename}")
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                progress_bar.update(len(data))
            progress_bar.close()
    except Exception as e:
        logging.error(f"Failed to download file from {url}: {str(e)}")

# Function to convert IPv4 address to "||ipv4 address^" format
def convert_line(line):
    return "||" + line.strip() + "^"
    return line.strip()

# Function to download files concurrently
def download_files(urls, dest_folder, max_concurrent=100):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url, dest_folder))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        if len(threads) >= max_concurrent:
            for thread in threads:
                thread.join()
            threads = []

    # Wait for remaining threads to finish
    for thread in threads:
        thread.join()

# Download files and merge into a single file
merged_lines = set()  # Using a set for faster duplicate removal
download_folder = "downloads_ipsets"
os.makedirs(download_folder, exist_ok=True)

# Download files concurrently
download_files(urls, download_folder)

# Process downloaded files
for filename in os.listdir(download_folder):
    filepath = os.path.join(download_folder, filename)
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith(("@@", "!", "#")):  # Exclude lines starting with "@@", "!", "#"
                merged_lines.add(convert_line(line))

# Save updated file with unique lines and remove lines starting with "!"
merged_unique_file = "Country-block-3.txt"
with open(merged_unique_file, "w", encoding="utf-8") as file:
    for line in sorted(merged_lines):  # Sort lines alphabetically
        file.write(line + "\n")

# Delete downloaded files
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    os.remove(file_path)
