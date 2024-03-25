# Жадный алгоритм, используя множества и хеш-таблицы (словари).
# Здесь нам нужно найти набор радиостанций для покрытия определенного количество штатов, используя жадный алгоритм.

# Множество - это тип структуры данных, похожий на список, который не может иметь дубликаты.
# Создаем множество "states_needed", которое хранит перечень штатов для покрытия.
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}

# Создаем словарь "stations", в котором его ключи представляет из себя имена радиостанций,
# а его значения представляют из себя штаты для покрытия этими радио станциями.
# В этом словаре значения являются множествами.
stations = {"kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "са"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}

# Создаем множество "final_stations", которое хранит итоговый набор радиостанций для покрытия штатов.
# Изначально этот словарь пустой.
final_stations = set()
# Создаем цикл while, который генерирует итоговый набор радиостанций для покрытия штатов "final_stations".
# Этот цикл while работает, пока множество "states_needed" не является пустым,
# то есть пока у нас имеются непокрытые штаты.
while states_needed:
    # Создаем переменную "best_station", которая хранит имя радиостанции,
    # покрывающей больше всего штатов, которые еще не покрыты.
    # Изначально эта переменная хранит "None".
    best_station = None
    # Создаем переменную "states_covered", которая хранит множество штатов,
    # которые еще не покрыты и могут быть покрыты радиостанцией "best_station".
    # Изначально эта переменная хранит пустое множество.
    states_covered = set()
    # Создаем цикл for, в котором мы перебираем все ключи ("station") и значения ("states_for_station")
    # в словаре "stations" и находим радиостанцию "best_station".
    for station, states_for_station in stations.items():
        # Создаем переменную "covered", которая хранит множество штатов,
        # которые еще не покрыты и которые могут быть покрыты текущей радиостанцией "station".
        # Мы находимо это множество путем пересечения следующих множеств:
        # 1. "states_needed" - множество еще не покрытых штатов.
        # 2. "states_for_station" - множество штатов, которые может покрыть текущая радиостанция "station".
        covered = states_needed & states_for_station
        # Если множество "covered" больше, чем множество "states_covered", то
        if len(covered) > len(states_covered):
            # текущая радиостанция "station" становится новой лучшей радиостанцией "best_station",
            best_station = station
            # а также мы обновляем множество "states_covered".
            states_covered = covered
    # После работы каждого цикла for мы уменьшаем перечень штатов, которые необходимо покрыть,
    # вычитая список штатов, которые покрываются текущей лучшей радиостанцией "best_station".
    # Мы это делаем путем вычитания из множества "states_needed" множества "states_covered".
    states_needed -= states_covered
    # А также после работы каждого цикла for мы добавляем текущую лучшую радиостанцию "best_station"
    # в итоговый набор радиостанций "final_stations".
    # Для добавления нового элемента в множества мы используем метод "add".
    final_stations.add(best_station)

# Выводим на экран итоговый набор радиостанций для покрытия штатов "final_stations".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
print(final_stations)
