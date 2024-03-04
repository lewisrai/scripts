pip freeze > requirements.txt
python update_packages.py
pip install -r requirements.txt --upgrade
del requirements.txt
