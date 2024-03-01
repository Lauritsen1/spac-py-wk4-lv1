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

    # Print data to console
    print(f"\033[92m 1. names:\033[0m {names}\n")
    print(f"\033[93m 2. unique_names:\033[0m {unique_names}\n")
    print(f"\033[94m 3. sorted_unique_names:\033[0m {sorted_unique_names}\n")
    print(f"\033[95m 4. letter_frequency:\033[0m {letter_frequency}\n")

    # Figure/Plot layout and styling
    plt.style.use('bmh')

    fig = plt.figure(tight_layout=True, figsize=(8, 6))
    fig.subplots_adjust(hspace=0.5)

    gs = fig.add_gridspec(2, 2)

    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[2:])
    ax3 = plt.subplot(gs[1])

    # Bar chart showing frequency of letters
    letter, frequency = zip(*letter_frequency.items())
    ax1.bar(letter, frequency)

    # Wordcloud showing letters with sizes depending on frequency
    wordCloud = WordCloud().generate_from_frequencies(letter_frequency)
    ax2.imshow(wordCloud, interpolation="bilinear")
    ax2.axis("off")

    # Bar chart showing lenght of names and average length
    unique_name_lengths = list(map(lambda n: len(n), sorted_unique_names))
    average_name_length = mean(unique_name_lengths)
    median_name_length = median(unique_name_lengths)
    ax3.barh(sorted_unique_names, unique_name_lengths)
    ax3.axvline(average_name_length, color="red", linestyle="--", label="Average")
    ax3.axvline(median_name_length, color="blue", linestyle="--", label="Median")
    ax3.legend()

    plt.show()

# Maps unique letters to their frequencies
def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letters = [letter.upper() for name in names for letter in name]
    return dict(Counter(letters).most_common())

if __name__ == "__main__":
    main()