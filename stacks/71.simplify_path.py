class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curPath = ''
        for c in path + '/':
            if c == '/':
                if curPath == '..':
                    if stack: stack.pop()
                elif curPath != '' and curPath != '.':
                    stack.append(curPath)
                curPath = ""
                
            else:
                curPath += c
                
        return '/' + '/'.join(stack)
            
