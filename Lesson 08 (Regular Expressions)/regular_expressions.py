import re


def find_email(text):
    match = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
    return match.group() if match else None


def is_valid_phone(phone):
    return re.fullmatch(r"\d{3}-\d{3}-\d{4}", phone) is not None


def extract_numbers(text):
    return re.findall(r"\d+", text)


def format_dates(text):
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", text)


def split_words(text):
    return re.split(r"\s+", text.strip())


def contains_word(text, word):
    return re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE) is not None


def main():
    print(find_email("Contato: aluno@example.com"))
    print(is_valid_phone("617-495-1000"))
    print(extract_numbers("CS50 tem 8 aulas e 3 projetos."))
    print(format_dates("A aula foi em 2026-10-08."))
    print(split_words("Python   usa\texpressões regulares"))
    print(contains_word("Estou aprendendo Python.", "python"))


if __name__ == "__main__":
    main()