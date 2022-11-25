import json

import pytest
from lib.logger import log
from lib import utils


def get_test_prohibited_names_info():
    """
    return 2 cases:
    1. player with empty username
    2. player with null username
    note: username in the first place and page in the second place and description case in the third place
    @return: this method return list of triples that contains username and page number and description case to the test
    parametrize
    """
    return [("", 2, "empty username"), ("null", 17, "null username")]


@pytest.mark.functionality_test
@pytest.mark.parametrize("test_prohibited_names", get_test_prohibited_names_info())
def test_verify_no_prohibited_usernames(test_prohibited_names):
    f"""
    here we send a request with page_index={test_prohibited_names[1]} 
    and see if there is an {test_prohibited_names[2]} 
    """
    log.info(
        f"here we send a request with page={test_prohibited_names[1]} "
        f"and see if there is an {test_prohibited_names[2]}")
    log.info("The test_prohibited_names test is starting")
    log.info(f"send the request with page={test_prohibited_names[1]} "
             f"and with right username and password")
    output = utils.run_web_server_request(test_prohibited_names[1], "admin", "admin")
    output_list = json.loads(output)
    prohibited_name_id = ""
    for json_object in output_list:
        if json_object["Name"] == test_prohibited_names[0]:
            prohibited_name_id = json_object["ID"]
            break
    is_prohibited_name_exist = prohibited_name_id == ""
    assert is_prohibited_name_exist, f"The player of ID '{prohibited_name_id} " \
                                     f"has an {test_prohibited_names[2]}! "


def get_test_verify_id_is_uniq_info():
    """
    here we tell the page indexes of 2 pages that we want to verify if they have uniq players ids
    """
    return [(1, 18)]


@pytest.mark.functionality_test
@pytest.mark.parametrize("test_verify_id_is_uniq_info", get_test_verify_id_is_uniq_info())
def test_verify_id_is_uniq(test_verify_id_is_uniq_info):
    """
    here we verify if two pages have an ID with different players usernames
    """

    log.info(
        f"here we verify if two pages ({test_verify_id_is_uniq_info[0]}, "
        f"{test_verify_id_is_uniq_info[1]}) have an ID with different players usernames")
    log.info("The test_verify_id_is_uniq test is starting")
    log.info(f"get the players of page index {test_verify_id_is_uniq_info[0]}")
    output_page1_list = json.loads(
        utils.run_web_server_request(test_verify_id_is_uniq_info[0], "admin", "admin"))
    log.info(f"get the players of page index {test_verify_id_is_uniq_info[1]}")
    output_page2_list = json.loads(
        utils.run_web_server_request(test_verify_id_is_uniq_info[1], "admin", "admin"))
    for json_object_1 in output_page1_list:
        json_object_2 = next(filter(lambda x: (x["ID"] == json_object_1["ID"]), output_page2_list))
        if json_object_2:
            log.info(
                f"in page {test_verify_id_is_uniq_info[0]} "
                f"the username of id {json_object_1['ID']} is {json_object_1['Name']}"
                f" and in page {test_verify_id_is_uniq_info[1]} "
                f"the username same id is {json_object_2['Name']}")
            assert (json_object_1["Name"] == json_object_2["Name"]), \
                f"The username of ID {json_object_1['ID']} " \
                f"in page {test_verify_id_is_uniq_info[0]} is {json_object_2['Name']} " \
                f"but username of the same id in page " \
                f"{test_verify_id_is_uniq_info[1]} is {json_object_1['Name']} "
