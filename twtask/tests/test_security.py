import pytest

from lib import utils
from lib.logger import log
from lib.utils import is_string_found


def get_test_credentials_info():
    """
    return 4 cases:
    1. correct username and incorrect pass
    2. incorrect username and correct pass
    3. empty username and correct pass
    4. correct username and spacial character
    note: username in the first place and the pass in the second place
    @return: this method return list of tuples that contains username and password to test it with using the pytest
    parametrize
    """
    return [("admin", "ad"), ("ad", "admin"), ("", "admin"), ("admin", ".")]


def helper_for_a_proper_message(username, password, logged_in_condition):
    """
    this method get the username and the password to return the proper string to add it if the test is failed
    @param username: string - username
    @param password: string - password
    @param logged_in_condition: boolean - true that mean logged in
    @return: list of 3 strings
    """
    result = []

    if username == "":
        result.append('empty username')
    else:
        if username == "admin":
            result.append('correct username')
        else:
            result.append('incorrect username')
    if password == ".":
        result.append('password with spacial character')
    else:
        if password == "admin":
            result.append('correct password')
        else:
            result.append('incorrect password')
    result.append('logged in') if logged_in_condition else result.append('not logged in')
    return result


@pytest.mark.security_tests
@pytest.mark.parametrize("test_credentials", get_test_credentials_info())
def test_login_credentials(test_credentials):
    log.info(f"here the test verify some wrong credentials id they can login (username='{test_credentials[0]}', "
             f"password='{test_credentials[1]}')")
    log.info("The test_credentials is starting")
    username = test_credentials[0]
    password = test_credentials[1]
    output = utils.run_web_server_request(1, username, password)
    # regex indicate that logged in - data returned from the request
    logged_in = is_string_found(r"[{.*}]", output)
    # return list of 3 strings - [0] for user [1] for password [2] if logged in
    helper_strings = helper_for_a_proper_message(username, password, logged_in)
    log.info("Verify the login with the credentials - username: '{0}', password: '{1}'".format(username, password))
    if username == "admin" and password == "admin":
        assert logged_in, f"The request has sent but the login is not succeed, " \
                          f"'{helper_strings[0]} ({username})', '{helper_strings[1]} ({password})', '{helper_strings[2]}' "
    else:
        assert not logged_in, f"The request has sent with " \
                              f"'{helper_strings[0]} ({username})' and '{helper_strings[1]} ({password})', so it " \
                              f"shouldn't '{helper_strings[2]}' But it is! "
