import requests

url = "https://jsonplaceholder.typicode.com/posts"
def pedir_inteiro(mensagem: str):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido!")
def consultar_post():
    idpost = pedir_inteiro("Digite o ID do post: ")
    url = f"https://jsonplaceholder.typicode.com/posts/"
    try:
        posts = requests.get(f"{url}/{idpost}", timeout=5)
        posts.raise_for_status()
        posts_json = posts.json()
        print(f"Título: {posts_json['title']}")
        print(f"Corpo: {posts_json['body']}")
        print(f"User ID: {posts_json['userId']}")
    except requests.exceptions.Timeout:
        print(f"Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
#consultar_post(2)
def listar_posts():
    usuario = pedir_inteiro("Digite o numero de usuario: ")
    try:
        posts_usuario = requests.get(url, timeout=5)
        posts_usuario.raise_for_status()
        posts_usuario_json = posts_usuario.json()
        for post in posts_usuario_json:
            if post['userId'] == usuario:
                print(f"Post: {post}")
    except requests.exceptions.Timeout:
        print("Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro> {e}")
#listar_posts(7)

def criar_post():
    titulo = input("Digite o titulo: ")
    corpo = input("Digite o corpo: ")
    user_id = pedir_inteiro("Digite o numero de usuario: ")
    dicionario_post = {"title": titulo, "body": corpo, "userId": user_id}
    try:
        post = requests.post(url, json=dicionario_post, timeout=5)
        post.raise_for_status()
        print(f"Status code: {post.status_code}")
        print(post.json())
    except requests.exceptions.Timeout:
        print("Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

#criar_post()

def atualizar_post():
    idpost = pedir_inteiro("Digite o ID do post: ")
    titulo = input("Digite o titulo: ")
    corpo = input("Digite o corpo: ")
    user_id = pedir_inteiro("Digite o numero de usuario: ")
    dicionario_post = {"title": titulo, "body": corpo, "userId": user_id}
    url = f"https://jsonplaceholder.typicode.com/posts/{idpost}"
    try:
        post_att = requests.put(url, json=dicionario_post, timeout=5)
        post_att.raise_for_status()
        print(f"Status code: {post_att.status_code}")
        print(f"Post atualizado: {post_att.json()}")
    except requests.exceptions.Timeout:
        print(f"Requisição expirada...")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

#atualizar_post()

def excluir_post():
    idpost = pedir_inteiro("Digite o id do post que quer deletar: ")
    url = f"https://jsonplaceholder.typicode.com/posts/{idpost}"
    try:
        post_del = requests.delete(url, timeout=5)
        post_del.raise_for_status()
        print(f"Status code: {post_del.status_code}")
        print(f"Post deletado!")
    except requests.exceptions.Timeout:
        print("Requisição expirada!")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

#excluir_post(2)




