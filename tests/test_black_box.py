from application.black_box import BlackBox


def test_box_creation() -> None:
    """Checks that black box is created properly"""
    box = BlackBox()
    assert isinstance(box, BlackBox)


def test_box_has_name() -> None:
    """Checks that you can name black boxes"""
    box = BlackBox('Cypher')
    assert box.name == 'Cypher'


def test_black_box_unsolved() -> None:
    """Checks that they are created unsolved"""
    box = BlackBox()
    assert box.solved is False


def test_box_can_be_solved() -> None:
    """They can be solved with correct solution"""
    box = BlackBox(solution='test')
    box.solve('test')
    assert box.solved is True


def test_wrong_values_leave_unsolved() -> None:
    """Wrong solutions won't solve them"""
    box = BlackBox(solution='test')
    box.solve('foo')
    assert box.solved is False
