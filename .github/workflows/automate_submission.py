import os
import shutil

# Retrieve Kaggle username and token from GitHub variables
kaggle_username = os.environ.get('KAGGLE_USERNAME')
kaggle_token = os.environ.get('KAGGLE_TOKEN')

files = os.listdir(os.curdir)
print(files)

# Install Kaggle CLI
os.system('pip install kaggle')

# Authenticate Kaggle CLI
os.system(f'kaggle config set -n username -v {kaggle_username}')
os.system(f'kaggle config set -n key -v {kaggle_token}')

# Copy sample_submission.csv from your GitHub repository
shutil.copy('samples/sample_submission.csv', 'sample_submission.csv')

# Submit the output file
# Replace the following line with the command to submit your output file to the Kaggle competition
os.system('kaggle competitions submit -c spaceship-titanic -f sample_submission.csv -m "Auto submission"')

# Cleanup files
os.remove('sample_submission.csv')
