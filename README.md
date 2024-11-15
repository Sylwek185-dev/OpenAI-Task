# AI Article Generator

Celem aplikacji jest wykorzystanie API OpenAI do przekształcania treści tekstowych w profesjonalnie sformatowany kod HTML.

## Wprowadzenie

Aplikacja przekształca plik tekstowy z artykułem na gotowy kod HTML, wykorzystując model OpenAI:

- **Łączy się z API OpenAI**
- **Odczytuje plik tekstowy z artykułem**
- **Przetwarza treść artykułu w profesjonalny kod HTML**
- **Zapisuje wynik w pliku `artykul.html`**

---

## Wymagania wstępne

1. **API Key OpenAI** – Pobierz [tutaj](https://platform.openai.com/).
2. **Python 3.7+** – Pobierz [tutaj](https://www.python.org).
3. **Git** – Pobierz [tutaj](https://git-scm.com/).

---

## Instalacja

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/Sylwek185-dev/OpenAI-Task.git
   cd OpenAI-Task
   ```

2. **Zainstaluj wymagane pakiety:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Konfiguracja

1. Otwórz plik `src/main.py` i dodaj swój klucz API w zmiennej:

   ```python
   openai.api_key = 'your_openai_api_key_here'
   ```

2. Upewnij się, że plik wejściowy z artykułem jest w formacie `.txt` i podaj jego ścieżkę:

   ```python
   article_file = './data/artykul.txt'
   ```

3. Plik wyjśćiowy znajdował się będzie w
   ```python
   output_file = './output/artykul.html'
   ```

---

## Uruchomienie aplikacji

1. Przejdź do katalogu projektu:

   ```bash
   cd /ścieżka/do/OpenAI-Task
   ```

2. Uruchom aplikację:
   - **Linux/macOS:**
     ```bash
     python3 src/main.py
     ```
   - **Windows:**
     ```bash
     python src\main.py
     ```

---

## Przykład wygenerowanego HTML:

```html
<article>
	<section>
		<h1>Tytuł artykułu</h1>
		<p>Treść wstępna artykułu...</p>
	</section>
	<section>
		<h2>Podtytuł</h2>
		<p>Dalsza część treści...</p>
		<img src="image_placeholder.jpg" alt="Opis obrazu" />
		<figcaption>Podpis pod obrazkiem</figcaption>
	</section>
</article>
```

## Struktura projektu

```
OpenAI-Task/
├── data/                 # Pliki wejściowe
│   └── artykul.txt       # Przykładowy plik tekstowy z artykułem
├── img/                  # Folder na obrazy
├── output/               # Pliki wynikowe
│   └── artykul.html      # Wygenerowany plik HTML
├── src/                  # Kod źródłowy
│   └── main.py           # Główna aplikacja
├── static/               # Folder na zasoby statyczne
│   ├── css/              # Pliki CSS
│   └── js/               # Pliki JavaScript
├── podglad.html          # Plik HTML do podglądu
├── szablon.html          # Szablon HTML
├── requirements.txt      # Lista zależności
└── README.md             # Dokumentacja
```

---

## Rozwiązywanie problemów

1. **Nie znaleziono modułu OpenAI:**
   Upewnij się, że zainstalowałeś wymagane biblioteki:

   ```bash
   pip install -r requirements.txt
   ```

2. **Błąd uwierzytelnienia API:**
   Sprawdź, czy klucz API został poprawnie wpisany w pliku `main.py`.

3. **Błąd zapisu pliku wynikowego:**
   Upewnij się, że masz uprawnienia do zapisu w katalogu `output`.

---

## Technologie użyte w projekcie

- **Python** – Język programowania użyty do budowy aplikacji.
- **OpenAI API** – Platforma sztucznej inteligencji do przetwarzania i generowania tekstu.
- **HTML5 i CSS3** – Format wyjściowego kodu HTML.
- **Git** – Kontrola wersji projektu.

---

## Podziękowania

Dziękuję za poświęcony czas na zapoznanie się z aplikacją. W razie pytań zapraszam do kontaktu: **sylwek185@op.pl**.
