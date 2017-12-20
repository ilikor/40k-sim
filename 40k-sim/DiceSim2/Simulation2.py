

"""
Auteur: Samuel Turgeon
Pour le plaisir personnel

Ce program est cree pour simuler des jets de des qui suivent les règles de wh40k. 

Une regle special doit modifier le résultat qui lui est donne et doit RETOURNER une attaque.
"""

from copy import copy
import matplotlib.pyplot as plt
import numpy

from DiceSim2.Attack import Attack
from DiceSim2.Defense import Defense
from DiceSim2 import RollingFunctions as RF


class Simulation():
    
    
    
    
    
    def __init__(self):
        
        self.shooters = [] #Contient les profils des differentes attaques
        self.target = Defense(4,1,3,None,None)
        self.target.FnP = [0]
        self.attackers = []
        
        self.hit_rules = [None]  #Le nom des fonctions agissant sur le jet de touche   Exploding dices --> Ambush of Blades --> Tesla
        self.wound_rules = [None]  #Le nom des fonctions agissant sur le jet de blessure  Rending --> Sniper  --> Haywire
        
        pass


    
    def hit_roll(self):
        
        """
        Number est le nombre de de e lancer
        target nombre pour être considéré un succes  (Pour une save c'est l'inverse)
        
        functions is a list of function to run on the results after reroll 
        Each function needs to be added in order of resolution
        """
        
       # print("hit roll")
        
        next_shooters = []
        
        for i in range(len(self.shooters)):
            
            attack_type = self.shooters[i]
            
            target = attack_type.H
            
            dices = self.determine_attack(attack_type)
            
            results = RF.rollingd6s(dices, attack_type.RHT)
            #print(results)

            for specialRule in attack_type.hit_rules:
                
                temp = specialRule.rule(results, attack_type)
                if(temp != None):
                    
                    next_shooters.append(temp)
                    
                
           # print(results)
            
            mod_target = target - attack_type.Hit_Mod
            
            if(mod_target < 2):
                
                mod_target = 2   
            
            success = results[(mod_target-1):]
            sum_succ = int(numpy.sum(success))  
                
          #  print(success)
          #  print(sum_succ)
            
            temp = copy(attack_type)
            temp.R = sum_succ
            next_shooters.append(temp)   
        
        self.shooters = copy(next_shooters)
        
        
    def wound_roll(self):
        
        """
        Number est le nombre de de à lancer
        target nombre pour être considéré un succes  
        
        functions is a list of function to run on the results after reroll 
        Each function needs to be added in order of resolution
        """
        
       # print("wound roll")
        
        next_shooters = []
        #print(self.shooters)
        #print("Just Before")
        for attack_type in self.shooters:

            target = self.determine_wound_roll(attack_type)
            results = RF.rollingd6s(attack_type.R, attack_type.RWT)

            for specialRule in attack_type.wnd_rules:
                #print(specialRule)
                temp = specialRule.rule(results, attack_type)
                if(temp != None):
                    
                    next_shooters.append(temp)
                    
            success = results[(target-1):]
            sum_succ = int(numpy.sum(success))  
            
            temp = copy(attack_type)
            temp.R = sum_succ
            next_shooters.append(temp)   
        
        self.shooters = copy(next_shooters)
    
    def save_roll(self):
        
        """
        Number est le nombre de de à lancer
        target nombre pour être considere un succes 
        
        functions is a list of function to run on the results after reroll 
        Each function needs to be added in order of resolution
        """
        
        #print("save roll")
        
        next_shooters = []
        #print(self.shooters)
        for attack_type in self.shooters:
            #print(attack_type.AP)
            target = self.determine_save(attack_type)
            
            results = RF.rollingd6s(attack_type.R)
           # print(results)
            
            success = results[:(target-1)]
            
            sum_succ = int(numpy.sum(success))  
                
            #print(success)
           # print(sum_succ)
            
            temp = copy(attack_type)
            temp.R = sum_succ
            next_shooters.append(temp)   
        
        self.shooters = next_shooters
        
    def damage_phase(self):
        
        """
        The damage phase is when you roll for damage and save damage. It will calculate to make sure overkill is taken into account
        """
        
        #print("damage roll")
        
        dead = 0
        wounds_dealt_to_model = 0
        
        for attack_type in self.shooters:
            
            reading = str(attack_type.D)
            
            split = reading.split("d")
            
            number = 0
            type = 0
            damage_array = 0
            
            if(len(split)> 1):  #Has another element
                type = int(split[1])
                number = int(split[0])*attack_type.R
                damage_array = RF.rollingdXs_time_dependant(number, type)
            
            else: #No other element, thus dmg 1
                type = int(split[0])
                number = attack_type.R
                damage_array = [type]*number
            
            for i in range(0, len(damage_array)):
                
                dmgI = damage_array[i]

                for FNP in self.target.FnP:
                    
                    results = RF.rollingd6s(int(dmgI), 0)
                    succ = int(numpy.sum(results[(FNP-1):]))
                    dmgI -= succ
                if(attack_type.AP == "MW"):
                    
                    while(dmgI > 0):
                        
                        wounds_dealt_to_model += 1
                        dmgI -= 1
                        
                        if(wounds_dealt_to_model >= self.target.W):
                            dead += 1
                            wounds_dealt_to_model = 0
                            
                        
                else:
                    if(dmgI+wounds_dealt_to_model >= self.target.W):
                        dead += 1
                        wounds_dealt_to_model = 0
                    else:
                        wounds_dealt_to_model += dmgI
                    
      #  print(dead)
       # print(wounds_dealt_to_model)      
        
        return dead, wounds_dealt_to_model        
    
    def moral_phase(self, dead, reroll = False):
        
        morale = self.target.moral
    
        ded = 0
        roll = numpy.random.randint(1,7)
        total =  roll + dead
        
        
        
        if(total > morale):
            
            if(reroll == "CAN" and roll > 4):
                
                roll = numpy.random.randint(1,7)
                total = roll + dead

            elif(reroll == "MUST"):
                
                roll = numpy.random.randint(1,7)
                total = roll + dead       
            
            elif(reroll == "COMMI"):
                
                ded += 1
                roll = numpy.random.randint(1,7)
                total = roll + dead
            
            elif(reroll == "KNIFE" and roll == 6):
                
                total = 0
                
            elif(reroll == "AUTO"):
                
                total = 0
            
            if(total > morale):
                
                
            
                dedL = (total - morale)
                ded += dedL
            
        
        return ded
        
    
    def determine_attack(self, attack):
        
        """
        Une fonction pour determiner le nombre d'attaque des modèles avec des nombres aleatoires
        
        Elle fait la lecture du nombre d'attaque et fait la bonne truc lol
        
        """
        retour = 0
        reading =str(attack.R)
        
        split = reading.split("d")
       # print(split)
        number = split[0]
        
        if(len(split)>1):

            type = split[1]
            
            results = RF.rollingdXs(int(number), int(type))
            w = numpy.arange(1, len(results)+1,1)
            retour = int(numpy.inner(results, w))
            
        else:
            
            retour = int(number)
            
       # print(retour)    
        return retour
     
    def determine_attack2(self, attack):
        """
        
        This will be used after I made sure that everything is transferred to ignore attack.R
        """
        
        
        retour = 0
        reading = str(attack.attacks)
        
        if("d" in reading):
            
            split = reading.split("d")
            number = split[0]
            type = split[1]
            results = RF.rollingdXs(int(number), int(type))
            w = numpy.arange(1, len(results)+1,1)
            retour = int(numpy.inner(results, w))
            
        else:
            
            retour = int(reading)
        
        
        return retour
    
    def determine_wound_roll(self, attack):
        
        Sa = attack.S
        Tt = self.target.T
        wound_roll = 4
        
        if(Sa >= 2*Tt):
            
            wound_roll = 2
            
        elif(Sa > Tt):
            
            wound_roll = 3
            
        elif(2*Sa <= Tt):
            
            wound_roll = 6
            
        elif(Sa < Tt):
            
            wound_roll = 5
            
        return wound_roll
    
    def determine_save(self, attack):
        """
        Une fonction pour determiner la save du défendeur
        Elle va applique à la save
        Puis retourner le plus haut entre la save modifié et la save invuln
        """
        
        
        
        APa = attack.AP
        save = self.target.SV
        
        if(APa == "MW"):
            
            return 7
        
        mod_save = save - APa
        
        if(self.target.ISV != None):
        
            if(mod_save < self.target.ISV):
                
                mod_save = self.target.ISV
            
        
        return mod_save
        
    def total_cost_attack(self):
        """
        Une fonction qui calcul le prix en point de toutes les unités impliquées dans l'attaque
        """
        
        total = 0
        
        for attk in self.attackers:
            
            total += attk.models * attk.points
            
        
        return total
        
    def efficiency(self, dead):
        
        points_in_attack = float(self.total_cost_attack())
       # print(points_in_attack)
        points_dead = float(dead * self.target.Points)
        #print(points_dead)
        
        eff = points_dead/points_in_attack
        #print(eff)
        return  eff
        
        
        
    
    def exploding_dices(self, resultats, attack_type):
        """
        Exploding dices is when on a result, you generate additional attacks (Which cannot generate additional attacks)
        
        """
        
        target = attack_type.Exploding_Target - attack_type.Hit_Mod
        
        exploding = copy(resultats[(target-1):]) 
        sum_explode = int(numpy.sum(exploding)) * attack_type.Exploding_Add
        
        explode_result = RF.rollingd6s(sum_explode, attack_type.RHT)
        
        resultats += explode_result
    
    def rending(self):
        
        pass
    
    def sniper(self):
        
        pass
    
    def ambush_of_blades(self, resultats, attack_type):
        
        """
        The rule Ambush Of Blade is that on a roll of 6+, the attack AP improves by 1
        As such, we check the results of the hit roll, take any 6+ and add it to a new result table
        We then remove results 6+ from the original result table
        We then create a new attack with the improved AP
        
        """
        
        target = 6 - attack_type.Hit_Mod
        
        ambush = copy(resultats[(target-1):])
        resultats[(target-1):] = 0
        
        sum_ambush = int(numpy.sum(ambush))
        
        temp = copy(attack_type)
        temp.R = sum_ambush
        temp.AP = temp.AP - 1
        
        self.next_shooters.append(temp)
        
        
    def sim(self):
        
        self.shooters = copy(self.attackers)
        
        hits = self.hit_roll()
        
        wounds = self.wound_roll()
        
        unsaved = self.save_roll()
        
        dead, wounds = self.damage_phase()
        
        moral = self.moral_phase(dead, self.target.moral_rule) + copy(dead)
        
        if(dead > self.target.unit_size):
            
            dead = self.target.unit_size
        
        if(moral > self.target.unit_size):
            
            moral = self.target.unit_size
        
        eff = self.efficiency(moral)
        
        self.shooters = []
        
        ### boucle pour chaque type de FnP huh?
        return dead, wounds, eff, moral
    
    def add_Attacker(self, attacker):
        
        self.attackers.append(attacker)
      
    def add_Attackers(self, attackers_Init):
        
        self.attackers = attackers_Init  
    
    def change_Defender(self, defender_Init):
        
        self.target = defender_Init
        
        
    
    def overall_Sim(self, number):
        
        #temp = Attack()
        #temp.R = 72
        #temp.S = 6
        #temp.D = "1"
        #temp.AP = -1
        #temp.set_reroll(2, 2)
        #temp.hit_rules.append(self.exploding_dices)
        #temp.hit_rules.append(self.ambush_of_blades)
        #self.attackers.append(temp)
        
        
        dead_array = numpy.zeros(number,dtype=numpy.int64)
        wounds_but_no_dead = numpy.zeros(number, dtype=numpy.int64)
        eff = numpy.zeros(number)
        moral = numpy.zeros(number, dtype=numpy.int64)
        
        for i in range(number):
            
           # ded, wounds_but_no_dead = self.sim()
            
            dead_array[i],wounds_but_no_dead[i],eff[i], moral[i] = self.sim()
            
            
            
        
        #dmgav = numpy.average(dead_array)  
        #print(dmgav) 
        #wav = numpy.average(wounds_but_no_dead)
        #print(wav)
        
        #print(eff)
        print(dead_array)
        print(moral)
        return dead_array, wounds_but_no_dead, eff, moral 

    def reset_sim(self):
        
        self.attackers = []
        self.shooters = []
        self.target = None
        self.hit_rules = []
        self.wound_rules = []
        
        pass

if __name__ == '__main__':
    
    
    sim = Simulation()
    
    sim.overall_Sim(1000)
    
    