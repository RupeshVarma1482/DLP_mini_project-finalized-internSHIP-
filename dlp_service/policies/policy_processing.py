from dlp_service.policies.prohibited_keyword_policy import check_policy
from dlp_service.pub_sub import Broker
from dlp_service.database import get_client_policy_criteria

def process_policy(metadata, content):
    return check_policy(metadata, content)