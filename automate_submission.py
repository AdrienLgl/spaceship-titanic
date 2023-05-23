import os
import shutil
import json

# Retrieve Kaggle username and token from GitHub variables
kaggle_username = os.environ.get('KAGGLE_USERNAME')
kaggle_token = os.environ.get('KAGGLE_TOKEN')

# Set Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = kaggle_username
os.environ['KAGGLE_KEY'] = kaggle_token

files = os.listdir(os.curdir)
print(files)

# Install Kaggle CLI
os.system('pip install kaggle')

# Define the path to the .kaggle directory
kaggle_dir = os.path.expanduser('~/.kaggle')

# Create the .kaggle directory if it doesn't exist
os.makedirs(kaggle_dir, exist_ok=True)

# Define the path to the kaggle.json file
kaggle_json_path = os.path.join(kaggle_dir, 'kaggle.json')

# Create a dictionary with the Kaggle credentials
kaggle_credentials = {
    'username': kaggle_username,
    'key': kaggle_token
}

# Save the Kaggle credentials to the kaggle.json file
with open(kaggle_json_path, 'w') as f:
    json.dump(kaggle_credentials, f)

# Set the appropriate permissions for the kaggle.json file
os.chmod(kaggle_json_path, 0o600)

# Copy sample_submission.csv from your GitHub repository
shutil.copy('samples/sample_submission.csv', 'sample_submission.csv')

# Submit the output file
# Replace the following line with the command to submit your output file to the Kaggle competition
os.system('kaggle competitions submit -c spaceship-titanic -f sample_submission.csv -m "Auto submission"')

# Cleanup files
os.remove('sample_submission.csv')
