class Solution (object):
    def palindrome(self):
        x=(input("Enter Number"))
        if x==x[::-1]:
            print('Palindrome')
        else:
            print('Not Palindrome')
test1=Solution()
test1.palindrome()
            