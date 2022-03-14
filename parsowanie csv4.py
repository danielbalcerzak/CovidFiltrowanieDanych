import csv
import time

ALLOTMENT = "-" * 45


def take_file():
    while True:
        file = input('Wprowadź nazwę pliku lub ścieżkę do pliku: ')
        try:
            csv_file = open(file.strip('\u202a'))
            csv_file_sec = open(file.strip('\u202a'))
        except:
            print("Wprowadzono błędne dane. Spróbuj jeszcze raz")
            print(ALLOTMENT)
            continue
        else:
            reader_dict = csv.DictReader(csv_file)
            reader_list = list(csv.reader(csv_file_sec))
            print('Wczytałeś plik o nazwie', file)
            return reader_dict, reader_list, csv_file, csv_file_sec


def show_column(reader_list):
    print('Kolumny, które możesz przefiltrować to: ')
    for i in reader_list[0]:
        print(i, end=', ')
    print()


def take_column(reader_list):
    while True:
        column = input('Podaj kolumnę, którą chcesz przefiltrować: ')
        if column in reader_list[0]:
            return column
        else:
            print('Wprowadzono błędną kolumnę. Spróbuj jeszcze raz.')
            print(ALLOTMENT)
            continue


def take_value():
    value = input('Wpisz wartość, który chcesz wyświetlić: ')
    return value


def show_value(reader, column, csv_file):
    print('Wartości szczegółowe, które możesz zobaczyć to: ')
    print()
    list_value = []
    for row in reader:
        value = row[column]
        if value not in list_value:
            list_value.append(value)
    for i in list_value:
        print(i, end=', ')
    print()
    csv_file.seek(0)


def save_file(reader, column, data, reader_list):
    print('Czy chcesz zapisać filtrowane dane? Wciśnij [t] i zatwierdź')
    zgoda = input('Jeżeli nie chcesz zapisywać pliku wciśnij ENTER: ')
    print(ALLOTMENT)
    if zgoda.lower() == "t":
        while True:
            file_name = input('Podaj nazwę pod którą chcesz zapisać plik: ')
            print(ALLOTMENT)
            start_time = time.time()
            try:
                out_file = open(file_name, 'w')
            except:
                print("Nie wprowadzono danych. Spróbuj jeszcze raz")
                print(ALLOTMENT)
                continue
            else:
                for i in reader_list[0]:
                    out_file.write(str('{:^10}'.format(i))[:10] + '|')
                out_file.write('\n')
                for row in reader:
                    if row[column] == data:
                        for value in reader_list[0]:
                            dane = str('{:^10}'.format(row[value])[:10] + '|')
                            if reader_list[0].index(value) is len(reader_list[0]) - 1:
                                out_file.write(dane)
                                out_file.write('\n')
                            else:
                                out_file.write(dane + '')
                out_file.close()
                end_time = time.time()
                print('Plik zapisano pod nazwą', file_name)
                print('Zapis pliku trwał:', format(end_time - start_time, '.3f'), 'sek.')
                break

    else:
        print('Nie zapisano filtrowanych danych')


def show_data(reader, column, data, reader_list, csv_file):
    start_time = time.time()
    for i in reader_list[0]:
        print(str('{:^10}'.format(i))[:10] + '|', end=' ')
    print()
    records = 0
    rows = 0
    for row in reader:
        if row[column] == data:
            for value in reader_list[0]:
                dane = str('{:^10}'.format(row[value])[:10] + '|', )
                if reader_list[0].index(value) is len(reader_list[0]) - 1:
                    records += 1
                    print(dane)
                    rows += 1
                else:
                    records += 1
                    print(dane, end=' ')
    print('Wyświetlono', records, 'rekordów w', rows, 'wierszach')
    end_time = time.time()
    print('Czas wyszukiwania danych to: ', format(end_time - start_time, '.3f'), 'sek.')
    csv_file.seek(0)


def main():
    reader_dict, reader_list, csv_file, csv_file_sec = take_file()
    print(ALLOTMENT)
    show_column(reader_list)
    print()
    column = take_column(reader_list)
    print(ALLOTMENT)
    show_value(reader_dict, column, csv_file)
    print()
    value = take_value()
    print(ALLOTMENT)
    show_data(reader_dict, column, value, reader_list, csv_file)
    print(ALLOTMENT)
    save_file(reader_dict, column, value, reader_list)
    csv_file.close()
    csv_file_sec.close()
    print(ALLOTMENT)


main()
