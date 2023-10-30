# BlockStakML Assignment

Worked in Ubuntu 22.04 and vscode ipython shell for the ml-script.ipynb . For accessing the rest api used Postman

"""
git clone git@github.com:aqifcse/BlockstakML.git
cd BlockStackML
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
"""

1. The excel file is renamed as bank_data.xlsx. In the root directory there is a file named ml-script.ipynb. Here all the analysis are done and charts are visualized. I have used the .ipynb extension of vscode to code and run analysis script. 

2. Stay in the root directory and open a .env file. copy and paste the text of env_sample.txt file. Save and close it. 

For running the ml-model-output api the following command is to run django local server.

"""
cd BlockStackML
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
"""

There is only one API that takes GET request and "query" as parameter.
"""
GET http://127.0.0.1/api/ml-model-output/?query=dt for Decision Tree output
GET http://127.0.0.1/api/ml-model-output/?query=nb for Naive Bayes output
GET http://127.0.0.1/api/ml-model-output/?query=both for both output
"""

I have checked with Postman.

Thanks!!