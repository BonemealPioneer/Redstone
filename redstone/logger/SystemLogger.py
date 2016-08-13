from redstone.logger.SystemLoggerError import SystemLoggerError
import sys, datetime

class SystemLogger(object):

    def __init__(self):
        super(SystemLogger, self).__init__()

    def getTimestamp(self):
        return datetime.datetime.now()

    def log_info(self, message):
        sys.stdout.write('\033[1;32m%s \033[1;33m[NOTIFY]: \033[1;37m%s\n' % ( \
            self.getTimestamp(), message))

    def log_debug(self, message):
        sys.stdout.write('\033[1;32m%s \033[1;34m[DEBUG]: \033[1;37m%s\n' % ( \
            self.getTimestamp(), message))

    def log_warning(self, message):
        sys.stdout.write('\033[1;32m%s \033[1;31m[WARNING]: \033[1;37m%s\n' % ( \
            self.getTimestamp(), message))

    def log_error(self, message):
        raise SystemLoggerError('\033[1;32m%s \033[1;31m[ERROR]: \033[1;37m%s\n' % ( \
            self.getTimestamp(), message))