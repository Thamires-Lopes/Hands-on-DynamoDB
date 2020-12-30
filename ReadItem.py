import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def get_user(name, occupation, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')

    try:
        response = table.get_item(Key={'name': name, 'occupation': occupation})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    user = get_user("Thamires", "Student")
    if user:
        print("Get user succeeded:")
        pprint(user, sort_dicts=False)
