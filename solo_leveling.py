#Created on Mon May 20 20:29:30 2024
# solo leveling verse
import random
class Player:

    def __init__(self,name):
        self.name=name
        self.max_hp=100
        self.chestplate_defense=0
        self.boots_defense=0
        self.helmet_defense=0
        self.leggings_defense=0
        self.defense=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
        self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
        self.attack_weapon=0
        self.attack=10
        self.inventory={}
        self.weapons={'bloodmoon_dagger':15,'shadow_strike_dagger':12,'razen_slayer':25,
                      'kasaka_venom_fang':100,'baruka_dagger':550,'groctar_sword':470,'orc_battle_axe':575,
                      'demon_king_dagger':700,'demon_king_longsword':1000,'orb_of_avarice':self.attack*2,
                      'frost_bite_spear':4500,'regeneration_orb':100000,'monarch_fangblade':7000,
                      'chimera_glaw_gauntlets':8000,'ethereal_grimoire':500000,'ruin_blade':60000,
                      'knight_killer':250,'moonshadow':7200,'shadow_scythe':8000,
                      'demonic_plum_flower_sword':17000,'kamish_wrath':35000}
        self.chestplate={'magicians_robe':150,'demon_king_chestplate':120000,
                         'high_knight_chestplate':80,'high_demon_chestplate':6000,'destroyer_chestplate':18000,
                        'dragon_knight_chestplate':50000,'shadow_monarch_chestplate':400000}
        self.helmet={'knight_helmet':90,'demon_king_helmet':70000,'igris_helmet':5000,
                     'high_knight_helmet':50,'high_demon_helmet':3000,'destroyer_helmet':9000,
                    'dragon_knight_helmet':30000,'shadow_monarch_helmet':250000}
        self.leggings={'archers_leggings':100,'demon_king_leggings':150000,
                       'high_knight_leggings':60,'high_demon_leggings':4000,'destroyer_leggings':12000,
                        'dragon_knight_leggings':40000,'shadow_monarch_leggings':300000}
        self.boots={'knight_boots':85,'demon_king_boots':75000,
                    'high_knight_boots':50,'high_demon_boots':3000,'destroter_boots':9000,
                    'dragon_knight_boots':30000,'shadow_monarch_boots':270000}
        self.inventory_weapon=[]
        self.inventory_helmet=[]
        self.inventory_chestplate=[]
        self.inventory_leggings=[]
        self.inventory_boots=[]
        self.level=1
        self.money=0
        self.required_xp=0
        self.amount_xp=0
        self.shadow_army=[]
        self.weapon=None
        self.shadow_army=[]
        self.equiped_gear = {
            'helmet': None,
            'chestplate': None,
            'leggings': None,
            'boots': None,
            'weapon': None,
        }
    
    def info(self,enemy):
        print('\n')
        print(f"{self.name} has health {self.hp} ")
        print(f"{enemy.name} has health of {enemy.hp} ")
        print(f"attack : {self.attack+self.attack_weapon}")
        print(f"your current level is {self.level} and the xp store {self.amount_xp} , required xp is {self.required_xp}")
        print(f"your cash : {self.money}")
        print(f"inventory : {self.inventory}")
        print(f"inventory_weapon :{self.inventory_weapon}")# damage : {self.weapon[self.inventory_weapon[0]]}")
        print(f"inventory_chestplate : {self.inventory_chestplate}")
        print(f"inventory_helmet : {self.inventory_helmet}")
        print(f"inventory_leggings : {self.inventory_leggings}")
        print(f"inventory_boots : {self.inventory_boots}")
        print('\n')
        for i in self.equiped_gear:
            if self.equiped_gear[i]!=None:
                if i=='weapon':
                    stat=self.weapons[self.equiped_gear[i]]
                elif i=='helmet':
                    stat=self.helmet[self.equiped_gear[i]]
                elif i=='chestplate':
                    stat=self.chestplate[self.equiped_gear[i]]
                elif i=='leggings':
                    stat=self.leggings[self.equiped_gear[i]]
                elif i=='boots':
                    stat=self.boots[self.equiped_gear[i]]
                else:
                    stat=0
                print(f"equiped {i} : {self.equiped_gear[i]} , stat : {stat}")
        print('\n')       
    
    def equip_weapon(self):

        print(self.inventory_weapon)
        weapon=input('enter the name of weapon to equip : ')
        check=False
        for thing in self.inventory_weapon:
            if thing in self.weapons:
                if thing==weapon:
                    self.attack_weapon=0
                    self.equiped_gear['weapon']=weapon
                    self.attack_weapon+=self.weapons[weapon]
                    print(self.equiped_gear)
                    check=True
        if check==False:
            print(f'there is no weapon called {weapon} in your inventory')
        else:
            check=False
    
    def equip_gear(self,gear_name,gear,inventory_gear,gear_defense):
        print(inventory_gear)
        gear_type=input(f"enter the name of {gear_name} to equip : ")
        check=False 
        for thing in inventory_gear:
            if thing in gear:
                if thing==gear_type:
                    gear_defense=0
                    self.equiped_gear[gear_name]=gear_type
                    gear_defense+=gear[gear_type]
                    print('gear defense : ',gear_defense)
                    if gear_name=='chestplate':
                        self.chestplate_defense=0
                        self.chestplate_defense+=gear_defense
                        #self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
                        #print('chestplate : ',self.chestplate_defense)
                    elif gear_name=='helmet':
                        self.helmet_defense=0
                        self.helmet_defense+=gear_defense
                        #self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
                    elif gear_name=='leggings':
                        self.leggings_defense=0
                        self.leggings_defense+=gear_defense
                        #self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
                    elif gear_name=='boots':
                        self.boots_defense=0
                        self.boots_defense+=gear_defense
                    check=True
                    self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
                    #self.defense+=self.gear_defense
                    print(self.equiped_gear)
        if check==False:
            print(f'there is no equipment called {gear_type} in your inventory')
        else:
            check=False      
            
    def level_up(self,enemy):
        self.amount_xp+=enemy.xp
        while True:
            self.required_xp=100*((1.15)**(self.level-1))
            if(self.amount_xp>=self.required_xp):
                self.amount_xp-=self.required_xp
                self.level+=1
                self.attack+=10*self.level*0.25
                self.max_hp+=30*self.level*0.25
                print(f'\n YOU HAVE LEVELED UP , your current level is {self.level}')
                print(f'your max hp : {self.max_hp}')
                self.required_xp=100*((1.15)**(self.level-1))
            else:
                break
            
    def damage_taken(self,enemy):
        self.hp-=enemy.damage
        print(f"you have taken {enemy.damage} damage points from {enemy.name}")
        if(self.hp<=0):
            print(f"you are defeated at level {self.level}")
            
    def attack_enemy(self,enemy):
        damage=random.randint(int(self.attack+self.attack_weapon-2),int(self.attack+self.attack_weapon+2))
        enemy.hp-=damage
        if(enemy.hp<=0):
            print(f"you defeated a {enemy.name}")
            self.level_up(enemy)
            self.collect_loot(enemy)
            self.coins_gained(enemy)
           
    def coins_gained(self,enemy):
        self.money+=enemy.coins
        
    def collect_loot(self,enemy):
        item=random.choice(enemy.loot)
        weapon_enemy=['goblin','assassins','KASAKA_RULER_OF_SWAMP','BARUKA_BOSS','GROCTAR_WARLORD','high_orc_commander','METUS','SILLAD_MONARCH_OF_FROST',
                      'QUEREHSHA_MONARCH_OF_PLAGUE','RAKAN_MONARCH_OF_FANGS','TARNAK_MONARCH_OF_IRONBODY','YOGUMUNT_MONARCH_OF_TRANSFIGURATION',
                      'ANTARES_MONARCH_OF_DESTRUCTION']
        #healing_weapons=
        chestplate_enemy=['magician']
        leggings_enemy=['archer']
        helmet_enemy=['knight','RED_BLOOD_IGRIS']
        baran_loot=[['demon_king_dagger','demon_king_longsword'],'demon_king_chestplate','demon_king_helmet','demon_king_leggings','demon_king_boots']
        #shadow_enemy=['RED_BLOOD_IGRIS','KARGALGAN_shaman']
            
        if enemy.name in weapon_enemy:
            if item not in self.inventory_weapon and item not in self.inventory:
                self.inventory_weapon.append(item)
                print(f"You have collected {item} from {enemy.name}.")
        #elif enemy.name in shadow_enemy:
        #   if item not in self.shadow_army:
        #       self.shadow_army.append(item)
        #       print(f"ARISE {item}")
        elif enemy.name in chestplate_enemy:
            if item not in self.inventory_chestplate:
                self.inventory_chestplate.append(item)
                print(f"You have collected {item} from {enemy.name}.")
        elif enemy.name in leggings_enemy:
            if item not in self.inventory_leggings:
                self.inventory_leggings.append(item)
                print(f"You have collected {item} from {enemy.name}.")
        elif enemy.name in helmet_enemy:
            if item not in self.inventory_helmet:
                self.inventory_helmet.append(item)
                print(f"You have collected {item} from {enemy.name}.")
        else:
            if item in self.inventory:
                self.inventory[item] += 1 
            else:
                self.inventory[item] = 1  
                print(f"You have collected {item} from {enemy.name}.")
        #boss loots    
        if enemy.name == 'DEMON_KING_BARAN':
            for i in baran_loot[0]:
                self.inventory_weapon.append(i)
                print(f"You have collected {i} from {enemy.name}.")
            self.inventory_chestplate.append(baran_loot[1])
            print(f"You have collected {baran_loot[1]} from {enemy.name}.")
            self.inventory_helmet.append(baran_loot[2])
            print(f"You have collected {baran_loot[2]} from {enemy.name}.")
            self.inventory_leggings.append(baran_loot[3])
            print(f"You have collected {baran_loot[3]} from {enemy.name}.")
            self.inventory_boots.append(baran_loot[4])
            print(f"You have collected {baran_loot[4]} from {enemy.name}.")
        
    #cheak this out *******************************************************
    def purchase_weapon(self,market):
        print('your money : ',self.money)
        gear=input('enter the gear to buy : ')
        if gear in market.weapon_price:
            if self.money>=market.weapon_price[gear]:
                self.money-=market.weapon_price[gear]
                self.weapons[gear]=market.weapon_store[gear]
                self.attack_weapon=0
                self.equiped_gear['weapon']=gear
                self.attack_weapon+=self.weapons[gear]
                print(self.equiped_gear)
                self.inventory_weapon.append(gear)
                del market.weapon_price[gear]
            else:
                print('you didnt have enough money for ',gear)
        else:
            print(f'there is no weapon called {gear} here')
                
    def order(self,gear_name,gear_type,gear,gear_price,gear_store,gear_defense,invent):
        if gear in gear_price:
            if self.money>=gear_price[gear]:
                self.money-=gear_price[gear]
                gear_type[gear]=gear_store[gear]
                gear_defense=0
                self.equiped_gear[gear_name]=gear
                gear_defense+=gear_type[gear]
                print(self.equiped_gear)
                print('defense added : ',gear_defense)
                if gear in gear_type :
                        invent.append(gear)
                        del gear_price[gear]
                return gear_defense
            else:
                print('you didnt have enough money for ',gear)
                return 0
        else:
            print(f'there is no equipment called {gear} here')        
          
    def purchase_armour(self,market):
        market.info_armour()
        print('''
1)purchase chestplate
2)purchase helmet
3)purchase boots
4)purchase leggings
9)resume''')
        print('your money : ',self.money)
        while True:
            try:
                choice=int(input('enter your choice : '))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                    
        if(choice==1):
            gear=input('enter the gear to buy : ')
            defense_chest=self.order('chestplate',self.chestplate,gear,market.chestplate_price,market.chestplate_store,self.chestplate_defense,self.inventory_chestplate)
            self.chestplate_defense=defense_chest
            #print('defense : ',self.chestplate_defense)
            self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
            
        elif(choice==2):
            gear=input('enter the gear to buy : ')
            defense_helmet=self.order('helmet',self.helmet,gear,market.helmet_price,market.helmet_store,self.helmet_defense,self.inventory_helmet)
            self.helmet_defense=defense_helmet
            #print('defense : ',self.helmet_defense)
            self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
                    
        elif(choice==3):
            gear=input('enter the gear to buy : ')
            defense_boots=self.order('boots',self.boots,gear,market.boots_price,market.boots_store,self.boots_defense,self.inventory_boots)
            self.boots_defense=defense_boots
            #print('defense : ',self.boots_defense)
            self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense
            
        elif(choice==4):
            gear=input('enter the gear to buy : ')
            defense_leggings=self.order('leggings',self.leggings,gear,market.leggings_price,market.leggings_store,self.leggings_defense,self.inventory_leggings)
            self.leggings_defense=defense_leggings
            #print('defense : ',self.leggings_defense)
            self.hp=self.max_hp+self.chestplate_defense+self.helmet_defense+self.boots_defense+self.leggings_defense

