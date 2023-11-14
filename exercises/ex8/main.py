from WiFiLogParser import WiFiLogParser


wifilogparser = WiFiLogParser()
log_file_path = wifilogparser.get_log_file_path()
print(f"Log file path: {log_file_path}")

wifilogparser.parse_logs()

