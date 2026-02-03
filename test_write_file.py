from functions.write_file import write_file


def test():
    print("Testing...")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    print("Testing...")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    print("Testing...")
    result = write_file("calculator", "/mp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()
