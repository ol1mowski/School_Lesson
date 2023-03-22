from time import sleep


def endFile():
    end = str(input('Zakończyć program ?: '))
    if end == 'n':
        notepad()
    elif end =='t':
        exit()

def notepad():
    print('Witaj w programie Notatnik')
    print('---------------------------')
    print('Powiedz co chcesz zrobić: ')

    print('1. Zapis do nowego pliku')
    print('2. Otwarcie pliku')
    print('3. Otwarcie pliku i dopisz')

    choice = int(input('Wybierz liczbę: '))

    def choiceOne():
        print('Wybrałeś zapis do nowego pliku')
        sleep(1)
        print('Oto nowy plik: ')
        fileOne = open('file.txt', 'w')
        print('Napisz tu coś')
        string = str(input('|'))
        fileOne.write(string)
        fileOne.close()
        endFile()
        

    def choiceTwo():
        print('Wybrałeś Otwarcie pliku')
        sleep(1)
        patch = input('Podaj ścieżkę do pliku: ')
        print('Oto plik: ')
        fileTwo = open(patch, 'r')
        print('Oto twój plik: ')
        sleep(1)
        fileContent = fileTwo.read()
        print(fileContent)
        fileTwo.close()
        endFile()
        
    def choiceThree():
        print('Wybrałeś Otwarcie pliku i zapis nowych danych')
        sleep(1)
        patchT = input('Podaj ścieżkę do pliku: ')
        print('Oto plik: ')
        fileThree = open(patchT, 'r+')
        print('Oto twój plik: ')
        sleep(1)
        fileContent = fileThree.read()
        print(fileContent)
        string2 = str(input(''))
        fileThree.write(' ' + string2)
        fileThree.close()
        endFile()
        
    if choice == 1:
        choiceOne()
    elif choice == 2:
        choiceTwo()
    elif choice == 3:
        choiceThree()

notepad()