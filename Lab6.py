import requests

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
