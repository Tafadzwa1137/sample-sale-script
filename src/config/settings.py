# src/config/settings.py
import os

AWS_REGION = os.environ.get("AWS_REGION", "eu-west-2")
ITEMS_TABLE_NAME = os.environ["ITEMS_TABLE_NAME"]
IMAGES_BUCKET_NAME = os.environ["IMAGES_BUCKET_NAME"]
BEDROCK_MODEL_ID = os.environ["BEDROCK_MODEL_ID"]
MAX_IMAGE_BYTES = int(os.environ.get("MAX_IMAGE_BYTES", "5000000"))