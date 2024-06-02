from constants import Constant

def check_validity(value:str, library:list)->bool:
    return value in library
  
def check_region_validity(provider:str, region:str)->bool:
    if provider == Constant.AWS:
        return check_validity(region, Constant.AWS_REGIONS)
    if provider == Constant.GCP:
        return check_validity(region, Constant.GCP_REGIONS)
    if provider in Constant.AZR:
        return check_validity(region, Constant.AZR_REGIONS)

def check_az_validity(provider:str, zone:str)->bool:
    if provider == Constant.AWS:
        return check_validity(zone, Constant.AWS_ZONES)
    if provider == Constant.GCP:
        return check_validity(zone, Constant.GCP_ZONES)
    if provider in Constant.AZR:
        return check_validity(zone, Constant.AZR_ZONES)
    
