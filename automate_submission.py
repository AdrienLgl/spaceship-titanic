import os
import shutil
import json

# Retrieve Kaggle username and token from GitHub variables
kaggle_username = os.environ.get('KAGGLE_USERNAME')
kaggle_token = os.environ.get('KAGGLE_TOKEN')


print('Kaggle credentials:')
print(f'Username: {kaggle_username}')
print(f'Token: {kaggle_token}')

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

os.system('kaggle competitions submissions -c spaceship-titanic > score.txt')

f = open("score.txt")
contents = f.read()
f.close()
offsetStart = str.find(contents, 'mmddyyyy-n.csv')
score = contents[offsetStart+123:offsetStart+130]

# Cleanup files
os.remove('sample_submission.csv')
os.remove('score.txt')

print(f'Accuracy score: {score}')

# Save the accuracy score as a GitHub environment variable
os.environ['ACCURACY_SCORE'] = str(score)

# Update the README badge with the accuracy score
readme_file = 'README.md'
badge_url = 'https://img.shields.io/badge/accuracy-{accuracy}-brightgreen'

with open(readme_file, 'r') as f:
    readme_content = f.read()

updated_readme_content = readme_content.replace('https://img.shields.io/badge/accuracy-', badge_url)
with open(readme_file, 'w') as f:
    f.write(updated_readme_content)
