import random
import os

# 鏡射
equip = ['帽', '衣,套服', '褲', '手', '鞋', '披風,腰帶,肩膀', '飾']
equip_S_STR = [0.0755, 0.0784, 0.0889, 0.0769, 0.0833, 0.0889, 0.0784]
equip_S_all = [0.0566, 0.0588, 0.0667, 0.0577, 0.0625, 0.0667, 0.0588]
equip_critical = 0.0769
equip_CD1 = 0.0566
equip_CD2 = 0.0377
skill_head_bless_S = 0.0566
invincible_clothes_S = 0.0588
skill_glove_speed_S = 0.0577
skill_shoe_order_S = 0.0625
item_get_S = 0.0588

# 累進機率
for i in range(0,7):
    equip_S_all[i] = equip_S_all[i] + equip_S_STR[i]
equip_critical = equip_critical+equip_S_all[3]
equip_CD1 = equip_CD1 + equip_S_all[0]
equip_CD2 = equip_CD2 + equip_CD1

def getS(state_percent, kind, CD, only_appear):
    line = random.random()
    
    if kind == 0: #帽子的實用
        if only_appear[0]==1:
            line = line * (1-skill_head_bless_S)
        elif line>(1-skill_head_bless_S):
            only_appear[0] = only_appear[0]+1
    elif kind == 1: #衣服的無敵
        if only_appear[0]==1:
            line = line * (1-invincible_clothes_S)
        elif line>(1-invincible_clothes_S):
            only_appear[0] = only_appear[0]+1
    elif kind == 3: #手套的實用
        if only_appear[0]==1:
            line = line * (1-skill_glove_speed_S)
        elif line>(1-skill_glove_speed_S):
            only_appear[0] = only_appear[0]+1
    elif kind == 4: #鞋子的實用
        if only_appear[0]==1:
            line = line * (1-skill_shoe_order_S)
        elif line>(1-skill_shoe_order_S):
            only_appear[0] = only_appear[0]+1
    elif kind == 6: #掉寶
        if only_appear[0]==2:
            line = line * (1-item_get_S)
        elif line>(1-item_get_S):
            only_appear[0] = only_appear[0]+1
    
    if (line < equip_S_STR[kind]):
        if min(state_percent) <12:
            state_percent[state_percent.index(min(state_percent))] = 12
    elif (line < equip_S_all[kind]):
        if min(state_percent) <9.2:
            state_percent[state_percent.index(min(state_percent))] = 9.2
    elif kind == 3:
        if (line < equip_critical):
            if min(state_percent) <100:
                state_percent[state_percent.index(min(state_percent))] = 100
    elif kind == 0:
        if (line < equip_CD1):
            CD[0] = CD[0]+1
        elif (line < equip_CD2):
            CD[1] = CD[1]+1
        
CD6head = 0
CD5head = 0
CD4head_12 = 0
CD4head_9all = 0
CD4head = 0
only_appear = [0]

print("洗對等")
for equip_i in range(0,7):
    top = 0
    second_all = 0
    second = 0
    third = 0
    third_2top = 0
    third_1all = 0
    third_2all = 0
    
    for exp in range(0,int(1e7)):
        CD = [0,0]
        only_appear[0] = 0
        STR_percent = [0,0,0]
        # 第1排
        getS(STR_percent, equip_i, CD, only_appear)
        
        # 第2排
        getS(STR_percent, equip_i, CD, only_appear)
            
        # 第3排
        getS(STR_percent, equip_i, CD, only_appear)
        
        # 確認要的裝備
        if equip_i == 0:
            if CD[1] >= 3:
                CD6head = CD6head+1
            elif CD[1] == 2:
                if CD[0] >= 1:
                    CD5head = CD5head+1
                elif max(STR_percent)==12:
                    CD4head_12 = CD4head_12+1
                elif max(STR_percent)==9.2:
                    CD4head_9all = CD4head_9all+1
                else:
                    CD4head = CD4head+1
            elif sum(STR_percent) == 36:
                top = top+1
            elif sum(STR_percent) == 33.2:
                second_all = second_all+1
            elif sum(STR_percent) == 33:
                second = second+1
            elif sum(STR_percent) == 30.1:
                third_2top = third_2top+1
            elif sum(STR_percent) == 30:
                third = third+1
            elif sum(STR_percent) == 30.2:
                third_1all = third_1all+1
            elif sum(STR_percent) == 30.4:
                third_2all = third_2all+1
            
        elif equip_i == 3:
            if sum(STR_percent) == 300:
                top = top+1
            elif sum(STR_percent) == 212:
                second = second+1
            elif sum(STR_percent) == 209.2:
                second_all = second_all+1
            elif sum(STR_percent) == 209:
                third_2top = third_2top+1
            elif sum(STR_percent) == 206.1:
                third_1all = third_1all+1
            elif sum(STR_percent) == 200:
                third = third+1
                
        else:
            if sum(STR_percent) == 36:
                top = top+1
            elif sum(STR_percent) == 33.2:
                second_all = second_all+1
            elif sum(STR_percent) == 33:
                second = second+1
            elif sum(STR_percent) == 30.1:
                third_2top = third_2top+1
            elif sum(STR_percent) == 30:
                third = third+1
            elif sum(STR_percent) == 30.2:
                third_1all = third_1all+1
            elif sum(STR_percent) == 30.4:
                third_2all = third_2all+1
    
    print('\n', equip[equip_i])
    
    if equip_i == 0: #帽子
        print("    6CD: ", CD6head)
        print("    5CD: ", CD5head)
        print("    4CD: ", CD4head_12+CD4head_9all+CD4head)
        print("        4CD13屬: ", CD4head_12)
        print("        4CD10全: ", CD4head_9all)
        print("\n\n        4CD爛: ", CD4head)
        print("    頂: ", top)
        print("    次頂: ", second_all+second)
        print("        含全: ", second_all)
        print("    次次: ", third_2top + third + third_1all + third_2all)
        print("\n\n        含18全: ", third_2all)
    elif equip_i == 3: #手套
        print("    三爆: ", top)
        print("    雙爆: ", second + second_all + third_2top + third_1all + third)
        print("        雙爆13: ", second)
        print("        雙爆10全: ", second_all)
        print("\n\n        雙爆爛: ", third)
    else:
        print("    頂: ", top)
        print("    次頂: ", second_all+second)
        print("        含全: ", second_all)
        print("    次次: ", third_2top + third + third_1all + third_2all)
        print("\n\n        含18全: ", third_2all)
    
os.system("pause")
            