class SysLogParser(object):
    log_file_path = '/var/log/system.log'

    def info(self):
        print("This is syslog parser!")

    def getLogFilePath(self):
        return self.log_file_path