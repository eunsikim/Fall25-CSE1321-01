def main():
    my_List = [3, 3.14, True, False, "Hello", "World", [], [], ()]

    my_2d_list = [
        [1, 2, 3, 4],
        ["Hello", "World"]
    ]

    print(my_2d_list[1][1])

    my_3d_list = [
        [1, 2, 3, 4],
        ["Hello", "World", [3.14, True, False]]
    ]

    print(my_3d_list[1][2][0])
    

if __name__ == "__main__":
    main()