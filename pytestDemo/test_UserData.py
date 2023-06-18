from logging import Logger

import pytest

import test_logs
Logs = test_logs.Logs

#import test_logs

#logs = test_logs.Logs()
#log = logs.test_loggingDemo()

#from test_logs import Logs

#log = Logs.test_loggingDemo()

@pytest.mark.usefixtures("data")
class Test(Logs):
    def test_createUser(self, data):
        log = self.test_loggingDemo()
        for dat in data:
            log.info(dat)
