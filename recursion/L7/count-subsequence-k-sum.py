class Solution():
    def f(self, i, arr, s, k, n):
        if i == n:
            if k == s:
                return 1
            else:
                return 0

        s += arr[i]
        l = self.f(i + 1, arr, s, k, n)

        s -= arr[i]
        r = self.f(i + 1, arr, s, k, n)

        return l + r


arr = [1, 2, 1]
n = len(arr)
s = Solution()
print(s.f(0, arr, 0, 2, n))
