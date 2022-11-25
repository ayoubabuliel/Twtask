import subprocess
import time

import pytest
import os
from pathlib import Path
import platform


@pytest.fixture(scope="session", autouse=True)
def before_all_the_tests():
    if platform.system() != "Linux":
        raise Exception("you can't up the web server on this os, the executable file run only on 'Linux' os")
    project_directory_path = os.getcwd()
    web_server_tw_task_dir = os.path.join(str(Path(__file__).parent), "web_server")
    os.chdir(web_server_tw_task_dir)
    subprocess.Popen(["./twtask"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(10)
    os.chdir(project_directory_path)
