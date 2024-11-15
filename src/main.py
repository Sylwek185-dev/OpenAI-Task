import openai

# Ustaw swój klucz API OpenAI
openai.api_key = ''  # Wstaw swój klucz API tutaj

# Funkcja do odczytu pliku z artykułem
def read_article(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Plik jest pusty. Sprawdź zawartość pliku.")
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Plik {filename} nie istnieje. Upewnij się, że ścieżka do pliku jest poprawna.")
    except Exception as e:
        raise RuntimeError(f"Błąd podczas odczytu pliku: {e}")

# Funkcja do wysłania żądania do OpenAI i wygenerowania HTML
def generate_html(article_text):
    if not article_text:
        raise ValueError("Tekst artykułu jest pusty. Podaj poprawny plik wejściowy.")

    prompt = (
        "Przekształć poniższy artykuł w kod HTML, używając odpowiedniej struktury HTML, w tym nagłówków (<h1>, <h2>, <article>, ...), paragrafów (<p>) i innych elementów HTML. "
        "Każda wyróżniona nagłówkiem część powinna znajdować się w znaczniku <section>. "
        "Całość kodu powinna znajdować się w znaczniku <article>. "
        "Wskaż najlepsze miejsca na obrazy zgodnie z zasadami UX/UI i estetyką stron internetowych, używając tagów <img src='image_placeholder.jpg' alt='...'>. "
        "Dla każdego obrazka wstaw opis w atrybucie alt, składający się z 5 zdań, który możemy wykorzystać do generowania grafiki. "
        "Pod obrazkami dodaj podpisy z tagiem <figcaption>. "
        "Zwróć tylko zawartość do umieszczenia w sekcji <body>, bez znaczników <html>, <head> lub <body>. "
        "Nie dodawaj żadnego formatowania ani backticków."
        "\n\n"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Jesteś asystentem generującym profesjonalny kod HTML."},
                {"role": "user", "content": f"{prompt}\n\n{article_text}"},
            ],
            max_tokens=2500,
            temperature=0.4,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return response.choices[0].message['content'].strip()
    except openai.error.AuthenticationError:
        raise ValueError("Błąd uwierzytelnienia. Sprawdź klucz API i upewnij się, że jest poprawny.")
    except openai.error.RateLimitError:
        raise RuntimeError("Przekroczono limit żądań. Spróbuj ponownie później.")
    except openai.error.APIConnectionError:
        raise RuntimeError("Nie udało się połączyć z API OpenAI. Sprawdź swoje połączenie internetowe.")
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"Błąd API OpenAI: {e}")

# Funkcja do zapisu wygenerowanego kodu HTML w pliku
def save_html(filename, html_content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
    except Exception as e:
        raise RuntimeError(f"Błąd podczas zapisu pliku: {e}")

# Główna funkcja aplikacji
def main():
    article_file = './OpenAI-Task/data/artykul.txt'  # Podaj nazwę pliku z artykułem
    output_file = './OpenAI-Task/output/artykul.html'
    
    try:
        article_text = read_article(article_file)  # Odczytanie artykułu
        html_content = generate_html(article_text)  # Generowanie HTML
        save_html(output_file, html_content)  # Zapisanie do pliku
        print(f"Wygenerowany kod HTML zapisano w pliku {output_file}")
    except FileNotFoundError as e:
        print(f"Błąd pliku: {e}")
    except ValueError as e:
        print(f"Błąd danych: {e}")
    except RuntimeError as e:
        print(f"Błąd aplikacji: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
