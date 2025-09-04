## Dia 2 – Autenticação e Segurança  

**Implementação da autenticação:**  
1. O usuário preenche o formulário na página de registro (`register.html`) e envia os dados via método POST para a função `registrar` no `register/views.py`.  
2. O sistema verifica se já existe um usuário com o mesmo nome:  
   - Caso exista, retorna erro e recarrega a página de registro.  
   - Caso não exista, cria o novo usuário no banco de dados.  
3. Após o cadastro, o usuário é autenticado automaticamente e redirecionado para a página principal de tarefas (`/home/`).  
4. O acesso à página principal é protegido com o decorador `@login_required(login_url="/login/")`, garantindo que apenas usuários logados acessem.  
5. O login é implementado em `login/views.py`, permitindo que usuários cadastrados acessem o sistema.  

**Superusuário:**  
- Criado via terminal Django para monitorar registros de usuários e tarefas diretamente no painel administrativo.  

**Desafios do dia:**  
- **Registro não concluído:**  
  - Motivo: O formulário de registro estava redirecionando diretamente para o login antes de concluir o cadastro.  
  - Solução: Ajustar o redirecionamento para a função correta no `views.py`.  

- **Erro no painel admin:**  
  - Motivo: O Django, no Python 3.12 dentro do Termux, não localizava arquivos de timezone via `zoneinfo`.  
  - Solução: Substituir `zoneinfo` por `pytz` e ajustar o `TIME_ZONE` para `"America/Sao_Paulo"` no `settings.py`.  

