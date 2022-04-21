import random
import numpy as np

class RESULTS:
    def __init__(self):
        self.WeaponAttack_BOSSDamage = np.zeros((10, 9), 'int64')
        self.ATK_table = [0, 9, 12, 18, 21, 24, 27, 30, 33, 36] #(共10種)
        self.BOSS_table = [0, 30, 35, 40, 60, 65, 70, 75, 80] #(共9種)
    
    def add_equip(self, ATK, BOSS):
        ATK = sorted(ATK, reverse = True)
        BOSS = sorted(BOSS, reverse = True)
        
        #choose 0B
        ATK_result = sum(ATK)
        BOSS_result = 0
        self.WeaponAttack_BOSSDamage[0:self.ATK_table.index(ATK_result)+1, 0:self.BOSS_table.index(BOSS_result)+1] += 1
        
        #choose 1B
        ATK_result = ATK[0]+ATK[1]
        BOSS_result = BOSS[0]
        self.WeaponAttack_BOSSDamage[0:self.ATK_table.index(ATK_result)+1, 1:self.BOSS_table.index(BOSS_result)+1] += 1
        
        #choose 2B
        ATK_result = ATK[0]
        BOSS_result = sum(BOSS)
        self.WeaponAttack_BOSSDamage[0:self.ATK_table.index(ATK_result)+1, 4:self.BOSS_table.index(BOSS_result)+1] += 1
        
    def output(self):
        print('\n武器')
        for i in range(0,10):
            for j in range(0,9):
                print(self.WeaponAttack_BOSSDamage[i, j], end = '\t')
            print("")
        

class Prob:
    def __init__(self, cube): # 0/1/2 = 閃炫、鏡射、對等
        if(cube == 0):
            # 閃炫
            self.attack_A = 0.0652
            self.ingore_A = 0.087
            self.B30_A = 0.0652  
            self.attack_S = 0.0444
            self.ingore_S = 0.1334
            self.B30_S = 0.0444
            self.B35_S = 0.0444  
            self.B40_S = 0.0444             
            
        elif(cube == 1):
            # 鏡射
            self.attack_A = 0.027
            self.ingore_A = 0.0541
            self.B30_A = 0.0541 
            self.attack_S = 0.0278
            self.ingore_S = 0.1112
            self.B30_S = 0.0278  
            self.B35_S = 0.0278  
            self.B40_S = 0.0278    
        elif(cube == 2):
            # 對等
            self.attack_S = 0.0444
            self.ingore_S = 0.1334
            self.B30_S = 0.0444
            self.B35_S = 0.0444  
            self.B40_S = 0.0444   
    
    def getS(self, ATK, BOSS, only_appear): 
        #only_appear B傷、無視
        line = random.random()
        cummulate = 0
        
        #決定機率倍率
        multiplier = 0 #要被排除的機率
        if only_appear[0]>=2:
            multiplier += self.B30_S
            multiplier += self.B35_S
            multiplier += self.B40_S
        if only_appear[1]>=2:
            multiplier += self.ingore_S
        multiplier = 1/(1-multiplier)
        
        #開始抽
        cummulate += self.attack_S * multiplier
        if (line < cummulate): #抽12物
            if min(ATK) <12:
                ATK[ATK.index(min(ATK))] = 12
            return
           
        #沒有洗到排數限制的抽完了  
        #第一種限制        
        if only_appear[0]<2: #抽B傷
            cummulate += self.B30_S * multiplier
            if (line < cummulate):
                if min(BOSS) <30:
                    BOSS[BOSS.index(min(BOSS))] = 30
                only_appear[0] += 1
                return
                
            cummulate += self.B35_S * multiplier
            if (line < cummulate):
                if min(BOSS) <35:
                    BOSS[BOSS.index(min(BOSS))] = 35
                only_appear[0] += 1
                return
            
            cummulate += self.B40_S * multiplier
            if (line < cummulate):
                if min(BOSS) <40:
                    BOSS[BOSS.index(min(BOSS))] = 40
                only_appear[0] += 1
                return
        
        #第二種限制
        if only_appear[1]<2: #抽無視
            cummulate += self.ingore_S * multiplier
            if (line < cummulate):
                only_appear[1] += 1
        
    def getA(self, ATK, BOSS, only_appear): 
        #only_appear B傷、無視
        line = random.random()
        cummulate = 0
        
        #決定機率倍率
        multiplier = 0 #要被排除的機率
        if only_appear[0]>=2:
            multiplier += self.B30_A
        if only_appear[1]>=2:
            multiplier += self.ingore_A
        multiplier = 1/(1-multiplier)
        
        #開始抽
        cummulate += self.attack_A * multiplier
        if (line < cummulate): #抽9物
            if min(ATK) <9:
                ATK[ATK.index(min(ATK))] = 9
            return
           
        #沒有洗到排數限制的抽完了  
        #第一種限制        
        if only_appear[0]<2: #抽B傷
            cummulate += self.B30_A * multiplier
            if (line < cummulate):
                if min(BOSS) <30:
                    BOSS[BOSS.index(min(BOSS))] = 30
                only_appear[0] += 1
                return
        
        #第二種限制
        if only_appear[1]<2: #抽無視
            cummulate += self.ingore_A * multiplier
            if (line < cummulate):
                only_appear[1] += 1