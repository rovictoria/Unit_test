import pytest
from check_average import Check_Average

class TestAverage:

    def test_equal(self):
        average = Check_Average()
        result = average.compare_averages([1, 2, 3], [1, 2, 3])
        assert result == 'Средние значения равны'

    def test_first_greater(self):
        average = Check_Average()
        result = average.compare_averages([1, 2, 3], [1, 2])
        assert result == 'Первый список имеет большее среднее значение'

    def test_second_greater(self):
        average = Check_Average()
        result = average.compare_averages([1, 2], [1, 2, 3])
        assert result == 'Второй список имеет большее среднее значение'

    def test_empty_first(self):
        average = Check_Average()
        with pytest.raises(AssertionError):
            average.compare_averages([], [1, 2, 3])

    def test_empty_second(self):
        average = Check_Average()
        with pytest.raises(AssertionError):
            average.compare_averages([1, 2, 3], [])