class Market:
    def __init__(self):     
        self.inventory={}     
        self.money=0     
        self.thing=''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        self.weapon_store={'knight_killer':250,'moonshadow':7200,'shadow_scythe':8000,
                           'demonic_plum_flower_sword':17000,'kamish_wrath':35000}
        self.chestplate_store={'high_knight_chestplate':80,'high_demon_chestplate':6000,'destroyer_chestplate':18000,
                        'dragon_knight_chestplate':50000,'shadow_monarch_chestplate':400000}
        self.leggings_store={'high_knight_leggings':60,'high_demon_leggings':4000,'destroyer_leggings':12000,
                        'dragon_knight_leggings':40000,'shadow_monarch_leggings':300000}
        self.boots_store={'high_knight_boots':50,'high_demon_boots':3000,'destroter_boots':9000,
                    'dragon_knight_boots':30000,'shadow_monarch_boots':270000}
        self.helmet_store={'high_knight_helmet':50,'high_demon_helmet':3000,'destroyer_helmet':9000,
                    'dragon_knight_helmet':30000,'shadow_monarch_helmet':250000}
        self.weapon_price={'knight_killer':25000,'moonshadow':520000,'shadow_scythe':600000,'demonic_plum_flower_sword':1500000,'kamish_wrath':2500000}
        self.chestplate_price={'high_knight_chestplate':300,'high_demon_chestplate':18000,'destroyer_chestplate':54000,
                               'dragon_knight_chestplate':150000,'shadow_monarch_chestplate':6000000}
        self.leggings_price={'high_knight_leggings':250,'high_demon_leggings':12000,'destroyer_leggings':36000,
                             'dragon_knight_leggings':120000,'shadow_monarch_leggings':4800000}
        self.boots_price={'high_knight_boots':200,'high_demon_boots':9000,'destroyer_boots':27000,
                          'dragon_knight_boots':90000,'shadow_monarch_boots':3200000}
        self.helmet_price={'high_knight_helmet':150,'high_demon_helmet':9000,'destroyer_helmet':27000,
                           'dragon_knight_helmet':90000,'shadow_monarch_helmet':3200000}
        self.sell_items={'slime_essence':50,'leather':300,'core':500,'fangs':200,'d_rank_core':100,'b_rank_core':3000,
                         'yetis_fangs':5000,'bear_fur':8000,'c_rank_core':700,'a_rank_core':12000,
                         's_rank_core':100000}
    def info_weapon(self):
        print('            WEAPONS OF ELITE       ')
        for i in self.weapon_price:
            print('price of ',i,' is ',self.weapon_price[i])
            
    def info_armour(self):
        print('     \nCHESTPLATES\n')
        for i in self.chestplate_price:
            print('price of ',i,' is ',self.chestplate_price[i])
        print('     \nHELMET\n')
        for i in self.helmet_price:
            print('price of ',i,' is ',self.helmet_price[i])
        print('     \nBOOTS\n')
        for i in self.boots_price:
            print('price of ',i,' is ',self.boots_price[i])
        print('     \nLEGGINGS\n')
        for i in self.leggings_price:
            print('price of ',i,' is ',self.leggings_price[i])
            
    def sell_things(self):
        self.thing=input('enter item to sell : ')
        try:
            number=int(input('enter number of items to sell : '))
        except ValueError:
            print('please enter appropriate inputs')
            number=0
        if self.thing in self.sell_items and self.inventory:
            if self.inventory[self.thing]>=number:
                self.money+=self.sell_items[self.thing]*number
                self.inventory[self.thing]-=number
                print(f"you have successfully sold {number} {self.thing} for {self.sell_items[self.thing]*number}")
            else:
                print(f"you only number {self.inventory[self.thing]} {self.thing}")
        else:
            print(f'you didnt have {self.thing}')
            
