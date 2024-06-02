def subSetSum(i, sum, arr, ans):
    if len(arr) == i:
        ans.append(sum)
        return
    subSetSum(i + 1, sum + arr[i], arr, ans)
    subSetSum(i + 1, sum, arr, ans)
    return ans

subset = subSetSum(0, 0, [5, 2, 1], [])
subset.sort()
print(subset)