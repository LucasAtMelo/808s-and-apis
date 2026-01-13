# 808s & APIs 💔🤖 (Backend API)

> "Beats by Ye. Code by Lucas."

Uma **API RESTful** robusta desenvolvida com **Django REST Framework** para gerenciar um catálogo musical complexo e um sistema de críticas (reviews) da comunidade.

Este projeto foca na arquitetura backend, integridade de dados relacionais e implementação de regras de negócio para sistemas de streaming.

---

## ⚙️ Funcionalidades Principais

* **Autenticação e Permissões:**
    * Sistema de Token Authentication.
    * Permissões granulares: Apenas usuários autenticados podem criar reviews; apenas o dono pode editar seus registros (`IsOwnerOrReadOnly`).
* **Modelagem de Dados Complexa:**
    * Implementação de relacionamentos **Many-to-Many com Atributos Extras** (Tabela Intermediária `TrackArtist`) para suportar múltiplos papéis (Main, Feat, Producer) na mesma faixa.
* **Integridade de Dados:**
    * Constraints de banco de dados (`unique_together`) para impedir duplicidade de reviews (1 review por usuário/música).
    * Tratamento de erros e validação de dados automática via Serializers.
* **Endpoints Customizados:**
    * Rotas especializadas para leitura de créditos detalhados e injeção automática de dependências (User context).

---

## 🛠 Tech Stack

* **Linguagem:** Python 3.10+
* **Framework:** Django 5 & Django REST Framework (DRF)
* **Banco de Dados:** SQLite (Dev) / PostgreSQL (Prod)
* **Ferramentas:** Insomnia/Postman (para testes de rotas)

---

## 🔌 API Endpoints

Aqui estão as principais rotas disponíveis na API:

### 🎵 Catálogo (Tracks & Albums)
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/albums/` | Lista todos os álbuns |
| `POST` | `/api/tracks/` | Cria uma nova faixa (metadados básicos) |
| `POST` | `/api/track-artists/` | Vincula um artista a uma faixa com um papel (Ex: FEAT, PROD) |
| `GET` | `/api/tracks/{id}/credits/` | **Rota Especial:** Retorna JSON detalhado com todos os créditos da música |

### ⭐ Reviews (The Convo)
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/reviews/` | Lista todas as avaliações |
| `POST` | `/api/reviews/` | Cria uma avaliação (Requer Token). O usuário é injetado automaticamente. |

---

## 🧠 Destaques de Engenharia

### 1. The "Through" Model Strategy
Diferente de sistemas simples que usam listas de IDs, este projeto implementa um modelo intermediário explícito (`TrackArtist`) para resolver o problema de **Créditos Musicais**:

```python
# models.py snippet
class TrackArtist(models.Model):
    role = models.CharField(choices=ROLE_CHOICES, default='MAIN')
    # Permite saber QUEM fez O QUE na música (Producer, Lyricist, Vocalist)
```

### 2. Segurança na Escrita (Write Safety)
Para evitar dados corrompidos ou incompletos, as Views sobrescrevem o método `perform_create` para garantir que o usuário logado seja associado à ação, sem confiar no input do frontend:

```python
# views.py snippet
def perform_create(self, serializer):
    # Injeção automática de dependência do usuário autenticado
    serializer.save(user=self.request.user)
```

---

## 🚀 Como Rodar Localmente

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/seu-usuario/808s-and-apis.git](https://github.com/seu-usuario/808s-and-apis.git)
   cd 808s-and-apis
   ```

2. **Crie o Ambiente Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare o Banco de Dados**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o Servidor**
   ```bash
   python manage.py runserver
   ```
   Acesse a API navegável em: `http://127.0.0.1:8000/api/`

---

## 📞 Contato

Desenvolvido por **Lucas**.

* [LinkedIn](https://www.linkedin.com/in/seu-linkedin)
* [GitHub](https://github.com/seu-usuario)
