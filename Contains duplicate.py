#We can check an array in several ways to check whether it contains duplicates or not. The most common method is the “Brute Force method” But it has a time complexity of O(n2) and it is good for academic purposes only. But we another to solve our problem in less time complexity “Hash set method” or “Hash table method” this method is much more efficient than the “Brute Force method”. The Hash Set method takes the time complexity of O(n).*/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
            
        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False
            