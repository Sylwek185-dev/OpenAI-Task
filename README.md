# AI Article Generator

Prosta i intuicyjna aplikacja do generowania artykułów HTML z wykorzystaniem OpenAI API

## Wprowadzenie

Zadaniem aplikacji jest wygenerowanie kodu HTML, na podstawie wczytanego pliku tekstowego z artykułem:

- **Program łączy się z API OpenAI**
- **Odczytuje plik tekstowy z artykułem**
- **Przekazuje treść artykułu oraz prompt do OpenAI w celu obróbki**
- **Zapisuje otrzymany od OpenAI kod HTML w pliku `artykul.html`**

## Wymagania wstępne

Upewnij się, że posiadasz wygenerowany API key z OpenAI. Jeśli nie, możesz to zrobić [tutaj](https://platform.openai.com/)

Upewnij się, że masz zainstalowany git na swoim komputerze. Jeśli nie, możesz go pobrać [tutaj](https://git-scm.com/).

### Przykład użycia

- **W pliku `task.py` dodaj swój API KEY.**
- **Podaj ścieżkę do pliku z artykułem oraz lokalizacje pliku wyjsciowego html.**
  `article_file = 'plik zrodlowy' output_file = "plik wyjsciowy"`

- **Uruchom aplikację.**
- **Aplikacja wygeneruje i zapisze artykuł jako `artykul.html`.**

## Technologie

Projekt został zbudowany przy użyciu następujących technologii:

- **Python**
- **OpenAI API**
- **HTML5**
- **CSS3**

### Klonowanie repozytorium

```bash
git clone https://github.com/Sylwek185-dev/OpenAI-Task.git
```

### Kontakt

Sylwek185 - sylwek185@op.pl
