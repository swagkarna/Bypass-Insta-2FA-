# 2FAInstagram
## Disclaimer
  This repository is meant for educational purposes only.  
I'm not an expert developer, the code will be improved in futher versions._
## Decripción
Two-factor authentication (2FA) adds an additional layer of protection in authentication systems consisting on the proof that the user shows to be the real user.
This repository aims at demonstrating how the attackers can bypass 2FA for instagram's authentication system. In this case, the two factors are password and a code sent to mobile user._

## Dependencias
- [Apache2](https://www.apache.org/)
- [Python](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)

## How to run

```
git clone https://github.com/afernandezb92/2FAInstagram.git
cd 2FAInstagram
pip install -r requirements.txt
chmod +x run.sh
chmod +x geckodriver
./run.sh
```
All the codes will be saved in codes.txt file . You must delete code.txt file for capturing new users.
You can use Ngrok to use outside the wan. Type this command on your terminal 
./ngrok http 80

````
rm /var/www/html/instagram/code.txt
```
The attacker using hacking techniques (dnsspoofing, social engineering, etc.) redirect the victim with 2FA active in instagram to fake instagram web. Once the victim logs in the fake web, the attacker's machine will run a web browser and it will go to original instagram to log in with victim's credentials. This will cause instagram send the validation code to the victim. When the victim receives the code, he will put it in the fake web. The attacker will get the code and will complete the log in the original instagram web, gaining the access to the victim account._

## POC
![alt text](https://i.imgur.com/hfkIwyO.gif). Special Thanks to Alejandro Fernandez



