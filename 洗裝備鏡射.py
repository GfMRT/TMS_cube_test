import random
import os
import Prob_generate

print("洗鏡射")
cube_kind = 1
Prob = Prob_generate.Prob(cube_kind)

for equip_i in range(0,7):
    results = Prob_generate.RESULTS()
    for exp in range(0,int(1e8)):
        CD = [0,0]
        only_appear = [0,0,0]
        STR_percent = [0,0,0]
        # 第1排
        Prob.getS(STR_percent, equip_i, CD, only_appear)
        
        # 第2排
        level = random.random()
        if level>0.8:
            CD[0] = CD[0]*2
            CD[1] = CD[1]*2
            STR_percent[1] = STR_percent[0]
        elif level<0.08:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
            
        # 第3排
        if random.random()<0.01:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
        
        # 確認要的裝備
        results.add_equip(STR_percent, equip_i, CD, only_appear)
        
    results.output(equip_i)
    
os.system("pause")
            