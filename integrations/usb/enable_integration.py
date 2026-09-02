def usb_integration(db_details):
    if db_details["query_match_count"] > 1:
        print(f"duplicate users identified")
        return
    if db_details["policy_criteria"] == "waive":
        stop_api_server()
        return
    elif db_details["policy_criteria"] == "apply":
        # logic to start server
        start_api_server(db_details)