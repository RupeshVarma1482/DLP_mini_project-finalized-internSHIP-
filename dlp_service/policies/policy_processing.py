from dlp_service.policies.prohibited_keyword_policy import check_policy
from dlp_service.pub_sub import Broker
from dlp_service.database import get_client_policy_criteria

def process_policy(file_data):
    subscription = Broker()
    win_user_details = subscription.Subscribe(topic = "USER_LOGIN").get()
    
    policy_criteria = get_client_policy_criteria(user_details["user"])

    return