from random import randint
from termcolor import colored
maxHp = 10
level = 1
name = ""
scrambled_name = ""
guild = "Gray"

# TODO: make spells have custom names.
class Enemy(object):
    def __init__(self, name, health, status, color, arsenal):
        self.playerHealth = maxHp  # yours
        self.wait = 0  # enemy's
        self.name = name  # enemy's
        self.health = health  # enemy's
        self.maxHealth = health  # enemy's
        self.status = status  # enemy's
        self.color = color  # enemy's
        self.arsenal = arsenal  # enemy's
        self.defeated = True  # enemy's
        self.oneGameFreeze = False
        self.fireyRevive = False
        self.tempGuild = guild # yours
        raw_input("\n\tENCOUNTER: " + self.name + "\n")
        Enemy.your_turn(self)

    def attacked(self, damage, att_color, status):
        if damage != 0:
            if self.color == "Blue" and att_color == "Green" or self.color == "Green" and att_color == "Red" or self.color == "Red" and att_color == "Yellow" or self.color == "Yellow" and att_color == "Blue":
                damage = damage*2
                print "Effective, increased Damage!"
            if att_color == "Blue" and self.color == "Green" or att_color == "Green" and self.color == "Red" or att_color == "Red" and self.color == "Yellow" or att_color == "Yellow" and self.color == "Blue":
                damage = damage/2
                damage = round(damage, 0)
                print "Ineffective, decreased damage!"
            self.health -= damage
            raw_input("Dealt " + str(damage) + " damage!")
        Enemy.status(self, status)
        if self.health <= 0:
            if self.defeated:
                self.defeated = False
                raw_input(self.name + "'s HP was brought to zero!")
                raw_input(self.name + " was defeated!")
                global guild
                guild = self.tempGuild
            return
        if self.wait == 0:
            return Enemy.enemy_turn(self)

    def status(self, status):
        if status == "Burn":
            self.status = "Burn"
        if self.status == "Burn":
            print self.name + " is burned! -1 HP!"
            self.health -= 1

        if status == "Frozen":
            if not self.oneGameFreeze:
                self.oneGameFreeze = True
                self.status = "Frozen"
                self.wait = 4
            else:
                raw_input("Can only Freeze someone once per game!\n")
                Enemy.your_turn(self)
        if self.status == "Frozen":
            if self.health <= 0:
                return
            if self.wait > 0:
                self.wait -= 1
                print self.name + " is frozen for " + str(self.wait) + " more turns!\n"
                Enemy.your_turn(self)
            self.status = "None"

        if status == "Heal":
            origin_hp = self.playerHealth
            self.playerHealth += 9
            self.status = "None"
            if self.playerHealth >= maxHp:
                self.playerHealth = maxHp
            print "Healed " + str(self.playerHealth - origin_hp) + " HP!"

        if status == "Invisible":
            global guild
            guild = "Gray"
            raw_input("Changed Color to Gray!")
            raw_input(self.name + "Couldn't see you, and missed!")
            return Enemy.your_turn(self)

    def your_turn(self):
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        if self.status == "Invisible":
            self.color = "Gray"
            print "Enemy Health: ???  Your Health: " + str(self.playerHealth)
        else:
            print "Enemy Health: " + str(self.health) + "  Your Health: " + str(self.playerHealth)
        print spell_list
        try:
            spell_use = spell_list[input("Slot Number: ") - 1]
            raw_input("You used " + spell_use + " ...")
            damage, status, color = spell(spell_use)
        except Exception:
            raw_input("You don't have a spell in that spell slot!\n")
            Enemy.your_turn(self)
        try:
            Enemy.attacked(self, damage, color, status)
        except Exception:
            return

    def enemy_turn(self):
        length = len(self.arsenal) - 1
        attack = self.arsenal[randint(0, length)]
        print self.name + " used " + attack + "!"
        [damage, status, color] = spell(attack)
        if status == "Full Heal" and self.color == "Gold":
            self.health = 1000000
            print "Healed to full health!\n"
        elif status == "Heal":
            origin_hp = self.health
            self.health += 9
            self.status = "None"
            if self.health >= self.maxHealth:
                self.health = self.maxHealth
            print "Enemy healed " + str(self.health - origin_hp) + " HP!\n"
        else:
            if color == "Blue" and guild == "Green" or color == "Green" and guild == "Red" or color == "Red" and guild == "Yellow" or color == "Yellow" and guild == "Blue":
                damage = damage / 2
                damage = round(damage, 0)
                print "Ineffective, decreased damage!"
            if guild == "Blue" and color == "Green" or guild == "Green" and color == "Red" or guild == "Red" and color == "Yellow" or guild == "Yellow" and color == "Blue":
                damage = damage * 2
                print "Effective, increased Damage!"
            raw_input("You lost " + str(damage) + " HP!\n")
            self.playerHealth -= damage
            if self.playerHealth <= 0:
                raw_input("Your HP was brought to zero!")
                raw_input("You have been defeated!")
                if guild == "Red" and not self.fireyRevive:
                    raw_input("But the passion inside of you made you keep going!")
                    self.playerHealth = maxHp
                    self.fireyRevive = True
                elif self.name == "Thomson":
                    raw_input("")
                    raw_input("But you were revived!")
                    return
                else:
                    raw_input("Game Over")
                    print "You were defeated at level " + str(level) + " with the spells: "
                    print spell_list
                    quit()
        Enemy.your_turn(self)


def spell(spell):
    if spell == "Freeze":
        return 0, "Frozen", "Blue"
    elif spell == "Fireball":
        return 5, "Burn", "Red"
    elif spell == "Lightning":
        return 8, "None", "Yellow"
    elif spell == "Heal":
        return 0, "Heal", "Green"
    elif spell == "Magic Beam":
        return randint(2, 3), "None", "Gray"
    elif spell == "Invisibility":
        return 0, "Invisible", "Gray"
    elif spell == "Nothing":
        return 0, "None", "Gray"
    elif spell == "Raged Claws":
        return 5, "None", "Green" # Status of rage? Cuts HP in half?
    elif spell == "Sparks":
        return 4, "None", "Yellow"
    elif spell == "Magic Laser":
        return randint(4, 7), "None", "Gray"
    elif spell == "Smite":
        return 100000, "None", "Yellow"
    elif spell == "Firewall":
        return 100000, "Burn", "Red"
    elif spell == "Full Regenerate":
        return 0, "Full Heal", "Green"
    elif spell == "Frost Bite":
        return 6, "None", "Blue"
    elif spell == "Bite":
        return randint(5, 6), "None", "Gray"
    elif spell == "Snowball":
        return 3, "None", "Blue"

