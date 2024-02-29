from matplotlib import pyplot as plt, gridspec
from wordcloud import WordCloud
from faker import Faker

from collections import Counter
from statistics import mean, median
import random

fake = Faker()

def main():
    names = generate_name_list(10, 2)
    unique_names = list(set(names))
    sorted_unique_names = sorted(unique_names, key=lambda n: (-len(n), n))

    letter_frequency = calculate_letter_frequency(sorted_unique_names)
    print(letter_frequency)

    fig = plt.figure(figsize=(10, 8))

    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1]) 

    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[2:])
    ax3 = plt.subplot(gs[1])

    plt.subplots_adjust(hspace = 0.5)

    x, y = zip(*letter_frequency.items())

    ax1.bar(x, y)
    ax1.set_title("Frequency of each letter in list of names")

    wordCloud = WordCloud().generate_from_frequencies(letter_frequency)

    ax2.imshow(wordCloud, interpolation="bilinear")
    ax2.axis("off")

    name_len = list(map(lambda n: len(n), names))
    mean_len = mean(name_len)
    median_len = median(name_len)

    ax3.barh(names, name_len)
    ax3.axvline(mean_len, color="red", linestyle="--", label="Average")
    ax3.axvline(median_len, color="blue", linestyle="--", label="Median")
    ax3.legend()
    ax3.set_title("Lenght of names")
  
    plt.show()

def generate_name_list(total_amount: int, duplicates: int) -> list[str]:
    names = []

    if duplicates <= 0: # Returns list of unique names
        names = [fake.unique.name() for _ in range(total_amount)]
    elif duplicates > 0: # Returns list of names with duplicates
        names = [fake.first_name() for _ in range(total_amount - duplicates)]
        names.extend(random.choices(names, k = duplicates))
        random.shuffle(names)

    return names

def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letters = [letter.upper() for name in names for letter in name]
    return Counter(letters)

main()