class Enemy:
    def __init__(self,name,hp,attack,xp,coins,loot):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.xp=xp
        self.coins=coins
        self.loot=loot 
    
    def attack_player(self,player):
        self.damage=random.randint(self.attack-2,self.attack+2)

class Rank_dungeon:
    def enter_dungeon(self,Monsters,Player):
        print('''1)E rank
2)D rank
3)C rank
4)B rank
5)A rank
6)S rank
7)demon castle(s+)
8)awakening monarch(ss+)
9)FINAL BATTLE(sss+)
    ''')
        while True:
            try:
                dungeon_choice=int(input('enter your choice : '))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        if dungeon_choice==1:
            monsters=Monsters('e')
            monsters.dungeon(Enemy)
       
        elif dungeon_choice==2:
            monsters=Monsters('d')
            monsters.dungeon(Enemy)
            
        elif dungeon_choice==3:
            monsters=Monsters('c')
            monsters.dungeon(Enemy)
        
        elif dungeon_choice==4:
            print('''
1)red gate dungeon
2)great orc dungeon(b+)
''')
            choice=input('enter your choice : ')
            if choice=='1':
                monsters=Monsters('b_red')
                monsters.dungeon(Enemy)
             
            elif choice=='2':
                monsters=Monsters('b_orc')
                monsters.dungeon(Enemy)
          
        elif dungeon_choice==5:
            monsters=Monsters('a_orc')
            monsters.dungeon(Enemy)
           
        elif dungeon_choice==6:
            print('''
1)jeju s rank island
2)tokyo s rank gate(s+)
''')
            choice=input('enter your choice : ')
            if choice=='1':
                monsters=Monsters('s_ant')
                monsters.dungeon(Enemy)
           
            elif choice=='2':
                monsters=Monsters('s_giant')
                monsters.dungeon(Enemy)
             
        elif dungeon_choice==7:
            monsters=Monsters('demon_castle')
            monsters.dungeon(Enemy)
        
        elif dungeon_choice==8:
            monsters=Monsters('awakening')
            monsters.dungeon(Enemy)
            
        elif dungeon_choice==9:
            monsters=Monsters('final')
            monsters.dungeon(Enemy)

        try:  
            monsters.raid(Enemy,Player)
        except:
            print('please enter correct input')
        
        if dungeon_choice==9 and Player.hp>0:
            print('''you have successfully saved this world and climbed the top position even god is afraid of
thank you for your time and dedication you have spent on this world to complete it,,,,  by creator kandan''')  
        if(Player.hp<=0):
                decision=input('do you want to respawn [Y/N] : ')
                if (decision.upper()=='Y'):
                    Player.hp=Player.max_hp
                    
