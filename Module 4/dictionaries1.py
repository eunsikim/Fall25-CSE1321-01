def main():
    s = "abc"
    n = [1, 2, 3]

    print(list(zip(s, n)))

    zip_to_list = list(zip(s, n))

    list_to_list = []

    for tup in zip_to_list:
        list_to_list.append(list(tup))
    
    print(list_to_list)

    my_dictionary = dict(list_to_list)

    print(my_dictionary)

    my_list = [["a", 1], ["b", 2], ["c", 3]]
    my_tuple = (("a", 1), ("b", 2), ("c", 3))

    print(dict(my_tuple))

if __name__ == "__main__":
    main()