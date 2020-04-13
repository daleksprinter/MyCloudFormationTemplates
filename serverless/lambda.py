import boto3

dynamo = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = 'User'
    user_table = dynamo.Table(table_name)
    res = user_table.scan()
    item = res["Items"]
    return item
