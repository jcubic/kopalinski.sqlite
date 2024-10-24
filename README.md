## Słownik Wyrazów Obcych Kopalińskiego jako baza sqlite

Słownik pobrany ze strony [www.slownik-online.pl](http://www.slownik-online.pl), na której
w chwili pisania skryptu nie działa już wyszukiwarka. W między czasie strona przestała
istnieć a domena jest do kupienia na after market

wygenerowany przez skrypt [sqlite.py](https://github.com/jcubic/kopalinski.sqlite/blob/master/sqlite.py) operujący na katalogu ze stroną pobraną poprzez wget:

```
wget -r http://www.slownik-online.pl/indeks_hasel.php
```

Strona z [indexem w archive.org](https://web.archive.org/web/20121115000000*/http://www.slownik-online.pl/indeks_hasel.php) jest niestety uszkodzona.

Archiwum strony jest zawarte w pliku [tag.gz](https://github.com/jcubic/kopalinski.sqlite/blob/master/www.slownik-online.pl.tar.gz)

Baza zawiera jedną tabelę `terms` która zawiera 3 pola `id`, `name` oraz `description`.

Do otwarcia bazy możesz użyć biblioteki sqlite3 dla ulubionego języka.

## Licencja

Kod dostępny na licencji [CC0 Public Domain](https://creativecommons.org/share-your-work/public-domain/cc0/)<br/>
Jednak baza może zawierać dane, które są chronione prawem autorskim, używaj na własną odpowiedzialność.
