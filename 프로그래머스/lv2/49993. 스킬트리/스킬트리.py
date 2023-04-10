def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        fixed_skill = list(skill)
        
        for i in skills:
            if i in fixed_skill and i != fixed_skill.pop(0):
                break
        else:
            answer+=1        
    return answer