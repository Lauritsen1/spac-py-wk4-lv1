from collections import Counter
from statistics import mean, median

from matplotlib import pyplot as plt
from wordcloud import WordCloud
from faker import Faker

def main():
    fake = Faker()

    # Data
    names = [fake.first_name() for _ in range(10)]
    unique_names = list(set(names))
    sorted_unique_names = sorted(unique_names, key=lambda n: (-len(n), n))

    letter_frequency = calculate_letter_frequency(sorted_unique_names)
    sorted_letter_frequency = dict(sorted(letter_frequency.items(), key=lambda item: -item[1]))

    # Figure/Plot layout and styling
    plt.style.use('bmh')

    fig = plt.figure(tight_layout=True, figsize=(8, 6))
    fig.subplots_adjust(hspace=0.5)

    gs = fig.add_gridspec(2, 2)

    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[2:])
    ax3 = plt.subplot(gs[1])

    # Bar chart showing frequency of letters
    letter, frequency = zip(*sorted_letter_frequency.items())
    ax1.bar(letter, frequency)

    # Wordcloud showing letters with sizes depending on frequency
    wordCloud = WordCloud().generate_from_frequencies(letter_frequency)
    ax2.imshow(wordCloud, interpolation="bilinear")
    ax2.axis("off")

    # Bar chart showing lenght of names and average length
    name_len = list(map(lambda n: len(n), sorted_unique_names))
    mean_len = mean(name_len)
    median_len = median(name_len)
    ax3.barh(names, name_len)
    ax3.axvline(mean_len, color="red", linestyle="--", label="Average")
    ax3.axvline(median_len, color="blue", linestyle="--", label="Median")
    ax3.legend()

    plt.show()

# Maps unique letters to their frequencies
def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letters = [letter.upper() for name in names for letter in name]
    return Counter(letters)

if __name__ == "__main__":
    main()