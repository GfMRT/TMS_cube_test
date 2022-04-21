import random
import os
import Prob_weapon

print("洗閃炫")
cube_kind = 0
Prob = Prob_weapon.Prob(cube_kind)

results = Prob_weapon.RESULTS()
for exp in range(0,int(1e8)):
    BOSS = [0,0]
    ATK = [0,0,0] 
    only_appear = [0,0] # B傷、無視
    
    # 第1排
    Prob.getS(ATK, BOSS, only_appear)
    
    # 第2排
    if random.random()<0.2:
        Prob.getS(ATK, BOSS, only_appear)
    else:
        Prob.getA(ATK, BOSS, only_appear)
        
    # 第3排
    if random.random()<0.15:
        Prob.getS(ATK, BOSS, only_appear)
    else:
        Prob.getA(ATK, BOSS, only_appear)
    
    # 第4排
    Prob.getS(ATK, BOSS, only_appear)
    
    # 第5排
    if random.random()<0.2:
        Prob.getS(ATK, BOSS, only_appear)
    else:
        Prob.getA(ATK, BOSS, only_appear)
        
    # 第6排
    if random.random()<0.15:
        Prob.getS(ATK, BOSS, only_appear)
    else:
        Prob.getA(ATK, BOSS, only_appear)
    
    # 確認要的裝備
    results.add_equip(ATK, BOSS)
    
results.output()
        
    
os.system("pause")
            