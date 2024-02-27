from collections import defaultdict, Counter
from matplotlib import pyplot as plt

def main():
    names = ["Frank", "Alice", "Judy", "Bob", "Ivan", "Dave", "Heidi", "Charlie", "Eve", "Grace"]
    sorted_names = sorted(names, key=lambda n: (-len(n), n))

    letter_frequency = calculate_letter_frequency(sorted_names)

    items = sorted(letter_frequency.items(), key=lambda item: -item[1])

    x, y = zip(*items)

    plt.bar(x, y)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Frequency of each letter in list of names')
    plt.show()

# First approach
def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letter_frequency = defaultdict(int)
    for name in names:
        for letter in name.upper():
            letter_frequency[letter] += 1

    return letter_frequency

# Second/Simpler approach
def calculate_letter_frequency(names: list[str]):
    letters = [letter.upper() for name in names for letter in name]
    return Counter(letters)

main()