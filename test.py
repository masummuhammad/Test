import requests
import base64
import random
import time
import proxyReader
import urllib3
from capmonster_python import ImageToTextTask
urllib3.disable_warnings()

user_agents = [
    # Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    # Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    # Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    # Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
]


 
def get_random_user_agent():
    return random.choice(user_agents)



def get_new_token(email,password):
    captcha_url = "https://ticketingweb.passo.com.tr/api/passoweb/getcaptcha"
    captcha_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer DHZHUMUdA8HUDTlgRWfY+lZQcha0OceuLSq44jFUUy8t5MjZ+bOyoxNfseZkWjUP/Vn2HJ5cLnfbhwPYvB/qZ7XnWMyVn8gTz5YeteZ+dUwxXXAV8uAKAKx7yC3GVusBpThRJJo2A4OqlZ2SEuxmI+wp8yNQwYPpRDzLAJSxuB0=",
    "CurrentCulture": "en-US",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": get_random_user_agent()}
    requests.get("https://www.passo.com.tr/TSPD/?type=22")
    time.sleep(1)
    res_data=requests.post(captcha_url, proxies=proxyReader.retriveProxy(),headers=captcha_headers,json={},verify=False).json()
    captcha_input=''
    guid=''
    if not res_data['isError']:
        if res_data['value']['isCaptcha']:
            guid=res_data['value']['captchaGuid']
            
            byte=res_data['value']['captchaByteData']
            decoded_data=base64.b64decode((byte))
            
            img_file = open('captcha.png', 'wb')
            img_file.write(decoded_data)
            img_file.close()
            capmonster = ImageToTextTask("1b3f112f66da3fcabb80951591f0693d")
            task_id = capmonster.create_task(image_path="captcha.png")
            result = capmonster.join_task_result(task_id)
            captcha_input=result['text']
            #########################################
            get_new_token_url = "https://ticketingweb.passo.com.tr/api/passoweb/login"
            get_new_token_headers = {
                "Content-Type": "application/json",
                 "Authorization": "Bearer DHZHUMUdA8HUDTlgRWfY+lZQcha0OceuLSq44jFUUy8t5MjZ+bOyoxNfseZkWjUP/Vn2HJ5cLnfbhwPYvB/qZ7XnWMyVn8gTz5YeteZ+dUwxXXAV8uAKAKx7yC3GVusBpThRJJo2A4OqlZ2SEuxmI+wp8yNQwYPpRDzLAJSxuB0=",
                "CurrentCulture": "en-US",
                "Accept": "application/json, text/plain, */*" , 
                "User-Agent": get_random_user_agent()}
            data={"username":email,"password":password,"rememberMe":True,"captchaGuid":guid,"captchaText":captcha_input}
            header={"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","Connection":"keep-alive","Content-Length":"157","Content-Type":"application/json","CurrentCulture":"en-US","Host":"ticketingweb.passo.com.tr","Origin":"https://www.passo.com.tr","Referer":"https://www.passo.com.tr/en/login","User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
            time.sleep(1)
            requests.get("https://www.passo.com.tr/TSPD/?type=22")
            time.sleep(3)
            token_res = requests.post(get_new_token_url, proxies=proxyReader.retriveProxy(), headers=get_new_token_headers,json=data, verify=False)
            
            
            if token_res.status_code==200:
                token_res_data=token_res.json()
                print(token_res_data)
                if token_res_data['isError'] and token_res_data['resultCode']!=0:
                    return 'error'
                refresh_token_id=token_res_data['value']['refresh_token']
                access_token=token_res_data['value']['access_token']
                try:
                        cursor=connection.cursor()
                        cursor.execute("update header_data set refresh_token ='%s' where email ='%s';"%(refresh_token_id,email))
                        connection.commit()
                        cursor.execute("update header_data set token = '%s'  where email = '%s';"%(access_token,email))
                        connection.commit()
                except Exception as e:
                    print(e)

                return access_token
get_new_token("mainulislammasum@gmail.com","Masum@1234")