class Monsters:
    def __init__(self,monster_rank):
        self.monster_rank=monster_rank
        self.monster_list=[]
    def dungeon(self,enemy):
        if(self.monster_rank=='e'):
            goblin_loot=['bloodmoon_dagger','shadow_strike_dagger']
            slime_loot=['slime_essence']
            #igris_loot=['igris']
            #s_demon_loot=['s_rank_core']
            self.monster_list=[]
            for i in range(2):
                self.monster_list.append(Enemy('goblin',50,7,8,100,goblin_loot))
                self.monster_list.append(Enemy('slime',30,5,6,75,slime_loot))
                self.monster_list.append(Enemy('goblin',50,7,8,100,goblin_loot))
            #self.monster_list.append((Enemy('RED_BLOOD_IGRIS',10,175,300,5500,igris_loot)))
            #self.monster_list.append(Enemy('DEMON_KING_BARAN',5,17000,110000,2500000,s_demon_loot))
            
        elif(self.monster_rank=='d'):
            steel_fanged_raikan_loot=['fangs','leather','d_rank_core']
            stone_golem_loot=['d_rank_core']
            razor_clawed_briga_loot=['d_rank_core','leather']
            black_shadow_razan_loot=['fangs','leather','d_rank_core']
            kasaka_loot=['kasaka_venom_fang']
            self.monster_list=[]
            for i in range(2):
                self.monster_list.append(Enemy('steel_fanged_raikan',100,12,20,200,steel_fanged_raikan_loot))
                self.monster_list.append(Enemy('stone_golem',150,10,30,300,stone_golem_loot))
                self.monster_list.append(Enemy('black_shadow_razan',100,12,20,200,black_shadow_razan_loot))
                self.monster_list.append(Enemy('razor_clawed_briga',100,15,30,250,razor_clawed_briga_loot))
            self.monster_list.append(Enemy('KASAKA_RULER_OF_SWAMP',600,80,110,2500,kasaka_loot))
                
        elif(self.monster_rank=='c'):
            knights_loot=['knight_helmet']
            magicians_loot=['magicians_robe']
            assassins_loot=['razen_slayer']
            archers_loot=['archers_leggings']
            igris_loot=['igris_helmet']
            self.monster_list=[]
            for i in range(3):
                self.monster_list.append(Enemy('knight',200,20,50,500,knights_loot))
                self.monster_list.append(Enemy('magician',150,30,75,750,magicians_loot))
                self.monster_list.append(Enemy('assassins',100,45,75,800,assassins_loot))
                self.monster_list.append(Enemy('archer',200,20,50,600,archers_loot))
            self.monster_list.append((Enemy('RED_BLOOD_IGRIS',2700,250,300,5500,igris_loot)))
        elif(self.monster_rank=='b_red'):
            ice_elves_loot=['b_rank_core']
            yetis_loot=['yetis_fangs']
            ice_bear_loot=['bear_fur']
            baruka_boss_loot=['baruka_dagger']
            self.monster_list=[]
            for i in range(3):
                self.monster_list.append(Enemy('ice_elves',600,110,100,1600,ice_elves_loot))
                self.monster_list.append(Enemy('yetis',900,100,80,1200,yetis_loot))
                self.monster_list.append(Enemy('ice_bear',1000,150,120,1400,ice_bear_loot))
            self.monster_list.append(Enemy('BARUKA_BOSS',6000,470,600,20000,baruka_boss_loot))
        elif(self.monster_rank=='b_orc'):
            great_orc_loot=['b_rank_core']
            groctar_loot=['groctar_sword']
            for i in range(10):
                self.monster_list.append(Enemy('great_orc',900,150,120,1300,great_orc_loot))
            self.monster_list.append(Enemy('GROCTAR_WARLORD',6500,500,800,35000,groctar_loot))
        elif(self.monster_rank=='a_orc'):
            high_orc_loot=['a_rank_core']
            high_orc_commander_loot=['orc_battle_axe','a_rank_core']
            kargalgan_loot=['tusk']
            self.monster_list=[]
            for i in range(16):
                self.monster_list.append(Enemy('high_orc',2500,500,600,16000,high_orc_loot))
            for i in range(4):
                self.monster_list.append(Enemy('high_orc_commander',5000,750,1000,28000,high_orc_commander_loot))
            self.monster_list.append(Enemy('KARGALGAN_shaman',25000,2700,2500,100000,high_orc_loot))
        elif(self.monster_rank=='s_ant'):
            ant_loot=['a_rank_core']
            royal_ant_loot=['s_rank_core']
            queen_ant_loot=['s_rank_core']
            ant_king_loot=['beru']
            self.monster_list=[]
            for i in range(20):
                self.monster_list.append(Enemy('ant',8000,700,1100,25000,ant_loot))
            for i in range(5):
                self.monster_list.append(Enemy('royal_ant',22000,1200,2000,66000,royal_ant_loot))
            self.monster_list.append(Enemy('queen_ant',70000,2700,11000,250000,royal_ant_loot))
            self.monster_list.append(Enemy('ANT_KING',300000,10000,70000,700000,royal_ant_loot))
        elif(self.monster_rank=='demon_castle'):
            d_demon_loot=['d_rank_core']
            c_demon_loot=['c_rank_core']
            b_demon_loot=['b_rank_core']
            a_demon_loot=['a_rank_core']
            s_demon_loot=['s_rank_core']
            metus_loot=['orb_of_avarice']
            self.monster_list=[]
            
            for i in range(25):
                self.monster_list.append(Enemy('low_demon',100,15,30,250,d_demon_loot))
            for i in range(20):
                self.monster_list.append(Enemy('mid_demon',200,20,80,500,c_demon_loot))
            for i in range(15):
                self.monster_list.append(Enemy('high_demon',900,100,170,1200,b_demon_loot))
            for i in range(10):
                self.monster_list.append(Enemy('top_demon',2400,500,600,16000,a_demon_loot))
            for i in range(3):
                self.monster_list.append(Enemy('vulcans_gaurd',29000,1750,5500,96000,s_demon_loot))
            self.monster_list.append(Enemy('VULCAN',55000,2400,65000,250000,s_demon_loot))
            for i in range(7):
                self.monster_list.append(Enemy('demon_knight',22000,1200,4500,66000,s_demon_loot))
            for i in range(20):
                self.monster_list.append(Enemy('undead',200,20,80,500,c_demon_loot))
            self.monster_list.append(Enemy('METUS',70000,2800,75000,300000,metus_loot))
            for i in range(4):
                self.monster_list.append(Enemy('demon_lord',30000,1500,11000,74000,s_demon_loot))
            
            self.monster_list.append(Enemy('DEMON_KING_BARAN',500000,17000,110000,2500000,s_demon_loot))
            
        elif(self.monster_rank=='s_giant'):
            giant_loot=['s_rank_core']
            self.monster_list=[]
            for i in range(15):
                self.monster_list.append(Enemy('giant',50000,3500,10000,100000,giant_loot))
            self.monster_list.append(Enemy('gate_keeper',225000,10000,55000,800000,giant_loot))
            self.monster_list.append(Enemy('LEGIA_MONARCH_OF_GIANTS',600000,15000,150000,4500000,giant_loot))
        
        elif(self.monster_rank=='awakening'):
            frost_loot=['frost_bite_spear']
            plague_loot=['regeneration_orb']
            fangs_loot=['monarch_fangblade']
            self.monster_list=[]
            self.monster_list.append(Enemy('SILLAD_MONARCH_OF_FROST',450000,16000,175000,5500000,frost_loot))
            self.monster_list.append(Enemy('QUEREHSHA_MONARCH_OF_PLAGUE',500000,12500,150000,5800000,plague_loot))
            self.monster_list.append(Enemy('RAKAN_MONARCH_OF_FANGS',600000,20000,250000,4000000,fangs_loot))
        
        elif(self.monster_rank=='final'):
            tarnak_loot=['chimera_glaw_gauntlets']
            yogumunt_loot=['ethereal_grimoire']
            antares_loot=['ruin_blade']
            self.monster_list=[]
            self.monster_list.append(Enemy('TARNAK_MONARCH_OF_IRONBODY',600000,22000,270000,7000000,tarnak_loot))
            self.monster_list.append(Enemy('YOGUMUNT_MONARCH_OF_TRANSFIGURATION',450000,16000,190000,6000000,yogumunt_loot))
            self.monster_list.append(Enemy('ANTARES_MONARCH_OF_DESTRUCTION',1500000,69000,900000,15000000,antares_loot))
            
    def raid(self,enemy,player):
        for enemy in self.monster_list :
            print(f"A {enemy.name} blocks your path!")
            while (player.hp>0 and enemy.hp>0):                
                action = input("Do you want to [A]ttack or [B]lock or [I]nfo or [C]hange gear? ").lower()
                if(action=='a'):
                    player.attack_enemy(enemy)
                    if(enemy.hp>0):
                        enemy.attack_player(player)
                        player.damage_taken(enemy)
                    else:
                        break
                elif(action=='b'):
                    #defense=player.max_hp+player.chestplate_defense+player.helmet_defense+player.boots_defense+player.leggings_defense
                    #print('defense : ',player.defense)
                    if (player.hp<=(player.max_hp+player.chestplate_defense+player.helmet_defense+player.boots_defense+player.leggings_defense)*0.75):
                        player.hp+=(0.25*(player.max_hp+player.chestplate_defense+player.helmet_defense+player.boots_defense+player.leggings_defense))
                        if player.hp>player.max_hp+player.chestplate_defense+player.helmet_defense+player.boots_defense+player.leggings_defense:
                            player.hp=player.max_hp+player.chestplate_defense+player.helmet_defense+player.boots_defense+player.leggings_defense
                        print(f'your total hp points : {player.hp}')
                elif(action=='i'):
                    player.info(enemy)
                elif(action=='c'):
                    print('''1)change weapon
2)change chestplate
3)change helmet
4)change boots
5)change leggings
9)resume''')
                    choice=input('enter your choice : ')
                    if(choice=='1'):
                        player.equip_weapon()
                    elif(choice=='2'):
                        player.equip_gear('chestplate',player.chestplate,player.inventory_chestplate,player.chestplate_defense)
                    elif(choice=='3'):
                        #player.equip_helmet()
                        player.equip_gear('helmet',player.helmet,player.inventory_helmet,player.helmet_defense)
                    elif(choice=='4'):
                        #player.equip_boots()
                        player.equip_gear('boots',player.boots,player.inventory_boots,player.boots_defense)
                    elif(choice=='5'):
                        player.equip_gear('leggings',player.leggings,player.inventory_leggings,player.leggings_defense)
                    elif(choice=='9'):
                        continue  
                    else:
                        print('invalid choice input , enter a valid integer')
                else:
                     print("Invalid choice. Try again.")
                
            if(player.hp<=0):
                print('game over, you died') 
                break 
        if player.hp>0:
            print("Congratulations! You defeated all enemies in this dungeon!")
                
            
