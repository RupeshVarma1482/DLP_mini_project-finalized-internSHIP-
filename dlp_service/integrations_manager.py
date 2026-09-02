from integrations.gmail.enable_integration import gmail_integration
from integrations.usb.enable_integration import usb_integration
from integtations.usb.enable_integration import roundcube_integration

def start_integrations(db_details):
    gmail_integration(db_details)
    usb_integration(db_details)
    roundcube_integration(db_details)