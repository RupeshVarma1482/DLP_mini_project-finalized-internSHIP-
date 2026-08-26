import win32ts
import win32security
import win32net

def helper(session, arg_name):
    return win32ts.WTSQuerySessionInformation(
        Server = win32ts.WTS_CURRENT_SERVER_NAME,
        # SessionId = win32ts.WTSGetActiveConsoleSessionId(),
        SessionId = session,
        WTSInfoClass = arg_name
    )

def user_info(session_id):
    client_data_target = {
                    "current_user": win32ts.WTSUserName,
                    "application_name": win32ts.WTSApplicationName,
                    "clirent_directory": win32ts.WTSClientDirectory,
                    "domain_name": win32ts.WTSDomainName,
                    "initial_program": win32ts.WTSInitialProgram,
                    "working_directory": win32ts.WTSWorkingDirectory,
                    "client_protocol_type": win32ts.WTSClientProtocolType,
                    "client_display": win32ts.WTSClientDisplay,
                    "client_address": win32ts.WTSClientAddress
                }
    
    client_data_actual = {}

    print(f"the client details are:")
    counter = 1
    for key, value in client_data_target.items():
        data = helper(session = session_id, arg_name = value)
        client_data_actual[key] = data
        # print(f"iteration number {counter}")
        print(f"{key} : {data}")
        counter += 1
    print(f"current_user: {client_data_actual["current_user"]}")
    print(f"current_user_domain_name: {client_data_actual["domain_name"]}")
    return client_data_actual["current_user"]
    
