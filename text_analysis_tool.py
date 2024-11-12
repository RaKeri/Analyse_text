import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# Убедитесь, что у вас установлены необходимые ресурсы NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Функция для анализа текста
def analyze_text(text):
    # Удаление лишних символов
    text = re.sub(r'[^\w\s]', '', text)

    # Токенизация
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)

    # Удаление стоп-слов
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Частотный анализ
    word_freq = Counter(filtered_words)
    char_count = len(text)
    sentence_count = len(sentences)

    return word_freq, char_count, sentence_count

# Функция для генерации облака слов
def generate_wordcloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Пример проверки грамматики (упрощённая версия)
def grammar_check(text):
    errors = []
    words = word_tokenize(text.lower())
    for word in words:
        if not word.isalpha():
            errors.append(f"Некорректное слово: {word}")
    return errors

# Основная программа
if __name__ == "__main__":
    print("Введите текст для анализа:")
    user_text = input()

    # Анализ текста
    word_freq, char_count, sentence_count = analyze_text(user_text)
    print("\nРезультаты анализа:")
    print(f"Количество символов: {char_count}")
    print(f"Количество предложений: {sentence_count}")
    print(f"10 самых частых слов: {word_freq.most_common(10)}")

    # Проверка грамматики
    grammar_errors = grammar_check(user_text)
    if grammar_errors:
        print("\nОшибки грамматики:")
        for error in grammar_errors:
            print(error)
    else:
        print("\nОшибки грамматики не обнаружены.")

    # Генерация облака слов
    print("\nГенерация облака слов...")
    generate_wordcloud(word_freq)
