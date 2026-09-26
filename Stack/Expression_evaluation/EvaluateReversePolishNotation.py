class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        
        for token in tokens:
            
            if token not in '+-*/':
                st.append(token)
            else:
                op = token
                
                a = int(st.pop())
                b = int(st.pop())
                
                if op == '*':
                    result = b * a
                elif op == '+':
                    result = b + a 
                elif op == '-':
                    result = b - a 
                else:
                    result = int(b/a)          

                   
                st.append(result)  
        return int(st.pop())         


        