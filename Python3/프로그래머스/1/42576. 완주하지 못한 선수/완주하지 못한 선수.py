def solution(participant, completion):
    hash_dict = {}  
    sum_hash = 0
    
    # (Hash)를 구해서 다 더하기
    for part in participant:
        part_hash = hash(part)     
        hash_dict[part_hash] = part 
        sum_hash += part_hash     

    # 완주한 사람들의 고유 번호를 빼기
    for comp in completion:
        sum_hash -= hash(comp)   
        
    return hash_dict[sum_hash]      