from functions.get_files_info import get_files_info


def test():
    print("Testing...")
    result = get_files_info("calculator", ".")
    print(result)

    print("Testing...")
    result = get_files_info("calculator", "pkg")
    print(result)

    print("Testing...")
    result = get_files_info("calculator", "/bin")
    print(result)

    print("Testing...")
    result = get_files_info("calculator", "../")
    print(result)


if __name__ == "__main__":
    test()
