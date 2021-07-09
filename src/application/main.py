import blessed


def main() -> str:
    """
    This is a start of application's structure
    """
    term = blessed.Terminal()
    return "Hello World!"


if __name__ == '__main__':
    main()
