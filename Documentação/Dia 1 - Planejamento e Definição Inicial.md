## Dia 1 – Planejamento e Definição Inicial  

**Planejamento:**  
Com base na proposta da RzCode, iniciei o planejamento do projeto, definindo as ferramentas, a estrutura e a aparência que serviriam como base para o desenvolvimento.  

**Ferramentas:**  
- **Backend:** Python e Django, aproveitando o ORM para facilitar a manipulação do banco de dados.  
- **Banco de Dados:** SQLite3 para desenvolvimento local.
- **Frontend:** HTML e CSS, garantindo um ambiente mais imersivo.  
- **Controle de versão:** Git e GitHub para versionamento e organização do código.  

**Estrutura do projeto:**  
- Um sistema de autenticação para registro e login de usuários.  
- Área principal dedicada a uma lista de tarefas, onde cada usuário teria acesso apenas às próprias informações.  
- Funções de CRUD (criar, visualizar, editar e excluir tarefas).   

**Aparência:**  
- Definição de identidade visual alinhada com a paleta de cores da RzCode:  
  - **Preto predominante** (fundo principal).  
  - **Amarelo (#E5BF2E)** para destaques e botões de ação.  
  - **Branco** para contrastes e legibilidade.  

**Primeiras funcionalidades implementadas:**  
- Navegação entre páginas dos aplicativos do Django por meio de botões e links.  
- Estrutura básica de templates configurada.  

**Nome escolhido:**  
- **"Priorizando"**, por refletir a essência do sistema: ajudar o usuário a organizar suas tarefas e decidir o que deve ser feito primeiro para aumentar a produtividade.  

**Desafio do dia:**  
- Problema: Os arquivos HTML dos aplicativos não estavam renderizando corretamente.  
- Motivo: Uso incorreto do `{% url 'caminho' %}` nos templates.  
- Solução: Substituir pelos caminhos diretos (`/caminho/`) nos próprios arquivos HTML.  
