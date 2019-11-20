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

    unique_classes = list(Counter(classes).keys())

    print('\nUnique classes\n| ', end = '')
    for i in unique_classes:
        print(i, end = ' | ')