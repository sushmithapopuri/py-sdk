from storage import Storage
from common import util

from common import validation as validator
from common.constants import Constant
import boto3
import json

class AWS_Storage(Storage) :

    def check_mandatory_param(cnfg:json, type: str) -> bool:
        try:
            if type == 'block':
                validator.check_az_validity(Constant.AWS,cnfg['AvailabilityZone'])
        except Exception as e:
            print(e)
        return True

    def parse_cnfg(cnfg:json):
        try:
            json.loads(cnfg)
        except Exception:
            print('Please provide a valid configuration')

    def create_block_storage(cnfg:json, output: bool = True):

        client = boto3.client('ec2')
        response = client.create_volume(cnfg)
        if output:
            util.write_output(response)


    def create_file_storage():
        pass

    def create_object_storage():
        pass
