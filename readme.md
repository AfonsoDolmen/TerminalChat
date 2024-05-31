<h1 align="center">TerminalChat</h1>
<hr>

<h2>Descrição do Projeto</h2>
<p>TerminalChat é um simples projeto escrito em Python que permite a troca de mensagens
via servidor TCP com conexões simultâneas diretamente de um terminal.</p>

<img alt="TerminalChat" src="C:\Users\Afonso\Pictures\terminalchat.png"/>

<h2>Bibliotecas Utilizadas</h2>
* <strong>Socket:</strong> Permite a programação em baixo nível de redes, criando assim um pacote de conexão
para comunicação cliente/servidor.

* <strong>Blessed:</strong> Uma API de alto nível para o desenvolvimento de aplicações em terminais de forma
amigável.

* <strong>Threading:</strong> Biblioteca que permite trabalhar com MultiThreading.

<h2>Como utilizar</h2>

<p>Instale a biblioteca <i>blessed</i></p>

```shell
pip install blessed
```

<p>Após, inicie o servidor</p>

```shell
python server.py
```

<p>Por fim, inicie o cliente</p>

```shell
python client.py
```

<h2>Observações</h2>
<p>Este projeto foi desenvolvido para consolidar meus conhecimentos na linguagem Python, ousei por optar
um desafio que envolvesse programação de sockets de baixo nível em uma linguagem de alto nível.</p>

<p>Um grande aprendizado ao lidar com tratamento de exceções, estrutura de dados e treinar a lógica de programação.</p>

<h2>Referências</h2>

* https://realpython.com/python-sockets/
* https://docs.python.org/3/library/threading.html
* https://pypi.org/project/blessed/