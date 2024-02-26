class Check_Average:
    def calc_average(self, arr):
        return sum(arr) / len(arr)

    def compare_averages(self, arr1, arr2):
        assert len(arr1) > 0, f'{arr1} пуст'
        assert len(arr2) > 0, f'{arr2} пуст'
        average_1 = self.calc_average(arr1)
        average_2 = self.calc_average(arr2)

        if average_1 == average_2:
            return 'Средние значения равны'

        if average_1 > average_2:
            return 'Первый список имеет большее среднее значение'

        return 'Второй список имеет большее среднее значение'