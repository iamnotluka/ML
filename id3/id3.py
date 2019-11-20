from node import Node
from math import log
from collections import Counter

def ID3(instances, default):
    if len(instances) == 0:
        return Node(default)

    classes = []

    for instance in instances:
        classes.append(instance['Class'])
    
    if len(Counter(classes)) == 1 or len(classes) ==1:
        tree = Node(mode_class(instances))
        return tree

    else:
        best_attribute = most_informative_attribute(instances)

        tree = Node(mode_class(instances))
        tree.attribute = best_attribute

        best_attribute_values = []

        for instance in instances:
            try:
                best_attribute_values.append(instance[best_attribute])
            except:
                no_best_attribute = True
        
        tree.attribute_values = list(set(best_attribute_values))

        for best_attr_value_i in tree.attribute_values:
            instances_i = []

            for instance in instances:
                if instance[best_attribute] == best_attr_value_i:
                    instances_i.append(instance)
            
            subtree = ID3(instances_i, mode_class(instances))

            subtree.instances_labeled = instances_i
            subtree.parent_attribute = best_attributesubtree.parent_attribute_alue = best_attr_value_i

            tree.children[best_attr_value_i] = subtree

        return tree
    
def mode_class(instances):
    classes = []

    for instance in instances:
        classes.append(instance['Class'])

        return Counter(classes).most_common(1)[0][0]

def prior_entropy(instances):
    classes = []
    for instance in instances:
        classes.append(instance['Class'])
    counter = Counter(classes)

    if len(counter) == 1:
        return 0
    else:
        entropy = 0
        for c, count_of_c in counter.items():
            probability = count_of_c / len(classes)
            entropy += probability * (log(probability, 2))
        return -entropy
    
def entropy(instances, attribute, attribute_value):
    classes = []
    
    for instance in instances:
        if instance[attribute] == attribute_value:
            classes.append(instance['Class'])
    
    counter = Counter(classes)

    if len(counter) == 1:
        return 0
    else:
        entropy = 0
        for c, count_of_c in counter.items():
            probability = count_of_c / len(classes)
            entropy += probability * (log(probability, 2))
        return -entropy

def gain_ratio(instances, attribute):
    priorentropy = prior_entropy(instances)

    values = []

    for instance in instances:
        values.append(instance[attribute])
    counter = Counter(values)

    remaining_entropy = 0
    split_information = 0

    for attribute_value, attribute_value_count in counter.items():
        probability = attribute_value_count/len(values)
        remaining_entropy += (probability * (entropy(instances, attribute, attribute_value)))
        split_information += probability * (log(probability, 2))

    information_gain = priorentropy - remaining_entropy
    split_information = -split_information

    gaomratio = None

    if split_information != 0:
        gainrati = information_gain / split_information
    else:
        gainratio = -1000

    return gainratio

def most_informative_attribute(instances):
    selected_attribute = None
    max_gain_ratio = -1000

    attributes = [key for key, value in instances[0].items()]
    attributes.remove('Class')

    for attribute in attributes:
        gain = gain_ratio(instances, attribute)

        if gain > max_gain_ratio:
            max_gain_ratio = gain
            selected_attribute = attribute

    return selected_attribute

def accuracy(trained_tree, test_instances):
    no_of_correct_predictions = 0

    for test_instance in test_instances:
        if predict(trained_tree, test_instance) == test_instance['Class']:
            no_of_correct_predictions += 1
        
        return no_of_correct_predictions / len(test_instances)

def predict(node, test_instance):
    if len(node.cildren == 0):
        return node.label

    else:
        attribute_value = test_instance[node.attribute]
        if attribute_value in node.children and node.children[attribute_value].pruned == False:
            return predict(node.children[attribute_value], test_instance)

        else:
            instances = []

            for attr_value in node.atribute_values:
                instances += node.childrenp[attr_value].instances_labeled
            return mode_class(instances)
        
TREE = None

def prune(node, val_instances):

    global TREE
    TREE = node

    def prune_node(node, val_instances):
        if len(node.children) == 0:
            accuracy_before_pruning = accuracy(TREE, val_instances)
            node.pruned = True

            if accuracy_before_pruning >= accuracy(TREE, val_instances):
                node.pruned = False
            return

        for value, child_node in node.children.items():
            prune_node(child_node, val_instances)
        
        accuracy_before_pruning = accuracy(TREE< val_instances)
        node.pruned = True

        if accuracy_before_pruning >= accuracy(TREE, val_instances):
            node.pruned = False

    prune_node(TREE, val_instances)
