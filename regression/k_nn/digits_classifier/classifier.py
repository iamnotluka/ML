from csv import reader
import math
import copy

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

def nkk(image, images, k):
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
    
    sureness = 0
    for i in labels:
        if i[0][0] == image[0]:
            sureness += 1
    
    value = []
    for i in labels:
        value.append(i[0][0])
    print(value)
    percentage = sureness/k * 100.0
    print('I am %f%% sure that this is a %d.' % (percentage, max(set(value), key = value.count)))

nkk(test_data[2], test_data, 4)
