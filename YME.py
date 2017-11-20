import json
import requests
import random
import string
import threading

def run(threadName):
    while True:
        s = requests.session()
        if gmail:
            email = base_email
            email = email.split("@")
            email = str(str(email[0]) + "+" + str(random.randint(1,9999999999)) + "@" + str(email[1]))
        if not gmail:
            char_set = string.ascii_uppercase + string.digits
            randomstring = str(''.join(random.sample(char_set * 6, 6)))
            email = str(random.randint(1, 99999999)) + str(random.getrandbits(128)) + str(
                random.randint(1, 99999999)) + str(randomstring) + str(base_email)

        postDict["email"] = email
        try:
            post = s.get(postURL, headers=headers, params=postDict)
            if post.status_code != 200:
                print("Web Error Code: " +str(post.status_code))
            else:
                success.append(1)
            print(str(threadName) + "\tTotal Entered: |" +str(len(success)) + "|\t\tEmail: " +str(email))
        except:
            pass




def setDict():
    global headers
    global postDict
    postDict["SleeknoteId"] = "f85d95e8-52b8-4b06-a717-9cbebad1593e"  # do not change this!
    postDict["CustomerId"] = "3096"  # do not change this!
    postDict["UserAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    postDict["SignupPage"] = "https://www.ymeuniverse.com/en/blog/2017/11/15/yeezy-boost-350-v2-semi-frozen-yellow/"
    postDict["name"] = name + " " # do not change this!
    postDict["input-1"] = size # do not change this!
    postDict["input-2"] = city # do not change this!


    headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch, br",
	"Accept-Language":"en-GB,en-US;q=0.8,en;q=0.6",
	"Cache-Control":"no-cache",
	"Connection":"keep-alive",
	"Host":"mailchimp.sleeknote.com",
	"Pragma":"no-cache",
	"Referer":"http://sleeknotestaticcontent.sleeknote.com/editorv2/desktoptoggler/f85d95e8-52b8-4b06-a717-9cbebad1593e.html",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    }

if __name__ == "__main__":
    success = []
    raffleURL = "https://www.ymeuniverse.com/en/blog/2017/11/15/yeezy-boost-350-v2-semi-frozen-yellow/"
    postURL = "https://mailchimp.sleeknote.com/"
    postDict = {}
    headers = {}
    firstRun = True
    with open("config.json") as f:
        configfile = json.load(f)["setup"]
    name = configfile["name"]
    size = configfile["input-1"]
    city = configfile["input-2"]
    while True:
        while firstRun:
            gmailQ = input("Gmail mode or domain mode? (G/D):\t").upper()
            while gmailQ != "D" and gmailQ != "G":
                print("\n\nEnter G or D!")
                gmailQ = input("Gmail mode or domain mode? (G/D):\t").upper()
            if gmailQ == "G":
                gmail = True
                base_email = configfile["gmail"]["my_gmail"]
            elif gmailQ == "D":
                gmail = False
                base_email = configfile["my_domain"]["my_domain"]
            firstRun = False
        setDict()  # set our dictionaries
        try:
            entries = int(input("How many threads do you want ?:  (-1 to go back, 20 max advised)\t"))
            if entries == -1:
                firstRun = True
            for i in range(entries):
                t = threading.Thread(target=run, args=("Thread- " + str(i + 1),))
                t.start()
            t.join()
        except ValueError:
            pass
