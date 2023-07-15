#lambda function

import boto3

def lambda_handler(event, context):
    print(event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('login')
    usr = event['username']
    pwd= event['password']
    print(usr,pwd)
    
    response = table.scan()
    items = response['Items']
    for item in items:
        # Process each item as needed
        print(item)
        dynamodb_u =item['username']
        dynamodb_p =item['password']
        if usr == dynamodb_u and pwd == dynamodb_p:
             return {
                    'statusCode': 200,
                    'body': 'Successfully Logged In!'
                }

    return {
        'statusCode': 200,
        'body': 'Login Failed'
    }
