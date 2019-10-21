
CONTRACT_DOCS = {
    "Gosudarstvenny_kontrakt_77.docx": (list(range(3, 9)), [1] * len(list(range(3, 10 + 1)))),
    "doc14.docx": ([0, 1, 2, 3, 4], [1, 1, 1, 1, 1]),
    "doc5.docx": ([0, 1, 2, 3, 4], [1, 1, 1, 1, 1])
}

KEYWORDS_FILE = "keywords.pickle"

STOP_WORDS = [
    "на", 'из', 'в', 'от', 'с', 'др.', 'и', ',', '.', '(', ')', '!', '?', 'при', 'ежедневно', 'по', 'до'
]

PUNCTUATION = '.()!,?'
