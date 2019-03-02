# O Aplikacji

Jest to prosta aplikacja Django do zarządzania zadaniami (todo). Aplikacja synchronizuje się ze wskazanym kalendarzem Google.


# Instalacja

W ustawieniach projeku Django settings.py należy dodać zmienną:

```GOOGLE_CRED = os.path.join(BASE_DIR, 'testy/credentials.json')```

```GOOGLE_CAL = 'testcallnedar0@group.calendar.google.com'```


# Plany
- synchronizacja z kalendarzem Google (~~dodawanie~~, usuwanie, edycja)
- powiadomienia o zbliżającym się terminie zadania


# Changelog

v0.1 
  - Pierwsza wersja


# Zrzut ekranu
![Zrzut ekranu](https://github.com/artekw/django_todoapp/blob/master/assets/screen.png)
