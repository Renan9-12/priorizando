# Priorizando
Este projeto utiliza Django com SQLite3 e é gerenciado através do ORM.

---

## Clonando o projeto

Para começar, clone o repositório do projeto:
```
git clone https://github.com/Renan9-12/priorizando
```

---

## Instalação das dependências

1. Crie e ative um ambiente virtual do Python:

```
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

2. Instale todas as dependências listadas no arquivo requirements.txt:

```
pip install -r requirements.txt
```
---

## Configuração do banco de dados

O projeto utiliza SQLite3, que já vem integrado com o Django. Para criar o banco e as tabelas:

1. Rode os migrations do Django:

```
python manage.py migrate
```
2. (Opcional) Crie um superusuário para acessar o painel administrativo:


```
python manage.py createsuperuser
```
---

## Rodando o servidor

Para verificar se tudo está funcionando, rode:
```
python manage.py runserver
```
Em seguida, abra o navegador em:

http://127.0.0.1:8000/

---

## Tecnologias utilizadas

- **Python 3.12**  
- **Django 5.2.5**  
- **SQLite3** (banco de dados integrado)  
- **Django ORM** (para gerenciamento das tabelas e consultas)  
- **HTML5 e CSS3** (para um ambiente mais imersivo)
- **pytz** (para configuração de timezone)

---

## Observações finais

- Todos os pacotes necessários estão no requirements.txt.
- Dúvida? Entre em contato por pablorenan1946@gmail.com

---
