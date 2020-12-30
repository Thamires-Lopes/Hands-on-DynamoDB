from decimal import Decimal
from pprint import pprint
import boto3


def update_user(name, occupation, hobby, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')

    response = table.update_item(
        Key={
            'name': name,
            'occupation': occupation
        },
        UpdateExpression="set hobby=:h",
        ExpressionAttributeValues={
            ':h': hobby
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_user("Thamires", "Student", "Read books")
    print("Update user succeeded:")
    pprint(update_response, sort_dicts=False)
