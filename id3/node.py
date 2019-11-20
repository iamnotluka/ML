class Node:
    def __init__(self, label):
        self.attribute = None
        self.attribute_values = []
        self.label = label
        self.children = {}

        self.parent_attribute = None
        self.parent_attribute_value = None

        self.pruned = False
        self.instances_labeled = []