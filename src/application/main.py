import blessed


def main() -> str:
    """This is a start of application's structure"""
    term = blessed.Terminal()
    # to avoid "never used" from flake
    print(term)
    return "Hello World!"


if __name__ == '__main__':
    main()
