# -*- coding: utf-8 -*-
# 一、冒泡排序 BubbleSort，时间复杂度O(n2)
# 冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for j in range(1,n-i):    # 从第二个数到上次沉淀的数前的数，开始往前比较
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j],arry[j-1]      #如果前者比后者大，则交换两者
    return arry
print bubble_sort([1,3,2,5,6,4])

# 优化1、在i的情况下，如所有j都不需要和j-1交换顺序，则i不用再往后走了；如交换顺序，则一直往后走，设置flag
def bubble_sort1(arry):
    n = len(arry)
    for i in range(n):
        flag=1
        for j in range(1,n-i):
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j],arry[j-1]
                flag=0
        if flag:    # 如果所有j都没有交换顺序，说明该i后面的arry都是升序的，跳出该循环
            break
    return arry
print bubble_sort1([1,3,2,5,6,4])

# 优化2、每次遍历一边j，记录最后交换的位置j，该位置后已经排好序了，下一个i可以只走到该位置前
def bubble_sort2(arry):
    n = len(arry)
    stop=n
    for i in range(n):
        flag=1
        for j in range(1,stop):    # 对于每个i，j只需要遍历到stop位置
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j],arry[j-1]
                flag=0
                stop=j    # 记录位置，之后的已经排好序
        if flag:
            break
    return arry
print bubble_sort2([1,3,2,5,6,4])


# 二、选择排序 SelectionSort，时间复杂度O(n2)
# 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的起始位置。
# 以此类推，直到所有元素均排序完毕。
def select_sort(arry):
    n = len(arry)
    for i in range(0,n):
        min = i                             # 初始位置标记
        for j in range(i+1,n):
            if arry[j] < arry[min] :
                min = j                     # 找到最小值的位置
        arry[min],arry[i] = arry[i],arry[min]   #交换两者
    return arry
print select_sort([1,3,2,5,6,4])


# 三、插入排序 InsertionSort，时间复杂度O(n2)
# 插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 从第一个元素开始，该元素可以认为已经被排序
# 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 将新元素插入到该位置后
# 重复步骤2~5
def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]    #待插入前面已排序序列的数
            index = i        #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 倒着循环到 0
                if ary[j] > temp :
                    ary[j+1] = ary[j] #j往后移动一位，j本身暂时不变
                    index = j   #记录待插入下标。即j，j+1（待插入的数）=j（待插入的位置），j
                else :
                    break
            ary[index] = temp
    return ary
print insert_sort([1,3,2,5,6,4])


# 四、希尔排序 ShellSort，时间复杂度O(nlogn)~O(n2)
# 将数组分为几行列在一个表中，对每列分别进行插入排序，重复该过程的时候使用更少步长更多列。最后整个表就只有一列了。
def shell_sort(ary):
    n = len(ary)
    gap = n//2      #设置初始步长 , 数组分为两行（或多一个元素的第三行）
    while gap > 0 :
        for i in range(gap,n):        #从第二行开始，每一列的元素与上排相同位置对比，进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #与上一行相同位置的数对比
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = gap//2                     #重新设置步长
    return ary
print shell_sort([1,3,2,5,6,4])


# 五、归并排序 MergeSort，时间复杂度O(nlogn)
# 归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
# 先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
# 再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。然后合并排序相邻二个小组即可。
def merge_sort(ary):
    if len(ary) <= 1:
        return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]  # 加left数组剩余的数
    result += right[r:] # 加right数组剩余的数
    return result
print merge_sort([1,3,2,5,6,4])


# 六、快速排序 QuickSort，时间复杂度O(nlogn)
# 从数列中挑出一个元素作为基准数。
# 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
# 再对左右区间递归执行第二步，直至各区间只有一个数。
def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right:
        return ary      # 如数组为空或只有一个元素
    key = ary[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while ary[rp] >= key and lp < rp :
            rp -= 1    # 找到最右边小于基数的数
        while ary[lp] <= key and lp < rp :
            lp += 1    # 找到最左边大于基数的数
        ary[lp],ary[rp] = ary[rp],ary[lp]    #交换
    ary[left],ary[lp] = ary[lp],ary[left]    # 基数左右全部交换完后，将左边界left与最左边的数交换
    qsort(ary,left,lp-1)    # 左区间做相同排序
    qsort(ary,rp+1,right)   # 右区间做相同排序
    return ary
print quick_sort([1,3,2,5,6,4])


# 七、堆排序 HeapSort，时间复杂度O(nlogn)
# 构建堆，将数组依次放入堆，并使上面都大于下面
# 将调整好的堆从上到下放入数组（不是有序的）
# 从堆的上面开始，一层一层往下比较，把下层较大的数和上层比较，并把其中大的换到上面。等到最下层，将顶端的大数换到最右下角，从堆中删去。
# 由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。

def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点，也就是倒数第二层最右边
    for start in range(first,-1,-1) :     #第一步，构造大根堆，将最顶端到first倒着遍历一遍
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #第二步，堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]  # 最上端和最下端交换后删除最下端最大数，再转换剩下的
        max_heapify(ary,0,end-1)
    return ary

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child    # 移动指针到该子节点
        else :
            break
print heap_sort([1,3,2,5,6,4])


# 来源http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/