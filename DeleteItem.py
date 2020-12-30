from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_user(name, occupation, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')

    try:
        response = table.delete_item(
            Key={
                'name': name,
                'occupation': occupation
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


if __name__ == '__main__':
    delete_response = delete_user("Thamires", "Student")
    if delete_response:
        print("Delete user succeeded:")
        pprint(delete_response, sort_dicts=False)
