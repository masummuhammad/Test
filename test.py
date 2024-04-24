import requests
import base64

import proxyReader
import urllib3
from capmonster_python import ImageToTextTask
urllib3.disable_warnings()


def get_new_token(email,password):
    captcha_url = "https://ticketingweb.passo.com.tr/api/passoweb/getcaptcha"
    captcha_headers = {
    "Access-Control-Request-Headers":
    "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "close","Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

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
            "Access-Control-Request-Headers":
            "authorization,content-type,currentculture","Accept":"Accept: application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "close","Content-Type": "application/json;charset=utf-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
            data={"username":email,"password":password,"rememberMe":True,"captchaGuid":guid,"captchaText":captcha_input}
            header={"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","Connection":"keep-alive","Content-Length":"157","Content-Type":"application/json","CurrentCulture":"en-US","Host":"ticketingweb.passo.com.tr","Origin":"https://www.passo.com.tr","Referer":"https://www.passo.com.tr/en/login","User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
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