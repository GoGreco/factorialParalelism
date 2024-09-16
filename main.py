import multiprocessing as mp



def calc(number, fila):
    multi = 1

    for i in range(1, number+1):
        multi *= i  
    
    fila.put(multi)

if __name__ == '__main__':

    fila = mp.Queue()
    numbers =[9,2,3,4,2]

    factorial = []

    processesList =[]

    for i in range(len(numbers)):

        processesList.append(mp.Process(target=calc , args=(numbers[i], fila)))
        processesList[i].start()
    for i in range(len(processesList)):
        processesList[i].join()


    position = 0
    while fila.empty() == False:
        
        factorial.append(fila.get())

    print(factorial)