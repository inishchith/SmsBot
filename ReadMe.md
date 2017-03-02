# SmsBot :calling:

### A Python Package which can be used to send Sms to any Number in India using [Way2Sms](http://site23.way2sms.com/content/index.html).

**Features**
  * Send Up-to 100 Daily Sms.
  * Delivered under 10 seconds .
  * Maximum length 139 characters .
  * You can also send Group SMS to many friends in one go .

**Installation**
* You'll need python3
* Pip is recommended for installing
```
$ pip install SmsBot
```

**Usage**

```python
from Bot import SmsBot
query = SmsBot.sms("username","password") # username is usually Mobile Number (Logging in)
my_message=input("Enter Your Message")
query.send("recipient",my_message) # recipient = receiver's number
query.Logout()
```

**List Of External Packages and their installation**
>BeautifulSoup
```sh
#python3
$ pip3 install BeautiifulSoup4
```
Requests
```sh
$ pip3 install requests
```

**Note-** Do not Misuse .
