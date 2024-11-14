import openai

# Ustaw swój klucz API OpenAI
# openai.api_key = ''  # Dodaj klucz API tutaj lub użyj zmiennej środowiskowej

# Funkcja do odczytu pliku z artykułem
def read_article(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Funkcja do wysłania żądania do OpenAI i wygenerowania HTML
def generate_html(article_text):
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

    
    #proba wygenerowania 
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "Jesteś asystentem generującym profesjonalny kod HTML, który przestrzega zasad poprawnej struktury, dostępności (accessibility) oraz UX/UI. Twój kod powinien być czysty, dobrze zorganizowany i zgodny z najlepszymi praktykami, gotowy do użycia na profesjonalnej stronie internetowej. Dbasz o estetykę kodu i rozmieszczenie elementów, aby zapewnić przejrzystość i zgodność z zasadami UX/UI."},
                {"role": "user", "content": f"{prompt}{article_text}"}
            ],

            #parametryzacja zapytania do API
            max_tokens=2500,
            temperature=0.4,
            top_p=1.0,
            frequency_penalty=0.5, 
            presence_penalty=0.0
        )
        
        return response.choices[0].message['content'].strip()
    
    #obsluga bledow
    except openai.error.OpenAIError as e:
        print(f"Wystąpił błąd podczas komunikacji z API OpenAI: {e}")
        return None



# Funkcja do zapisu wygenerowanego kodu HTML w pliku
def save_html(filename, html_content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Główna funkcja aplikacji
def main():
    article_file = './OpenAI-Task/data/artykul.txt'  # Podaj nazwę pliku z artykułem
    output_file = './OpenAI-Task/output/artykul.html'
    
    # 1. Odczytanie artykułu
    article_text = read_article(article_file)
    
    # 2. Wygenerowanie HTML za pomocą OpenAI
    html_content = generate_html(article_text)
    
    if html_content:
        # 3. Zapisanie wygenerowanego HTML do pliku
        save_html(output_file, html_content)
        print(f"Wygenerowany kod HTML zapisano w pliku {output_file}")
    else:
        print("Nie udało się wygenerować kodu HTML.")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()