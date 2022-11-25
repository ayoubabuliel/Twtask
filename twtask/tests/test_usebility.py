import pytest

from lib import utils
from lib.logger import log
from lib.utils import is_string_found


def get_test_verify_error_message_info():
    """
    here we tell wrong page index
    """
    return [0, -1]


@pytest.mark.usebility_test
@pytest.mark.parametrize("page_index", get_test_verify_error_message_info())
def test_verify_error_message(page_index):
    """
    here we send a wrong request with wrong page index and see if the error message is understood
    """
    log.info(f"here we send a wrong request with wrong page index ('{page_index}'), and see if "
             f"the error message is understood")
    log.info("The verify_error_message test is starting")
    log.info("send the request with page=0 and with right username and password")
    output = utils.run_web_server_request(page_index, "admin", "admin")
    is_error_message_exist = is_string_found(r"I am a teapot", output)
    assert not is_error_message_exist, f"the response of the request with page=0 is: {output}, " \
                                       f"and this message isn't " \
                                       f"understood! "
