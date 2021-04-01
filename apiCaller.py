import requests
import json

def printAllResponseAttr(res):
    return f"""
    ok: {res.ok}
    url: {res.url}
    status_code: {res.status_code}
    text: {res.text}
    content: {res.content}
    apparent_encoding: {res.apparent_encoding}
    encoding: {res.encoding}
    elapsed: {res.elapsed}
    cookies: {res.cookies}
    headers: {res.headers}
    history: {res.history}
    is_permanent_redirect: {res.is_permanent_redirect}
    is_redirect: {res.is_redirect}
    links: {res.links}
    next: {res.next}
    reason: {res.reason}
    request: {res.request}
    """
#if result is writted in JSON format can get with res.json(), if result isnt writted in JSON raises an error
def exampleGet():
    try:
        url = 'https://www.google.es/'
        res = requests.get(url)
        print(res)
        if res.status_code == 200:
            #We can do here what we need with the response, for example save the content. => content.html
            content = res.content
            file = open('content.html', 'wb') #wb because res.content returns the content of the response, in bytes
            file.write(content)
            file.close()
        else:
            print(f"Error: {res.status_code}, {res.text}")
        print(printAllResponseAttr(res))
    except Exception as ex:
       print(f"Except: {ex}")

def exampleGet2():
    try:
        # url = 'http://httpbin.org/get' #Without param
        # url = 'http://httpbin.org/get?nombre=beatrix&app=py' #Send param static
        #send param dynamically
        url = 'http://httpbin.org/get'
        args = {'nombre':'BeatrixSwain', 'app':'py<3'}
        res = requests.get(url, params=args)
        print(res)
        if res.status_code == 200:
            #We can do here what we need with the response, for example save the content. => content.html
            text = res.text #str Returns the content of the response, in unicode
            content = res.content #Returns the content of the response, in bytes
            print(text)
            response_json = res.json()#json
            #We can get json too with:
            #j = json.loads(text)
            print(res.text)

            
            # print(res.url)
            # print(response_json)
            # print(response_json['args'])
        else:
            print(f"Error: {res.status_code}, {res.text}")
        # print(printAllResponseAttr(res))
    except Exception as ex:
        print(f"Except: {ex}")

def examplePost():
     try:
        url = 'http://httpbin.org/post'
        args = {'nombre':'BeatrixSwain', 'app':'py<3'} #params=envia los datos por la url
        payload = {'nombre':'BeatrixSwain', 'testing':True} #Json los datos en data
       
        res = requests.post(url, json=payload) #Si se envían en jason, se guardan en data porque él se encarga de serializarlo a str
        # res = requests.post(url, data=payload) #Si se envía en data; data=payload -> Se envían en el campo form        
        res = requests.post(url, data=json.dumps(payload))#Pero si queremos que se envíen en data, hay que serializar el diccionaro a str
        if res.status_code == 200:
            text = res.text #str Returns the content of the response, in unicode
            print(text)
            print(res.url)
        else:
            print(f"Error: {res.status_code}, {res.text}")
     except Exception as ex:
        print(f"Except: {ex}")

def testEncabezados():
    #Cuando Auth, se envía el token por los encabezados.
     try:
        url = 'http://httpbin.org/post'
        payload = {'nombre':'BeatrixSwain', 'testing':True} #Json los datos en data
        headers = {'Content-Type':'application/json', 'access-token':'asdf'} 

        res = requests.post(url, data=json.dumps(payload), headers=headers)
        if res.status_code == 200:
            text = res.text #str Returns the content of the response, in unicode
            print(text)
            headers_res = res.headers
            print(headers_res['Server'])
        else:
            print(f"Error: {res.status_code}, {res.text}")
     except Exception as ex:
        print(f"Except: {ex}")
