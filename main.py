def main():
    names = ["Frank", "Alice", "Judy", "Bob", "Ivan", "Dave", "Heidi", "Charlie", "Eve", "Grace"]
    names.sort(key=lambda n: (-len(n), n))
    print(count_letter_frequency(names))

def count_letter_frequency(names: list[str]):
    letter_freq = {}
    for n in names:
        for l in n:
            capitalized_letter = l.capitalize()
            item = letter_freq.setdefault(capitalized_letter, 0)
            letter_freq.update({capitalized_letter: item + 1})

    return letter_freq

main()