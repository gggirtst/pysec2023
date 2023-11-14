class WiFiLogParser:
    def __init__(self, log_file_path='/var/log/wifi.log'):
        self.log_file_path = log_file_path

    def parse_logs(self):
        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    if 'Error' in line:
                        # Process or print lines that contain 'Error'
                        self.process_error_log(line)

        except FileNotFoundError:
            print(f"Log file not found: {self.log_file_path}")
        except Exception as e:
            print(f"An error occurred while parsing the log file: {str(e)}")


    def process_error_log(self, log_line):
        # You can customize this method to print, save, or process the error lines as needed
        print(log_line.strip())  # Print the error line

    def get_log_file_path(self):
        return self.log_file_path
