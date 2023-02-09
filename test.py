import zipfile
import os

def extract_all_files(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()
    for root, dirs, files in os.walk(os.path.splitext(zip_file)[0]):
        for file in files:
            print(os.path.join(root, file))

zip_file = '/home/vinay/vinay_code/sia/test.zip'
extract_all_files(zip_file)