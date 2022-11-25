import sys
import threading
from datetime import datetime
import pytest
from lib import utils
from lib.logger import log
from lib.utils import is_string_found


def get_test_verify_time_performance_info():
    """
    here we tell page index that we want to verify time performance
    """
    return [7, 8]


def get_test_stress_performance():
    """
    here we tell page indexes that we want to stress the server performance
    """
    return [([1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 7, 102,
              24, 25, 26])]


class ReturnValueThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    def run(self):
        if self._target is None:
            return  # could alternatively raise an exception, depends on the use case
        try:
            self.result = self._target(*self._args, **self._kwargs)
        except Exception as exc:
            print(f'{type(exc).__name__}: {exc}', file=sys.stderr)  # properly handle the exception

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self.result


@pytest.mark.all_tests
@pytest.mark.parametrize("test_verify_time_performance_info", get_test_verify_time_performance_info())
def test_verify_time_performance(test_verify_time_performance_info):
    """
    here we send the request with page index and see if the time performance not more than 1 second
    """
    log.info("here we send the request with page index and see if the time performance not more than 1 second")
    log.info("The verify_time_performance test is starting")
    log.info(f"send the request with page={test_verify_time_performance_info} and with right username and password")
    start_time = datetime.now()
    log.info(f"the time before the sending request is {str(start_time)}")
    utils.run_web_server_request(test_verify_time_performance_info, "admin", "admin")
    end_time = datetime.now()
    log.info(f"the time after the sending request is {str(end_time)}")
    total_period = (end_time - start_time).total_seconds()
    log.info(f"the duration time of the request is {str(total_period)}")
    assert total_period < 1, f"the total period of the request is {str(total_period)}, and i is more than 1 second"


@pytest.mark.all_tests
@pytest.mark.parametrize("test_test_stress_performance_info", get_test_stress_performance())
def test_stress_performance(test_test_stress_performance_info):
    threads = list()
    outputs = list()
    for i in test_test_stress_performance_info:
        threads.append(ReturnValueThread(target=utils.run_web_server_request, args=(i, "admin", "admin")))
    for i in threads:
        i.start()
    for i in threads:
        outputs.append(
            "page index =" + str(test_test_stress_performance_info[threads.index(i)]) + "\n" + str(i.join()))
    log.info(f"my outputs are {str(outputs)}")
    for i in outputs:
        is_like_json_file = is_string_found(r"[{.*}]", i.split("\n")[1])
        if not is_like_json_file:
            assert is_like_json_file, "After number of requests, The output of response of " + \
                                      i.split("\n")[0] + " isn't like json file,\n The actual response is\n" + \
                                      i.split("\n")[1]
