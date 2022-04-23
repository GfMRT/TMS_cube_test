import random

class RESULTS:
    def __init__(self):
        self.CD6head = 0
        self.CD5head = 0
        self.CD4head_12 = 0
        self.CD4head_9all = 0
        self.CD4head_9 = 0
        self.CD4head_6all = 0
        self.CD4head = 0
        self.meso_get_2row = 0
        self.meso_get_3row = 0
        self.top = 0
        self.second_all = 0
        self.second = 0
        self.third = 0
        self.third_2top = 0
        self.third_1all = 0
        self.third_2all = 0
    
    def add_equip(self, STR_percent, equip_i, CD, only_appear):
        if equip_i == 0: # 帽子
            if CD[1] >= 3:
                self.CD6head += 1
            elif CD[1] == 2:
                if CD[0] >= 1:
                    self.CD5head += 1
                elif max(STR_percent)==12:
                    self.CD4head_12 += 1
                elif max(STR_percent)==9.2:
                    self.CD4head_9all += 1
                elif max(STR_percent)==9:
                    self.CD4head_9 += 1
                elif max(STR_percent)==6.1:
                    self.CD4head_6all += 1
                else:
                    self.CD4head += 1
            elif sum(STR_percent) == 36:
                self.top += 1
            elif sum(STR_percent) == 33.2:
                self.second_all += 1
            elif sum(STR_percent) == 33:
                self.second += 1
            elif sum(STR_percent) == 30.1:
                self.third_2top += 1
            elif sum(STR_percent) == 30:
                self.third += 1
            elif sum(STR_percent) == 30.2:
                self.third_1all += 1
            elif sum(STR_percent) == 30.4:
                self.third_2all += 1
            
        elif equip_i == 3: # 手套
            if sum(STR_percent) == 300:
                self.top += 1
            elif sum(STR_percent) == 212:
                self.second += 1
            elif sum(STR_percent) == 209.2:
                self.second_all += 1
            elif sum(STR_percent) == 209:
                self.third_2top += 1
            elif sum(STR_percent) == 206.1:
                self.third_1all += 1
            elif sum(STR_percent) == 200:
                self.third += 1
            
        elif equip_i == 6: # 飾品
            if sum(STR_percent) == 36:
                self.top += 1
            elif sum(STR_percent) == 33.2:
                self.second_all += 1
            elif sum(STR_percent) == 33:
                self.second += 1
            elif sum(STR_percent) == 30.1:
                self.third_2top += 1
            elif sum(STR_percent) == 30:
                self.third += 1
            elif sum(STR_percent) == 30.2:
                self.third_1all += 1
            elif sum(STR_percent) == 30.4:
                self.third_2all += 1 
            if CD[1] + CD[0] > 2: #次頂>3(楓+掉)
                self.meso_get_3row += 1 
            elif CD[1] + CD[0] == 2:
                self.meso_get_2row += 1
                
        else:
            if sum(STR_percent) == 36:
                self.top += 1
            elif sum(STR_percent) == 33.2:
                self.second_all += 1
            elif sum(STR_percent) == 33:
                self.second += 1
            elif sum(STR_percent) == 30.1:
                self.third_2top += 1
            elif sum(STR_percent) == 30:
                self.third += 1
            elif sum(STR_percent) == 30.2:
                self.third_1all += 1
            elif sum(STR_percent) == 30.4:
                self.third_2all += 1
                
    def output(self, equip_i):
        equip = ['帽', '衣,套服', '褲', '手', '鞋', '披風,腰帶,肩膀', '飾']
        print('\n', equip[equip_i])
        
        if equip_i == 0: #帽子
            print("    6CD: ", self.CD6head)
            print("    5CD: ", self.CD5head)
            print("    4CD: ", self.CD4head_12 + self.CD4head_9all + self.CD4head_9 + self.CD4head_6all + self.CD4head)
            print("        4CD13屬: ", self.CD4head_12)
            print("        4CD10全: ", self.CD4head_9all)
            print("        4CD10屬: ", self.CD4head_9)
            print("        4CD7全: ", self.CD4head_6all)
            print("        4CD爛: ", self.CD4head)
            print("    頂: ", self.top)
            print("    次頂: ", self.second_all + self.second)
            print("        含全: ", self.second_all)
            print("    次次: ", self.third_2top + self.third + self.third_1all + self.third_2all)
            print("        含6全: ", self.third_2top)
            print("        含9全: ", self.third_1all)
            print("        含18全: ", self.third_2all)
        elif equip_i == 3: #手套
            print("    三爆: ", self.top)
            print("    雙爆: ", self.second + self.second_all + self.third_2top + self.third_1all + self.third)
            print("        雙爆13: ", self.second)
            print("        雙爆10全: ", self.second_all)
            print("        雙爆10: ", self.third_2top)
            print("        雙爆7全:  ", self.third_1all)
            print("        雙爆爛: ", self.third)
        else:
            print("    頂: ", self.top)
            print("    次頂: ", self.second_all + self.second)
            print("        含全: ", self.second_all)
            print("    次次: ", self.third_2top + self.third + self.third_1all + self.third_2all)
            print("        含6全: ", self.third_2top)
            print("        含9全: ", self.third_1all)
            print("        含18全: ", self.third_2all)
        
        if equip_i == 6: #飾品
            print("    兩排楓掉: ", self.meso_get_2row)
            print("    三排楓掉: ", self.meso_get_3row)

