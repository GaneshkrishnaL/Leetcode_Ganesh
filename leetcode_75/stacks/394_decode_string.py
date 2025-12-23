class Solution:
    def decodeString(self, s: str) -> str:

        #first we iterate through the s str and add  to stack until we fing the inner most close bracket
        # then we use curr to back track current string until we fing open bracket
        # next we use num to track num and net num value and append to stack at end num times curr


        stack=[]                  

        for i in s:
            if i !="]":
                stack.append(i)
            else:   
                curr=""
                while stack and stack[-1]!="[":
                    curr=stack.pop()+curr
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=""
                    num=stack.pop()+num
                stack.append(curr*int(num))
        return "".join(stack)

        # time complexity O(N)
        # space complexity O(M) for M elements in encoded staring 


        
