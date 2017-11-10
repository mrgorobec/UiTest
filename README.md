# TestRepo
**It's Python 3.6 UI tests for Google form.**

Run Tests local on Mac OS:  

* Install ChromeDriver version 2.33:
    > https://chromedriver.storage.googleapis.com/index.html?path=2.33/
    
* Please install Google Chrome version: 62.0.3202.89
    >https://chromereleases.googleblog.com/2017/11/stable-channel-update-for-desktop.html
   
* Install git:
    > brew install git
    
* Next step - install python:
    > brew install python3.6 
    
* Install python virtualenv: 
    > sudo pip install virtualenv
    
* Create virtual environment for mes-backend-automation:
    > virtualenv env

* Activate virtual environment:
    > source env/bin/activate
    
* Clone GitHubAPI repository with ssh ( need configure two factor authorisation and add ssh public key to git hub repository) :
    > git clone git@github.com:nashiluduvsudu/UiTest.git

* Navigate to project folder and install requirements :
    > pip install -r requirements.txt
    
* Run PyTest tests :
    > py.test -v py_test/


