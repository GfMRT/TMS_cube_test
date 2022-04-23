import random
import os
import Prob_weapon

print("洗紅閃")
cube_kind = 3
Prob = Prob_weapon.Prob(cube_kind)

for case in [0,1]:
    results = Prob_weapon.RESULTS()
    if case == 0:
        print("第三排鎖B40")
    else:
        print("第三排鎖物12")
    for exp in range(0,int(1e8)):
        if case ==0:
            #第三排鎖B40
            BOSS = [40,0,0]
            ATK = [0,0,0] 
            only_appear = [1,0] # B傷、無視
        else:
            BOSS = [0,0,0]
            ATK = [12,0,0] 
            only_appear = [0,0] # B傷、無視
        
        # 第1排
        Prob.getS(ATK, BOSS, only_appear)
        
        # 第2排
        if random.random()<0.1:
            Prob.getS(ATK, BOSS, only_appear)
        else:
            Prob.getA(ATK, BOSS, only_appear)
            
        # 確認要的裝備
        results.add_equip(ATK, BOSS)
        
    results.output()
        
    
os.system("pause")
            