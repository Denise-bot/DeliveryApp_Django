# 🛵 Delivery - Sistema de Pedidos Online

Projeto de código aberto desenvolvido como parte do curso Técnico em Desenvolvimento de Sistemas no Senac, sob orientação da Profª Maristela.  
O sistema simula um serviço de delivery, com foco na prática de desenvolvimento web utilizando o framework **Django**.

---

## 👩‍🏫 Sobre o Projeto

A proposta tem como objetivo a aplicação prática dos conhecimentos em:

- Backend com **Django**
- Frontend com **HTML**, **CSS** e **Bootstrap**
- Banco de dados com **SQLite**
- Integração com **painel administrativo**

Embora criado com fins didáticos, o projeto tem potencial para expansão como um sistema real de delivery.

---

## 🚀 Funcionalidades

- Autenticação de usuários (login e logout)
- Cadastro e gerenciamento de produtos, categorias, adicionais e opções
- Visualização de produtos com imagem, descrição e ingredientes
- Sistema de carrinho de compras
- Interface responsiva com **Bootstrap**
- Painel administrativo completo com **Django Admin**

---

## 💻 Tecnologias Utilizadas

- Python 3.12
- Django
- HTML + CSS (Bootstrap)
- SQLite3
- JavaScript (básico)

---


## 📦 Como rodar o projeto

1. Clone o repositório:

git clone https://github.com/Denise-bot/Tutorial_Delivery.git
cd Tutorial_Delivery

2. Crie e ative um ambiente virtual:

python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

3. Instale as dependências:

pip install -r requirements.txt

4. Aplique as migrações:

python manage.py migrate

5. Crie um superusuário:
 
python manage.py createsuperuser

6. Rode o servidor local:
 
python manage.py runserver

7. Acesse:

Painel administrativo: http://127.0.0.1:8000/admin/

Página inicial do sistema: http://127.0.0.1:8000/

📁 Estrutura de Mídia
As imagens dos produtos devem ser adicionadas à pasta media/post_img/ com os nomes correspondentes ao que foi salvo no banco de dados.

🤝 Contribuindo
Por ser um projeto educacional de código aberto, você está livre para estudar, adaptar ou expandir este sistema como quiser. Sugestões e melhorias são sempre bem-vindas!

📝 Licença
Este projeto está licenciado sob a licença MIT.
