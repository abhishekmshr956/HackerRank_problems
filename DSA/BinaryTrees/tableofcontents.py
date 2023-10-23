from generaltreeADT import LinkedGeneralTree

tree = LinkedGeneralTree()
# print(tree.size)
# print(tree.root)

paper = tree.addRoot("Paper")
title = tree.addChild(paper, "Title")
abstract = tree.addChild(paper, "Abstract")
chapter1 = tree.addChild(paper, "chapter1")
chapter2 = tree.addChild(paper, "chapter2")
chapter3 = tree.addChild(paper, "chapter3")
references = tree.addChild(paper, "References")

chapter1_1 = tree.addChild(chapter1, "chap1.1")
chapter1_2 = tree.addChild(chapter1, "chap1.2")

chapter2_1 = tree.addChild(chapter2, "chap2.1")
chapter2_2 = tree.addChild(chapter2, "chap2.2")
chapter2_3 = tree.addChild(chapter2, "chap2.3")

chapter3_1 = tree.addChild(chapter3, "chap3.1")
chapter3_2 = tree.addChild(chapter3, "chap3.2")

# print(tree.size)
# print(tree.root.getElement())
# for c in tree.root.getChildren():
#     print(c.getElement(), end = " ")

for c in tree.positions():
    # print(" " * tree.depth(c), end = "")
    print("  " * tree.depth(c), c.getElement())

def printPreoderIndent(t, p, d):
    print("  " * d, p.getElement())
    for c in t.children(p):
        printPreoderIndent(t, c, d+1)

printPreoderIndent(tree, tree.root, 0)
