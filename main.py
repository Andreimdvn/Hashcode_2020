
in_file = "a_example.txt"
books_no = 0
lib_no = 0
days = 0
book_scores = []
libraries = []  # list of tuples (signup_process, books_per_day, list_of_books)


def parse_input():
    global books_no, books, lib_no, days, book_scores, libraries
    with open(in_file) as fin:
        books_no, lib_no, days = map(int, fin.readline().split())
        book_scores = list(map(int, fin.readline().split()))
        for i in range(lib_no):
            _, a, b = map(int, fin.readline().split())
            books = list(map(int, fin.readline().split()))
            libraries.append((a, b, books))
    print("Books: {} lib_no: {} days: {} books_scores: {}".format(books_no, lib_no, days, book_scores[:30]))


def main():
    parse_input()


if __name__ =="__main__":
    main()
