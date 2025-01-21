from flask import Flask, render_template, request

app = Flask(__name__)

# Liste des livres
books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020},
]

# Page d'accueil
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# Route pour la recherche
@app.route('/search', methods=['GET'])
def search():
    # Récupération de l'auteur depuis les paramètres GET
    author_from_search = request.args.get('author', '').strip()
    if not author_from_search:
        return "Veuillez entrer un nom d'auteur.", 400  # Erreur si aucun auteur n'est fourni

    # Recherche du livre correspondant
    for livre in books:
        if livre['author'].lower() == author_from_search.lower():  # Comparaison insensible à la casse
            return f"Livre : {livre['title']} ({livre['year']})"

    # Aucun résultat trouvé
    return "Aucun livre trouvé !"

# Lancement de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
