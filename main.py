from collections import defaultdict

def main():
    names = ["Frank", "Alice", "Judy", "Bob", "Ivan", "Dave", "Heidi", "Charlie", "Eve", "Grace"]
    sorted_names = sorted(names, key=lambda n: (-len(n), n))

    letter_frequency = calculate_letter_frequency(sorted_names)
    sorted_letter_frequency = dict(sorted(letter_frequency.items(), key=lambda item: -item[1]))

    print(sorted_letter_frequency)

def calculate_letter_frequency(names: list[str]) -> dict[str, int]:
    letter_frequency = defaultdict(int)
    for name in names:
        for letter in name.upper():
            letter_frequency[letter] += 1

    return letter_frequency

main()