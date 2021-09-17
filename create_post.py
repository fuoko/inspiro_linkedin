from linkedin_api import Linkedin
from utils import send_request_linkedin, generate_inspiro_image
from json import load as load_json
from os import stat
from time import sleep
import base64

# Génération de l'image avec inspirobot, et enregistrement sur la machine
nom_image = "image_inspirante.jpg"
generate_inspiro_image(nom_image)

# Connexion à son compte Linkedin
with open('./identifiants.json') as fichier_identifiants:
    donnees_compte = load_json(fichier_identifiants)
api = Linkedin(donnees_compte["nom_compte"], donnees_compte["mot_de_passe"])

# On prépare la requête 1, on va envoyer à l'API voyager les informations concernant l'image qu'on veut envoyer 
contenu_requete_1 = {
  "mediaUploadType":"IMAGE_SHARING",
  "fileSize":stat(nom_image).st_size,
  "filename":nom_image
  }

reponse_requete_1 = send_request_linkedin(
  api, 
  contenu_requete_1, 
  "https://www.linkedin.com/voyager/api/voyagerMediaUploadMetadata?action=upload"
 )

# On récupère la réponse de la requête 1, qui va nous donner récupérer l'url de l'image stockée chez linkedin
url = reponse_requete_1["value"]["singleUploadUrl"]
urn = reponse_requete_1["value"]["urn"]

# On envoie physiquement l'image sous format binaire
with open(nom_image, 'rb') as contenu_requete_2:
  reponse_requete_2 = api.client.session.put(
    url, 
    contenu_requete_2
  )
print(reponse_requete_2)
sleep(2)

# On prépare le message à envoyer sur son compte Linkedin
message = """
          J'ai entendu dire que pour scale, il faut être disruptif.
          J'ai brainstormé, fait un benchmark, et je me suis focus en fulltime sur un process challenging ASAP: 
          faire du wording pro-actif pour atteindre ma target : être force de proposition.
          """

# On prépare la dernière requête où on insère l'urn de l'image qu'on a récupéré, et le contenu du message
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
  api, 
  contenu_requete_3, 
  "https://www.linkedin.com/voyager/api/contentcreation/normShares"
  )
print(reponse_requete_3)
