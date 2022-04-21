import random
import os
import Prob_generate

print("洗閃炫")
cube_kind = 0
Prob = Prob_generate.Prob(cube_kind)

for equip_i in range(0,7):
    results = Prob_generate.RESULTS()
    for exp in range(0,int(1e8)):
        CD = [0,0] # -1/meso, -2
        only_appear = [0,0,0] #only_appear 1技能/1被擊中後無敵時間增加, 2被擊中時有一定機率無視傷害/2掉寶, 2被擊時以一定機率一定時間內無敵
        STR_percent = [0,0,0]
        
        # 第1排
        Prob.getS(STR_percent, equip_i, CD, only_appear)
        
        # 第2排
        if random.random()<0.2:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
            
        # 第3排
        if random.random()<0.15:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
        
        # 第4排
        Prob.getS(STR_percent, equip_i, CD, only_appear)
        
        # 第5排
        if random.random()<0.2:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
            
        # 第6排
        if random.random()<0.15:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
        
        # 確認要的裝備
        results.add_equip(STR_percent, equip_i, CD, only_appear)
        
    results.output(equip_i)
        
    
os.system("pause")
            