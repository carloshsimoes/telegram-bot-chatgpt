# BotTelegram + ChatGPT (OpenAI)

Exemplo de um Bot Telegram Integrado ao ChatGPT (API OpenAI) para estudo.

Foi criada integração para iteração com Chat e criar imagens usando IA.


# Executando o BOT local (sem container):


# Primeiro vamos criar nosso environment

Vamos criar nosso ENV e instalar as LIBs que já estão anunciadas no `requirements.txt`.

```bash

python3 -m venv --prompt bot .venv

. .venv/bin/activate

pip install -r requirements.txt

```


# Definindo as configuração/parametrizações do BOT:

Precisamos definir/setar as configurações/parametrizações para rodar nosso BOT.

**Requisitos:**

- Criar uma conta no OpenAI e obter um Token de API;
- Criar um BOT no Telegram (@BotFather) e obter o Token;

Após obter o API KEY/TOKEN para integração com ambos serviços, você vai exportar ele para seu Environtment no contexto o qual vai executar o script/projeto:


```bash

export OPENAI_API_TOKEN='SEU TOKEN AQUI'

export TELEGRAM_API_TOKEN='SEU TOKEN AQUI'

```

**Após, você também pode definir o NOME e os COMANDOS do BOT!**

Você podera fazer isso entro do arquivo `config.py`.


```python

#--------------------------------------------------------------------
# BotName
#--------------------------------------------------------------------

botName = "BarbaRoots"

botCommands = {
    "chat": "barba", # Aqui defini o comando "barba" para iteração via Chat
    "image": "criar", # Aqui defini o comando "criar" para Criação de Imagens com AI
    "start": ['start', 'olá', 'oi', 'help', 'ajuda'] # Aqui defini os comandos de start/help e etc.
}

```


Pronto, já definida as configurações do BOT, podemos então iniciar o mesmo!!


```bash

# python3 bot.py

```


# Opção de Iniciar nosso BOT utilizando Container:

Adicionalmente, foi disponibilizado dois arquivos:

- **Dockerfile**
- **runAPP.sh**

Já com o que é preciso para buildar/construir sua imagem de Container.


**Criando nossa imagem Docker:**

```bash

docker image build -t bottelegram . --no-cache

```

**Executando nosso container/BOT em seguida:**

> OBS; Da mesma forma, ao rodar o Container, vamos "evaluar" os dois ENVs `TELEGRAM_API_TOKEN` e `OPENAI_API_TOKEN`, de forma que possam ser recuperados dentro do Container!

```bash

docker container run -d --env "TELEGRAM_API_TOKEN" --env "OPENAI_API_TOKEN" bottelegram:latest

```


=)