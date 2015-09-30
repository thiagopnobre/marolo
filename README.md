Marolo
======

[![Join the chat at https://gitter.im/grupythonUFLA/marolo](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/grupythonUFLA/marolo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Projeto inicialmente desenvolvido pelo Grupython UFLA, com intuito de
agregar conhecimento aos participantes do grupo e ajudar membros de
um grupo de estudo da universidade, mas com o tempo acabou sendo abandonado.

Hoje, apenas uma ferrramenta de estudo e aprimoramento de conhecimento,
aberta a contribuições. O intuito da continuação do projeto de forma aberta
é servir como referências a iniciantes  em web2py assim como um ótimo
ponto de aprendizado para quem está começando ou está querendo se aprimorar
neste framework.

O que deve conter no projeto
----------------------------

- Home

  - Noticias
  - Divulgação de atividades

- O que é o Projeto

  - Descrição do Projeto

- Membros

  - Fotos, descrição e contatos dos membros

- Eventos

  - informações de eventos realizados

- Contatos
  - infromação do contato com o projeto

- Deve haver uma área para apoiadores, patrocinadores e parceiro
- Área para exposição de materiais desenvolvidos com marolo
![Screenshot](static/images/screenshot.gif?raw=true)
Instalação
----------

- Baixe o repositório git
- Extraia na pasta applications do web2py
- No diretório /marolo dentro de /applications  execute o script `startup.sh`
utilizando o comando:
`./startup.sh`
- Execute o web2py e a aplicação já estará rodando

FAQ
---

**Segui todos passos, iniciando por baixar o .zip no github,
mas a aplicação não aparece?**

**R:** Baixar o repositório compactado, traz uma nomeclatura com traços,
o que faz com que o web2py não reconheça a aplicação. Modifique o nome
da pasta para algo não contendo este caracter. Uma mudança simples é
transforma-lo em `_`.

**Um dos requisitos é a pillow, como proceder a instalação da mesma?**

**R:** A biblioteca pillow pode ser instalada através do gerenciador de
pacotes pip. Ou através de pacote específico como no Ubuntu o python-imaging.
Caso decida instalar via pip alguns problemas podem surgir.
Se utiliza Ubuntu recomendo ler
[este](http://cassiobotaro.github.io/instalando-pillow.html) tutorial,
mas independente da plataforma ao fim deste post, eu aponto links úteis.

**Tentei rodar script setup_project.py sem a opção `sudo ` e ocorre erro 
de permissão.**
**R:** É recomendado aprender sobre o uso de ambientes virtuais python.
Um vídeo interessante:

[Virtualenv no Linux/Mac](https://www.youtube.com/watch?v=9ptewqAEjNc)

Se ainda insiste instalar diretamente no sistema operacional, vá no arquivo `startup.sh` e modifique a quarta linha para `pip install --user -U -r requirements.txt`. 
