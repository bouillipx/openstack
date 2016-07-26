__author__ = 'bouilli'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, n):
        return n[::-1]

    def add(self, x): #
        print x
        return x*100

    def abc(self, a, b, c):
        return a*100+b*10+c

    def add_digits(self, num):
        return (num - 1) % 9 + 1 if num != 0 else 0

    def intersection1(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

    def intersection2(self, nums1, nums2):
        result = []
        for num in nums1:
            if num in nums2:
                nums1.remove(num)
                result.append(num)
        return result

    def invertTree(self, root):
        if root:
            tmp = root.right
            root.right = root.left if root.left is None else invertTree(root.left)
            root.left = tmp if tmp is None else invertTree(tmp)
        return root

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return p == q

    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

    def reverseList(self, head):
        tmp = None
        curr = head
        while (curr != None and curr.next != None):
            tmp = curr.next.next
            curr.next.next = head
            head = curr.next
            curr.next = tmp
        return head

    def romanToInt(self, s):
        sum = 0
        tmp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        for i in xrange(len(s)):
            if i == len(s) - 1:
                sum += tmp[s[i]]
            elif tmp[s[i]] >= tmp[s[i+1]]:
                sum += tmp[s[i]]
            else:
                sum -= tmp[s[i]]

        return sum

    def isPowerOfThree(self, n):
        # return n > 0 and 1162261467 % n == 0
        if n == 1:
            return True
        elif n <= 0:
            return False
        while n != 3:
            if n % 3 != 0:
                return False
            n /= 3
        return True

    def isPowerOfTwo(self, n):
        return n & (n-1) == 0 if n > 0 else False

    def isUgly(self, num):
        if num == 1:
            return True
        elif num <= 0:
            return False
        if num % 2 == 0:
            return self.isUgly(num/2)
        elif num % 3 == 0:
            return self.isUgly(num/3)
        elif num % 5 == 0:
            return self.isUgly(num/5)
        return False

    def deleteDuplicates(self, head):
        curr = head
        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def isHappy(self, n):
        happy = [n]
        while n != 1:
            l = list(str(n))
            l = map(lambda x: int(x), l)
            n = 0
            for i in l:
                n += i * i
            if n in happy:
                break
            happy.append(n)
        return n == 1

    def climbStairs(self, n):
        # a(n) = a(n-1) + a(n-2)
        # if n < 3 :
        #     return n
        # a_n_1, a_n_2, sum = 1, 2, 0
        #
        # for i in xrange(3, n+1):
        #     sum = a_n_1 + a_n_2
        #     a_n_1, a_n_2 = a_n_2, sum
        # return sum

        if n == 0 or n == 1 or n == 2:
            return n
        import math
        two = n / 2
        sum = 0
        for i in xrange(two+1):
            sum += math.factorial(n-i) / math.factorial(i) / math.factorial(n-i-i)
        return sum

    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        tmp = 0
        curr = prices[0]
        for i in prices[1:]:
            if i > curr and i - curr > tmp:
                tmp = i - curr
            elif i <= curr:
                curr = i
        return tmp

    def hasCycle(self, head):   # 141
        pass

    def mergeTwoLists(self, l1, l2):    # 21
        head = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is None:
            curr.next = l2
        elif l2 is None:
            curr.next = l1
        return head.next

    def reverseVowels(self, s):     # 345
        # Time Limit Exceeded
        # vowels = list('aeiouAEIOU')
        # l = list()
        # ind = list()
        # for index, letter in enumerate(s):
        #     if letter in vowels:
        #         l.append(letter)
        #         ind.append(index)
        # l.reverse()
        # for i, v in enumerate(ind):
        #     s = s[:v] + l[i] + s[v+1:]
        # return s

        # vowels = list('aeiouAEIOU')
        # l = list(s)
        # first, last = 0, len(s) - 1
        # while first < last:
        #     if l[first] in vowels and l[last] in vowels:
        #         l[first], l[last] = l[last], l[first]
        #         first += 1
        #         last -= 1
        #     if l[first] not in vowels:
        #         first += 1
        #     if l[last] not in vowels:
        #         last -= 1
        # return ''.join(l)

        import re
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

        # vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        # return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)

    def swapPairs(self, head):
        result = head if head is None or head.next is None else head.next
        curr = ListNode(0)
        curr.next = head
        prev = curr
        curr = curr.next
        while curr and curr.next:
            prev.next = curr.next
            tmp = curr.next.next
            curr.next.next = curr
            curr.next = tmp
            prev = curr
            curr = tmp
        return result

    def rob(self, nums):    # 198
        # f(0) = nums[0]
        # f(1) = max(nums(1), nums(0))
        # f(k) = max(f(k-2) + nums[k], f(k-1))
        prev = 0
        now = 0
        for i in nums:
            prev, now = now, max(prev + i, now)
        return now

    def isPowerOfFour(self, num):    # 342
        # format = '{:b}'.format(num)
        # format = format[::-1]
        # count = format.count('1')
        # if count == 1 and num > 0:
        #     ind = format.find('1')
        #     if ind % 2 == 0:
        #         return True
        # return False
        import math
        return round(math.log(num, 4)) == math.log(num, 4) if num > 0 else False

    def removeElement(self, nums, val):    # 27
        count = nums.count(val)
        for i in xrange(count):
            nums.remove(val)
        return len(nums)

    def plusOne(self, digits):  # 66
        num = ''.join(map(str, digits))
        result = list(str(int(num) + 1))
        return map(int, result)

    def generate(self, numRows):    # 118
        if numRows > 1:
            result = [[1]]
            for i in xrange(numRows - 1):
                row = [1]
                for j in xrange(len(result[i]) - 1):
                    row.append(result[i][j] + result[i][j+1])
                row.append(1)
                result.append(row)
            return result
        elif numRows == 1:
            return [[1]]
        else:
            return []

        """
        res = [[1]]
        for i in xrange(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
        """

    def removeDuplicates(self, nums):   # 26
        # l = len(nums)
        # prev = nums[l - 1]
        # for i in xrange(l - 1):
        #     print "last:",nums[l - 2 - i]
        #     print "prev:",prev
        #     if nums[l - 2 - i] == prev:
        #         nums.pop(l - 2 - i)
        #     else:
        #         prev = nums[l - 2 - i]
        #     print "nums:",nums
        # return len(nums)
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

test = Solution()
print test.removeDuplicates([1,1,1,2,2,3,3,4])