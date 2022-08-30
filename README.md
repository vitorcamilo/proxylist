
# Título do Projeto

Bem vindo ao Proxylist 1.0


## Instalação

Após baixar o repositório Git execute os seguintes passos.

Crie uma virtual env:
```bash
  python3 -m venv /path/to/new/virtual/environment
```
On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate

On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh

On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish

On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat

On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1

[See Virtual Enviroment docs](https://docs.python.org/3/library/venv.html)


## Requerimentos

Após estarem com o Virtual environment ativado execute o comando:
```bash
  pip install -r requirements.txt
```


## Scraper

Entre com o terminal no local do arquivo "scrape\proxyscraper\proxylist.py":

Rode o comando ,
```bash
  scrapy crawl proxylist
```
para popular o banco de dados.


## Django App

Após o populamento do banco vá a pasta base onde o "manage.py" se encontra.

Execute o comando:
```bash
python manage.py runserver 
```



## Funcionalidades

- Criar dados
- Atualizar dados
- Apagar dados
- Apagar TODOS! (not recommended) (caso apague todos será necessário rodar o scraper novamente.)

[Veja o site em funcionamento](https://proxylist.vitorcamilo1.repl.co/) <-----------------------