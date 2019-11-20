from csv import reader
import math
import copy
from PIL import Image

test_image = []

# open the image
img = Image.open('number.png').convert('L')
for pixel in iter(img.getdata()):
    test_image.append(abs(pixel-255))

# draw the image
for i in range(28*28):
    if test_image[i] < 122:
        print('_', end = ' ')
    else:
        print('@', end = ' ')
    if i%28 == 0 and i != 0:
        print()
print()

# open testing set
with open('./datasets/mnist_test.csv') as raw_test_data:
    csv_reader = reader(raw_test_data, delimiter = ',')

    test_data = []

    for line in csv_reader:
        pixels = [int(x) for x in line[1:]]
        test_data.append([int(line[0]), pixels])

def euclidean(point1, point2):
    distance = 0.0

    for i in range(len(point1[1])):
        distance += (point1[1][i] - point2[1][i]) ** 2
    return math.sqrt(distance)

def nkk(image, images, k, training):
    labels = []

    shortest_distances = []
    
    for i in images:
        current_distance = euclidean(i, image)
        # if current_distance with the same point
        if current_distance == 0:
            continue
        elif len(shortest_distances) < k:
            shortest_distances.append(current_distance)
            label = [i, current_distance]
            labels.append(label)
        else:
            # check if the shortest distance is shorter then the largest one currently stored
            for j in range(k):
                if labels[j][1] > current_distance:
                    shortest_distances[shortest_distances.index(max(shortest_distances))] = current_distance
                    label = [i, current_distance]
                    labels[j] = copy.deepcopy(label)
                    break

    value = []
    for i in labels:
        value.append(i[0][0])
    result = max(set(value), key = value.count)
    
    if training == 0:
        print('With k = %d I think this is a %d.' % (k, result))

training = input('Training [1/0]: ')

if training[0] == '1':

    # open training set

    with open('./datasets/mnist_train.csv') as raw_training_data:
        csv_reader = reader(raw_training_data, delimiter = ',')

        training_data = []

        for line in csv_reader:
            pixels = [int(x) for x in line[1:]]
            training_data.append([int(line[0]), pixels])

    # do actual training
    for i in range(3,10):
        correct = 0
        for test_image in test_data:
            result = nkk(test_image, training_data, i, 1)
            if test_image[0] == result:
                correct += 1

        percentage = correct/len(test_data) * 100.0
        print(k, percentage)
else:
    nkk([0, test_image], training_data, 5, 0)