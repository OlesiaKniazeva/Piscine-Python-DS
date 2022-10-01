import json
import os
import logging
from random import randint
import requests


class Research:
    def __init__(self, path, header):
        logging.debug("Creating class Research")
        self.path = path
        self.header = header

    def check_header(self, head):
        logging.debug("Check if header is right")
        header = head.split(',')
        if len(header) != 2 or header[0] != 'head' or header[1] != 'tail':
            raise Exception("Wrong header")

    def file_reader(self):
        logging.debug("Start to checking if file is right")
        if not os.access(self.path, os.R_OK):
            raise Exception('Couldn\'t read file')
        with open(self.path, 'r') as f:
            data_to_check = f.read().split('\n')
            if len(data_to_check) < 2:
                raise Exception('Wrong data')
            if self.header is True:
                self.check_header(data_to_check[0])
                data_to_check.pop(0)
            result = []
            for line in data_to_check:
                nums = line.split(',')
                res = ''.join(nums)
                if len(nums) != 2 or (res != '01' and res != '10'):
                    raise Exception('Wrong data')
                result.append([int(x) for x in nums])
            return result

    def send_message_to_slack(self, message):
        logging.debug("Sending message to slack")
        webhook = "https://hooks.slack.com/services/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"
        payload = {"text": message}
        requests.post(webhook, json.dumps(payload))

    class Calculations:
        def __init__(self, data):
            logging.debug("Creating class Calculations")
            self.data = data

        def counts(self):
            logging.debug("Count sum of heads and tails")
            head = sum([row[0] for row in self.data])
            tail = sum([row[1] for row in self.data])
            return head, tail

        def fractions(self, head_tail):
            logging.debug("Count fractions of heads and tails")
            s = head_tail[0] + head_tail[1]
            return 100.0 * head_tail[0] / s, 100.0 * head_tail[1] / s

    class Analytics(Calculations):
        def count_random(self, random):
            logging.debug("Calculating random sum of heads and tails")
            head = sum([row[0] for row in random])
            tail = sum([row[1] for row in random])
            return head, tail

        def save_file(self, file_name, message):
            logging.debug("Saving a message in file")
            with open(file_name, 'w') as file:
                file.write(message)

        def predict_random(self, amount):
            logging.debug("Making random list for predictions")
            data = []
            for s in range(amount):
                if randint(0, 1) == 0:
                    data.append([0, 1])
                else:
                    data.append([1, 0])
            return data

        def predict_last(self):
            logging.debug("Return last data for predictions")
            return self.data
