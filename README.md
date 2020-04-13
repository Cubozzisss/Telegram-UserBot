# TELEGRAM USERBOT ITA

# Come installare il Bot?

Entra su https://t.me/AnonBotSupport per aggiornamenti e supporto

### Deploya Il Bot Su Heroku (dopo aver ottenuto la string session ↓)

![Deploy In Heroku (https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Ottenere la String Session con Termux

Apri temux e incolla questa stringa, poi premi invio.
```sh
termux-setup-storage && cd $RK && apt update -y && apt upgrade -y && apt install git -y && git clone https://github.com/AlpHyx74/USERBOT-ITA && apt install git python -y && pip install telethon
```

Adesso inserisci questo comando:
```sh
cd $RK && cd USERBOT-ITA && python telesetup.py
```

inserisci tutti i campi necessari e copia l'ultima stringa
esempio:
```
Enter App ID: 00000
Enter App HASH: aaaaaaaaa58aajsksksois628
Enter Phone Number: +393000000000
Enter the code you received: 00000
Logged in as: Nome Cognome
qui ci dovrebbe essere la stringa che dovete copiare
```

## Variabili Necessarie e Come Ottenerle
```
API_KEY: my.telegram.org e crea una app
API_HASH: my.telegram.org e crea una app
STRING_SESSION: segui il passaggio qui sopra elencato
PRIVATE_GROUP_ID: crea un gruppo e ottiedi l'id digitando /id dopo aver aggiunto il bot @MissRose_bot
SUDO_USER: il tuo id (puoi settarlo dopo)
TG_BOT_TOKEN_BF_HER: crea un bot su @BotFather e copia il token
TG_BOT_USER_NAME_BF_HER: crea un bot su @BotFather e inserisci l'username (con la @)
HEROKU_API_KEY: vai sul tuo account heroku (https://dashboard.heroku.com/account) e copia la API key
HEROKU_APP_NAME: nome dell'app che si sta creando (quella che avete messo all'inizio)
```

***tutte queste sono necessarie per avere le funzionalità del bot principali***
