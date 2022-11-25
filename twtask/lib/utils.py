import re
import subprocess


def is_string_found(regex, original_string):
    """
    @param regex: the regex to search for in the original string can be list or string
    @param original_string: the original string to search in
    @return: true if regex has matches in the original string, false otherwise
    """
    if type(regex) is list:
        result: list = []
        for item in regex:
            result.append(bool(re.search(item, original_string)))
        return result
    else:
        return bool(re.search(regex, original_string))


def run_web_server_request(page_index, username, password):
    return subprocess.check_output(
        ['curl', '-s', 'localhost:8000/players?page=' + str(page_index), '-u', username + ':' + password],
        stderr=subprocess.STDOUT, timeout=1200).decode()
