import json
import boto3

endpoint = 'sagemaker-xgboost-2023-03-12-10-54-34-350'
runtime = boto3.client('runtime.sagemaker')
dynamodb = boto3.resource('dynamodb')
table_name = 'cardio_data'

def lambda_handler(event, context):
    
   
    age = event['queryStringParameters']['age']
    gender = event['queryStringParameters']['gender']
    height = event['queryStringParameters']['height']
    weight = event['queryStringParameters']['weight']
    ap_hi = event['queryStringParameters']['ap_hi']
    ap_lo = event['queryStringParameters']['ap_lo']
    cholesterol = event['queryStringParameters']['cholesterol']
    gluc = event['queryStringParameters']['gluc']
    smoke = event['queryStringParameters']['smoke']
    alco = event['queryStringParameters']['alco']
    active = event['queryStringParameters']['active']
    
    
    body =  body = f'{age},{gender},{height},{weight},{ap_hi},{ap_lo},{cholesterol},{gluc},{smoke},{alco},{active}'
    
    
    response = runtime.invoke_endpoint(EndpointName = endpoint, 
                                       ContentType = 'text/csv',
                                       Body = body)
                                       

    
    
    message = 'Your probability of having a cardiovascular disease is equal to'
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': message,
            'prediction': response['Body'].read().decode()
        })
    }
                                


