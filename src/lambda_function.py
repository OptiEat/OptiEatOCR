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
    textract = boto3.client('textract')
    response = textract.analyze_document(
        Document={
            'S3Object': {
                'Bucket': 'optieat.images',
                'Name': 'image.png'
            }
        },
        FeatureTypes=['TABLES']
    )
    lines = []
    print(response)
    for textDet in response['Blocks']:
        if textDet['BlockType'] == 'LINE':
            lines.append(textDet['Text'])
    return {
        'statusCode': 200,
        'body': lines
    }