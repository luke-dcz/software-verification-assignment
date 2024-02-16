from hypothesis import given, strategies as st

""" 

Advanced example to test manipulating data structures.

Challenges:
- Ensure merged BSTs contain all elenents from both input trees.
- Maintains BST property, for every node, left subtree is less than node, right is more.

"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert_into_bst(root, value):
    """Inserts a new value into the binary search tree."""

    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.right, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


def bst_to_list(root):
    """Converts a binary search tree to a list for Hypothesis."""

    if root is None:
        return []
    return bst_to_list(root.left) + [root.value] + bst_to_list(root.right)


def merge_bst(root_one, root_two):
    """Create a new binary search tree from two separate BSTs."""

    all_values = bst_to_list(root_one) + bst_to_list(root_two)
    all_values.sort()

    # Create new BST.
    new_root = None
    for value in all_values:
        new_root = insert_into_bst(new_root, value)
    return new_root


def bst_strategy():
    return st.recursive(
        base=st.none(),
        extend=lambda children: st.builds(
            TreeNode,
            value=st.integers(),
            left=children,
            right=children
        ),
    )


@given(bst1=bst_strategy(), bst2=bst_strategy())
def test_merge_bsts_properties(bst1, bst2):
    """Hypothesis tests to check if new BST is correctly sorted and contains all elements."""

    # Check if elements from BST are correctly sorted.
    merged = merge_bst(bst1, bst2)
    merged_list = bst_to_list(merged)
    assert merged_list == sorted(merged_list), "Merged BST is not correctly sorted"

    # Check if elements from both BSTs exist.
    bst1_list = bst_to_list(bst1)
    bst2_list = bst_to_list(bst2)
    assert all(val in merged_list for val in bst1_list + bst2_list), "Merged BST is missing elements"


test_merge_bsts_properties()
