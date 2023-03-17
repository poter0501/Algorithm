import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def search_data(self, data):
        result = None
        if self.data == data:
            return self
        if self.left is not None:
            result = self.left.search_data(data)
            if result is not None:
                return result
        if self.right is not None:
            result = self.right.search_data(data)
            if result is not None:
                return result
        if self.left is None and self.right is None:
            return None
    
    def preorder_traversal(self, result):
        temp = self.data  # 본인
        
        if self.left is not None:  # 왼쪽
            temp += self.left.preorder_traversal(temp)
            
        if self.right is not None:  # 오른쪽
            temp += self.right.preorder_traversal(temp)
        
        return temp

    def inorder_traversal(self, result):
        temp = result
        
        if self.left is not None:  # 왼쪽
            temp = self.left.inorder_traversal(temp)
            
        temp += self.data  # 본인
        
        if self.right is not None:  # 오른쪽
            temp = self.right.inorder_traversal(temp)
    
        return temp

    def postorder_traversal(self, result):
        temp = result
    
        if self.left is not None:  # 왼쪽
            temp = self.left.postorder_traversal(temp)
    
        if self.right is not None:  # 오른쪽
            temp = self.right.postorder_traversal(temp)

        temp += self.data  # 본인
    
        return temp


def main():
    n = int(sys.stdin.readline())
    root = Node('')
    for i in range(n):
        data, left_data, right_data = sys.stdin.readline().rstrip().split()
        if i == 0:
            root.data = data
            if left_data != '.':
                root.left = Node(left_data)
            
            if right_data != '.':
                root.right = Node(right_data)
        else:
            temp = root.search_data(data)
            if temp is not None:
                if left_data != '.':
                    temp.left = Node(left_data)
                if right_data != '.':
                    temp.right = Node(right_data)
    print(root.preorder_traversal(''))
    print(root.inorder_traversal(''))
    print(root.postorder_traversal(''))


if __name__ == '__main__':
    main()
