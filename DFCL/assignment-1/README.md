# analyzing mail headers
### create .env file with following 

```bash
HOST="<imap server address. for eg. imap.gmail.com>"
EMAIL="<email id>"
PASSWORD="<password>"
```

and run the following commands

```bash
python3 -m venv venv/
source venv/bin/activate
pip3 install -r requirements.txt
python3 mail_headers.py
```