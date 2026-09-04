# import wmi
# import win32file

# def paste_operations_detection():
#     c = wmi.WMI()
#     watcher = c.Win32_VolumeChangeEvent.watch_for()
#     drive_name = None
#     while True:
#         event = watcher()
#         if event.EventType == 2:
#             print(f"drive inserted")
#             drive_name = event.DriveName
#             print(f"drive name:", drive_name)

#     drive_type = win32file.GetDriveType(drive_name)
#     print(f"drive_type:", drive_type)
    
#     if drive_type == "DRIVE_REMOVABLE":
        

# paste_operations_detection()




import psutil
import time

time_var = 1
destn_drives = []
while time_var <= 1:
    print(f"type of psutil.disk_partitions(): {type(psutil.disk_partitions()[0])}")
    for drive in psutil.disk_partitions():
        # if "fixed" in drive["opts"]:
        if drive.opts.split(",")[1] == "fixed":
            print(f"target drive found: {drive}")
            print(f"target drive name: {drive.device}", end = "\n\n\n")
            destn_drives.append(drive.device)
            time.sleep(1)
            time_var += 1

print(f"destn_drives: {destn_drives}")
print(f"type of destn_drives[0]: {type(destn_drives[0])}")

if 