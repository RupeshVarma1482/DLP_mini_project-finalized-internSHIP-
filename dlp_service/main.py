# import time
# import win32event
# # import roundcube_svc from "./services/roundcube.py"

# def mainFunc(event):
#     try:
#         while True:
#             with open("service_test.txt", "a") as file:
#                 file.write("service is running\n")

#             result = win32event.WaitForSingleObject(event, 2000)
#             if result == win32event.WAIT_OBJECT_0:
#                 print(f"windows requested to stop the event")
#                 break
#             # raise Exception("test error")
#             elif result == win32event.WAIT_TIMEOUT:
#                 print(f"windows did not request to stop so carrying on with the next iteration")
#     except Exception as error:
#         win32event.SetEvent(event)
#         print(f"error occured so manually requesting windows to stop the service | error being : {error}")

# if __name__ == "__main__":
#     main()












# import time
# import win32event
# # import Broker from "./pub_sub.py"
# from dlp_service.pub_sub import Broker
# # import main from "./user_session.py"
# from dlp_service.user_session import user_info
# from dlp_service.database import get_client_policy_criteria
# # from services.roundcube import roundcube_service

# def mainFunc(event):
#     try:
#         subscription = Broker()
#         user_data = subscription.Subscribe(topic = "USER_LOGIN").get()

#         print(f"user_data available on main.py as a subscription : {user_data}")

#         target_user_policy_details = get_client_policy_criteria(user_data)
#         print(f"user's policy from database : {target_user_policy_details}")

#         if target_user_policy_details["query_match_count"] == 1:
#             print(f"no duplicates of target user | no. of target users found: {target_user_policy_details["query_match_count"]}")
            
#         else:
#             print(f"duplicate records of target user exist in the db")
         
         




#         result = win32event.WaitForSingleObject(event, 1000)
#         if result == win32event.WAIT_TIMEOUT:
#             print(f"windows did not request for a halt during the time out perioud")
#         elif result == win32event.WAIT_OBJECT_0:
#             print(f"windows requested for a halt...")
#     except Exception as err:
#         print(f"there seems to be an exception while executing the main.py file")
        
# if __name__ == "__main__":
#     mainFunc(event)
    



  














import time
import win32ts
import win32event
from dlp_service.pub_sub import broker
from dlp_service.user_session import user_info, is_admin
from dlp_service.policies.policy_processing import process_policy
from dlp_service.database import get_client_policy_criteria
from dlp_service.api_manager import start_api_server, stop_api_server
# from integrations.usb.file_movement_detector import paste_operations_detection

def handle_user_login(user_info):
    user_name, user_sid = user_info
    if is_admin():
        print(f"current logged in user contains admin group")
        print(f"proceeding to disable DLP service...")
        return
    print(f"current logged in user does NOT contain admin group")
    print(f"proceeding to enable DLP service...")

    db_details = get_client_policy_criteria(user_sid)
    # policy_criteria = db_details["policy_criteria"]
    start_integrations(db_details)
    
    # process_policy()
    pass

def handle_user_logoff(user_info):
    user_name, user_sid = user_info
    stop_api_server()

def mainFunc(event):
    try:
        broker.subscribe(
            topic = "USER_LOGIN",
            callback = handle_user_login
        )
        
        broker.subscribe(
            topic = "USER_LOGOUT",
            callback = handle_user_logoff
        )

        while True:
            result = win32event.WaitForSingleObject(event, 1000)
            if result == win32event.WAIT_TIMEOUT:
                print(f"MAIN did not recieve any halt message from windows.")
                continue
            elif result == win32event.WAIT_OBJECt_0:
                print(f"MAIN recieved HALT message from windows... proceeding to stop MAIN")
                break
    except Exception as error:
        print(f"there was an issue: {error}")