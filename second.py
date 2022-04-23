nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [-7,-8,7,5,7,1,6,0]
k = 4
def maxSlidingWindow(nums, k):
    queue = []
    res = []
    for i in range(k):
        if not queue or queue[-1] > nums[i]:
            queue.append(nums[i])
        else:
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
    res.append(queue[0])

    for i in range(k, len(nums)):
        outElement = nums[i - k]
        inElement = nums[i]

        if outElement == queue[0]:
            queue.pop(0)
        if not queue or queue[-1] > inElement:
            queue.append(inElement)
        else:
            while queue and queue[-1] < inElement:
                queue.pop()
            queue.append(inElement)
        res.append(queue[0])

    return res

print(maxSlidingWindow(nums, k))