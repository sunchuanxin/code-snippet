# 冒泡排序
def bubbleSort(arr):
    for i in range(0, len(arr) - 1):  # 确定循环次数 比长度-1 最后一个数默认排好了
        for j in range(0, len(arr) - i - 1):  # 每次比较减去已经比较的数量再-1 因为有 j+1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 选择排序
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    arr = [5, 3, 4, 2, 1]
    for i in range(len(arr)):
        print(arr[i], i)

    sorted()
    # d = bubbleSort(arr)
    # print(d)
