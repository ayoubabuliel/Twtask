# Twtask
Readme file:
In this project, the pytest framework is used to manage automation tests and the pytest-html for generating HTML reports. 
The attached docker file is ready for building:

the project should be in the same folder as the docker file - in the docker file the COPY is used to copy the project to the image under the following path:"/home/twtask"

the web server file is under the web_server folder in the project

in this project, the python version that is used is 3.11

pip is the package manager that used to manage the packages in this project

the folder twtask is the project itself

in this repository attached other files like:  1. test plane  2. test strategy  3. blank reports folder  Steps to run the tests:

build an image from the attached docker file (twtask_dockerfile) e.g from the current folder: “docker build . -f twtask_dockerfile --tag twimage:1.0”


// <image name>= ‘twimage’
// <image tag>=’ 1.0’

to run the tests from the image that was built: run the following command with volume mapping the folder reports: e.g: 
docker run -v <reports folder absolute path>:/home/reports <image name>:<image tag> bin/bash -c "pytest /home/twtask/tests --html=/home/reports/report.html"

#####################################################################################
methods and tests are documented in the project, I used pycharm IDE to write my code :)

![image](https://user-images.githubusercontent.com/10289531/203976056-c016aa0f-c9b2-4f95-94fb-8929c20c73ab.png)
