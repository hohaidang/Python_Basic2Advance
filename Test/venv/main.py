import cv2
import numpy as np

class TESTCLASSS:
    list = None
    def __init__(self):
        list = [];
        list.append(1)
        list.append(2)
        list.append(3)
        self.list = list

    def modifyList(self):
        self.list[1] = 10;

def main():
    list1 = TESTCLASSS();
    list2 = TESTCLASSS();
    # list1.modifyList();
    list1.modifyList();
    for i in range(0, len(list1.list)):
        print(list1.list[i])
        print(list2.list[i])


if __name__ == "__main__":
    main()