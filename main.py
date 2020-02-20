
files = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
in_file = files[5]
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


def output_sol(sol):
    output_file = "sol_{}".format(in_file)
    with open(output_file, "w") as fout:
        fout.write("{}\n".format(len(sol)))
        for lib in sol:
            fout.write("{} {}\n".format(lib, len(libraries[lib][2])))
            fout.write("{}\n".format(" ".join([str(x) for x in libraries[lib][2]])))


def solve_c():
    lst = []
    book_duplicates = [0] * books_no
    for lib in libraries:
        lst.extend(lib[2])
        for l in lib[2]:
            book_duplicates[l] += 1

    print(len(lst))
    print(len(set(lst)))
    print(sum(book_duplicates)/len(book_duplicates))
    print(min(book_duplicates))
    print(max(book_duplicates))
    print("total signup: {}" .format(sum([x[0] for x in libraries])))

    lib_scores = []
    for lib in libraries:
        lib_scores.append(sum([book_scores[i] for i in lib[2]]))

    libs = list(range(0, lib_no))
    # sol = sorted(libs, key=lambda x: lib_scores[x], reverse=True)
    sol = sorted(libs, key=lambda x: lib_scores[x]//libraries[x][1], reverse=True)
    # sol = sorted(libs, key=lambda x: libraries[x][0])
    output_sol(sol)


def solve():
    lib_scores = []
    for lib in libraries:
        lib_scores.append(sum([book_scores[i] for i in lib[2]]))

    time = [0] * days
    lib_usage = [-1] * days
    # time_set = set()
    # could also improve if at each step remove the book from lib scores?
    for idx, lib in enumerate(libraries):
        if time[lib[0]] < lib_scores[idx]:
            time[lib[0]] = lib_scores[idx]
            # time_set.add(lib[0])
            lib_usage[lib[0]] = idx

    for idx, lib in enumerate(libraries):
        for t in range(days-1, -1, -1):
            if time[t] > 0:
                next_time = t + lib[0]
                if next_time < days:
                    if time[next_time] < time[t] + lib_scores[idx]:
                        time[next_time] = time[t] + lib_scores[idx]
                        lib_usage[next_time] = idx

    # for idx, lib in enumerate(libraries):
    #     if idx%1000 == 0:
    #         print(idx)
    #     for t in sorted(list(time_set), reverse=True):
    #         if time[t] > 0:
    #             next_time = t + lib[0]
    #             if next_time < days:
    #                 if time[next_time] < time[t] + lib_scores[idx]:
    #                     if time[next_time] == 0:
    #                         time_set.add(next_time)
    #                     time[next_time] = time[t] + lib_scores[idx]
    #                     lib_usage[next_time] = idx

    maxim = -1
    max_pos = 0
    for t in range(days-1, -1, -1):
        if time[t] > maxim:
            maxim = time[t]
            max_pos = t

    lib_sol = []
    t = max_pos
    while t > 0:
        lib_sol.append(lib_usage[t])
        t = t - lib_scores[lib_usage[t]]

    output_sol(lib_sol)
    pass


def nice_output_sol(sol, sol_books):
    output_file = "sol_{}".format(in_file)
    used_books = set()
    with open(output_file, "w") as fout:
        fout.write("{}\n".format(len(sol)))
        for idx, lib in enumerate(sol):
            # aux = [x for x in libraries[lib][2] if x not in used_books]
            # aux = sorted(aux, key= lambda x: book_scores[x], reverse=True)
            # for x in aux:
            #     used_books.add(x)
            fout.write("{} {}\n".format(lib, len(sol_books[idx])))
            fout.write("{}\n".format(" ".join([str(x) for x in sol_books[idx]])))


def solve_greedy():
    current_time = 0
    sol = []
    sol_books = []
    ignore_books = set()
    used_libs = set()
    while current_time < days:
        best_score = -1
        best_lib = -1
        best_sols = []
        for idx, lib in enumerate(libraries):
            if idx in used_libs:
                continue
            remaining_books = [b for b in lib[2] if b not in ignore_books]
            lst = sorted(remaining_books, key=lambda x: book_scores[x], reverse=True)
            remaining_time = days - current_time
            score = 0
            lst_idx = 0
            sols = []
            while remaining_time > 0 and lst_idx < len(lst):
                score += book_scores[lst[lst_idx]]
                sols.append(lst[lst_idx])
                lst_idx += 1
                remaining_time -= lib[1]
            if score > best_score:
                best_score = score
                best_lib = idx
                best_sols = sols

        # remove common books
        for book in libraries[best_lib][2]:
            ignore_books.add(book)
        sol.append(best_lib)
        sol_books.append(best_sols)
        used_libs.add(best_lib)
        current_time += libraries[best_lib][0]
        print(current_time)
    nice_output_sol(sol, sol_books)


def main():
    parse_input()
    solve_greedy()


if __name__ == "__main__":
    main()
