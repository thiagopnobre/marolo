Como contribuir
---------------

- Faça um fork do projeto(somente caso vá contribuir com código)
- Clone o seu fork em sua máquina
- Crie uma issue ou proponha um PR propondo alguma funcionalidade ou corrigindo algum erro:
- Antes de realizar qualquer modificação:
    + sincronize seu fork com o projeto original
      * como configurar um remoto para um fork
        -`git remote add upstream https://github.com/grupythonUFLA/marolo.git`
      * sincronizando um fork
        - `git fetch upstream`
        - `git rebase upstream/master`
    + crie um branch (localmente) para a issue que você deseja resolver com:
        - ` git checkout -b "fix_issue_X" `
- Trabalhe localmente, faça suas modificações e commits no seu branch "fix_issue_X" e suba suas alterações para o seu fork remoto com:
    - ` git push -u origin "fix_issue_X" `
- Proponha um PR tomando o seu branch "fix_issue_X" como base no branch "master" do grupython
- Aguarde aprovação de um dos membros responsáveis pelo projeto.
Caso seja membro do grupython da equipe do Marolo, aguarde aprovação de outro membro que não você próprio.

Dicas
-----

- Crie issues com boa descrição.
- Quando funcionalidade envolver estilo e/ou design do site, tente mandar imagem.
- Quando reverter algum commit ou discordar de alguma funcionalidade, crie discussões apontando seus argumentos.
- Mudanças que podem causar o interrompimento do funcionamento correto do site devem notificar todos os membros da equipe do Marolo.
- Ao criar Issues, marque com tags relevantes. O mesmo vale para PR's.
