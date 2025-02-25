#Importes
import requests
import hashlib
import pathlib

BASE_URL = "https://download.videolan.org/pub/videolan/vlc/3.0.21/win64/"
FILE_NAME_SHA256 = "vlc-3.0.21-win64.exe.sha256"
FILE_NAME = "vlc-3.0.21-win64.exe"

#Step 1

def get_expected_sha256():
    response = requests.get(f'{BASE_URL}/{FILE_NAME_SHA256}')
    if not response.ok:
        print("Did not get the SHA256 file. Exiting...")
        exit()
    resp_text = response.text 
    file_sha256 = resp_text.split()[0] 
    print(f"Expected SHA-256: {file_sha256}")
    return file_sha256

#Step 2

def download_installer():
    response = requests.get(f'{BASE_URL}/{FILE_NAME}')
    if not response.ok:
        print("Did not get the installation file. Exiting...")
        exit()
    file_binary = response.content  
    print(f"Downloaded file size: {len(file_binary)} bytes")
    return file_binary

#Step 3
def installer_ok(installer_data, expected_sha256):
    sha256 = hashlib.sha256(installer_data).hexdigest()
    print(f"Computed SHA-256: {sha256}")

#Step 4
    if sha256 == expected_sha256:
        print("SHA-256 values match. Integrity verified.")
        return True
    else:
        print("Downloaded SHA-256 does not match expected value. Exiting...")
        return False
#Step 5
def save_installer(installer_data):
    file_path = pathlib.Path(os.getenv('TEMP')) / FILE_NAME
    with open(file_path, "wb") as outfile:  # Write a binary file
        outfile.write(installer_data)
    print(f"Installer saved to: {file_path}")
    return file_path
