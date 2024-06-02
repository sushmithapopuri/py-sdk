from enum import Enum

class Constant(Enum):
    
    AWS = 'aws'
    GCP = 'gcp'
    AZR = 'azr'

    AWS_REGIONS = []
    GCP_REGIONS = []
    AZR_REGIONS = []

    AWS_ZONES = []
    GCP_ZONES = []
    AZR_ZONES = []