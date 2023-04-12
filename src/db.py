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
        # TODO handle case where the key is not found
        # TODO handle connection issues
        # TODO add connection timeout
        # TODO handle non-200 response
        response = self.table.get_item(Key={
            "shortURL": key
        })

        item = response['Item']
        url = item['longURL']
        return url

    def put(self, key, value):
        # TODO handle repeat key entry

        response = self.table.put_item(Item={
            "shortURL": key,
            "longURL": value,
        }, Expected={
            key: {
                'Exists': False
            }
        })

        return response
