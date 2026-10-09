import stats


def test_mean():
    assert stats.mean([1, 2, 3, 4]) == 2.5
    assert stats.mean([5]) == 5
    assert stats.mean([-1, 0, 1]) == 0


def test_median_odd_length():
    assert stats.median([3, 1, 2]) == 2


def test_median_even_length():
    # even-length must average the two middles
    assert stats.median([1, 2, 3, 4]) == 2.5
    assert stats.median([4, 1, 3, 2]) == 2.5


def test_mode():
    assert stats.mode([1, 2, 2, 3]) == 2


def test_mode_ties_broken_by_first_appearance():
    assert stats.mode([1, 1, 2, 2]) == 1
