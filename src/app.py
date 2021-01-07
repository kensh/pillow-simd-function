import boto3
import os

from PIL import Image

# Download the image to /tmp
s3 = boto3.client('s3')
s3.download_file('pillow-function-bucket', 'photo.jpeg', '/tmp/photo.jpeg')

def lambda_handler(event, context):

    for num in range(1000):
        # Open image and perform resize
        image = Image.open('/tmp/photo.jpeg')

        # Select one of the three algorithms
        image = image.resize((256, 128), Image.BILINEAR) 
        # image = image.resize((256, 128), Image.BICUBIC) 
        # image = image.resize((256, 128), Image.LANCZOS) 
        
        # Save and upload to S3
        image.save('/tmp/thumbnail.jpeg', 'JPEG')

    s3.upload_file('/tmp/thumbnail.jpeg', 'pillow-function-bucket', 'thumbnail.jpeg')
    
    return "Success!"