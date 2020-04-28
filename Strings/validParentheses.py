def isValid(s: str) -> bool:
        if(len(s)==0):
            return True
        
        stack = []
        
        for i in range(len(s)):
            if(s[i]=='(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
                
            if(len(stack)>0):
                
                
                if((s[i] == ')' and stack.pop() != '(') or (s[i] == '}' and stack.pop() != '{') or (s[i] == ']' and stack.pop() != '[')):
                    return False
                
            else:
                return False
            
        if(len(stack)==0):
            return True
        else:
            return False

print(isValid("[][][]()"))