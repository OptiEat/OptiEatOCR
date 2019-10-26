import json
import boto3
import base64

def lambda_handler(event, context):
    imageBytes = event['image']
    s3Client = boto3.client('s3')
    s3Client.put_object(
        Bucket='optieat.images',
        Key='image.png',
        ContentEncoding='base64',
        Body=base64.b64decode(imageBytes)
    );
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': 'optieat.images',
                'Name': 'image.png'
            }
        }
    )
    print(response)
    return {
        'statusCode': 200,
        'body': response
    }