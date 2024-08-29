from collections import defaultdict

class MapReduce:
    def __init__(self, input_content):
        self.input_content = input_content

    def split_and_map(self):
        # Split input content into lines and words
        lines = self.input_content.split("\n")
        word_pairs = []
        for line in lines:
            words = line.split()
            for word in words:
                word_pairs.append((word, 1))
        return word_pairs

    def shuffle_and_reduce(self, word_pairs):
        # Create a dictionary to store word counts
        word_count_dict = defaultdict(int)

        # Reduce step: combine counts for each word
        for word, count in word_pairs:
            word_count_dict[word] += count

        return dict(word_count_dict)

if __name__ == "__main__":
    input_content = """Deer Bear River
Car Car River
Deer Car Bear"""

    mr = MapReduce(input_content)
    word_pairs = mr.split_and_map()
    word_counts = mr.shuffle_and_reduce(word_pairs)

    # Print the final word counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")