def chapter_one():
    global object1, spell_list, level, maxHp
    start = raw_input(colored('Elder Wizard:', 'magenta') + " Welcome new Wizard, to the Guild of Wizards! (Press enter to continue, or type 'C' to go to a certian point.)")
    if start.lower() == "c":
        return checkpoint()
    raw_input(colored('Elder Wizard:', 'magenta') + " Since it is your first time here, grab an Object and I'll Enchant it for you!")
    object1 = raw_input(colored('Elder Wizard:', 'magenta') + " What will your first object be?\n")
    print colored('Elder Wizard:', 'magenta') + " So you want a " + object1 + " to be Enchanted?"
    yorn = raw_input("(Y)es or (N)o")
    while yorn.lower() not in ["yes", "y"]:
        object1 = raw_input(colored('Elder Wizard:', 'magenta') + " What will your first object be?\n")
        print colored('Elder Wizard:', 'magenta') + " So you want a " + object1 + " to be Enchanted?"
        yorn = raw_input("(Y)es or (N)o")
    raw_input(colored('Elder Wizard:', 'magenta') + " Then let it be done! Watch closely now.")
    raw_input(colored('Elder Wizard:', 'magenta') + " First, draw a chalk circle around the Object you want to Enchant. It does not need to be perfect.")
    raw_input(colored('Elder Wizard:', 'magenta') + " Then we will find the Book for a Spell you want to Enchant the Object with.")
    raw_input(colored('Elder Wizard:', 'magenta') + " For now we will give you a basic one, Magic Beam.")
    raw_input(colored('Elder Wizard:', 'magenta') + " From the book, we cast this Spell at the circle. The chalk will then absorb the spell and enchant the Object.")
    raw_input(colored('Elder Wizard:', 'magenta') + "    La Grezz Maginka Beamos!")
    spell_list = ["Magic Beam"]
    raw_input(colored('Elder Wizard:', 'magenta') + " During the time the circle is absorbing the spell, shout what you want to say to cast the spell.")
    raw_input(colored('Elder Wizard:', 'magenta') + "    Magic Beam!")
    raw_input(colored('Elder Wizard:', 'magenta') + " The reason we do this whole process is because some spells take time, and are complex to preform.")
    raw_input(colored('Elder Wizard:', 'magenta') + " It's much easier to just say 'Magic Beam' and point than do specific motions chanting strange words.")
    raw_input(colored('Elder Wizard:', 'magenta') + " Now your " + object1 + " is Enchanted with Magic Beam. Good luck on your Wizard Way!")
    first_encounter()


def first_encounter():
    global object1, spell_list, level, maxHp, name, scrambled_name
    print "\n", object1, "has the spells:", spell_list
    raw_input("You decide to try out your new spell in the forest")

    Enemy(colored('The Tree', 'green'), 5, "None", "Green", ["Nothing"])
    raw_input("But what's this?")
    raw_input("That was no tree! It was an Ent! And it's angry!")

    # V This code makes the battle go unscripted, and you will lose. The other code is made so that you get saved.
    # ent = enemy("The Raged Ent", 25, "None", "Green", ["Raged Claws"])

    raw_input("\n\tENCOUNTER: " + colored('Raged Ent', 'green') + "\n")
    ent = 15

    while True:
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        print "Enemy Health: " + str(ent) + "  Your Health: 10"
        print spell_list
        try:
            spell_use = spell_list[input("Slot Number: ") - 1]
            damage, status, color = spell(spell_use)
            raw_input("You used " + spell_use + " ...")
            raw_input("The colored('Raged Ent', 'green') lost " + str(damage) + " HP!")
            ent -= damage
            if ent <= 0:
                break
        except Exception:
            raw_input("You don't have a spell in that spell slot!")
        break

    raw_input("The " + colored('Raged Ent', 'green') + " is attacking!")
    raw_input("   'Raged Claws'")
    raw_input("             " + colored('???:', 'red') + " Fireball!")
    raw_input("             Effective, Double Damage, -10 HP!  Burned! -1 HP!")
    ent -= 11
    if ent > 0:
        raw_input("The " + colored('Raged Ent', 'green') + " recoiled at the attack!\n")
        while True:
            print "What spell slot will you use? Equipped Objects: " + object1 + "."
            print "Enemy Health: " + str(ent) + "  Your Health: 10"
            print spell_list
            try:
                spell_use = spell_list[input("Slot Number: ") - 1]
                damage, status, color = spell(spell_use)
                raw_input("You used " + spell_use + " ...")
                raw_input("The " + colored('Raged Ent', 'green') + " lost " + str(damage) + " HP!\n")
                ent -= damage
                if ent <= 0:
                    break
            except Exception:
                raw_input("You don't have a spell in that spell slot!")
                try:
                    spell_use = spell_list[input("Slot Number: ") - 1]
                    damage, status, color = spell(spell_use)
                    raw_input("You used " + spell_use + " ...")
                    raw_input("The " + colored('Raged Ent', 'green') + " lost " + str(damage) + " HP!\n")
                    ent -= damage
                    if ent <= 0:
                        break
                except Exception:
                    raw_input("You don't have a spell in that spell slot!")
                    raw_input("The " + colored('Raged Ent', 'green') + " is attacking!")
                    raw_input("   'Raged Claws'")
                    raw_input("   Off guard, Increased Damage, -10 HP!")
                    raw_input("Your HP was brought to zero!")
                    raw_input("You have been defeated!")
                    raw_input("Game Over")
                    print "You were defeated at level 1 with the spells: "
                    print spell_list
                    quit()

    raw_input("The " + colored('Raged Ent', 'green') + "'s HP was brought to zero!")
    raw_input("The " + colored('Raged Ent', 'green') + " was defeated!")
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1

    raw_input("             " + colored('???:', 'red') + " Woah! That was a close call!")
    raw_input(colored('Noah:','red') + " Hey there, I'm Noah, member from the " + colored('Red Guild', 'red') + "!")
    raw_input(colored('Noah:','red') + " Good thing " + colored('Red Magic', 'red') + " is strong against " + colored('Green', 'green') + " creatures, else you would've been toast!")
    while True:
        name = raw_input(colored('Noah:','red') + " So, what's your name?\n")
        name = name.lower().capitalize()
        yorn = raw_input(colored('Noah:','red') + " So your name is '" + name + "' huh? (Y)es or (N)o")
        if yorn.lower() in ['y', 'yes', '1']:
            break
    raw_input(colored('Noah:','red') + " That's an interesting name, I'll be sure to remember that!")
    scrambled_name = name.lower().replace('a', '*').replace('e', '#').replace('i', '$').replace('o', ')').replace('u', '(').replace('*', 'i').replace('#', 'a').replace('$', 'e').replace(')', 'u').replace('(', 'o').capitalize()
    raw_input(colored('Noah:','red') + " So what were you doing in the Ent Woods, " + scrambled_name + "?")
    raw_input(colored('Noah:','red') + " Just testing out your first spell? Cool!")
    raw_input(colored('Noah:','red') + " OH! I got your name wrong didn't I? Yeah I don't have the best memory, but I make up for it in strength!")
    raw_input(colored('Noah:','red') + " Huh, you don't have a Guild yet. Follow me! I'll show you how to select one!")
    get_guild()


