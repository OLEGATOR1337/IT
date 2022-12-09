class NNClassifier:
  
    def func_for_hist(self):                                      # определяет на основе гистограмм тип нового объекта

        with open('object.txt', 'r', encoding='utf-8') as file1:
            new_hist = file1.readline().strip()[1:-1].split(',')
            new_hist = [int(i) for i in new_hist if i.strip().isdigit()]
                  
        with open('data.txt', 'r', encoding='utf-8') as file2:
            typ = file2.readline().strip()                        # находим тип, вышестоящий над гистограммой
            hist = file2.readline().strip()[1:-1].split(',')
            hist = [int(i) for i in hist if i.strip().isdigit()]  # представляем гистограмму из файла как список
            
            lens, types = [], []
            while hist:                                           # находим список расстояний и список типов
                x = 0
                for i in range(len(hist)):
                    x += (hist[i] - new_hist[i]) ** 2
                x = x ** 0.5
                lens.append(x)
                types.append(typ)

                typ = file2.readline().strip()
                hist = file2.readline().strip()[1:-1].split(',')
                hist = [int(i) for i in hist if i.strip().isdigit()]

            mins, three_types = [], []                            # список минимальных расстояний и список типов
            count = 0
            while count != 3:
                i = lens.index(min(lens))
                mins.append(lens[i])
                three_types.append(types[i])
                del lens[i]
                del types[i]
                count += 1

            if three_types.count(three_types[0]) >= 2:            # находит тип
                print('type of your object is', three_types[0])
            elif three_types.count(three_types[1]) >= 2:
                print('type of your object is', three_types[1])
            else:
                i = mins.index(min(mins))
                print('type of your object is', three_types[i])        
                
x = NNClassifier()
x.func_for_hist()












