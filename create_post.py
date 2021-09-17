from linkedin_api import Linkedin
from json import dumps, load as load_json
from os import stat
from time import sleep
import base64
import inspirobot
import requests
import shutil

def send_request_linkedin(payload, url_api):
  payload = dumps(payload)
  res = api.client.session.post(
    url_api, 
    payload
  )
  return res.json()

def generate_inspiro_image(nom_image):
  url_image = str(inspirobot.generate())
  r = requests.get(url_image, stream = True)
  if r.status_code == 200:
      r.raw.decode_content = True
      with open(nom_image,'wb') as f:
          shutil.copyfileobj(r.raw, f)
      print('Image récupérée avec succès')

nom_image = "image_inspirante.jpg"
generate_inspiro_image(nom_image)
with open('./identifiants.json') as fichier_identifiants:
    donnees_compte = load_json(fichier_identifiants)
api = Linkedin(donnees_compte["nom_compte"], donnees_compte["mot_de_passe"])

contenu_requete_1 = {
  "mediaUploadType":"IMAGE_SHARING",
  "fileSize":stat(nom_image).st_size,
  "filename":nom_image
  }

reponse_requete_1 = send_request_linkedin(
  contenu_requete_1, 
  "https://www.linkedin.com/voyager/api/voyagerMediaUploadMetadata?action=upload"
 )

url = reponse_requete_1["value"]["singleUploadUrl"]
urn = reponse_requete_1["value"]["urn"]

with open(nom_image, 'rb') as contenu_requete_2:
  reponse_requete_2 = api.client.session.put(
    url, 
    contenu_requete_2
  )
print(reponse_requete_2)
sleep(2)

message = """
          J'ai entendu dire que pour scale, il faut être disruptif.
          J'ai brainstormé, fait un benchmark, et je me suis focus en fulltime sur un process challenging ASAP: 
          faire du wording pro-actif pour atteindre ma target : être force de proposition.
          """
contenu_requete_3 = {
  "visibleToConnectionsOnly":False,
  "commentsDisabled":False,
  "externalAudienceProviders":[],
  "commentaryV2":{
    "text":message,
    "attributes":[]
  },
  "origin":"FEED",
  "allowedCommentersScope":"ALL",
  "media":[
    {"category":"IMAGE","mediaUrn":urn,"tapTargets":[]}
  ]
  }
reponse_requete_3 = send_request_linkedin(
  contenu_requete_3, 
  "https://www.linkedin.com/voyager/api/contentcreation/normShares"
  )
print(reponse_requete_3)
