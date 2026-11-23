# src/handlers/analyse_item.py
import json
import boto3
from services.s3_service import get_image_bytes
from services.bedrock_service import analyse_image
from services.dynamodb_service import save_analysis

def handler(event, context):
    body = json.loads(event["Records"][0]["body"])
    item_id = body["itemId"]
    user_id = body["userId"]
    image_key = body["imageKey"]

    image = get_image_bytes(image_key)
    analysis = analyse_image(image, body.get("productText"))

    save_analysis(
        user_id=user_id,
        item_id=item_id,
        analysis=analysis.model_dump(),
        status="complete"
    )

    return {"statusCode": 200}