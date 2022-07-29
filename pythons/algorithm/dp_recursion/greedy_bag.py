"""
-------- 가장 최대 가치를 갖도록 배낭에 물건 넣기
- 물건 : 무게(W), 가치(V)로 표현함
- 물건을 쪼개서 일부분만 넣을 수 있음

"""

def bag(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1]/ x[0], reverse = True) # 가치 / 무게로 Sorting
    total_value = 0 # 최적의 무게
    details = list() # 디테일
    
    
    for data in data_list:
        if capacity - data[0] >= 0: # 무게가 0보다 크다 == 채울 공간이 되는지 안되는지
            capacity -= data[0] # 무게 
            total_value += data[1] # 가치 
            details.append([data[0], data[1], 1]) # 디테일 정리
            
        else : # 채울 공간이 되지 않는다면
            fraction = capacity / data[0]
            # 다음 물건들은 들어갈 수 없기 때문에 무게는 감소하지 않음.(마지막이기 때문)
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break # 다음 물건들이 들어갈 수 없기 때문에 break
            
    return total_value, details
    
    
data_list = [(10, 10), (15, 10), (20, 8), (25, 12), (30, 10)] # (가치, 무게)    
bag(data_list, 30)