# 🎮 Game Recommendation API

API REST desenvolvida em Flask para cadastro e recomendação de jogos com base em gênero e plataforma.

---

## 🚀 Funcionalidades

- Criar jogos
- Listar todos os jogos
- Buscar um jogo por ID
- Atualizar jogos
- Deletar jogos
- Recomendar jogos com base nas preferências do usuário

---

## 🤖 Sistema de Recomendação

O sistema analisa os jogos cadastrados e retorna recomendações com base nas preferências do usuário.
### 📸 Exemplo de uso da rota /recommend

[Exemplo de requisição no Thunder Client]<img width="1480" height="687" alt="Captura de tela 2026-04-15 122906" src="https://github.com/user-attachments/assets/829f5f1e-b55c-4e52-bafa-58072dd8b847" />

### 🧠 Como funciona

- +2 pontos para cada gênero compatível
- +1 ponto para plataforma compatível
- Os jogos são ordenados pelo score
- Retorna os 5 melhores resultados

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- SQLAlchemy

---

## 📌 Rotas da API

### 📥 Criar jogo
POST /games

### 📋 Listar todos os jogos
GET /games

### 🔍 Buscar jogo por ID
GET /games/<id>

### ✏️ Atualizar jogo
PUT /games/<id>

### ❌ Deletar jogo
DELETE /games/<id>

### 🤖 Recomendar jogos
POST /recommend

---

## ▶️ Como usar a API

### 📥 Criar jogo

POST /games

Exemplo:
{
  "nome": "God of War",
  "genero": "acao, aventura",
  "plataforma": "playstation"
}

---

### 📋 Listar jogos

GET /games

---

### 🔍 Buscar por ID

GET /games/1

---

### ✏️ Atualizar jogo

PUT /games/1

Exemplo:
{
  "nome": "Novo nome"
}

---

### ❌ Deletar jogo

DELETE /games/1

---

### 🤖 Recomendar jogos

POST /recommend

Exemplo com lista:
{
  "genero": ["acao", "rpg"],
  "plataforma": ["pc"]
}

Exemplo com string:
{
  "genero": "acao",
  "plataforma": "pc"
}

Resposta:
[
  {
    "name": "The Witcher 3",
    "score": 3
  }
]

---

## 📈 Melhorias futuras

- Paginação na listagem de jogos
- Filtro por gênero e plataforma
- Autenticação de usuários
- Melhorias no algoritmo de recomendação

---

## 👨‍💻 Autor

Desenvolvido por Matheus Ferreira
