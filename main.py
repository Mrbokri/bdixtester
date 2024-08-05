import json
import requests
import os
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the title
title = "Unknown Intellect"

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the title with fading effect
def fade_in_title(text, duration=1):
    clear_screen()
    length = len(text) + 4
    steps = 5  # Number of steps for the fading effect
    delay = duration / steps  # Time delay between each step
    
    for i in range(steps + 1):
        clear_screen()
        visible_length = int((i / steps) * length)
        print('*' * visible_length)
        print(f'* {text[:visible_length - 2]} *')  # Adjust to fit the visible length
        print('*' * visible_length)
        time.sleep(delay)

# Print the fading title
fade_in_title(title)





print("starting the scan")
def read_urls_from_txt(file_path):
    urls = []
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

def read_servers_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        servers = data['servers']
    return servers

# Function to ping a URL
def ping_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return url, "UP"
        else:
            return url, "DOWN"
    except requests.exceptions.RequestException:
        return url, "DOWN"

# Read URLs from both text file and JSON file
txt_file_path = 'urls.txt'
json_file_path = 'servers.json'

# Initialize servers list
servers = []

if os.path.exists(txt_file_path):
    urls = read_urls_from_txt(txt_file_path)
    servers.extend([{"index": i + 1, "name": f"TextURL{i + 1}", "url": url, "category": "UNKNOWN"} for i, url in enumerate(urls)])

if os.path.exists(json_file_path):
    json_servers = read_servers_from_json(json_file_path)
    servers.extend(json_servers)

# Define a function to process each server
def process_server(server):
    url = server['url']
    status = ping_url(url)
    return server, status

# Ping each server URL concurrently
total_servers = len(servers)
up_urls = []

# Open the results file in write mode
with open('results.txt', 'w') as txt_file:
    with ThreadPoolExecutor(max_workers=15) as executor:
        future_to_server = {executor.submit(process_server, server): server for server in servers}
        
        for future in as_completed(future_to_server):
            server, (url, status) = future.result()
            
            # Write only the "UP" URLs to the text file
            if status == "UP":
                result = f"Server {server['index']} - {server['name']} ({server['category']}) at {url} is {status}.\n"
                txt_file.write(result)
                up_urls.append(url)
            
            # Calculate and display progress
            progress = (len(up_urls)) / total_servers * 100
            print(f"Progress: {progress:.2f}% - {url} is {status}")

print("All URLs have been pinged. Only 'UP' URLs are saved in results.txt")
