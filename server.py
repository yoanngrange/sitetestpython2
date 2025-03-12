from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyRequestHandler(SimpleHTTPRequestHandler):  
    def do_GET(self):
        # ✅ Servir les fichiers statiques depuis le dossier "static/"
        if self.path.startswith('/static/'):
            self.path = self.path.lstrip('/')  # Supprime le premier "/"
            return super().do_GET()

        # ✅ Routes pour les pages HTML
        if self.path == '/':
            self.path = '/index.html'
        
        elif self.path == '/jeux-videos/mario-odyssey':
            self.path = 'jeux-videos/mario-odyssey/index.html'
        elif self.path == '/jeux-videos/mario-odyssey/astuce':
            self.path = '/jeux-videos/mario-odyssey/astuce.html'
        elif self.path == '/jeux-videos/mario-odyssey/lunes':
            self.path = '/jeux-videos/mario-odyssey/lunes/lunes.html'
        elif self.path == '/jeux-videos/mario-odyssey/lunes-roche-lunaire':
            self.path = '/jeux-videos/mario-odyssey/lunes/lunes-roche-lunaire.html'
        
        elif self.path == '/jeux-videos/zelda-breath-of-the-wild':
            self.path = '/jeux-videos/zelda-breath-of-the-wild/index.html'
        elif self.path == '/jeux-videos/zelda-breath-of-the-wild/astuce':
            self.path = '/jeux-videos/zelda-breath-of-the-wild/astuce.html'
        elif self.path == '/jeux-videos/zelda-breath-of-the-wild/solution':
            self.path = '/jeux-videos/zelda-breath-of-the-wild/solution.html'
        elif self.path == '/jeux-videos/zelda-breath-of-the-wild/inventaire':
            self.path = '/jeux-videos/zelda-breath-of-the-wild/inventaire-complet.html'
        elif self.path == '/jeux-videos/zelda-breath-of-the-wild/relais':
            self.path = '/jeux-videos/zelda-breath-of-the-wild/relais.html'

        elif self.path == '/jeux-videos/zelda-tears-of-the-kingdom':
            self.path = '/jeux-videos/zelda-tears-of-the-kingdom/index.html'
        elif self.path == '/jeux-videos/zelda-tears-of-the-kingdom/astuce':
            self.path = '/jeux-videos/zelda-tears-of-the-kingdom/astuce.html'
        elif self.path == '/jeux-videos/zelda-tears-of-the-kingdom/solution':
            self.path = '/jeux-videos/zelda-tears-of-the-kingdom/solution.html'
        
        elif self.path == '/jeux-videos/minecraft':
            self.path = '/jeux-videos/minecraft/index.html'
        elif self.path == '/jeux-videos/minecraft/astuce':
            self.path = '/jeux-videos/minecraft/astuce.html'
        elif self.path == '/jeux-videos/minecraft/solution':
            self.path = '/jeux-videos/minecraft/solution.html'

        try:
            content = self.render_template(self.path[1:])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def render_template(self, template_name):
        # Charger le fichier de base
        with open('templates/base.html', 'r', encoding='utf-8') as base_file:
            base_content = base_file.read()

        # Charger le menu commun
        with open('templates/menu.html', 'r', encoding='utf-8') as menu_file:
            menu_content = menu_file.read()

        # Charger le contenu spécifique
        with open(f'templates/{template_name}', 'r', encoding='utf-8') as page_file:
            page_content = page_file.read()

        # Charger le footer commun
        with open('templates/footer.html', 'r', encoding='utf-8') as footer_file:
            footer_content = footer_file.read()

        # Insérer le contenu spécifique, le menu et le footer dans la base
        base_with_menu = base_content.replace('{{ menu }}', menu_content)
        base_with_footer = base_with_menu.replace('{{ footer }}', footer_content)
        return base_with_footer.replace('{{ content }}', page_content)

# Configuration du serveur
PORT = 8000
os.chdir(os.path.dirname(__file__))  # Assurez-vous d'être dans le bon dossier

with HTTPServer(('localhost', PORT), MyRequestHandler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    httpd.serve_forever()
