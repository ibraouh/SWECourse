def permute(self, nums: List[int]) -> List[List[int]]:

    res = []
    n = len(nums)
    def solve(n, perm):
        if n==0:
            res.append(perm.copy())
            return None
        for i in range(len(nums)):
            if nums[i] in perm: continue
            perm.append(nums[i])
            solve(n-1, perm)
            perm.pop()
    solve(n, [])
    return res