from product import Product
import boto3
import base64


def lambda_handler(event, context):
    """
    AWS Lambda handler
    :param event: the lambda input event
    :param context: the lambda context (in this case unused)
    """
    image_bytes = event["image"]
    # clients init
    s3_client = boto3.client("s3")
    textract = boto3.client("textract")
    dynamo = boto3.client("dynamodb")
    s3_client.put_object(
        Bucket="optieat.images",
        Key="image.png",
        ContentEncoding="base64",
        Body=base64.b64decode(image_bytes)
    )
    db_data = dynamo.scan(
        TableName="OptiEatProducts"
    )
    inventory = []
    for prod in db_data["Items"]:
        inventory.append(Product(prod["ID"]["S"], prod["Description"]["S"], prod["Quantity"]["N"], prod["Quantity Type"]["S"], prod["Expiration"]["N"], prod["Short Name"]["S"]))

    response = textract.analyze_document(
        Document={
            "S3Object": {
                "Bucket": "optieat.images",
                "Name": "image.png"
            }
        },
        FeatureTypes=["TABLES"]
    )

    products = []
    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            for prod in inventory:
                if prod.id in block["Text"]:
                    products.append(prod)

    out = {"Products": []}
    out["Products"].append(p.to_json() for p in products)

    return {
        "statusCode": 200,
        "body": out
    }
