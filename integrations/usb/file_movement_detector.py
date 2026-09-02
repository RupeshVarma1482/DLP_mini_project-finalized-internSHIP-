import wmi
import win32file

def paste_operations_detection():
    c = wmi.WMI()
    watcher = c.Win32_VolumeChangeEvent.watch_for()
    drive_name = None
    while True:
        event = watcher()
        if event.EventType == 2:
            print(f"drive inserted")
            drive_name = event.DriveName
            print(f"drive name:", drive_name)

    drive_type = win32file.GetDriveType(drive_name)
    print(f"drive_type:", drive_type)
    
    if drive_type == "DRIVE_REMOVABLE":
        

paste_operations_detection()