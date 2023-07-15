# AWSLogin
Simple app uses amplify, api gateway, lambda, Dynamodb, IAM services

## Create an app using AWS Amplify

Goto AWS Amplify, New App > Host web app > Deploy without Git provider > Continue. Give the app name and drop the index.zip. It creates new URL for the web app.


## Create a table using AWS DynamoDB

Create a table 'login' with username and password field and insert records. This record will be validated against the web user entry while signing in


## Amazon API Gateway

Use this service to create login API with triggers lambda function to validate the user login

## Create a lambda function

Copy paste the lambda code with the correct role to access dynamodb

