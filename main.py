from collections import defaultdict, Counter
import random
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from faker import Faker

fake = Faker()

def main():
    names = generate_name_list(10, 2)

    # Sorts names by length (longest first), if same length, then alphabetically
    sorted_names = sorted(names, key=lambda n: (-len(n), n))

    letter_frequency = calculate_letter_frequency(sorted_names)

    # Sorts dictionary by value in descending order
    items = sorted(letter_frequency.items(), key=lambda item: -item[1])

    # Unpacks sorted items into two lists: x (letters) and y (frequencies)
    x, y = zip(*items)

    # Creates figure and plots
    fig, (ax1, ax2) = plt.subplots(2)

    # Bar chart
    ax1.bar(x, y)
    ax1.set_xlabel('Letters')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Frequency of each letter in list of names')

    # Wordcloud
    wordCloud = WordCloud().generate_from_frequencies(letter_frequency)
    ax2.imshow(wordCloud, interpolation="bilinear")
    ax2.axis("off")

    # Show figure
    plt.tight_layout()
    plt.show()

def generate_name_list(total_amount: int, duplicates: int) -> list[str]:
    names = []

    if duplicates < 0: # Returns list of unique names
        names = [fake.unique.name() for _ in range(total_amount)]
    elif duplicates > 0: # Returns list of names containing duplicates
        names = [fake.name() for _ in range(total_amount - duplicates)]
        names.extend(random.choices(names, k = duplicates))
        random.shuffle(names)

    return names

# 1. Calculates frequency of each letter in a list of names
def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letter_frequency = defaultdict(int)
    for name in names:
        for letter in name.upper():
            letter_frequency[letter] += 1

    return letter_frequency

# 2. Calculates frequency of each letter in a list of names
def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letters = [letter.upper() for name in names for letter in name]
    return Counter(letters)

main()