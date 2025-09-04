## Dia 3 – Modelagem e Funções da Lista de Tarefas  

**Tabela de tarefas (models.py):**  
Criada utilizando o ORM do Django, com os seguintes campos:  
- **Título:** CharField (100 caracteres).  
- **Descrição:** TextField (2000 caracteres).  
- **Tipo:** CharField com três opções (Pessoal, Estudo, Trabalho), pré-selecionado em "Pessoal".  
- **Data criada:** `DateTimeField(auto_now_add=True)`.  
- **Data atualizada:** `DateTimeField(auto_now=True)`.  
- **Status de concluída:** BooleanField, padrão `False`.  
- **Usuário:** ForeignKey relacionado ao modelo `User`, com exclusão em cascata.  

**Funções implementadas (views.py):**  
- **Visualizar lista de tarefas:** Listagem filtrada para o usuário logado.  
- **Adicionar tarefa:** Criação de novas tarefas vinculadas ao usuário autenticado.  
- **Editar tarefa:** Edição de título, descrição, tipo e status (pendente/concluída). Também possível excluir a tarefa.  

**Desafio do dia:**  
- A necessidade de aprender e aplicar diversas funções do Django (ORM, autenticação, decoradores, manipulação de objetos).  
- Isso demandou tempo extra, mas proporcionou aprendizado prático e consolidou conhecimentos que aceleraram o progresso posterior.  
