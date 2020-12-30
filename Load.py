import boto3


def load_users(users, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')
    for user in users:

        name = str(user['name'])
        occupation = str(user['occupation'])
        print("Adding user:", name, occupation)
        table.put_item(Item=user)


if __name__ == '__main__':
    user1 = {
        "name": "Paulo",
        "occupation": "Teacher"
    }
    user2 = {
        "name": "Ana",
        "occupation": "Mobile developer"
    }
    users_list = [user1, user2]
    load_users(users_list)