def main(): 
    print("                            Welcome To SOLO LEVELING ")
    title_ascii = '''
     ____   ___  _     ___       _     _______     _______ _     ___ _   _  ____ 
    / ___| / _ \| |   / _ \     | |   | ____\ \   / / ____| |   |_ _| \ | |/ ___|
    \___ \| | | | |  | | | |    | |   |  _|  \ \ / /|  _| | |    | ||  \| | |  _ 
     ___) | |_| | |__| |_| |    | |___| |___  \ V / | |___| |___ | || |\  | |_| |
    |____/ \___/|_____\___/     |_____|_____|  \_/  |_____|_____|___|_| \_|\____|
    '''
    print(title_ascii)
    player=Player('sung jin woo')
    print('''    you are reincarnated as a WEAKEST HUNTER OF MANKIND known as SUNG JIN WOO
          use this system to LEVEL UP and rise up to the TOP in this world         ''')
    print('              you will be playing this rpg game as SUNG JIN WOO')
    market=Market()
    rank_dungeon = Rank_dungeon()
    playing=True
    while playing:
        print('''\n
1)dungeon
2)buy weapons in market
3)buy armour in market
4)sell items in market
5)quit
        ''')
        
        while True:
            try:
                place_choice = int(input('Enter your choice: '))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

                
        if(place_choice==1):
            rank_dungeon.enter_dungeon(Monsters,player)
        elif(place_choice==2):
            while True:
                try:
                    choice=input('to continue press (o) : ')
                    if choice=='o':
                        market.info_weapon()
                        player.purchase_weapon(market)
                        print('your money : ',player.money)
                    else:
                        break
                except ValueError:
                    print('plese enter the inputs correctly')
                    
        elif(place_choice==3):
            while True:
                try:
                    choice=input('to continue press (o) : ')
                    if choice=='o':
                        player.purchase_armour(market)
                        print('your money : ',player.money)
                    else:
                        break
                except ValueError:
                    print('plese enter the inputs correctly')
            
        elif(place_choice==4):
            while True:
                try:
                    choice=input('to continue press (o) : ')
                    if choice=='o':
                        print('your loot : ')
                        print(player.inventory)
                        market.inventory.update(player.inventory)
                        market.sell_things()
                        player.money+=market.money
                        player.inventory=market.inventory
                        market.inventory={}
                    else:
                        break
                except ValueError:
                    print('plese enter the inputs correctly')
            
        elif(place_choice==5):
            print('quiting the game ....')
            break
    
if __name__ == "__main__":
    main()
# 2 june 23:38 2024
# edited for 30 min in 29 june 8:30 2024
# worked on 30 june 2024  