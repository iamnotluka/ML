# this is a five fold stratified cross validation code
import random
from collections import Counter

def get_five_folds(instances):
    print('[+] Doing the 5 fold stratified cross validation setup.')
    f0, f1, f2, f3, f4 = [], [], [], [], []

    # shuffle the data around
    random.shuffle(instances)
    classes = []

    # for each instance append the class
    for instance in instances:
        classes.append(instance['Class'])
        
    # after calling counter() -> {c1 : X, c2: X, c3: X...}
    # after doing counter().keys() -> {c1, c2, c3...}
    # after doing list(counter().key()) -> [c1, c2, c3...]
    unique_classes = list(Counter(classes).keys())

    # display unique classes
    print('\nUnique classes\n| ', end = '')
    for i in unique_classes:
        print(i, end = ' | ')

    # for each unique class, add it to the each fold rougly the same
    # ammount of time
    for uniqueclass in unique_classes:
        counter = 0

        for instance in instances:

            if uniqueclass == instance['Class']:
                if counter == 0:
                    f0.append(instance)
                    counter += 1
                
                elif counter == 1:
                    f1.append(instance)
                    counter += 1

                elif counter == 2:
                    f2.append(instance)
                    counter += 1
                
                elif counter == 3:
                    f3.append(instance)
                    counter += 1
                
                else:
                    f4.append(instance)
                    counter = 0

    
    # shuffle the folds again
    random.shuffle(f0)
    random.shuffle(f1)
    random.shuffle(f2)
    random.shuffle(f3)
    random.shuffle(f4)

    return f0, f1, f2, f3, f4
