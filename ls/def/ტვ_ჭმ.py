# 1
def solution(text, ending):
    return text[-len(ending):] == ending 
print(solution("gio","io"))


