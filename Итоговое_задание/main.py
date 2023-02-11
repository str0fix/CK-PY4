class City:
    """
    Родительский класс город
    """
    def __init__(self, arg1: str):
        """
        Делаем экземпляр города
        :param arg1: Страна, которая контроллирует город. Не предполагается, что страна может измениться.
        """
        self.__set_country_validation(arg1)
        self._country = arg1

    def __set_country_validation(self, country__: str):
        """
        Проверка корректности параметра country__ на соответствие типу str
        :param country__: проверяемый параметр
        """
        if not isinstance(country__, str):
            raise TypeError("Страна должна быть типа str")

    @property
    def country(self):
        """
        Getter для атрибута. setter'а не будет - если поменялась принадлежность к стране, то произошли огромные
        изменения в городе и нужно переинициализировать у всех экземпляров большую часть атрибутов
        Для этого необходимо создать новый (дочерний) экземпляр, чтобы избежать ошибок
        :return: возвращает атрибут. Его тип данных str
        """
        return self._country

    def __str__(self):
        return f"Город находится в {self.country}."

    def __repr__(self):
        return f"{self.__class__.__name__}(country={self.country!r})"

    def hail(self):
        """
        Метод для восхваления контроллирующей город страны
        :return: возвращается str с восхвалением
        """
        return f"ДА ЗДРАВСТВУЕТ {self.country}"

class Berlin(City):
    """
    Дочерний класс - конкретный город
    class City - родительский класс
    Атрибут класса __city_name - Все экземпляры класса Berlin имеют одно имя
    К этому аттрибуту нельзя приказаться -> __city_name
    """
    __city_name = "Berlin"

    def __init__(self, country_: str, year_: int):
        """
        Создаем экзепмпляр класса Berlin
        :param year_: Год, в котором экземпляр класса соответствовал реальности. Предполагается, что одному значению
        года соответствует свой экземпляр класса. Год измениться не может. Параметр предполагает год нашей эры.
        :param country_: Страна, контроллирующая город
        """
        super().__init__(country_)
        self.__set_year_validation(year_)
        self._year = year_

    def __set_year_validation(self, year__: int):
        """
        Проверка корректности присваемого значения атрибуту self.year
        Извне использовать нельзя - нарушает логику
        :param year__: Проверяемый параметр
        """
        if not isinstance(year__, int):
            raise TypeError("Год должен быть типа int")
        if year__ < 0:
            raise ValueError("Год должен быть неотрицательным целым числом! Поддерживается только год н.э.")

    @property
    def year(self):
        """
        Getter для параметра year. Setter отсутствует - необходимо создать новый экземпляр класса.
        :return: возвращает атрибут
        """
        return self._year

    @property
    def city_name(self):
        """
        Getter для параметра __city_name. Setter отсутствует - необходимо создать новый экземпляр класса.
        :return: возвращает атрибут
        """
        return self.__city_name

    def __str__(self):
        """
        Причина перегрузки: появился дополнительный атрибут, статическое поле
        """
        return f"{self.year} г. Город {self.city_name} контроллируется страной {self.country}."

    def __repr__(self):
        """
        Причина перегрузки: появился дополнительный атрибут
        """
        return f"{self.__class__.__name__}(country={self.country!r}, year={self.year})"

    def hail(self):
        """
        Метод для восхваления контроллирующей страны
        Причина перегрузки - нужно восхвалить теперь и Berlin и показать лояльность стране
        :return: возвращается str с восхвалением
        """
        return f"ДА ЗДРАВСТВУЕТ {self.country}! ПУСТЬ СЛАВИТСЯ {self.city_name}! {self.city_name} жемчужина {self.country}"





if __name__ == "__main__":
    # Write your solution here
    pass
