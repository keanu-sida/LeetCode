class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)                   # ensure that the shift doesn't "lap" itself
        nums[:] = nums[-k:] + nums[:-k]     # push last k elements to start of nums (rightshift)