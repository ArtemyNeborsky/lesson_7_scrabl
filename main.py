import random


LETTER_SCORES = {"А": 1,
                 "Б": 3,
                 "В": 1,
                 "Г": 3,
                 "Д": 2,
                 "Е": 1,
                 "Ё": 3,
                 "Ж": 5,
                 "З": 5,
                 "И": 1,
                 "Й": 4,
                 "К": 2,
                 "Л": 2,
                 "М": 2,
                 "Н": 1,
                 "О": 1,
                 "П": 2,
                 "Р": 1,
                 "С": 1,
                 "Т": 1,
                 "У": 2,
                 "Ф": 10,
                 "Х": 5,
                 "Ц": 5,
                 "Ч": 5,
                 "Ш": 8,
                 "Щ": 10,
                 "Ъ": 10,
                 "Ы": 4,
                 "Ь": 3,
                 "Э": 8,
                 "Ю": 8,
                 "Я": 3}


def get_random_letter():
    converted_dictionary = list(LETTER_SCORES.keys())
    random_letter = random.choice(converted_dictionary)
    return random_letter


def calculate_score(word):
    all_scores = []
    for key in word.upper():
        letter_score = LETTER_SCORES.get(key, 0)
        all_scores.append(letter_score)
    sum_scores = sum(all_scores)
    return sum_scores


def get_word_with_letter(letter, player_number):
    while True:
        word = input(f"Игрок {player_number}\nВведите слово на букву '{letter}': ").upper()
        if word[0] == letter:
            score = calculate_score(word)
            print(f"Слово принято, очки: {score}")
            return word
        else:
            print(f"Ошибка слово должно начинаться с буквы '{letter}'")


def main():
    letter = get_random_letter()
    print(f"Начальная буква: {letter}")
    first_word = get_word_with_letter(letter, 1)
    second_word = get_word_with_letter(letter, 2)
    print(f"Игрок 1: {first_word}: {calculate_score(first_word)} очков")
    print(f"Игрок 2: {second_word}: {calculate_score(second_word)} очков")
    if calculate_score(first_word) > calculate_score(second_word):
        print("Игрок 1 победил")
    elif calculate_score(first_word) == calculate_score(second_word):
        print("Ничья")
    else:
        print("Игрок 2 победил")


if __name__ == '__main__':
    main()

