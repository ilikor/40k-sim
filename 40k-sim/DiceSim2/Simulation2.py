#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
Auteur: Samuel Turgeon
Pour le plaisir personnel

Ce program est créé pour simuler des jets de dés qui suivent les règles de wh40k.
La classe Simulation est l'objet conteneur des attaquants et du defendeur
La fonction overall_Sim est le point d'entrée externe
On ajoute les attaquants avec la fonction add_Attacker ou add_Attackers
"""

import time
from copy import copy
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy

from DiceSim2 import SimHelper as shelp
from DiceSim2.Attack import Attack
from DiceSim2.Defense import Defense
from DiceSim2 import RollingFunctions as RF


class Simulation():
    # TODO: Class Docstring
    
    def __init__(self):

        self.shooters = []  # Contient les profils des differentes attaques
        self.target = Defense(4, 1, 3)
        self.target.FnP = [0]

        self.attackers = []

    def hit_phase(self, shooters, target):
        """
        WORK IN PROGRESS:
        Cette fonction fait le jet pour toucher dans 40k
        Elle cherche a etre parralelisable
        PARAMETERS:
        shooters est une liste [Attack]
        target est un objet Defense
        FONCTION GOAL:
        La fonction agit en deux moments
        Un premier moment fait le jet de dé pour tous les attaquants
        Un second moment applique les regles speciales
        Un troisieme moment enleve les resultats manquant et construit les nouveaux tireurs pour le jet pour blesser
        """
        
        results = list(self.hit_roll_iter(shooters))
        for result, shooter in zip(results, shooters):
            """
            Cette boucle va appliqué
            les regles special de chacun
            des tireurs sur ses resultats
            """
            for regle in shooter.hit_rules:
                new_result, new_shooter = regle.special_rule(result, shooter)
                if new_result.size != 0 and new_shooter:
                    results.append(new_result)
                    shooters.append(new_shooter)
                    
        next_step = list(self.hit_to_wound_iter(results, shooters))
        
        return next_step
            
    def hit_roll_iter(self, shooters):
        """
        Generateur des resultats de dés pour toucher
        """
        for shooter in shooters:
            number_dices = shelp.determine_attack(shooter)
            result_dices = RF.rollingd6s(number_dices, shooter.hit_reroll)
            yield result_dices
            
    def hit_to_wound_iter(self, results, shooters):
        """
        On passe les resultats des jets de des
        On passe les attaques associes
        On garde seulement les resultats au dessus
        du hitrate modifie de chaque attaque
        On compile le nombre de succes et cree des nouvelles attaques
        avec le nombre de des = nb success
        """
        for result, shooter in zip(results, shooters):
            if shooter.hit_rate != "AUTO":
                # Les results sous le nombre requis pour toucher son enlever
                target_number = shooter.hit_rate - shooter.hit_mod
                if target_number < 2:
                    target_number = 2
                result[:target_number - 1] = 0
            # print(result)
            sum_success = int(numpy.sum(result))
            # On construit prochaine etape
            temp = copy(shooter)
            temp.R = sum_success
            yield temp
              
    def wound_phase(self, shooters, target):
        # On genere l'array des resultats des des pour chacun des shooters
        results = [RF.rollingd6s(shooter.R, shooter.wnd_reroll)
                   for shooter in shooters]
        # Pour chaque pair, on fait leur regle special
        for result, shooter in zip(results, shooters):
            for regle in shooter.wnd_rules:
                new_result, new_shooter = regle.special_rule(result, shooter)
                if new_result.size != 0 and new_shooter:
                    results.append(new_result)
                    shooters.append(new_shooter)
        # On prepare les attack pour la prochaine etape
        next_step = list(self.wnd_to_save_iter(results, shooters))
        
        return next_step
        
    def wnd_to_save_iter(self, results, shooters):
        """
        On garde seulement les success pour les passer dans les nouveaux
        shooters pour la save phase
        """
        for result, shooter in zip(results, shooters):
            if shooter.ap != "MW":
                target_number = shelp.determine_wound_roll(shooter, self.target) - shooter.wnd_mod
                if target_number < 2:
                    target_number = 2
                result[:target_number - 1] = 0
            # print(result)
            sum_success = int(numpy.sum(result))
            # On construit prochaine etape
            temp = copy(shooter)
            temp.R = sum_success
            yield temp
    
    def save_phase(self, shooters, target):
        """
        Le saving throw
        """
        # On genere les des
        results = [RF.rollingd6s(shooter.R) for shooter in shooters]
        
        # On prepare les attaques pour la prochaine etape
        next_step = list(self.save_to_dmg_iter(results, shooters))
        return next_step
    
    def save_to_dmg_iter(self, results, shooters):
        """
        Une save manque (Donc un dommage qui passe a la 
        prochaine etape) est sous le nombre
        """
        for result, shooter in zip(results, shooters):
            # print(result)
            if shooter.ap != "MW":
                target_number = shelp.determine_save(shooter, self.target) - shooter.sv_mod
                if target_number < 2:
                    target_number = 2
                result[(target_number - 1):] = 0
            # print(result)
            sum_success = int(numpy.sum(result))
            temp = copy(shooter)
            temp.R = sum_success
            yield temp

    def damage_phase2(self, shooters, target):
        """
        On lance les degats 1 à 1 pour calculer 
        l'overkill et eviter le spillover
        """
        
        dead = 0
        for shooter in shooters:

            number, dx = shelp.damage_string_reader(str(shooter.dmg))

            for i in range(shooter.R):
                dmg = numpy.sum(RF.rollingdxs_time_dependant(number, dx + 1))
                target.feel_no_pain(dmg)
                dead += target.deal_wounds(shooter.AP, dmg)

        wounds_dealt = target.w - target.rem_w

        return dead, wounds_dealt

    def moral_phase(self, dead, reroll=None):
        
        morale = self.target.moral
    
        ded = 0
        roll = numpy.random.randint(1, 7)
        total = roll + dead
        if total > morale:
            
            if reroll == "CAN" and roll > 4:
                
                roll = numpy.random.randint(1, 7)
                total = roll + dead

            elif reroll == "MUST":
                
                roll = numpy.random.randint(1, 7)
                total = roll + dead       
            
            elif reroll == "COMMI":
                
                ded += 1
                roll = numpy.random.randint(1, 7)
                total = roll + dead
            
            elif reroll == "KNIFE" and roll == 6:
                
                total = 0
                
            elif reroll == "AUTO":
                
                total = 0
            
            if total > morale:

                dedl = (total - morale)
                ded += dedl
            
        return ded

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
        # print(points_dead)
        
        eff = points_dead / points_in_attack
        # print(eff)
        return eff
        
    def sim(self):
        
        self.shooters = deepcopy(self.attackers)

        wound_shooters = self.hit_phase(self.shooters, self.target)
        save_shooters = self.wound_phase(wound_shooters, self.target)
        dmg_shooters = self.save_phase(save_shooters, self.target)
        deads, wounds = self.damage_phase2(dmg_shooters, self.target)
        moral = self.moral_phase(deads) + deads
        eff = self.efficiency(moral)
        
        return deads, wounds, eff, moral
    
    def add_attacker(self, attacker):
        
        self.attackers.append(attacker)
      
    def add_attackers(self, attackers_init):
        
        self.attackers = attackers_init
    
    def change_defender(self, defender_init):
        
        self.target = defender_init
        
    def add_default_attacker(self):
        
        temp = Attack()
        temp.r = 1000
        temp.str = 6
        temp.dmg = "1"
        temp.ap = -1
        temp.set_reroll(2, 2)
        # temp.hit_rules.append(self.exploding_dices)
        # temp.hit_rules.append(self.ambush_of_blades)
        self.attackers.append(temp)
    
    def overall_sim(self, number):
        """
        
        repeat the simulate and accumulates the results
        it will release the accumulated results at the end
        dead, wounds, eff, moral is the order of returns
        """
        
        dead_array = numpy.zeros(number, dtype=numpy.int32)
        wounds_but_no_dead = numpy.zeros(number, dtype=numpy.int32)
        eff = numpy.zeros(number)
        moral = numpy.zeros(number, dtype=numpy.int32)
        
        for i in range(number):
            
            # ded, wounds_but_no_dead = self.sim()
            dead_array[i], wounds_but_no_dead[i], eff[i], moral[i] = self.sim()
    
        # dmgav = numpy.average(dead_array)
        # print(dmgav)
        # wav = numpy.average(wounds_but_no_dead)
        # print(wav)
        
        # print(eff)
        # print(dead_array)
        # print(moral)
        return dead_array, wounds_but_no_dead, eff, moral

    def reset_sim(self):
        
        self.attackers = []
        self.shooters = []
        self.target = None

    def sim_test(self):
        
        temp = Attack()
        temp.attack = "4"
        temp.r = 100
        temp.s = 3
        temp.dmg = "1"
        temp.ap = 0
        # temp.hit_reroll = 1
        # temp.add_wnd_rule(["4+,6+", "1,1", "Haywire"])
        
        self.add_attacker(temp)
        
        self.shooters = deepcopy(self.attackers)

        wound_shooters = self.hit_phase(self.shooters, self.target)
        # print(wound_shooters)
        save_shooters = self.wound_phase(wound_shooters, self.target)
        print(save_shooters)
        dmg_shooters = self.save_phase(save_shooters, self.target)
        # print(dmg_shooters)
        deads, wounds = self.damage_phase2(dmg_shooters, self.target)
        print(deads, wounds)
        moral = self.moral_phase(deads)
        print(moral)
        eff = self.efficiency(moral)

    def time_testing(self):
        # Fonction pour tester la complexité de l'algo
        
        list_r = range(200, 4000, 200)
        list_hit = []
        list_wnd = []
        list_save = []
        list_dmg = []
        list_total = []
        
        for r in list_r:
            print(r)
            temp = Attack()
            temp.r = r
            temp.s = 6
            temp.dmg = "1d6"
            temp.ap = 0
            #temp.hit_reroll = 1
            
            self.attackers= [temp, deepcopy(temp)]
            
            temps_dep_total = time.clock()
            print(self.sim())
            list_total.append( time.clock() - temps_dep_total)

        #plt.plot(list_r, list_hit)
        plt.plot(list_r, list_total)
        plt.show()


if __name__ == '__main__':
    
    sim = Simulation()
    sim.sim_test()
    #sim.time_testing()
    
    #sim.add_default_attacker()
    #sim.overall_Sim(1000)