from json import dumps
from requests import get as http_get
from shutil import copyfileobj 
from inspirobot import generate

def send_request_linkedin(api, payload, url_api):
  payload = dumps(payload)
  reponse_api = api.client.session.post(
    url_api, 
    payload
  )
  return reponse_api.json()

def generate_inspiro_image(nom_image):
  url_image = str(generate())
  r = http_get(url_image, stream = True)
  if r.status_code == 200:
      r.raw.decode_content = True
      with open(nom_image,'wb') as f:
          copyfileobj(r.raw, f)
      print('Image récupérée avec succès')
