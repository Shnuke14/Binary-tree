class Node:
  def init(self, value):
      self.value = value
      self.left = None
      self.right = None

## Создание рекурсивной функции прямого бинарного дерева
def pre_order(node):
  if node:
      print(node.value)
      pre_order(node.left)
      pre_order(node.right)

## Создание рекурсивной функции бинарного дерева правого вывода
def post_order(node):
  if node:
      post_order(node.left)
      post_order(node.right)
      print(node.value)

def in_order(node):
  if node:
    in_order(node.left)
    print(node.value)
    in_order(node.right)

## Создание значений
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

## Вызов рекурсивной функции бинарного дерева прямого обхода
pre_order(tree)

## Вызов рекурсивной функции бинарного дерева обратного обхода
post_order(tree)

## Вызов рекурсивной функции бинарного дерева симметричного обхода
in_order(tree)