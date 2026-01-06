import boto3
import zipfile
import os

from src.scripts.settings import Settings


def download_file(bucket_name: str, file_name: str, download_location: str):
    client = boto3.client('s3')
    client.download_file(bucket_name, file_name, download_location)


def unzip_file(file_location: str, extract_to: str):
    with zipfile.ZipFile(file_location, 'r') as zip_ref:
        zip_ref.extractall(extract_to)




if __name__ == "__main__":
    settings = Settings()

    os.makedirs(settings.ARTIFACTS_DIR, exist_ok=True)

    bucket_name = settings.BUCKET_NAME
    file_name = 'model.zip'
    download_location = settings.ARTIFACTS_DIR + "/" + file_name

    download_file(bucket_name, file_name, download_location)

    unzip_file(download_location, settings.ARTIFACTS_DIR)