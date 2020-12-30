import boto3
from pprint import pprint


def put_user(name, occupation, hobby, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')
    response = table.put_item(
        Item={
            'name': name,
            'occupation': occupation,
            'hobby': hobby
        }
    )
    return response


if __name__ == '__main__':
    user_resp = put_user("Thamires", "Student", "games")
    print("Put user succeeded:")
    pprint(user_resp, sort_dicts=False)
