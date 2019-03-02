# O Aplikacji

Jest to prosta aplikacja Django do zarządzania zadaniami (todo). Aplikacja synchronizuje się ze wskazanym kalendarzem Google.


# Instalacja

W ustawieniach projeku Django settings.py należy dodać zmienną:

```GOOGLE_CRED = os.path.join(BASE_DIR, 'testy/credentials.json')```

```GOOGLE_CAL = 'testcallnedar0@group.calendar.google.com'```


# Plany
- synchronizacja z kalendarzem Google (~~dodawanie~~, usuwanie, edycja)
- powiadomienia o zbliżającym się terminie zadania
- autoryzacja


# Changelog

v0.1 
  - Pierwsza wersja


# Zrzut ekranu
![Okno główne](https://github.com/artekw/django_todoapp/blob/master/assets/screen3.png)
![Dodawanie zdarzenia](https://github.com/artekw/django_todoapp/blob/master/assets/screen2.png)
![Podgląd szczegółów zdarzenia](https://github.com/artekw/django_todoapp/blob/master/assets/screen1.png)
