sudo yum install python3 -y
aws s3 cp s3://piyushbhomalefirstclibucket/FinalScrapper.py FinalScrapper.py
aws s3 cp s3://piyushbhomalefirstclibucket/itemlist.txt itemlist.txt
python3 -m venv my_app/env
source ~/my_app/env/bin/activate
pip install pip --upgrade
pip install boto3
pip install regex
pip install beautifulsoup4
pip install requests
pip install times
python FinalScrapper.py
ls
