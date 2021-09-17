Etapes pour exécuter le programme
1. Dans le terminal, exécuter ./setupenv.sh pour charger les dépendances 
2. Charger l'environnement virtuel avec la commande source ./dev-env/bin/activate 
3. Mettez vos identifiants linkedin dans le fichier identifiants.json
4. Lancez python create_post.py : cela va publier l'image sur votre compte linkedin

NB : 
- Pour générer l'image, j'utilise une API qui appelle le site https://inspirobot.me/
C'est une intelligence artificielle qui prend une image aléatoire et la complète avec un texte généré en simulant les citations inspirantes.
- Pour poster le message, le site de Linkedin utilise un service appelé Voyager, avec ce service on peut faire à peu près n'importe quoi (récupérer les profils, discuter, ajouter des personnes, etc.)
En simulant les requêtes du navigateur faite à  voyager, on peut programmer ce type d'actions, et c'est ce qui a été fait ici
/!\ Cette technique d'automatisation n'est pas autorisée par la charte de Linkedin, car elle n'utilise pas l'API officielle : vous risqueriez de vous faire bannir votre compte, donc faites attention ;)
Pour plus d'informations complémentaires sur cette méthode voir : https://github.com/tomquirk/linkedin-api
- Vous pouvez modifier le message d'envoi directement dans le code


