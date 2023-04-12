import boto3


class DBConfig:
    def __init__(self, config):
        self.table_name = config['table_name']


class DB(object):

    def __init__(self, config):
        self.config = config
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(config.table_name)

    def get(self, key):
        response = self.table.get_item(Key={
            "shortURL": {"S": "xyz"}
        })
        item = response['Item']
        return item

    def put(self, key, value):
        response = self.table.put_item(Item={
            key: value
        }, Expected={
            key: {
                'Exists': False
            }
        })
        return response
