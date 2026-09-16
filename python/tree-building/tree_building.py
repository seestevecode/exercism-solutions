"""Refactor a tree building algorithm"""

# pylint: disable=missing-function-docstring,missing-class-docstring
# pylint: disable=too-few-public-methods

class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


# pylint: disable=invalid-name
def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda record: record.record_id)

    # Record IDs must be 0, 1, 2, ...
    if [record.record_id for record in records] != list(range(len(records))):
        raise ValueError('Record id is invalid or out of order.')

    # Root must point to itself.
    if records[0].parent_id != 0:
        raise ValueError('Node parent_id should be smaller than its record_id.')

    for record in records[1:]:
        if record.parent_id == record.record_id:
            raise ValueError('Only root should have equal record and parent id.')

        if record.parent_id > record.record_id:
            raise ValueError('Node parent_id should be smaller than its record_id.')

    nodes = [Node(record.record_id) for record in records]

    for record in records[1:]:
        parent = nodes[record.parent_id]
        child = nodes[record.record_id]
        parent.children.append(child)

    return nodes[0]
    