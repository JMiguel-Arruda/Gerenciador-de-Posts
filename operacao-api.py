import requests

url = "https://jsonplaceholder.typicode.com/posts"

def consultar_post(id: int):
    try:
        posts = requests.get(url, timeout=5)
        posts.raise_for_status()
        posts_json = posts.json()
        for post in posts_json:
            if post['id'] == id:
                print(f"Título: {post['title']} - Corpo: {post['body']} - User ID: {post['userId']} - ID: {post['id']}")
    except requests.exceptions.Timeout:
        print(f"Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
#consultar_post(2)
def listar_posts(usuario: int):
    try:
        posts_usuario = requests.get(url, timeout=5)
        posts_usuario.raise_for_status()
        posts_usuario_json = posts_usuario.json()
        for i, post in enumerate(posts_usuario_json, start = 1):
            if post['userId'] == usuario:
                print(f"{i}. Post: {post}")
    except requests.exceptions.Timeout:
        print("Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro> {e}")
listar_posts(7)

def criar_post(titulo = None, corpo = None, user_id = None):
    titulo = input("Digite o titulo: ")
    corpo = input("Digite o corpo: ")
    user_id = int(input("Digite o numero de usuario: "))
    dicionario_post = {"title": titulo, "body": corpo, "userId": user_id}
    try:
        post = requests.post(url, json=dicionario_post, timeout=5)
        post.raise_for_status()
        print(post.status_code)
        print(post.json())
    except requests.exceptions.Timeout:
        print("Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

criar_post()



