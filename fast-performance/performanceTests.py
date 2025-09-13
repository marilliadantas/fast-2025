import random
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/", name="Acessando a home")

    @task
    def retornaLivros(self):
        self.client.get("/api/v1/Books", name="Listando livros do acervo")

    @task()
    def registrarLivro(self):
        book_id = random.randint(1000, 9999)
        self.client.post("/api/v1/Books", name="Criando livro", json={
            "id": book_id,
            "title": "Livro Teste de Performance",
            "description": "Introdução aos testes de performance",
            "pageCount": 250, 
            "excerpt": "Teste do Teste",
            "publishDate": "2025-09-06T00:37:16.386Z"
        })