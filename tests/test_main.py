from application.main import main


def test_launch():
    """
    This is the example test that shows that package initialises without errors
    """
    result = main()
    assert result == "Hello World!"