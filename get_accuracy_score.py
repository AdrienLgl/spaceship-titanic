import os
import json
import requests

# Retrieve Kaggle username and token from GitHub environment variables
kaggle_username = os.environ.get('KAGGLE_USERNAME')
kaggle_token = os.environ.get('KAGGLE_TOKEN')

# Set the competition slug and submission filename
competition_slug = 'spaceship-titanic'
submission_filename = 'sample_submission.csv'

# Set the Kaggle API base URL
base_url = 'https://www.kaggle.com/api/v1'

# Authenticate with Kaggle API
auth_headers = {
    'Authorization': f'Bearer {kaggle_token}',
}

# Get the competition ID
competition_url = f'{base_url}/competitions/list'
response = requests.get(competition_url, headers=auth_headers)
competitions = response.json()
competition_id = next((c['id'] for c in competitions if c['slug'] == competition_slug), None)

if competition_id is None:
    print('Competition not found.')
    exit()

# Get the submissions for the competition
submissions_url = f'{base_url}/competitions/{competition_id}/submissions'
response = requests.get(submissions_url, headers=auth_headers)
submissions = response.json()

# Find your submission and get the accuracy score
your_submission = next((s for s in submissions if s['fileName'] == submission_filename), None)

if your_submission is None:
    print('Submission not found.')
    exit()

accuracy = your_submission['publicScore']
print(f'Accuracy score: {accuracy}')

# Save the accuracy score as a GitHub environment variable
os.environ['ACCURACY_SCORE'] = str(accuracy)

# Update the README badge with the accuracy score
readme_file = 'README.md'
badge_url = 'https://img.shields.io/badge/accuracy-{accuracy}-brightgreen'

with open(readme_file, 'r') as f:
    readme_content = f.read()

updated_readme_content = readme_content.replace('https://img.shields.io/badge/accuracy-', badge_url)
with open(readme_file, 'w') as f:
    f.write(updated_readme_content)