def get_guild():
    global object1, spell_list, level, maxHp, guild, guild_spell
    raw_input(colored('Noah:','red') + " Here at the Guild of Wizards, we have 4 main guilds.\n")

    raw_input(colored('Noah:','red') + colored(' Red Guild', 'red') + ", the one I'm in, is for people with energy, and Burning passions.")
    raw_input(colored('Noah:','red') + " In battle, we're just gonna come at you with attacks and never let up.")
    raw_input("\n" + colored('Red Guild', 'red') + ", proficient in " + colored('Red Magic', 'red') + ". Unlocks the spell Fireball.\n")

    raw_input(colored('Noah:','red') + " Then comes the " + colored('Blue Guild', 'blue') + ". It's full of people who are Cool, calm, and collected.")
    raw_input(colored('Noah:','red') + " In battle, they're always strategizing and planning ahead.")
    raw_input("\n" + colored('Blue Guild', 'blue') + ", proficient in " + colored('Blue Magic', 'blue') + ". Unlocks the spell Freeze.\n")

    raw_input(colored('Noah:','red') + " Then there's the " + colored('Green Guild', 'green') + ". They're very positive and always Helping people")
    raw_input(colored('Noah:','red') + " In battle, they rely on boosting their own and other's abilities with spells.")
    raw_input("\n" + colored('Green Guild', 'green') + ", proficient in " + colored('Green Magic', 'green') + ". Unlocks the spell Heal.\n")

    raw_input(colored('Noah:','red') + " Last there's the " + colored('Yellow Guild', 'yellow') + ". They're quite Shocking in their actions, and not the nicest people.")
    raw_input(colored('Noah:','red') + " In battle, they have insanely powerful spells, and they pump them out fast!")
    raw_input("\n" + colored('Yellow Guild', 'yellow') + ", proficient in " + colored('Yellow Magic', 'yellow') + ". Unlocks the spell Lightning.\n")

    raw_input(colored('Noah:','red') + " Now before you choose a guild, you should know what color spells are stronger against what. Here's a chart:")
    print "\n    " + colored('Green', 'green')
    print "    v    ^ "
    print " " + colored('Blue', 'blue') + "    " + colored('Red', 'red')
    print "    v    ^ "
    print "    " + colored('Yellow', 'yellow') + " \n"
    raw_input(colored('Noah:','red') + " The arrow points to the side that will be taking twice the damage from the opposing color.")
    while True:
        print colored('Noah:','red') + " So, what guild will you choose?"
        guild = raw_input(colored('Red','red') + ", " + colored('Blue','blue') + ", " + colored('Green','green') + ", or " + colored('Yellow','yellow'))
        guild = guild.lower().capitalize()
        if guild == "Red":
            yorn = raw_input(colored('Noah:','red') + " You want to join the " + colored('Red Guild', 'red') + "? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input(colored('Noah:','red') + " Yay! Now we're in the same guild!!")
                raw_input("\nYou chose the " + colored('Red Guild', 'red') + "!\n")
                guild_spell = ["Fireball", "La Reedos Firon Bulos"]
                break
        elif guild == "Blue":
            yorn = raw_input(colored('Noah:','red') + " So you want to join the " + colored('Blue Guild', 'blue') + "? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input(colored('Noah:','red') + " Yes, good choice!")
                raw_input("\nYou chose the " + colored('Blue Guild', 'blue') + "!\n")
                guild_spell = ["Freeze", "Al Bleo Freson"]
                break
        elif guild == "Green":
            yorn = raw_input(colored('Noah:','red') + " So you want to join the " + colored('Green Guild', 'green') + "? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input(colored('Noah:','red') + " Yes, good choice!")
                raw_input("\nYou chose the " + colored('Green Guild', 'green') + "!\n")
                guild_spell = ["Heal", "Le Grin Medihelos"]
                break
        elif guild == "Yellow":
            yorn = raw_input(colored('Noah:','red') + " You want to join the " + colored('Yellow Guild', '') + "? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input(colored('Noah:','red') + " Oh, didn't realize you would be a " + colored('Yellow', 'yellow') + ".")
                raw_input("\nYou chose the " + colored('Yellow Guild', 'yellow') + "!\n")
                guild_spell = ["Lightning", "El Yelo Lumining"]
                break
        else:
            raw_input(colored('Noah:','red') + " I'm not sure " + guild + " is a Guild.")
            yorn = raw_input(colored('Noah:','red') + " Do you still want to join a Guild? (Y)es or (N)o.")
            if yorn.lower() in ['n', 'no', '0', '2']:
                raw_input(colored('Noah:','red') + " Oh- okay.")
                raw_input("\nYou didn't choose a guild...\n")
                guild = "Gray"
                guild_spell = ["Magic Laser", "La Grezz Maginka Lessar"]
                break
    second_spell()


def second_spell():
    global badPath, guild, guild_spell
    Enemy.setGuild = guild
    raw_input(colored('Noah:','red') + " Alright, lets teach you your new spell. The chalk and books are right here, we just have to set it up.")
    while True:
        step1 = raw_input("What do you do with the chalk?\n 1)Draw a circle and point your Object. 2)Draw a circle around your Object. 3)Point the chalk at the Object.")
        if step1 == "2":
            raw_input(colored('Noah:','red') + " The book says to cast " + guild_spell[0] + " you must chant '" + guild_spell[1] + "!'")
            step2 = raw_input("What must you chant?\n")
            if step2 == guild_spell[1] or step2 == guild_spell[1] + "!":
                step3 = raw_input("How do you call this spell?\n")
                if step3 == guild_spell[0] or step3 == guild_spell[0] + "!":
                    spell_list.append(guild_spell[0])
                    print "Successful Enchant!"
                    print object1, "has the spells:", spell_list
                    break
                else:
                    raw_input("The ritual failed.")
            else:
                raw_input("The ritual failed.")
        else:
            raw_input("The ritual failed.")

    badPath = False
    raw_input("\n" + colored('Noah:', 'red') + " Great! You got your second spell!")
    raw_input(colored('Noah:','red') + " And just in time, here come the local bullies, " + colored('The Sparks', 'yellow') + ".")
    the_sparks()


def the_sparks():
    global badPath, object1, spell_list, level, maxHp, Noah, Samantha
    raw_input("\n" + colored('???:', 'yellow') + " Hey look, No-brains is trying to help the newbie with its guild!")
    raw_input(colored('Noah:','red') + " Buzz off Ethan.")
    raw_input(colored('Ethan:','yellow') + " Be quiet loser. What Guild did ya choose newbie?")
    if guild.lower() == "red":
        raw_input(colored('Ethan:','yellow') + " You joined the " + colored('Red Guild', 'red') + "? HA! What a loser! You know they're just a weaker version of the " + colored('Yellow Guild', 'yellow') + " right?")
    elif guild.lower() == "blue":
        raw_input(colored('Ethan:','yellow') + " You joined the " + colored('Blue Guild', 'blue') + "? Ha! They have the lamest battling style! They make battles drag on and it just gets so boring!")
    elif guild.lower() == "green":
        raw_input(colored('Ethan:','yellow') + " The " + colored('Green Guild', 'green') + "? Only wimps join the " + colored('Green Guild', 'green') + "! They're just so fragile!")
    elif guild.lower() == "yellow":
        raw_input(colored('Ethan:','yellow') + " " + colored('Yellow Guild', 'yellow') + "? Nice. Your cool with us. But I wouldn't hang around that Noah kid.")
        raw_input(colored('Ethan:','yellow') + " He cant remember a thing you tell him. That's what makes him so great to mess with, you can re-use insults!")
        badPath = True
    else:
        raw_input(colored('Ethan:','yellow') + " You didn't choose a Guild? How lame! You're not gonna make any friends like that.")

    if badPath:
        raw_input(colored('Ethan:','yellow') + " So wadda ya say, wanna join " + colored('The Sparks', 'yellow') + ", and actually be part of something important in this world?")
        raw_input(colored('Noah:','red') + " Don't do it " + scrambled_name + ", you'll regret it.")
        yorn = raw_input(colored('Ethan:','yellow') + " Shut it walnut. So? (Y)es or (N)o?")
        if yorn.lower() in ['y', 'yes', '1']:
            raw_input(colored('Ethan:','yellow') + " Good good, now take down this bolts-for-brains for me, would ya?")
            Enemy(colored('Noah', 'red'), 12, "None", "Red", ["Magic Beam", "Fireball"])
        elif yorn.lower() in ['n', 'no', '0', '2']:
            raw_input(colored('Ethan:','yellow') + " Oh, how disappointing.")
            badPath = False
        else:
            raw_input(colored('Ethan:','yellow') + " Huh? Never mind. Your not getting in.")
            badPath = False
    if not badPath:
        raw_input(colored('Ethan:','yellow') + " Hey Samantha, help me deal with these twerps. I'll take No-brains, you take the Newbie.")
        raw_input(colored('Samantha:','yellow') + " Right away boss.")
        Enemy(colored('Samantha', 'yellow'), 13, "None", "Yellow", ["Magic Beam", "Sparks"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input(colored('Samantha:','yellow') + " Ahh! I couldn't defeat you.")
        raw_input(colored('Ethan:','yellow') + " Get up Samantha! I will not wave a weakling in my gang!")
        raw_input(colored('Samantha:','yellow') + " I- I can't...")
        raw_input(colored('Ethan:','yellow') + " Pathetic! My Goons do not get defeated! I hereby revoke your title as a " + colored('Spark', 'yellow') + ". To the rest of you " + colored('Sparks', 'yellow') + ", lets go.")
        raw_input(colored('Noah:','red') + " Ngh... He got me good. I didn't stand a chance.")
        raw_input(colored('Noah:','red') + " There's a healing potion behind you on that shelf, Heal us!")

        print "Who would you like to heal?"
        choice = raw_input("1)" + colored('Noah', 'red') + " 2)" + colored('Samantha', 'yellow') + " 3)Self")
        if choice == "1":
            raw_input(colored('Noah:','red') + " Thanks for that. I have an extra potion, now help Her!")
            Noah = True
            print "Who would you like to heal?"
            choice = raw_input("1)Self 2)" + colored('Samantha', 'yellow') + "")
            if choice == "2":
                raw_input(colored('Samantha:','yellow') + " Wow, even after I attacked you, you saved me? Huh.")
                Samantha = True
            else:
                raw_input(colored('Samantha:','yellow') + " You monster.")
                raw_input(colored('Samantha','yellow') + " was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
                Samantha = False
        elif choice == "2":
            raw_input(colored('Noah:','red') + " You monster.")
            raw_input(colored('Noah','red') + " was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            Samantha = True
        else:
            raw_input(colored('Noah','red') + " and " + colored('Samantha','yellow') + ": You monster.")
            raw_input(colored('Noah','red') + "Noah was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            raw_input(colored('Samantha','yellow') + " was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
            Samantha = False

        if Noah and Samantha:
            raw_input(colored('Noah:','red') + " Thanks for that. Look on the bright side! We just held off " + colored('The Sparks', 'yellow') + "!")
            raw_input(colored('Samantha:','yellow') + " Speaking of which, I don't think I'm gonna try to join them again. You guys seem pretty strong though. Could I hang with you?")
            raw_input(colored('Noah:','red') + " Sure! I don't see why not!")
            raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
        elif Noah:
            raw_input(colored('Noah:','red') + " Thanks for that, but, why didn't you heal Samantha?")
            raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! A " + colored('Spark', 'yellow') + " was defeated? Duels are only permitted in the arena! Clean up this mess, I'll work on reviving them")

        elif Samantha:
            raw_input(colored('Samantha:','yellow') + " Wow. Helping me more than a friend. I like the way you roll. Don't worry, your friend can be revived, it just takes a lot of magic.")
            raw_input(colored('Samantha:','yellow') + " But for now, Invisibility! That should hide him.")
            raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
            raw_input(colored('Samantha:','yellow') + " Alright, you have fun with that, er, what was your name?")
            raw_input(colored('Samantha:','yellow') + " " + name + ", got it. You have fun doing that " + name + ". I'll put in a good word for you with " + colored('The Sparks', 'yellow') + ". Speaking of which, I gotta see if they'll let me back in. Stop by once your done")
            badPath = False
        else:
            raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! Two people defeated? And your the only person around here. Duels are only permitted in the arena!")
            elder_wizard()
    else:
        raw_input(colored('Noah:','red') + " Ngh... got me good. I didn't stand a chance.")
        raw_input(colored('Noah:','red') + " There's a healing potion behind you on that shelf, Heal me " + name + "!")
        raw_input(colored('Ethan:','yellow') + " Don't you dare.")
        choice = raw_input("1)Heal 2)Don't Heal")
        if choice == "1":
            raw_input(colored('Ethan:','yellow') + " Y'know, I had hopes for ya, you looked strong. But you disappoint me. I'll take that.")
            raw_input(colored('Ethan:','yellow') + " took the Healing Potion and smashed it on the ground")
            badPath = False
        else:
            raw_input(colored('Ethan:','yellow') + " Ha! I knew you had it in ya.")
            badPath = True
        raw_input(colored('Noah:','red') + " You monster.")
        raw_input(colored('Noah','red') + " was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
        Noah = False
        if badPath:
            raw_input(colored('Ethan:','yellow') + " Come on, some other wizards will probably find him and waste their own magic reviving him.")
            raw_input(colored('Ethan:','yellow') + " For now, lets get you initiated as an official spark.")
        else:
            raw_input(colored('Ethan:','yellow') + " Pathetic! Let's go " + colored('Sparks', 'yellow') + ".")
            raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! Someone was defeated? Duels are only permitted in the arena! Clean up this mess, then you are EXPELLED!")
            raw_input("The Elder Wizard took your Magic Objects. While leaving, you encountered an Ent in the Ent Forest.")
            object1 = "None"
            spell_list = ["Nothing"]
            Enemy(colored('The Ent', 'green'), 25, "None", "Green", ["Raged Claws"])
    chapter_two()


def chapter_two():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    if not badPath:
        if Noah and Samantha:
            # You three go around training and trying to get better and defeat the Sparks, the cannon pathway.
            raw_input(
                "The three of you clean up the mess caused by your encounter with the " + colored('Sparks', 'yellow') + ", and vow to one day defeat them.")
            raw_input(
                colored('Noah:','red') + " If were gonna defeat the sparks, were gonna need to get stronger. I say we head back to the Ent woods and level up a bit.")
            raw_input(colored('Samantha:','yellow') + " I actually have something a bit more sinister planned.")
            raw_input(
                colored('Samantha:','yellow') + " The Elder Wizard is the most powerful Wizard alive. He is a master of all colored spells.")
            raw_input(
                colored('Samantha:','yellow') + " The spells he has are crazy powerful, and I bet the books for them are still in his room!")
            raw_input(colored('Noah:','red') + " No way that sounds too dangerous.")
            while True:
                fate = raw_input(colored('Noah:','red') + " What do you say, " + name + "?\n1)Ent Forest  2)Elder Wizard")
                if fate == "1":
                    raw_input(colored('Samantha:','yellow') + " Aw, you guys are lame.")
                    # Train in the forest, encounter a king ent
                    forest()
                    break
                    # TODO: End here. Later, Try to fight the sparks.

                elif fate == "2":
                    raw_input(colored('Noah:','red') + " Okay, if you say so " + scrambled_name + ".")
                    raw_input("The three of you go to the Elder Wizard's Lobby, Samantha guiding you.")
                    raw_input(colored('Noah:','red') + " Woah, that's a huge door.")
                    raw_input(colored('Samantha:','yellow') + " And it's even bigger inside. Just look at all the books on the wall!")
                    raw_input(colored('Samantha:','yellow') + " We should split up, and look for a powerful spell.")
                    library()
                    raw_input("The three of you narrowly escape")
                    raw_input(colored('Noah:','red') + " I can't believe we got out of there!")
                    raw_input(colored('Samantha:','yellow') + " Honestly neither can I. What did you say your idea was Noah?")
                    raw_input(colored('Noah:','red') + " I forgot, but I'm panicking too much to want to do anything else than rest.")
                    raw_input(colored('Samantha:','yellow') + " But you did get some experience from trying out those spells!")
                    raw_input("Level up! Max Hp +1")
                    level += 1
                    maxHp += 1
                    break
                    # TODO: End here. Later, Try to Fight the Sparks
            crew = ["Noah", "Samantha"]
        elif Noah and not Samantha:
            raw_input(colored('Samantha:','yellow') + " You are terrible people! I'm going back to " + colored('Spark HQ', 'yellow') + ", I will make them Hate you!")
            raw_input(
                colored('Noah:','red') + " That cant be good. We should probably train so that were prepared if they attack us again.")
            raw_input(colored('Noah:','red') + " Lucky for us, we have a perfect training grounds in the form of the Ent Forest!")
            forest()
            # TODO: Ending here. Later, Try to fight the Sparks.
        elif Samantha and not Noah:
            raw_input(
                "You finish cleaning, and then head off in the direction " + colored('Samantha', 'yellow') + " went. It isn't long before you encounter a room with constant yellow flashing lights")
            raw_input(
                "Inside you find a large group of people dueling with lightning, in a rectangular arena with lightning rods on each corner.")
            raw_input(colored('Ethan:','yellow') + " Hey it's the twat from earlier. What are you doing here.")
            raw_input(colored('Samantha:','yellow') + " This twat right here just abandoned his friend to save a " + colored('Sparks', 'yellow') + ".")
            crew = ["Samantha"]
            raw_input(colored('Ethan:','yellow') + " Your not a " + colored('Spark', 'yellow') + " anymore Samantha.")
            raw_input(colored('Samantha:','yellow') + " I know, but I thought I'd appeal with " + name + " here.")
            raw_input(
                colored('Ethan:','yellow') + " Alright, " + name + ", lets see if your worthy. The first thing your gonna need to do is change your guild.")
            yorn = raw_input("You think you can do that? (Y)es or (N)o?")
            if yorn.lower() in ['y', 'yes', '1']:
                badPath = True
                spark_init()
                raw_input(colored('Ethan:','yellow') + " Samantha, I should have never doubted you. You're back in.")
                # TODO: Ending here. Later, do stuff with sparks.
            elif yorn.lower() in ['n', 'no', '0', '2']:
                badPath = False
            if not badPath:
                raw_input(
                    colored('Ethan:','yellow') + " Samantha, you're supposed to bring someone who you think will join when you try to appeal. I just can't work with this. SPARKS! Get them outta here!")
                raw_input(colored('Samantha:','yellow') + " Well that didn't work, thanks a lot.")
                raw_input(
                    colored('Samantha:','yellow') + " Ya know, I'm still in the mood to cause trouble. The Elder wizard has a whole library of spells. Ill bring you to it.")
                library()
                raw_input(
                    colored('Samantha:','yellow') + " Ha! It worked! The elder wizard used to be a " + colored('Sparks', 'yellow') + ", so he kinda has a soft spot for them. Thats why we get away with so much. It's a shame we got kicked out though...")
                raw_input(
                    colored('Samantha:','yellow') + " Anyways, learning new spells is a good way to get experience. So you probably can level up!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                # TODO: Ending here. Later, just mess around doing gimicky stuff.
    if badPath:
        spark_init()
        if not badPath:
            raw_input(colored('Ethan:','yellow') + " " + colored('SPARKS', 'yellow') + "! Get them outta here!")
            raw_input("You got kicked out of the sparks, and now you have no friends.")
            crew = ["None"]
            while True:
                lonely = raw_input("What would you like to do?\n1)Check on noah  2)Train")
                if lonely == "1":
                    print "You decide to check up on Noah."
                    raw_input("There is another wizard standing over noah, healing him.")
                    raw_input(colored('Noah:','red') + " Ugh.. What happened?")
                    raw_input("???: Someone defeated you in battle. I'm Thomson and Ill be your healer today.")
                    raw_input("Noah notices you.")
                    raw_input(colored('Noah:','red') + " Wait a minute, you did this to me " + name + "!")
                    raw_input(colored('Thomson:','green') + " You stay lying down, I'll deal with him.")
                    Enemy(colored('Thomson', 'green'), 17, "None", "Green", ["Magic Beam", "Heal"])
                    raw_input("Thomson used Revive!")
                    raw_input(colored('Thomson:','green') + " You shouldn't be attacking people you stupid " + colored('Spark', 'yellow') + "! Everyone is valid!")
                    print colored('Thomson:','green') + " Why would you do something like that? "
                    why = raw_input("1)I stood no chance against a spark, but I did against Noah. 2)I wanted to be a Spark. 3)He was dumb")
                    if why == "1":
                        raw_input(colored('Thomson:','green') + " Oh baloney! I saw you had Lightning!")
                        raw_input(colored('Thomson:','green') + " Get outta here kid!")
                    elif why == "2":
                        raw_input(colored('Thomson:','green') + " And how'd that work out for you? I saw that you didn't have the spell Sparks!")
                        raw_input(colored('Thomson:','green') + " Get outta here kid!")
                    elif why == "3":
                        raw_input(colored('Thomson:','green') + " Well it's not very smart for you to push away other people! Look at you! Now you don't have any friends!")
                        raw_input(colored('Thomson:','green') + " Get outta here kid!")
                    else:
                        raw_input(colored('Thomson:','green') + " Oh, your ashamed of it. As you should be.")
                        raw_input(colored('Thomson:','green') + " Why don't you make it up to him?")
                        raw_input("You go over to Noah")
                        apology = raw_input("1)I'm sorry. 2)Nerd.")
                        if apology == "1":
                            raw_input(colored('Noah:','red') + " I know you are. It was a smart move to get on " + colored('The Sparks', 'yellow') + " good side.")
                            raw_input(colored('Noah:','red') + " I think I've recovered now.")
                            raw_input(colored('Thomson:','green') + " That's great! So you two made up?")
                            raw_input(colored('Noah:','red') + " Yeah.")
                            crew = ["Noah", "Thomson"]
                        elif apology == "2":
                            raw_input(colored('Noah:','red') + " You deserve this.")
                            raw_input("Noah blasted a fireball into your face! It wasn't very effective, but it still hurt.")
                            raw_input(colored('Thomson:','green') + " Get outta here kid!")
                        else:
                            raw_input(colored('Noah:','red') + " You don't have anything to say?")
                            raw_input(colored('Thomson:','green') + " Get outta here kid!")
                    break
                    # TODO: Ending Here. Later, do stuff with Noah and Thompson
                elif lonely == "2":
                    raw_input("You decide to train, there's a mountain around. You try to go there.")
                    mountain()
                    break
                    # TODO: Ending Here. Later, just keep finding more spells and get stronger.
                else:
                    print "You are still undecided."



def spark_init():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, guild
    raw_input(colored('Ethan:','yellow') + " Alright, we have a little Guild station over here. The book is right there, and you can just use the last chalk circle that got used.")
    step1 = raw_input("So, you've decided to become a member of " + colored('The Sparks', 'yellow') + ". Well no " + colored('Spark', 'yellow') + " can exist without the Spell Sparks! Get used to hearing the word sparks, we use it for everything. To cast the spell, you must chant El Yelo Sparkosus. But before you do that, you must swear in to the Sparks. Say \"I solemnly swear to only respect other Sparks.\"\n")
    if step1.lower() not in ["i solemnly swear to only respect other sparks.", "i solemnly swear to only respect other sparks"]:
        raw_input(colored('Ethan:','yellow') + " NOPE! He is not " + colored('Spark', 'yellow') + " material!")
        badPath = False
    else:
        step2 = raw_input("You place your " + object1 + " in the worn chalk circle. What must you chant?\n")
        if step2 not in ["El Yelo Sparkosus", "El Yelo Sparkosus!"]:
            raw_input(colored('Ethan:','yellow') + " NOPE! He is not " + colored('Spark', 'yellow') + " material!")
            badPath = False
        else:
            step3 = raw_input("How do you call this spell?\n")
            if step3 not in ["Sparks", "Sparks!"]:
                raw_input(colored('Ethan:','yellow') + " NOPE! He is not " + colored('Sparks', 'yellow') + " material!")
                badPath = False
            else:
                spell_list.append("Sparks")
                print "Successful Enchant!"
                print object1, "has the spells:", spell_list
                if guild != "Yellow":
                    raw_input("\nYou changed to the " + colored('Yellow Guild', 'yellow') + "!\n")
                    guild = "Yellow"
                raw_input("You joined " + colored('The Sparks', 'yellow') + "!\n")
                raw_input(colored('Ethan:','yellow') + " Well, I didn't think you could do it. Welcome to the sparks, in a world of awesome superiority!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                badPath = True
                crew = ["Sparks"]


def elder_wizard():
    Enemy(colored('Elder Wizard', 'magenta'), 1000000, "None", "Gold", ["Smite"])
    raw_input(colored('Elder Wizard:', 'magenta') + " Ooohhhh...")
    raw_input(colored('Elder Wizard:', 'magenta') + " You are very powerful.")
    raw_input(colored('Elder Wizard:', 'magenta') + " Almost... too powerful.")
    raw_input(colored('Elder Wizard:', 'magenta') + " Like a Hacker.")
    raw_input("Elder Wizard leveled up! HP +1!")
    raw_input("Elder Wizard regenerated to full health!")
    Enemy(colored('Raged Elder Wizard', 'magenta'), maxHp+1, "None", "Gold", ["Firewall", "Full Regenerate"])
    raw_input(colored('Elder Wizard:', 'magenta') + " Ngh...")
    raw_input("lder Wizard: you've...")
    raw_input("der Wizard: defeated me.")
    raw_input("er Wizard: Well then, I have no choice")
    raw_input("r Wizard: I hereby grant you...")
    raw_input(" Wizard: The title of Elder Wizard.")
    raw_input("The Wizard faded to dust, leaving no trace. You have gained the title of Elder Wizard!")


def library():
    global spell_list, name
    spells_found = []
    actions = 5
    while actions > 0:
        book = raw_input("From 1 to 9, what book will you look at?\n")
        if book == "1":
            actions -= 1
            print "Found a book with the spell Le Grin Medihelios"
            spells_found.append("Le Grin Medihelios")
        elif book == "2":
            actions -= 1
            print "Found a book with the spell La Reedos Firon Bulos"
            spells_found.append("La Reedos Firon Bulos")
        elif book == "3":
            actions -= 1
            print "Found a book with the spell Al Bleo Freson"
            spells_found.append("Al Bleo Freson")
        elif book == "4":
            actions -= 1
            print "Found a book with the spell El Yelo Lumining"
            spells_found.append("El Yelo Lumining")
        elif book == "5":
            actions -= 1
            print "Found a book with the spell La Grezz Insivion"
            spells_found.append("La Grezz Insivion")
        elif book == "6":
            actions -= 1
            print "Found a book with the spell El Yelo Sparkosus"
            spells_found.append("El Yelo Sparkosus")
        elif book == "7":
            actions -= 1
            print "Found a book with the spell La Grezz Maginka Beamos"
            spells_found.append("La Grezz Maginka Beamos")
        elif book == "8":
            actions -= 1
            print "Found a book with the spell Le Grin Raginos Claus"
            spells_found.append("Le Grin Raginos Claus")
        elif book == "9":
            actions -= 1
            print "Found a book with the spell La Grezz Maginka Lessar"
            spells_found.append("La Grezz Maginka Lessar")
        elif book == "0":
            actions -= 1
            print "Found a mysterious book with the spell Aleos Maximon Goludos Smitomiras Infiniron. Looks complicated."
            spells_found.append("Aleos Maximon Goludos Smitomiras Infiniron")
        else:
            actions -= 1
            print "Found a normal book"
            spells_found.append("Nothing")
    raw_input(colored('Samantha:','yellow') + " I think I hear someone coming!")
    spell_slot = raw_input("What spell slot will you use?\n" + str(spells_found))
    spell = spells_found[int(spell_slot)-1]
    if spell == "Le Grin Medihelios":
        spell_list.append("Heal")
        raw_input("Everyone around you got healed to full health!")
        raw_input(colored('Samantha:','yellow') + " Thanks, now we can last longer when the person coming down the hall kills us. Just, play along")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noise!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, you trouble making " + colored('Sparks', 'yellow') + ". Samantha didn't I tell you? This Library is off limits!")
        raw_input(colored('Samantha:','yellow') + " Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input(colored('Elder Wizard:', 'magenta') + " Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Reedos Firon Bulos":
        spell_list.append("Fireball")
        raw_input("A fireball erupted in the middle of the room.")
        raw_input(colored('Samantha:','yellow') + " Great! Now were gonna be in twice as much trouble for property damages!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noise!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Ahh! There's a fire! Water Geyser!")
        raw_input("The fire is put out and there is steam all around.")
        raw_input(colored('Samantha:','yellow') + " Quickly, lets get out of here!")
    elif spell == "Al Bleo Freson":
        spell_list.append("Freeze")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noi-")
        raw_input("You Froze the Elder Wizard!")
        raw_input(colored('Samantha:','yellow') + " That was bold Freezing the Elder Wizard, now lets get out of here before he thaws!")
    elif spell == "El Yelo Lumining":
        spell_list.append("Lightning")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input(colored('Samantha:','yellow') + " What the heck did you just do?!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "La Grezz Insivion":
        spell_list.append("Invisibility")
        raw_input("Everyone Around you turned invisible!")
        raw_input(colored('Samantha:','yellow') + " Good thinking! now lets get out of here before this spell wears off!")
    elif spell == "El Yelo Sparkosus":
        spell_list.append("Sparks")
        raw_input(colored('Samantha:','yellow') + " Sparks? Do you seriously want to be a " + colored('Spark', 'yellow') + " in a time like this? But that gives me an idea, just play along")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noise!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, you trouble making " + colored('Sparks', 'yellow') + ". Samantha didn't I tell you? This Library is off limits!")
        raw_input(colored('Samantha:','yellow') + " Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input(colored('Elder Wizard:', 'magenta') + " Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Grezz Maginka Beamos":
        spell_list.append("Magic Beam")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Magic Beam!")
        raw_input(colored('Samantha:','yellow') + " What the heck did you just do?!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Le Grin Raginos Claus":
        spell_list.append("Raged Claws")
        raw_input("You attack Samantha with Raged Claws!")
        raw_input(colored('Samantha:','yellow') + " Agh! Why did you do that?!?!?")
        raw_input("The spell made you attack again!")
        raw_input(colored('Samantha:','yellow') + " Auughh!")
        raw_input(colored('Samantha','yellow') + " was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
        raw_input(colored('Elder Wizard:', 'magenta') + " My word! What happened here! Broken into the spell room and someone defeated? Both those are off limits!")
        elder_wizard()
    elif spell == "La Grezz Maginka Lessar":
        spell_list.append("Magic Laser")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input(colored('Samantha:','yellow') + " What the heck did you just do?!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Aleos Maximon Goludos Smitomiras Infiniron":
        spell_list.append("Smite")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noi- ")
        raw_input("The entire room is obliterated with a Smite from the skies!!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Ngh... Those poor fools. They didn't know what they were messing with.")
        raw_input("Game Over")
        print "You were defeated at level " + str(level) + " with the spells: "
        print spell_list
        quit()
    else:
        raw_input("In your panic, you froze in place, but not like the spell Freeze.")
        raw_input(colored('Samantha:','yellow') + " what are you doing? Just- just follow my lead.")
        raw_input(colored('Elder Wizard:', 'magenta') + " Who's in here? I heard noise!")
        raw_input(colored('Elder Wizard:', 'magenta') + " Oh, just you trouble making " + colored('Sparks', 'yellow') + ". Samantha didn't I tell you? This Library is off limits!")
        raw_input(colored('Samantha:','yellow') + " Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input(colored('Elder Wizard:', 'magenta') + " Just don't get any ideas! Go ahead and get out of here you rascals.")


def mountain():
    global spell_list, level, maxHp, object1, guild
    path = 0
    while path not in ["1", "2", "3"]:
        print "Chose your path:"
        print "      / \      "
        print "     /~~~\     "
        print "    / | |(\    "
        print "   / /| |\ \   "
        print "  / / | | \ \  "
        print "  1    2    3  "
        path = raw_input("")
    if path == "1":
        raw_input("When traveling up the mountain, a monster emerged from the snow!")
        Enemy(colored('The Snow Golem', 'Blue'), randint(7, 12), "None", "Blue", ["Snowball"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input("You managed to defeat the Snow Golem, but now you're lost.")
    elif path == "3":
        yorn = raw_input("You found a cave! Would you like to enter it?\n(Y)es or (N)o?")
        if yorn.lower() in ["y", "yes"]:
            raw_input("You crawled into the cave.")
            raw_input("Something with red eyes brushed by your legs!")
            Enemy(colored('???', 'grey'), 17, "Invisibile", "Gray", ["Bite", "Raged Claws"])
            raw_input("Level up! Max Hp +1")
            level += 1
            maxHp += 1
            raw_input("But the creature got up and scurried away!")
            leave = raw_input("Leave the cave?\n(Y)es of (N)o?")
            if leave.lower() in ["n", "no"]:
                raw_input("You decide not to leave the cave. That creature doesn't scare you!")
                raw_input(colored('???:','grey') + " oh but we should")
                raw_input("Who said that? How can you read my mind? ...we?")
                raw_input(colored('???:','grey') + " KYYYYYSSSSHHHHAAAAAAAA!!!")
                raw_input("Tha walls around you start to move, the cave closes in, the only light is coming from those red eyes everywhere.")
                while True:
                    Enemy(colored('Shadow Swarm', 'grey'), 36, "None", "Gray", ["Bite", "Raged Claws"])
                    raw_input(colored('???:','grey') + " but we get up again.")
                    maxHp -= 1
            else:
                raw_input("You get the heck outta there!")
                raw_input("But you tripped on something! A book?")
                raw_input("You found the Spellbook for La Grezz Insivion, Invisibility!")
                raw_input("You place your " + object1 + " on the ground, and draw a ring in the snow around it.")
                while True:
                    chant = raw_input("What do you chant?")
                    if chant in ["La Grezz Insivion", "La Grezz Insivion!"]:
                        spellname = raw_input("What's the name of the spell?")
                        if spellname in ["Invisibility", "Invisibility!"]:
                            spell_list.append("Invisibility")
                            print "Successful Enchant!"
                            print object1, "has the spells:", spell_list, "\n"
                            break
                        else:
                            print "Enchant Failed."
                    else:
                        print "Enchant Failed."

        else:
            raw_input("You decided not to enter.")
    else:
        raw_input("A blizzard blew in, and now you're lost.")
    raw_input(colored('?', 'blue') + colored('??', 'magenta') + ": COOOOORRRAAAAAAAAAHHHHHHHH!")
    raw_input("What was that?")
    raw_input("A Snow Golem with a crown on it's head emerged from the snow! It's the Snow King!")
    raw_input(colored('Snow', 'blue') + colored('King', 'magenta') + " Your color is Artificial! It must be eliminated!")
    Enemy(colored('Snow', 'Blue') + colored('King', 'magenta'), 24, "None", "Gold", ["Frost Bite"])
    raw_input(colored('Snow','blue') + colored('King','Magenta') + ": Artificial.. Yet good...")
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1


def forest():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    raw_input("You head out to the Ent Forest")
    raw_input(colored('Noah:','red') + " Alright, there are a few Ents on the border, but that wont get us much experience.")
    raw_input(colored('Noah:','red') + " I say we sneak through and get to the center to get the stronger enemies")
    raw_input(colored('Noah:','red') + " There are many paths through the forest, we should choose wisely.")
    path1 = 0
    path2 = 0
    tree = 0
    while path1 not in ["1", "2", "3"]:
        print "Chose your path:"
        print "  1    2    3  "
        print "  \ \ | | / /  "
        print "   \ \| |/ /   "
        print "    \     /    "
        print "     \   /     "
        print "      | |      "
        path1 = raw_input("")
    while path2 not in ["1", "2"]:
        print "Chose your path:"
        print " 1       2  "
        print " \ \   / /  "
        print "  \ \ / /   "
        print "   \   /    "
        print "    | |     "
        path2 = raw_input("")
    while tree not in ["1", "2"]:
        print "There are two shifty looking trees, Which one do you engage in combat with?"
        print "  ___    ___  "
        print " (\ Y)  (/ \) "
        print " (Y /)  (\ y) "
        print " -| |}  <| |+ "
        print "  |1|    |2|  "
        tree = raw_input("")
    goal = int(path1) + int(path2) + int(tree)
    if goal == 3:
        raw_input("Yep, It was an Ent!")
        Enemy(colored('The Ent', 'green'), randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 4:
        if randint(1, 3) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy(colored('The Ent', 'green'), randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 5:
        if randint(1, 2) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy(colored('The Ent', 'green'), randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 6:
        if randint(1, 3) == 1:
            raw_input("Yep, It was an Ent!")
            Enemy(colored('The Ent', 'green'), randint(12, 17), "None", "Green", ["Raged Claws"])
        else:
            raw_input("Nope, not an Ent.")
    elif goal == 7:
        raw_input("Nope, not an Ent.")
    raw_input("Other Ents noticed you, and attacked!")
    raw_input(colored('Noah:','red') + " Ahh! Theres too many! Try to fend off your side!")
    Enemy(colored('The Ent', 'green'), randint(12, 17), "None", "Green", ["Raged Claws"])
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1
    raw_input(colored('Noah:','red') + " YEAH! I think we're geting them!")
    raw_input(colored('Noah:','red') + " Oh- Oh no.")
    raw_input(colored('?','green') + colored('??','magenta') + ": ROOOOOAAAAAAHHHH!")
    if guild != "Green":
        Enemy(colored('Ent', 'green') + colored('King', 'magenta'), 25, "None", "Gold", ["Raged Claws"])
        raw_input(
            "Having defeated the Ent King, The other Ents ran off, but they left behind a Spell Book for Raged Claws")
    else:
        raw_input("A giant Ent with a Golden Crown comes out from the trees, and points to you.")
        raw_input("The other Ents grab you, and start dragging you away from your group.")
        raw_input(colored('Noah:','red') + " Ahhh! The Ent King took " + name + "!")
        raw_input("The Ents made a circle around your group, blocking them off as they took you to the Ent King.")
        raw_input(
            "Ent King: Why have you done this? Are you not a " + colored('Green', 'green') + "? Why must you attack us with a malicious " + colored('Red', 'red') + " by your side?")
        raw_input("Ent King: Training? For what? To fight the " + colored('Yellow Sparks', 'yellow') + "? My my. That's a new Guild.")
        raw_input("Ent King: 1000 years ago when I was younger, there were only 3 Guilds. " + colored('Red', 'red') + ", " + colored('Blue', 'blue') + ", and " + colored('Green', 'green') + ".")
        raw_input("Ent King: This new Guild must be artificial and unnatural, you said they were like a stronger red?")
        raw_input(
            "Ent King: Hmm. This is concerning. While I musn't leave the forest, I will grant you the spell of out people.")
        raw_input("Ent King: The Spell Book for Raged Claws.")
        raw_input("Ent King: Now go, and stop the evil that is the sparks.")
        raw_input("The Ents dispersed, allowing you and your group to escape.")
    raw_input(colored('Noah:','red') + " Wow, this forest looks super empty now. Didn't realize quite how many Ents there were")
    raw_input(colored('Noah:','red') + "But we gotta learn that new Spell! I imagine it'll be useful when fighting the sparks!")
    raw_input("You cray a circle in the dirt with a stick around your " + object1)
    raw_input(colored('Noah:','red') + " Alright, to cast Raged Claws you must chant Le Grin Raginos Claus")
    while True:
        chant = raw_input("What do you chant?")
        if chant in ["Le Grin Raginos Claus", "Le Grin Raginos Claus!"]:
            spellname = raw_input("What's the name of the spell?")
            if spellname in ["Raged Claws", "Raged Claws!"]:
                spell_list.append("Raged Claws")
                print "Successful Enchant!"
                print object1, "has the spells:", spell_list, "\n"
                break
            else:
                print "Enchant Failed."
        else:
            print "Enchant Failed."


def checkpoint():
    print "Where would you like to start? (Warning: this feature may still be buggy.)"
    print "0)Quit"
    print "1)Chapter One 2)First fight 3)Choose your Guild 4)Learn your next spell 5)First encounter with the Sparks"
    print "6)Chapter Two 7)Enter the Library 8)Enter the Ent Forest 9)Climb the Mountain 10)Fight the Elder Wizard"
    print "5 is reccomended if you want to skip setup."
    choice = input("")
    while True:
        if choice == 0:
            quit()
        elif choice == 1:
            questions(False, False, False, False, False, False, False, False)
            chapter_one()
            break
        elif choice == 2:
            questions(False, True, True, False, False, False, True, False)
            first_encounter()
            break
        elif choice == 3:
            questions(True, True, True, False, False, False, True, False)
            get_guild()
            break
        elif choice == 4:
            questions(True, True, True, True, False, False, True, False)
            second_spell()
            break
        elif choice == 5:
            questions(True, True, True, True, False, False, True, False)
            the_sparks()
            break
        elif choice == 6:
            questions(True, True, True, True, False, True, True, True)
            chapter_two()
            break
        elif choice == 7:
            questions(True, True, True, True, False, True, True, True)
            library()
            break
        elif choice == 8:
            questions(True, True, True, True, False, True, True, True)
            forest()
            break
        elif choice == 9:
            questions(False, True, True, True, False, False, True, False)
            mountain()
            break
        elif choice == 10:
            questions(False, True, True, True, False, False, True, False)
            elder_wizard()
            break
        else:
            print "Please type an appropriate response."


def questions(nameNeed, objectNeed, spellsNeed, guildNeed, crewNeed, peopleNeed, levelNeed, pathNeed):
    # TODO: People aren't going to be perfect, make a menu for some options.
    global name, scrambled_name, object1, spell_list, guild, crew, Noah, Samantha, level, maxHp, badPath, guild_spell
    name = ""
    object1 = ""
    spell_list = []
    guild = ""
    crew = []
    Noah = True
    Samantha = True
    level = 1
    maxHp = 10
    badPath = False
    if nameNeed:
        name = raw_input("What is your name?")
        scrambled_name = name.lower().replace('a', '*').replace('e', '#').replace('i', '$').replace('o', ')').replace('u', '(').replace('*', 'i').replace('#', 'a').replace('$', 'e').replace(')', 'u').replace('(', 'o').capitalize()
    if objectNeed:
        object1 = raw_input("What was your first Object?")
    if spellsNeed:
        while True:
            allSpells = ["Finished", "Magic Beam", "Freeze", "Fireball", "Lightning", "Heal", "Invisibility", "Raged Claws", "Sparks", "Magic Laser", "Smite", "Firewall", "Full Regenerate", "Frost Bite", "Bite", "Snowball"]
            spell = input("\nWhat Spells did you have? Please type one slot number. " + str(spell_list) + "\n     0             1           2          3           4         5           6               7            8           9           10        11             12               13         14        15 \n" + str(allSpells) + "\n")
            if spell != 0:
                spell_list.append(allSpells[spell])
            else:
                break
        if spell_list is []:
            spell_list = ["Nothing"]
    if guildNeed:
        guild = raw_input("What Guild are you in?").capitalize()
        if guild == "Red":
            guild_spell = ["Fireball", "La Reedos Firon Bulos"]
        elif guild == "Blue":
            guild_spell = ["Freeze", "Al Bleo Freson"]
        elif guild == "Green":
            guild_spell = ["Heal", "Le Grin Medihelos"]
        elif guild == "Yellow":
            guild_spell = ["Lightning", "El Yelo Lumining"]
        else:
            guild_spell = ["Magic Laser", "La Grezz Maginka Lessar"]
    if crewNeed:
        crew = raw_input("Who was in your Crew?")
    if peopleNeed:
        while True:
            yorn = raw_input("Is Noah alive? Y/N")
            if yorn.upper() == "Y":
                Noah = True
                break
            elif yorn.upper() == "N":
                Noah = False
                break
        while True:
            yorn = raw_input("Is Samantha alive? Y/N")
            if yorn.upper() == "Y":
                Samantha = True
                break
            elif yorn.upper() == "N":
                Samantha = False
                break
    if levelNeed:
        maxHp = input("What was your maximum health?")
        level = maxHp - 9
    if pathNeed:
        while True:
            yorn = raw_input("Are you on the Bad Path? Y/N")
            if yorn.upper() == "Y":
                badPath = True
                break
            elif yorn.upper() == "N":
                badPath = False
                break
    raw_input("Let it begin\n")


if __name__ == '__main__':
    chapter_one()
    print "\nTo be continued..."
    print "On the Bad Path? ", badPath
    print "People you hang out with:", crew
    print "Spells:", str(spell_list)
    print "Guild: " + guild + ". Level: " + str(level) + ". HP: " + str(maxHp)
    
