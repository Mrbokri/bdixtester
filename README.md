Unknown Intellect Script
Overview
This Python script performs a network scan by pinging URLs and checking their status. It reads URLs from both a text file and a JSON file, and saves the results of the "UP" URLs to a results.txt file.

Requirements
Python 3.x
Requests library
Installation Instructions
Linux
Install Python 3:
Ensure Python 3 is installed. You can install it using your package manager. For example, on Debian-based systems:

sh
Copy code
sudo apt update
sudo apt install python3 python3-pip
Install Required Packages:
Install the required Python packages:

sh
Copy code
pip3 install requests
Download the Script:
Download or clone the repository containing the script.

Run the Script:
Execute the script using Python 3:

sh
Copy code
python3 your_script_name.py
Termux (Android)
Install Termux:
Download and install Termux from the Google Play Store or F-Droid.

Install Python:
Open Termux and install Python:

sh
Copy code
pkg install python
Install Required Packages:
Install the required Python packages:

sh
Copy code
pip install requests
Download the Script:
Use Termux to download or transfer the script to your Termux environment.

Run the Script:
Execute the script:

sh
Copy code
python your_script_name.py
Pydroid (Android)
Install Pydroid:
Download and install Pydroid from the Google Play Store.

Install Required Packages:
Open Pydroid and install the requests library from the Pydroid package manager.

Transfer the Script:
Use Pydroid’s file browser to navigate to the location of your Python script or transfer the script to your device.

Run the Script:
Open the script in Pydroid and run it.

Windows
Install Python:
Download and install Python from the official website.

Install Required Packages:
Open Command Prompt or PowerShell and install the required Python packages:

sh
Copy code
pip install requests
Download the Script:
Download or clone the repository containing the script.

Run the Script:
Open Command Prompt or PowerShell, navigate to the directory containing the script, and execute it:

sh
Copy code
python your_script_name.py
Configuration
Text File (urls.txt):
Create a text file named urls.txt in the same directory as the script. List each URL on a new line.

JSON File (servers.json):
Create a JSON file named servers.json in the same directory as the script. Ensure it has the following structure:

json
Copy code
{
  "servers": [
    {"index": 1, "name": "Server1", "url": "http://example.com", "category": "CATEGORY"}
    // Add more servers as needed
  ]
}
Notes
Ensure that the script has the appropriate permissions to read from urls.txt and servers.json.
For any issues or contributions, please refer to the repository’s issue tracker.
