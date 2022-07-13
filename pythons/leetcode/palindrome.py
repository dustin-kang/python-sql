"""
앞에서 읽으나 뒤에서 읽으나 같은 팰린드롬
1. 문자열 인지 아닌지로 리스트를 받는다.
2. 맨끝과 맨 처음이 같은지로 반복한다.
"""

def ispalindrome(str):
    return_numbers = [] # 결과로 받을 리스트
    
    for char in str:
        if char.isalnum(): # alnum(): 문자나 한글, 숫자일 경우 True 아니면 False
            return_numbers.append(char.lower())
            
    while len(return_numbers) > 1: # 결과로 받을 문자열의 갯수가 1이 될때까지 반복
        if return_numbers.pop(0) != return_numbers(): # 만약 맨 처음 문자와 맨 끝 문자가 같지 않다면
            return False
        return True 
    
    
input_word = input()
print(ispalindrome(input_word))