class Prob:
    def __init__(self, cube): # 0/1/2 = 閃炫、鏡射、對等、閃耀
        if(cube == 0 or cube == 3):
            # 閃炫閃耀機率一樣
            self.ingore_damage_A = [0.127, 0.1096, 0.1588, 0.1194, 0.127, 0.1356, 0] #2被擊中時有一定機率無視傷害
            self.equip_A_STR = [0.0794, 0.0685, 0.0794, 0.0746, 0.0794, 0.0847, 0.098]
            self.equip_A_all = [0.0635, 0.0548, 0.0635, 0.0597, 0.0635, 0.0678, 0.0784]
            self.ingore_damage_S = [0.1510, 0.1568, 0.1778, 0.1538, 0.1666, 0.1778, 0]
            self.equip_S_STR = [0.0755, 0.0784, 0.0889, 0.0769, 0.0833, 0.0889, 0.0784]
            self.equip_S_all = [0.0566, 0.0588, 0.0667, 0.0577, 0.0625, 0.0667, 0.0588]
            self.equip_critical = 0.0769
            self.equip_CD1 = 0.0566
            self.equip_CD2 = 0.0377
            self.skill_head_door_A = 0.0635     # 1帽子:實用的時空門
            self.invincible_time_A = 0.0548     # 1衣服:被擊中後無敵時間增加
            self.invincible_prob_A = 0.0548     # 2衣服:被擊時以一定機率一定時間內無敵
            self.skill_pant_fire_A = 0.0635     # 1褲子:實用的神聖之火
            self.skill_glove_eye_A = 0.0597     # 1手套:實用的會心之眼
            self.skill_shoe_speed_A = 0.0635    # 1鞋子:實用的速度激發
            self.skill_head_bless_S = 0.0566    # 1帽子:實用的祝福
            self.invincible_time_S = 0.0588     # 1衣服:被擊中後無敵時間增加
            self.invincible_prob_S = 0.0588     # 1衣服:被擊時以一定機率一定時間內無敵
            self.skill_glove_speed_S = 0.0577   # 1手套:實用的最終極速
            self.skill_shoe_order_S = 0.0625    # 1鞋子:實用的戰鬥命令
            self.item_get_S = 0.0588            # 1飾品:道具掉落率
            self.meso_get = 0.0588
        elif(cube == 1):
            # 鏡射
            self.ingore_damage_A = [0.1778, 0.1454, 0.2222, 0.1632, 0.1778, 0.1952, 0]
            self.equip_A_STR = [0.0444, 0.0364, 0.0444, 0.0408, 0.0444, 0.0488, 0.0606]
            self.equip_A_all = [0.0444, 0.0364, 0.0444, 0.0408, 0.0444, 0.0488, 0.0606]
            self.ingore_damage_S = [0.1904, 0.2, 0.2352, 0.1952, 0.2162, 0.2352, 0]
            self.equip_S_STR = [0.0476, 0.05, 0.0588, 0.0488, 0.0541, 0.0588, 0.0784]
            self.equip_S_all = [0.0476, 0.05, 0.0588, 0.0488, 0.0541, 0.0588, 0.0588]
            self.equip_critical = 0.0976
            self.equip_CD1 = 0.0714
            self.equip_CD2 = 0.0476
            self.skill_head_door_A = 0.0889
            self.invincible_time_A = 0.0727
            self.invincible_prob_A = 0.0727
            self.skill_pant_fire_A = 0.0889
            self.skill_glove_eye_A = 0.0816
            self.skill_shoe_speed_A = 0.0889
            self.skill_head_bless_S = 0.0714
            self.invincible_time_S = 0.075
            self.invincible_prob_S = 0.075
            self.skill_glove_speed_S = 0.0732
            self.skill_shoe_order_S = 0.0811
            self.item_get_S = 0.075
            self.meso_get = 0.075
        elif(cube == 2):
            # 對等
            self.ingore_damage_S = [0.1510, 0.1568, 0.1778, 0.1538, 0.1666, 0.1778, 0]
            self.equip_S_STR = [0.0755, 0.0784, 0.0889, 0.0769, 0.0833, 0.0889, 0.0784]
            self.equip_S_all = [0.0566, 0.0588, 0.0667, 0.0577, 0.0625, 0.0667, 0.0588]
            self.equip_critical = 0.0769
            self.equip_CD1 = 0.0566
            self.equip_CD2 = 0.0377
            self.skill_head_bless_S = 0.0566
            self.invincible_time_S = 0.0588
            self.invincible_prob_S = 0.0588
            self.skill_glove_speed_S = 0.0577
            self.skill_shoe_order_S = 0.0625
            self.item_get_S = 0.0588
            self.meso_get = 0.0588
        
    
    def getS(self, state_percent, kind, CD, only_appear): 
        #only_appear 1技能/1被擊中後無敵時間增加, 2被擊中時有一定機率無視傷害/2掉寶, 2被擊時以一定機率一定時間內無敵
        line = random.random()
        cummulate = 0
        
        #決定機率倍率
        multiplier = 0
        if only_appear[0]>=1:
            if kind == 0:
                multiplier += self.skill_head_bless_S
            elif kind == 1:
                multiplier += self.invincible_time_S
            elif kind == 3:
                multiplier += self.skill_glove_speed_S
            elif kind == 4:
                multiplier += self.skill_shoe_order_S
        if only_appear[1]>=2:
            if kind == 6:
                multiplier += self.item_get_S
            else:
                multiplier += self.ingore_damage_S[kind]
        if only_appear[2]>=2:
            multiplier += self.invincible_prob_S
        multiplier = 1/(1-multiplier)
        
        #開始抽
        cummulate += self.equip_S_STR[kind] * multiplier
        if (line < cummulate):
            if min(state_percent) <12:
                state_percent[state_percent.index(min(state_percent))] = 12
            return
        else:
            cummulate += self.equip_S_all[kind] * multiplier
            
        if (line < cummulate):
            if min(state_percent) <9.2:
                state_percent[state_percent.index(min(state_percent))] = 9.2
            return
        elif kind == 0:
            cummulate += self.equip_CD1 * multiplier
        elif kind == 3:
            cummulate += self.equip_critical * multiplier
        elif kind == 6:
            cummulate += self.meso_get * multiplier
            
        if (line < cummulate):
            if kind == 0:
                CD[0] += 1
                return
            elif kind == 3:
                if min(state_percent) <100:
                    state_percent[state_percent.index(min(state_percent))] = 100
                return
            elif kind == 6: #楓/掉
                CD[0] += 1
                return    
        elif kind == 0:
            cummulate += self.equip_CD2 * multiplier
            
        if (line < cummulate):
            if kind == 0:
                CD[1] += 1
                return
                
        #沒有洗到排數限制的抽完了  
        #第一種限制        
        if only_appear[0]<1:
            if kind == 0:
                cummulate += self.skill_head_bless_S * multiplier
            elif kind == 1:
                cummulate += self.invincible_time_S * multiplier
            elif kind == 3:
                cummulate += self.skill_glove_speed_S * multiplier
            elif kind == 4:
                cummulate += self.skill_shoe_order_S * multiplier
                
            if (line < cummulate):
                only_appear[0] += 1
                return
        
        #第二種限制
        if only_appear[1]<2:
            if kind == 6: #CD[0]用於飾品 = 楓幣
                cummulate += self.item_get_S * multiplier
            else:
                cummulate += self.ingore_damage_S[kind] * multiplier
                
            if (line < cummulate):
                only_appear[1] += 1
                if kind == 6:
                    CD[1] += 1
                return
        
        #第三種限制
        if only_appear[2]<2:
            if kind == 1:
                cummulate += self.invincible_prob_S * multiplier
                    
            if (line < cummulate):
                only_appear[2] += 1
        
        
    def getA(self, state_percent, kind, only_appear): 
        #only_appear 1技能/1被擊中後無敵時間增加, 2被擊中時有一定機率無視傷害/2掉寶, 2被擊時以一定機率一定時間內無敵
        line = random.random()
        cummulate = 0
        
        #決定機率倍率 (移出哪些項目的機率)
        multiplier = 0
        if only_appear[0]>=1:
            if kind == 0:
                multiplier += self.skill_head_door_A
            elif kind == 1:
                multiplier += self.invincible_time_A
            elif kind == 2:
                multiplier += self.skill_pant_fire_A
            elif kind == 3:
                multiplier += self.skill_glove_eye_A
            elif kind == 4:
                multiplier += self.skill_shoe_speed_A
        if only_appear[1]>=2:
            multiplier += self.ingore_damage_A[kind]
        if only_appear[2]>=2:
            multiplier += self.invincible_prob_A
        multiplier = 1/(1-multiplier)    
        
        #開始抽
        cummulate += self.equip_A_STR[kind] * multiplier
        if (line < cummulate):
            if min(state_percent) <9:
                state_percent[state_percent.index(min(state_percent))] = 9
            return
        else:
            cummulate += self.equip_A_all[kind] * multiplier
            
        if (line < cummulate):
            if min(state_percent) <6.1:
                state_percent[state_percent.index(min(state_percent))] = 6.1
            return
                
        #沒有洗到排數限制的抽完了  
        #第一種限制        
        if only_appear[0]<1:
            if kind == 0:
                cummulate += self.skill_head_door_A * multiplier
            elif kind == 1:
                cummulate += self.invincible_time_A * multiplier
            elif kind == 2:
                cummulate += self.skill_pant_fire_A * multiplier
            elif kind == 3:
                cummulate += self.skill_glove_eye_A * multiplier
            elif kind == 4:
                cummulate += self.skill_shoe_speed_A * multiplier
                
            if (line < cummulate):
                only_appear[0] += 1
                return
        
        #第二種限制
        if only_appear[1]<2:
            cummulate += self.ingore_damage_A[kind] * multiplier
                
            if (line < cummulate):
                only_appear[1] += 1
                return
        
        #第三種限制
        if only_appear[2]<2:
            if kind == 1:
                cummulate += self.invincible_prob_A * multiplier
                
            if (line < cummulate):
                only_appear[2] = only_appear[2]+1