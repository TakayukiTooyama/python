# プロパティ（getter, setter）属性（public, _protected, __private）

class Car:
    def __init__(self, model=None, enable_auto_run=False, enable_electric_run=False):
        # public
        self.model = model
        # protected（どうしても外から変えたい時はsetter, getter）
        self._enable_auto_run = enable_auto_run
        # private
        self.__enable_electric_run = enable_electric_run


    # read 可（getter）
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # write 可（setter）
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    # private
    def electric_car(self):
        print('電気運転中' if {self.__enable_electric_run} == True else 'ガソリン運転中')

car = Car()

# public（読み込み, 書き込み可）
car.model = 'Lexus'
print(car.model) # Lexus

# _では読み込めてしまう
print(car._enable_auto_run) # False
# __は外からは読み込めない
# print(car.__enable_electric_run)

# getter, setterにより読み込み, 書き込み可
car.enable_auto_run = True
print(car.enable_auto_run) # True
