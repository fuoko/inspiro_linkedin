1. Dans le terminal, exécuter ./setupenv.sh pour charger les dépendances 
2. Charger l'environnement virtuel avec la commande source ./dev-env/bin/activate 
3. Mettez vos identifiants linkedin dans le fichier identifiants.json
4. Lancez python create_post.py : cela va publier l'image sur votre compte linkedin

NB : 
- Vous pouvez modifier le message d'envoi directement dans le code
- Cette technique d'automatisation n'est pas autorisée par la charte de Linkedin, car elle n'utilise pas l'API officielle : vous risqueriez de vous faire bannir votre compte, donc faites attention ;)
Pour plus d'informations complémentaires sur cette méthode voir : https://github.com/tomquirk/linkedin-api
