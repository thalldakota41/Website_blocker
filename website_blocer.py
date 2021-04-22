import time
from dateime import dateime as dt

host_temp="hosts"
#host_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.instagram.com","instagram.com","facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt(dt.now() < dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(host_temp,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")
    else:
        with open(host_temp, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun hours...")
    time.sleep(5)