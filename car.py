#!/usr/bin/python3
import random
import time
import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class Car:
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        self.table = None

    def add_car(self, number, owner, speed, km):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('cars')
        table.put_item(
            Item={
                'car number': number,
                'owner name': owner,
                'speed': speed,
                'milage': km
            })
    def find_car(self, number):
        response = self.table.query(
            KeyConditionExpression=Key('car number').eq('johndoe')
        )
        items = response['Items']
        print(items)


