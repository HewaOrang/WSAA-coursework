# This program creates a program that reads a file from the github repository and changes some instances of the text and commits the changes
# Author: Hewa Orang

import requests
import json
import base64
from config import config as cfg

# Configuration
repo_url = 'https://api.github.com/repos/HewaOrang/aprivateone'
filename = 'Names.txt'
apikey = cfg["githubkey"]

# GitHub API headers
headers = {
    'Authorization': f'token {apikey}',
    'Accept': 'application/vnd.github+json'
}

# API endpoint for the file
file_url = f'{repo_url}/contents/{filename}'

print(f"Fetching {filename} from repository...")
response = requests.get(file_url, headers=headers)

if response.status_code == 200:
    file_data = response.json()
    
    # Decode the file content (GitHub returns it base64 encoded)
    file_content = base64.b64decode(file_data['content']).decode('utf-8')
    print(f"\nOriginal content:\n{file_content}")
    
    # Replace all instances of "Andrew" with "Hewa"
    updated_content = file_content.replace('Andrew', 'Hewa')
    print(f"\nUpdated content:\n{updated_content}")
    
    # Encode the updated content back to base64
    encoded_content = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')
    
    # Prepare the commit data
    commit_data = {
        'message': 'Replace Andrew with Hewa',
        'content': encoded_content,
        'sha': file_data['sha'],  # Required for updating existing files
        'committer': {
            'name': 'HewaOrang',
            'email': 'hewaorang@gmail.com'
        }
    }
    
    # Push the changes back to the repository
    print(f"\nCommitting changes...")
    update_response = requests.put(file_url, json=commit_data, headers=headers)
    
    print(f"Commit status: {update_response.status_code}")
    
    if update_response.status_code in [200, 201]:
        print("✓ Successfully committed and pushed changes to the repository!")
        commit_info = update_response.json()
        print(f"  Commit SHA: {commit_info['commit']['sha']}")
        print(f"  Message: {commit_info['commit']['message']}")
    else:
        print("✗ Failed to commit changes")
        print(f"  Error: {update_response.json()}")
        
else:
    print(f"✗ Error fetching file: {response.status_code}")
    print(response.json())
