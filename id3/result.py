import id3
import parse
import random
import ffscv
from matplotlib import pyplot as plt

file_name = 'car.csv'

trace_runs_file = 'output.txt'
imagefile = 'output.png'

outputfile_tr = open(trace_runs_file, 'w')
outputfile_tr.write('Results for ID3 Algorithm.\n')

data = parse.parse(file_name)
pruned_accuracies_avgs = []

unpruned_accuracies_avgs = []

random.shuffle(data)

upper_limit = (round(len(data) * 0.9 * 0.8) - round(len(data) * 0.9 * 0.8) % 10) + 10

if upper_limit <= 10:
    upper_limit = 50

default = id3.mode_class(data)

validation_set = data[:1*len(data)//10]
data = data[1*len(data)//10:len(data)]

f0, f1, f2, f3, f4 = ffscv.get_five_folds(data)

testset = []
trainset = []

testset.append(f0)
trainset.append(f1 + f2 + f3 + f4)

testset.append(f1)
trainset.append(f0 + f2 + f3 + f4)

testset.append(f2)
trainset.append(f1 + f0 + f3 + f4)

testset.append(f3)
trainset.append(f1 + f2 + f0 + f4)

testset.append(f4)
trainset.append(f1 + f2 + f3 + f0)

print(len(trainset[0]))
step_size = len(trainset[0])//10

for length in range(10, upper_limit, step_size):
    print('Number of Training Instances:', length)
    outputfile_tr.write('Number of Training Instances: ' + str(length) + '\n')

    pruned_accuracies = []
    unpruned_accuracies = []

    for experiment in range(5):
        train = trainset[experiment][:length]
        test = testset[experiment]

        tree = id3.ID3(train, default)
        id3.prune(tree, validation_set)
        acc = id3.accuracy(tree, test)
        pruned_accuracies.append(acc)

        tree = id3.ID3(train,default)
        acc = id3.accuracy(tree, test)
        unpruned_accuracies.append(acc)

    avg_pruned_accuracies = sum(pruned_accuracies) / len(pruned_accuracies)
    avg_unpruned_accuracies = sum(unpruned_accuracies) / len(unpruned_accuracies)

    print('  Accuracy for Pruned tree: ' + str(avg_pruned_accuracies))
    print('Accuracy for Unpruned tree: ' + str(avg_unpruned_accuracies))

    outputfile_tr.write('  Accuracy for Pruned tree: ' + str(avg_pruned_accuracies) + '\n')
    outputfile_tr.write('Accuracy for Unpruned tree: ' + str(avg_unpruned_accuracies) + '\n')
    
    pruned_accuracies_avgs.append(avg_pruned_accuracies)
    unpruned_accuracies_avgs.append(avg_unpruned_accuracies)

outputfile_tr.close()

plt.plot(range(10, upper_limit, step_size), pruned_accuracies_avgs, label = 'pruned tree')
plt.plot(range(10, upper_limit, step_size), unpruned_accuracies_avgs, label = 'unpruned tree')

plt.xlabel('Number of training instances')
plt.ylabel('Classification accuracy on test instances')
plt.grid(True)
plt.title('Learning Curve for ' + str(file_name))
plt.legend()
plt.savefig(imagefile)
plt.show()
