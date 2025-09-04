## Sinopse  
O projeto **Priorizando** foi desenvolvido como parte do desafio técnico proposto pela RzCode.  
O objetivo principal é fornecer uma aplicação web para gerenciamento de tarefas, ajudando o usuário a organizar atividades pessoais, de estudo ou de trabalho de forma eficiente, priorizando o que deve ser feito em seguida para otimizar os resultados.

A aplicação foi construída utilizando **Python e Django** no backend, **SQLite3** como banco de dados local, e **HTML, CSS** no frontend.  

---

## Funcionalidades  
O sistema oferece um conjunto de recursos que tornam o gerenciamento de tarefas simples, seguro e acessível:

### Autenticação de Usuários  
- Registro de novos usuários com verificação de nome já existente.  
- Login seguro com autenticação integrada ao Django.  
- Logout que encerra a sessão do usuário.  
- Restrições de acesso utilizando `@login_required`, garantindo que apenas usuários logados possam acessar suas tarefas.  

### Gerenciamento de Tarefas (CRUD)  
- **Criar:** Adicionar novas tarefas com título, descrição, tipo e status inicial.  
- **Visualizar:** Listar todas as tarefas do usuário autenticado, exibindo apenas os dados vinculados à sua conta.  
- **Editar:** Alterar informações das tarefas existentes, como título, descrição e categoria.  
- **Concluir/Pendente:** Marcar tarefas como concluídas ou retornar ao status de pendente.  
- **Excluir:** Remover definitivamente tarefas indesejadas.  

### Segurança  
- Cada usuário só tem acesso às próprias tarefas.  
- Exclusão em cascata: se um usuário for excluído, todas as suas tarefas também são removidas do banco.  
- Proteção contra acesso não autorizado em páginas internas.  

### Aparência  
- Interface minimalista com tema escuro.  
- Paleta de cores da RzCode: fundo preto, destaques em amarelo **#E5BF2E** e textos em branco.  
- Páginas estilizadas para garantir clareza e boa experiência de uso.  

---

## Tecnologias Utilizadas  
- **Linguagem:** Python 3.12  
- **Framework:** Django  
- **Banco de Dados:** SQLite3 (desenvolvimento local)  
- **Frontend:** HTML5 e CSS3  
- **Controle de versão:** Git e GitHub  
- **Bibliotecas adicionais:** pytz (para gerenciamento de fuso horário)  

---

## Destaques do Projeto  
- Sistema seguro e funcional de autenticação.  
- Estrutura de banco de dados clara e escalável com Django ORM.  
- Estilo visual padronizado, limpo e consistente com a identidade da RzCode.  
- Código documentado e organizado para manutenção futura.  
- Implementação de CRUD completo para tarefas, atendendo ao objetivo principal do sistema.  

---

## Conclusão  
O **Priorizando** é um projeto que alia simplicidade e eficiência, oferecendo aos usuários uma forma prática de gerenciar e priorizar suas atividades do dia a dia.  
Ele foi pensado para ser escalável, seguro e de fácil utilização, podendo futuramente ser expandido para novas funcionalidades, como integração com calendários externos, notificações e relatórios de produtividade.  

