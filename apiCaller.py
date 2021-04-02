import requests
import json
import utils

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
def exampleGet(): #Obtener
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
            print(res.text)
        else:
            print(f"Error: {res.status_code}, {res.text}")
        # print(printAllResponseAttr(res))
    except Exception as ex:
        print(f"Except: {ex}")

def examplePost(): #Crear
     try:
        url = 'http://httpbin.org/post'
        args = {'nombre':'BeatrixSwain', 'app':'py<3'} #params=envia los datos por la url
        payload = {'nombre':'BeatrixSwain', 'testing':True} #Json los datos en data
       
        res = requests.post(url, json=payload) #Si se envían en jason, se guardan en data porque él se encarga de serializarlo a str
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

def testPut(): #Modificar
    #Cuando Auth, se envía el token por los encabezados.
     try:
        url = 'http://httpbin.org/put'
        payload = {'nombre':'BeatrixSwain', 'testing':True} #Json los datos en data
        headers = {'Content-Type':'application/json', 'access-token':'asdf'} 

        res = requests.put(url, data=json.dumps(payload), headers=headers)
        if res.status_code == 200:
            text = res.text #str Returns the content of the response, in unicode
            print(text)           
        else:
            print(f"Error: {res.status_code}, {res.text}")
     except Exception as ex:
        print(f"Except: {ex}")

def testDelete(): #Borrar
    #Cuando Auth, se envía el token por los encabezados.
     try:
        url = 'http://httpbin.org/delete'
        payload = {'nombre':'BeatrixSwain', 'testing':True} #Json los datos en data
        headers = {'Content-Type':'application/json', 'access-token':'asdf'} 

        res = requests.delete(url, data=json.dumps(payload), headers=headers)
        if res.status_code == 200:
            text = res.text #str Returns the content of the response, in unicode
            print(text)           
        else:
            print(f"Error: {res.status_code}, {res.text}")
     except Exception as ex:
        print(f"Except: {ex}")

#Load files
def chucks():
    try:
        url= 'https://cdn.pixabay.com/photo/2020/06/19/09/16/fantasy-5316369_960_720.jpg'
        response = requests.get(url, stream=True) #Realiza la petición sin descargar el contenido, pero así hace que no cierre la conexión
        with open('test.jpg', 'wb') as f:
            for chunk in response.iter_content(): #Toma todo el contenido del servidor y la va descargando poco a poco. Por eso la conexión debe quedarse abierta
                f.write(chunk)
        response.close()#Cierra la conexión
    except Exception as ex:
        print(f"Exception: {ex}")
    finally:
        if response:
            response.close()

################################################################################################
# POKE API
################################################################################################

def getPokeApi(url):
    try:
        if(url!=None and url !='None'):
            response = requests.get(url)
            if response.status_code == 200:
                payload = response.json()
                count = payload['count']
                nextPage = payload['next']
                prevPage = payload['previous']
                data = payload.get('results', []) #Si está vacía, devuelve una lista vacía
                return count, nextPage, prevPage, data                
            else:
                print(f"Error[{response.status_code}]: {response.text}")
                return -1, None, None, {}
    except KeyboardInterrupt:
        raise KeyboardInterrupt()           
    except Exception as ex:
        print(f"Exception: {ex}")
        return -2, None, None, {}

def listPokemon():
    try:
        url = f"{utils.rootPokeApi()}pokemon-form/"

        while(url!=None):
            total, nextP, prevP, data = getPokeApi(url)
            if total > 0:
                url = nextP
                # print(f"Total: {total}")
                # print(f"nextPage: {nextP}")
                # print(f"prevPage: {prevP}")
                # print("DATOS:")
                for f in data:
                    print(f"\t{f['name']}")

                var = input("¿Continuar mostrando información? [Y/N]  ")    
                if var.strip().lower() != 'y' :
                    break
            else:
                break  
    except KeyboardInterrupt:
        print("Stoped!")        
    except Exception as ex:
        print(f"Exception: {ex}")


############################################################################

def oAuthFirstStep(client):#De esta forma no se puede hacer por aquí.
    try:
        url = 'https://github.com/login/oauth/authorize'      
        args = {"client_id":client, "scope":"repo"}
        res = requests.get(url, params=args)
        if res.status_code == 200:
            print("Ok")
            print(res.text) #Lo que envía aquí es la página de autentiación. Obviamente estas cosas son para aplicaciones web
        else:
            print(res.text)
    except Exception as ex:
        print(f"Exception: {ex}")

def oAuthSecondStep(code, client, secret):  #De un proceso parecido al paso uno, se obtiene el code que se utilizará aquí para obtener el access token 
    try:
        #get access token.
        url = 'https://github.com/login/oauth/access_token'
        params = {'client_id':client, 'client_secret':secret, 'code':code}
        headers = {'Accept':'application/json'}
        res = requests.post(url, json=params, headers=headers)
        if res.status_code == 200:
            print(f"[{res.status_code}]")
            response_json = res.json()
            if 'error' in response_json:
                print(f"Se produjo un error al solicitar el token: {response_json['error']}, {response_json['error_description']}")
                return None
            else:
                print(f"{response_json['token_type']} {response_json['access_token']}")
                token = response_json['access_token']
                return token
        else:
            print(f"{res.status_code}, {res.text}")
            return None
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def oAuthGetListReposUserAuthen(token):
    try:
        #Get list repos
        url = 'http://api.github.com/user/repos'
        headers = {'Authorization': f'token {token}'}

        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            # print(res.text)
            payload = res.json()

            for project in payload:
                print(f"name: {project['name']}")
        else:
            print(f"{res.status_code}, {res.text}")
            return None
    
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def createARepository(token):
    try:
        url = 'https://api.github.com/user/repos' #Si no tiene el https no lo crea :)
        headers = {'Accept':'application/vnd.github.v3+json',
                    'Authorization': f'token {token}'}
        request = {'name':'TestoAuth'}

        res = requests.post(url, headers=headers, json=request)
        if res.status_code == 201:
            print(res.status_code)
            payload = res.json()
          #  print(payload)
           
        else:
            print(f"ERROR: {res.status_code}, {res.text}")
            return None
    except Exception as ex:
        print(f"Exception: {ex}")

def oAuthProcessGitHub():
    client, secret = utils.gettingSecretsSHH()
    # oAuthFirstStep(client)
    # token = oAuthSecondStep(code, client, secret)
    token =  utils.getTokenTEMP()
    if token != None:
         oAuthGetListReposUserAuthen(token)
        # createARepository(token)

def cookies():
    try:
        url = 'http://httpbin.org/cookies'
        paramcookies = {'cookie':'chocolate'}

        res = requests.get(url, cookies=paramcookies)
        if res.status_code == 200:
            cookies = res.cookies
            print(cookies)
            print("Content: ")
            print(res.content)
        else:
            print(f"{res.status_code}, {res.text}")
            return None

    except Exception as ex:
        print(f"Exception: {ex}")

def session(email, token):
    try:
        url = 'https://api.github.com/user'
        session = requests.session()
        session.auth = (email, token)
        res = session.get(url)

        if res.ok:
            print(res.content)
            #Con la sesión, entonces se puede operar con la variable session para hacer peticiones.
        else:
            print(f"Error: {res.status_code}, {res.text}")
    except Exception as ex:
        print(f"Exception: {ex}")

