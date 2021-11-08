# infoshareacademy_webapi

Jeśli nie macie python3.9 (analogicznie też można 3.10)

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.9 python3.9-dev python3.9-venv
    sudo apt install python3.10 python3.10-dev python3.10-venv


Instalacja ręczna, sklonuj repo, wejdź do katalogu z projektem i dalej

    python3.9 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

* http://127.0.0.1:8000/admin/
* http://127.0.0.1:8000/words/
* http://127.0.0.1:8000/words/words
* http://127.0.0.1:8000/words/list-users
* http://127.0.0.1:8000/words/test_get_post


Do testowania
 
    import requests
    url = "http://127.0.0.1:8000/words/test_get_post"
    payload = {"dziala": "testowo"}
    r = requests.post(url, json=payload)
    r.status_code
    r.json()

Stwórz widoki w pliku: words/views.py, pomocnicze opisy w komentarzach.

Stwórz widok, który zwróci, ile zostało czasu do weekendu. Przyjmujemy, że weekend
zaczynamy w piątek o 17:00 i kończymy w niedzielę 23:59:59

Stwórz widok, który zwróci losową sentencję cytat dnia wraz z autorem. Przygotujcie listę
kilku tekstów i zwracajcie losowo.