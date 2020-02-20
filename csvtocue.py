import sys
import os
from os import path

# Настройки экспорта
inputfile = "markers.csv"
outputfile = "markers.cue"
podcastgenre = "Podcast"
podcastperformer = "Podcast Name"
podcastdate = "2020"
podcasttitle = "Podcast Episode Title"
podcastfilename = "filename.mp3"

# Открываем файл на чтение
if path.exists(inputfile):
    print("Открываем файл", inputfile, "на чтение")

    # С открытым файлом делаем следующее
    with open(inputfile) as f:
        # Читаем его по строчкам (отбрасываем символ новой строки)
        array = [line.rstrip('\n') for line in f]

        # Выкидываем первую строку массива целиком (всё равно там ерунда)
        del array[0]

        # Подсчитываем получившее количество строчек
        length = len(array)
        print("Всего строк в файле: ", length, "\n\n")

        # Построчно делаем массив для каждой строки
        for oneline in array:
            # Разделяем по табам в массив
            newline = oneline.split("\t")

            # Отбрасываем миллисекунды (они не нужны)
            timearray = newline[1].split(".")
            time = timearray[0]
            chaptername = newline[0]

            print("Глава %d:", chaptername, "время:", time)

        # Пока у нас открыт файл на чтение, мы можем открыть файл на запись
        with open(outputfile, 'w') as filetowrite:
            print("\n\nОткрываем файл", outputfile, "на запись")
            content = print("REM GENRE", podcastgenre, "\n")
            filetowrite.write(content)


else:
    print("Файл", inputfile, "не найден!")
