# import win32serviceutil
# import win32service
# import win32event

# class MyService(win32serviceutil.ServiceFramework):
#     _svc_name_ = "MyService"
#     _svc_display_name_ = "My Service"
    
#     def __init__(self, args):
#         super().__init__(args)
#         self.stop_event = win32event.CreateEvent(None, 0, 0, None)

#     def SvcDoRun(self):
#         import main
#         main.main()

#     def SvcStop(self):
#         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
#         self.ReportServiceStatus(win32service.stop_event)
#         self.ReportServiceStatus(win32service.SERVICE_STOPPED)

# if __name__ == "__main__":
#     win32serviceutil.HandleCommandLine(MyService)




































# import win32service # for accessing windows services
# import win32serviceutil # helpers to communicate with windows
# import win32event # takes care of creating the events

# class MyService(win32serviceutil.ServiceFramework):
#     _svc_display_name_ = "My Service"
#     _svc_name_ = "MyService"
#     def __init__(self, args):
#         super().__init__(args)
#         self.stop_event = win32event.CreateEvent(None, 0, 0, None)
#     def SvcDoRun(self, args):
#         import main
#         main.main()
#     def SvcStop(self, args):
#         self.ReportServiceStatus(SERVICE_STOP_PENDING)
#         self.ReportServiceStatus(event_stop)
#         self.ReportServiceStatus(SERVICE_STOPPED)


# if __name__ == "__main__":
#     win32serviceutil.HandleCommandLine(MyService)






















































import win32service
import win32serviceutil
import win32event
from dlp_service.user_session import user_info
from dlp_service.pub_sub import broker

# import main from "./user_session.py"
# import Broker from "./pub_sub.py"

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyService"
    _svc_display_name_ = "My Service"
    def __init__(self, args):
        super().__init__(args)
        self.event_stop = win32event.CreateEvent(None, 0, 0, None)
        self.user_data = null
        self._register_service_notifications()
    def SvcDoRun(self, args):
        import main
        main.mainFunc(self.event_stop)
        # win32event.WaitForSingleObject(self.event_stop, win32event.INFINITE)
        # print(f"stop requested by run")
    def SvcOtherEx(self, control, event_type, data):
        if control == win32service.SERVICE_CONTROL_SESSIONCHANGE:
            print(f"session change detected by windows")
            if event_type == win32service.WTS_SESSION_LOGON:
                print(f"a user logged in")
                session_id = data
                self.user_data = user_info(session_id)
                
                broker.Publish(
                    topic = "USER_LOGIN",
                    # message = self.user_data
                    message = self.user_data
                )
            elif event_type == win32service.WTS_SESSION_LOGOFF:
                print(f"a user logged out")
                
                broker.publish(
                    topic = "USER_LOGOUT",
                    message = self.user_data
                )
    def SvcStop(self):
        print(f"stopping the service")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.event_stop)
        # self.ReportServiceStatus(win32service.SERVICE_STOPPED)

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(MyService)