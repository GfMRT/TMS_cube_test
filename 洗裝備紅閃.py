import random
import os
import Prob_generate

print("洗紅閃")
cube_kind = 3
Prob = Prob_generate.Prob(cube_kind)

for equip_i in range(0,8): #['帽', '衣,套服', '褲', '手', '鞋', '披風,腰帶,肩膀', '飾']
    results = Prob_generate.RESULTS()
    case = 0
    if equip_i == 7:
        case = 1
        equip_i = 6
        
    for exp in range(0,int(1e8)):
        if equip_i == 0: #帽子鎖2CD
            CD = [0,1] # -1/meso, -2/掉寶
            only_appear = [0,0,0] #only_appear 1技能/1被擊中後無敵時間增加, 2被擊中時有一定機率無視傷害/2掉寶, 2被擊時以一定機率一定時間內無敵
            STR_percent = [0,0,0]
        elif equip_i == 3: #手套鎖爆傷   
            CD = [0,0] 
            only_appear = [0,0,0]
            STR_percent = [100,0,0]
        elif equip_i == 6: #飾品鎖掉寶
            if case == 0:
                CD = [0,1] 
                only_appear = [0,1,0] 
                STR_percent = [0,0,0]
            if case == 1:
                CD = [0,0] 
                only_appear = [0,0,0] 
                STR_percent = [12,0,0]
        else:
            CD = [0,0] 
            only_appear = [0,0,0] 
            STR_percent = [12,0,0]
        
        # 第1排
        Prob.getS(STR_percent, equip_i, CD, only_appear)
        
        # 第2排
        if random.random()<0.1:
            Prob.getS(STR_percent, equip_i, CD, only_appear)
        else:
            Prob.getA(STR_percent, equip_i, only_appear)
            
        # 確認要的裝備
        results.add_equip(STR_percent, equip_i, CD, only_appear)
        
    results.output(equip_i)
        
    
os.system("pause")
            