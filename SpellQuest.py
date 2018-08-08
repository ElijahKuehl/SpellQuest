from random import randint
maxHp = 10
level = 1
name = ""
scrambled_name = ""
guild = "Gray"


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
    start = raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Welcome new Wizard, to the Guild of Wizards! (Press enter to continue, or type 'C' to go to a certian point.)")
    if start.lower() == "c":
        return checkpoint()
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Since it is your first time here, grab an Object and I'll Enchant it for you!")
    object1 = raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m What will your first object be?\n")
    print "\033[0;35;0mElder Wizard:\033[0;0;0m So you want a " + object1 + " to be Enchanted?"
    yorn = raw_input("(Y)es or (N)o")
    while yorn.lower() not in ["yes", "y"]:
        object1 = raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m What will your first object be?\n")
        print "\033[0;35;0mElder Wizard:\033[0;0;0m So you want a " + object1 + " to be Enchanted?"
        yorn = raw_input("Yes(Y) or No(N)")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Then let it be done! Watch closely now.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m First, draw a chalk circle around the Object you want to Enchant. It does not need to be perfect.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Then we will find the Book for a Spell you want to Enchant the Object with.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m For now we will give you a basic one, Magic Beam.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m From the book, we cast this Spell at the circle. The chalk will then absorb the spell and enchant the Object.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m    La Grezz Maginka Beamos!")
    spell_list = ["Magic Beam"]
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m During the time the circle is absorbing the spell, shout what you want to say to cast the spell.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m    Magic Beam!")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m The reason we do this whole process is because some spells take time, and are complex to preform.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m It's much easier to just say 'Magic Beam' and point than do specific motions chanting strange words.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Now your " + object1 + " is Enchanted with Magic Beam. Good luck on your Wizard Way!")
    first_encounter()


def first_encounter():
    global object1, spell_list, level, maxHp, name, scrambled_name
    print "\n", object1, "has the spells:", spell_list
    raw_input("You decide to try out your new spell in the forest")

    Enemy("\033[0;32;0mThe Tree\033[0;0;0m", 5, "None", "Green", ["Nothing"])
    raw_input("But what's this?")
    raw_input("That was no tree! It was an Ent! And it's angry!")

    # V This code makes the battle go unscripted, and you will lose. The other code is made so that you get saved.
    # ent = enemy("The Raged Ent", 25, "None", "Green", ["Raged Claws"])

    raw_input("\n\tENCOUNTER: \033[0;32;0mRaged Ent\033[0;0;0m\n")
    ent = 15

    while True:
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        print "Enemy Health: " + str(ent) + "  Your Health: 10"
        print spell_list
        try:
            spell_use = spell_list[input("Slot Number: ") - 1]
            damage, status, color = spell(spell_use)
            raw_input("You used " + spell_use + " ...")
            raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m lost " + str(damage) + " HP!")
            ent -= damage
            if ent <= 0:
                break
        except Exception:
            raw_input("You don't have a spell in that spell slot!")
        break

    raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m is attacking!")
    raw_input("   'Raged Claws'")
    raw_input("             \033[0;31;0m???:\033[0;0;0m Fireball!")
    raw_input("             Effective, Double Damage, -10 HP!  Burned! -1 HP!")
    ent -= 11
    if ent > 0:
        raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m recoiled at the attack!\n")
        while True:
            print "What spell slot will you use? Equipped Objects: " + object1 + "."
            print "Enemy Health: " + str(ent) + "  Your Health: 10"
            print spell_list
            try:
                spell_use = spell_list[input("Slot Number: ") - 1]
                damage, status, color = spell(spell_use)
                raw_input("You used " + spell_use + " ...")
                raw_input("The Raged Ent lost " + str(damage) + " HP!\n")
                ent -= damage
                if ent <= 0:
                    break
            except Exception:
                raw_input("You don't have a spell in that spell slot!")
                try:
                    spell_use = spell_list[input("Slot Number: ") - 1]
                    damage, status, color = spell(spell_use)
                    raw_input("You used " + spell_use + " ...")
                    raw_input("The Raged Ent lost " + str(damage) + " HP!\n")
                    ent -= damage
                    if ent <= 0:
                        break
                except Exception:
                    raw_input("You don't have a spell in that spell slot!")
                    raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m is attacking!")
                    raw_input("   'Raged Claws'")
                    raw_input("   Off guard, Increased Damage, -10 HP!")
                    raw_input("Your HP was brought to zero!")
                    raw_input("You have been defeated!")
                    raw_input("Game Over")
                    print "You were defeated at level 1 with the spells: "
                    print spell_list
                    quit()

    raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m's HP was brought to zero!")
    raw_input("The \033[0;32;0mRaged Ent\033[0;0;0m was defeated!")
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1

    raw_input("             \033[0;31;0m???:\033[0;0;0m Woah! That was a close call!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Hey there, I'm Noah, member from the \033[0;31;0mRed Guild\033[0;0;0m!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Good thing \033[0;31;0mRed Magic\033[0;0;0m is strong against \033[0;32;0mGreen\033[0;0;0m creatures, else you would've been toast!")
    while True:
        name = raw_input("\033[0;31;0mNoah:\033[0;0;0m So, what's your name?\n")
        name = name.lower().capitalize()
        yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m So your name is '" + name + "' huh? (Y)es or (No)")
        if yorn.lower() in ['y', 'yes', '1']:
            break
    raw_input("\033[0;31;0mNoah:\033[0;0;0m That's an interesting name, I'll be sure to remember that!")
    scrambled_name = name.lower().replace('a', '*').replace('e', '#').replace('i', '$').replace('o', ')').replace('u', '(').replace('*', 'i').replace('#', 'a').replace('$', 'e').replace(')', 'u').replace('(', 'o').capitalize()
    raw_input("\033[0;31;0mNoah:\033[0;0;0m So what were you doing in the Ent Woods, " + scrambled_name + "?")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Just testing out your first spell? Cool!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m OH! I got your name wrong didn't I? Yeah I don't have the best memory, but I make up for it in strength!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Huh, you don't have a Guild yet. Follow me! I'll show you how to select one!")
    get_guild()


def get_guild():
    global object1, spell_list, level, maxHp, guild, guild_spell
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Here at the Guild of Wizards, we have 4 main guilds.\n")

    raw_input("\033[0;31;0mNoah:\033[0;0;0m \033[0;31;0mRed Guild\033[0;0;0m, the one I'm in, is for people with energy, and Burning passions.")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m In battle, we're just gonna come at you with attacks and never let up.")
    raw_input("\n\033[0;31;0mRed Guild\033[0;0;0m, proficient in \033[0;31;0mRed Magic\033[0;0;0m. Unlocks the spell Fireball.\n")

    raw_input("\033[0;31;0mNoah:\033[0;0;0m Then comes the \033[0;34;0mBlue Guild\033[0;0;0m. It's full of people who are Cool, calm, and collected.")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m In battle, they're always strategizing and planning ahead.")
    raw_input("\n\033[0;34;0mBlue Guild\033[0;0;0m, proficient in \033[0;34;0mBlue Magic\033[0;0;0m. Unlocks the spell Freeze.\n")

    raw_input("\033[0;31;0mNoah:\033[0;0;0m Then there's the \033[0;32;0mGreen Guild\033[0;0;0m. They're very positive and always Helping people")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m In battle, they rely on boosting their own and other's abilities with spells.")
    raw_input("\n\033[0;32;0mGreen Guild\033[0;0;0m, proficient in \033[0;32;0mGreen Spells\033[0;0;0m. Unlocks the spell Heal.\n")

    raw_input("\033[0;31;0mNoah:\033[0;0;0m Last there's the \033[0;33;0mYellow Guild\033[0;0;0m. They're quite Shocking in their actions, and not the nicest people.")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m In battle, they have insanely powerful spells, and they pump them out fast!")
    raw_input("\n\033[0;33;0mYellow Guild\033[0;0;0m, proficient in \033[0;33;0mYellow Magic\033[0;0;0m. Unlocks the spell Lightning.\n")

    raw_input("\033[0;31;0mNoah:\033[0;0;0m Now before you choose a guild, you should know what color spells are stronger against what. Here's a chart:")
    print "\n     \033[0;32;0m Green "
    print "   \033[0;0;0m v      ^ "
    print " \033[0;34;0m Blue    \033[0;31;0m Red "
    print "   \033[0;0;0m v      ^ "
    print "    \033[0;33;0m Yellow \n"
    raw_input("\033[0;31;0mNoah:\033[0;0;0m The arrow points to the side that will be taking twice the damage from the opposing color.")
    while True:
        print "\033[0;31;0mNoah:\033[0;0;0m So, what guild will you choose?"
        guild = raw_input("\033[0;31;0mRed\033[0;0;0m, \033[0;34;0mBlue\033[0;0;0m, \033[0;32;0mGreen\033[0;0;0m, or \033[0;33;0mYellow\033[0;0;0m ")
        guild = guild.lower().capitalize()
        if guild == "Red":
            yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m You want to join the \033[0;31;0mRed Guild\033[0;0;0m? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("\033[0;31;0mNoah:\033[0;0;0m Yay! Now we're in the same guild!!")
                raw_input("\nYou chose the \033[0;31;0mRed Guild\033[0;0;0m!\n")
                guild_spell = ["Fireball", "La Reedos Firon Bulos"]
                break
        elif guild == "Blue":
            yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m So you want to join the \033[0;34;0mBlue Guild\033[0;0;0m? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("\033[0;31;0mNoah:\033[0;0;0m Yes, good choice!")
                raw_input("\nYou chose the \033[0;34;0mBlue Guild\033[0;0;0m!\n")
                guild_spell = ["Freeze", "Al Bleo Freson"]
                break
        elif guild == "Green":
            yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m So you want to join the \033[0;32;0mGreen Guild\033[0;0;0m? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("\033[0;31;0mNoah:\033[0;0;0m Yes, good choice!")
                raw_input("\nYou chose the \033[0;32;0mGreen Guild\033[0;0;0m!\n")
                guild_spell = ["Heal", "Le Grin Medihelos"]
                break
        elif guild == "Yellow":
            yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m You want to join the \033[0;33;0mYellow Guild\033[0;0;0m? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("\033[0;31;0mNoah:\033[0;0;0m Oh, didn't realize you would be a \033[0;33;0mYellow\033[0;0;0m.")
                raw_input("\nYou chose the \033[0;33;0mYellow Guild\033[0;0;0m!\n")
                guild_spell = ["Lightning", "El Yelo Lumining"]
                break
        else:
            raw_input("\033[0;31;0mNoah:\033[0;0;0m I'm not sure " + guild + " is a Guild.")
            yorn = raw_input("\033[0;31;0mNoah:\033[0;0;0m Do you still want to join a Guild? (Y)es or (N)o.")
            if yorn.lower() in ['n', 'no', '0', '2']:
                raw_input("\033[0;31;0mNoah:\033[0;0;0m Oh- okay.")
                raw_input("\nYou didn't choose a guild...\n")
                guild = "Gray"
                guild_spell = ["Magic Laser", "La Grezz Maginka Lessar"]
                break
    second_spell()


def second_spell():
    global badPath, guild, guild_spell
    Enemy.setGuild = guild
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Alright, lets teach you your new spell. The chalk and books are right here, we just have to set it up.")
    while True:
        step1 = raw_input("What do you do with the chalk?\n 1)Draw a circle and point your Object. 2)Draw a circle around your Object. 3)Point the chalk at the Object.")
        if step1 == "2":
            raw_input("\033[0;31;0mNoah:\033[0;0;0m The book says to cast " + guild_spell[0] + " you must chant '" + guild_spell[1] + "!'")
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
    raw_input("\n\033[0;31;0mNoah:\033[0;0;0m Great! You got your second spell!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m And just in time, here come the local bullies, \033[0;33;0mThe Sparks\033[0;0;0m.")
    the_sparks()


def the_sparks():
    global badPath, object1, spell_list, level, maxHp, Noah, Samantha
    raw_input("\n\033[0;33;0m???:\033[0;0;0m Hey look, No-brains is trying to help the newbie with its guild!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Buzz off Ethan.")
    raw_input("\033[0;33;0mEthan:\033[0;0;0m Be quiet loser. What Guild did ya choose newbie?")
    if guild.lower() == "red":
        raw_input("\033[0;33;0mEthan:\033[0;0;0m You joined the \033[0;31;0mRed Guild\033[0;0;0m? HA! What a loser! You know they're just a weaker version of the \033[0;33;0mYellow Guild\033[0;0;0m right?")
    elif guild.lower() == "blue":
        raw_input("\033[0;33;0mEthan:\033[0;0;0m You joined the \033[0;34;0mBlue Guild\033[0;0;0m? Ha! They have the lamest battling style! They make battles drag on and it just gets so boring!")
    elif guild.lower() == "green":
        raw_input("\033[0;33;0mEthan:\033[0;0;0m The \033[0;32;0mGreen Guild\033[0;0;0m? Only wimps join the \033[0;32;0mGreen Guild\033[0;0;0m! They're just so fragile!")
    elif guild.lower() == "yellow":
        raw_input("\033[0;33;0mEthan:\033[0;0;0m \033[0;33;0mYellow Guild\033[0;0;0m? Nice. Your cool with us. But I wouldn't hang around that Noah kid.")
        raw_input("\033[0;33;0mEthan:\033[0;0;0m He cant remember a thing you tell him. That's what makes him so great to mess with, you can re-use insults!")
        badPath = True
    else:
        raw_input("\033[0;33;0mEthan:\033[0;0;0m You didn't choose a Guild? How lame! You're not gonna make any friends like that.")

    if badPath:
        raw_input("\033[0;33;0mEthan:\033[0;0;0m So wadda ya say, wanna join \033[0;33;0mThe Sparks\033[0;0;0m, and actually be part of something important in this world?")
        raw_input("\033[0;31;0mNoah:\033[0;0;0m Don't do it " + scrambled_name + ", you'll regret it.")
        yorn = raw_input("\033[0;33;0mEthan:\033[0;0;0m Shut it walnut. So? (Y)es or (N)o?")
        if yorn.lower() in ['y', 'yes', '1']:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Good good, now take down this bolts-for-brains for me, would ya?")
            Enemy("\033[0;31;0mNoah\033[0;0;0m", 12, "None", "Red", ["Magic Beam", "Fireball"])
        elif yorn.lower() in ['n', 'no', '0', '2']:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Oh, how disappointing.")
            badPath = False
        else:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Huh? Never mind. Your not getting in.")
            badPath = False
    if not badPath:
        raw_input("\033[0;33;0mEthan:\033[0;0;0m Hey Samantha, help me deal with these twats. I'll take No-brains, you take the Newbie.")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Right away boss.")
        Enemy("\033[0;33;0mSamantha\033[0;0;0m", 13, "None", "Yellow", ["Magic Beam", "Sparks"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Ahh! I couldn't defeat you.")
        raw_input("\033[0;33;0mEthan:\033[0;0;0m Get up Samantha! I will not wave a weakling in my gang!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m I- I can't...")
        raw_input("\033[0;33;0mEthan:\033[0;0;0m Pathetic! My Goons do not get defeated! I hereby revoke your title as a \033[0;33;0mSpark\033[0;0;0m. To the rest of you \033[0;33;0mSparks\033[0;0;0m, lets go.")
        raw_input("\033[0;31;0mNoah:\033[0;0;0m Ngh... He got me good. I didn't stand a chance.")
        raw_input("\033[0;31;0mNoah:\033[0;0;0m There's a healing potion behind you on that shelf, Heal us!")

        print "Who would you like to heal?"
        choice = raw_input("1)\033[0;31;0mNoah\033[0;0;0m 2)\033[0;33;0mSamantha\033[0;0;0m 3)Self")
        if choice == "1":
            raw_input("\033[0;31;0mNoah:\033[0;0;0m Thanks for that. I have an extra potion, now help Her!")
            Noah = True
            print "Who would you like to heal?"
            choice = raw_input("1)Self 2)\033[0;33;0mSamantha\033[0;0;0m")
            if choice == "2":
                raw_input("\033[0;33;0mSamantha:\033[0;0;0m Wow, even after I attacked you, you saved me? Huh.")
                Samantha = True
            else:
                raw_input("\033[0;33;0mSamantha:\033[0;0;0m You monster.")
                raw_input("\033[0;33;0mSamantha\033[0;0;0m was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
                Samantha = False
        elif choice == "2":
            raw_input("\033[0;31;0mNoah:\033[0;0;0m You monster.")
            raw_input("\033[0;31;0mNoah\033[0;0;0m was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            Samantha = True
        else:
            raw_input("\033[0;31;0mNoah\033[0;0;0m and \033[0;33;0mSamantha\033[0;0;0m: You monster.")
            raw_input("\033[0;31;0mNoah\033[0;0;0m was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            raw_input("\033[0;33;0mSamantha\033[0;0;0m was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
            Samantha = False

        if Noah and Samantha:
            raw_input("\033[0;31;0mNoah:\033[0;0;0m Thanks for that. Look on the bright side! We just held off \033[0;33;0mThe Sparks\033[0;0;0m!")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m Speaking of which, I don't think I'm gonna try to join them again. You guys seem pretty strong though. Could I hang with you?")
            raw_input("\033[0;31;0mNoah:\033[0;0;0m Sure! I don't see why not!")
            raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
        elif Noah:
            raw_input("\033[0;31;0mNoah:\033[0;0;0m Thanks for that, but, why didn't you heal \033[0;33;0mSamantha\033[0;0;0m?")
            raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! A \033[0;33;0mSpark\033[0;0;0m was defeated? Duels are only permitted in the arena! Clean up this mess, I'll work on reviving them")

        elif Samantha:
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m Wow. Helping me more than a friend. I like the way you roll. Don't worry, your friend can be revived, it just takes a lot of magic.")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m But for now, Invisibility! That should hide him.")
            raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m Alright, you have fun with that, er, what was your name?")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m " + name + ", got it. You have fun doing that " + name + ". I'll put in a good word for you with \033[0;33;0mThe Sparks\033[0;0;0m. Speaking of which, I gotta see if they'll let me back in. Stop by once your done")
            badPath = False
        else:
            raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! Two people defeated? And your the only person around here. Duels are only permitted in the arena!")
            elder_wizard()
    else:
        raw_input("\033[0;31;0mNoah:\033[0;0;0m Ngh... got me good. I didn't stand a chance.")
        raw_input("\033[0;31;0mNoah:\033[0;0;0m There's a healing potion behind you on that shelf, Heal me " + name + "!")
        raw_input("\033[0;33;0mEthan:\033[0;0;0m Don't you dare.")
        choice = raw_input("1)Heal 2)Don't Heal")
        if choice == "1":
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Y'know, I had hopes for ya, you looked strong. But you disappoint me. I'll take that.")
            raw_input("\033[0;33;0mEthan:\033[0;0;0m took the Healing Potion and smashed it on the ground")
            badPath = False
        else:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Ha! I knew you had it in ya.")
            badPath = True
        raw_input("\033[0;31;0mNoah:\033[0;0;0m You monster.")
        raw_input("\033[0;31;0mNoah\033[0;0;0m was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
        Noah = False
        if badPath:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Come on, some other wizards will probably find him and waste their own magic reviving him.")
            raw_input("\033[0;33;0mEthan:\033[0;0;0m For now, lets get you initiated as an official spark.")
        else:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Pathetic! Let's go \033[0;33;0mSparks\033[0;0;0m.")
            raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! Someone was defeated? Duels are only permitted in the arena! Clean up this mess, then you are EXPELLED!")
            raw_input("The Elder Wizard took your Magic Objects. While leaving, you encountered an Ent in the Ent Forest.")
            object1 = "None"
            spell_list = ["Nothing"]
            Enemy("\033[0;32;0mThe Ent\033[0;0;0m", 25, "None", "Green", ["Raged Claws"])
    chapter_two()


def chapter_two():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    if not badPath:
        if Noah and Samantha:
            # You three go around training and trying to get better and defeat the Sparks, the cannon pathway.
            raw_input(
                "The three of you clean up the mess caused by your encounter with the \033[0;33;0mSparks\033[0;0;0m, and vow to one day defeat them.")
            raw_input(
                "\033[0;31;0mNoah:\033[0;0;0m If were gonna defeat the sparks, were gonna need to get stronger. I say we head back to the Ent woods and level up a bit.")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m I actually have something a bit more sinister planned.")
            raw_input(
                "\033[0;33;0mSamantha:\033[0;0;0m The Elder Wizard is the most powerful Wizard alive. He is a master of all colored spells.")
            raw_input(
                "\033[0;33;0mSamantha:\033[0;0;0m The spells he has are crazy powerful, and I bet the books for them are still in his room!")
            raw_input("\033[0;31;0mNoah:\033[0;0;0m No way that sounds too dangerous.")
            while True:
                fate = raw_input("\033[0;31;0mNoah:\033[0;0;0m What do you say, " + name + "?\n1)Ent Forest  2)Elder Wizard")
                if fate == "1":
                    raw_input("\033[0;33;0mSamantha:\033[0;0;0m Aw, you guys are lame.")
                    # Train in the forest, encounter a king ent
                    forest()
                    break
                    # TODO: End here. Later, Try to fight the sparks.

                elif fate == "2":
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m Okay, if you say so " + scrambled_name + ".")
                    raw_input("The three of you go to the Elder Wizard's Lobby, Samantha guiding you.")
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m Woah, that's a huge door.")
                    raw_input("\033[0;33;0mSamantha:\033[0;0;0m And it's even bigger inside. Just look at all the books on the wall!")
                    raw_input("\033[0;33;0mSamantha:\033[0;0;0m We should split up, and look for a powerful spell.")
                    library()
                    raw_input("The three of you narrowly escape")
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m I can't believe we got out of there!")
                    raw_input("\033[0;33;0mSamantha:\033[0;0;0m Honestly neither can I. What did you say your idea was Noah?")
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m I forgot, but I'm panicking too much to want to do anything else than rest.")
                    raw_input("\033[0;33;0mSamantha:\033[0;0;0m But you did get some experience from trying out those spells!")
                    raw_input("Level up! Max Hp +1")
                    level += 1
                    maxHp += 1
                    break
                    # TODO: End here. Later, Try to Fight the Sparks
            crew = ["Noah", "Samantha"]
        elif Noah and not Samantha:
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m You are terrible people! I'm going back to \033[0;33;0mSparkHQ\033[0;0;0m, I will make them Hate you!")
            raw_input(
                "\033[0;31;0mNoah:\033[0;0;0m That cant be good. We should probably train so that were prepared if they attack us again.")
            raw_input("\033[0;31;0mNoah:\033[0;0;0m Lucky for us, we have a perfect training grounds in the form of the Ent Forest!")
            forest()
            # TODO: Ending here. Later, Try to fight the Sparks.
        elif Samantha and not Noah:
            raw_input(
                "You finish cleaning, and then head off in the direction \033[0;33;0mSamantha\033[0;0;0m went. It isn't long before you encounter a room with constant yellow flashing lights")
            raw_input(
                "Inside you find a large group of people dueling with lightning, in a rectangular arena with lightning rods on each corner.")
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Hey it's the twat from earlier. What are you doing here.")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m This twat right here just abandoned his friend to save a \033[0;33;0mSparks\033[0;0;0m.")
            crew = ["Samantha"]
            raw_input("\033[0;33;0mEthan:\033[0;0;0m Your not a \033[0;33;0mSparks\033[0;0;0m anymore \033[0;33;0mSamantha\033[0;0;0m.")
            raw_input("\033[0;33;0mSamantha:\033[0;0;0m I know, but I thought I'd appeal with " + name + " here.")
            raw_input(
                "\033[0;33;0mEthan:\033[0;0;0m Alright, " + name + ", lets see if your worthy. The first thing your gonna need to do is change your guild.")
            yorn = raw_input("You think you can do that? (Y)es or (N)o?")
            if yorn.lower() in ['y', 'yes', '1']:
                badPath = True
                spark_init()
                raw_input("\033[0;33;0mEthan:\033[0;0;0m \033[0;33;0mSamantha\033[0;0;0m, I should have never doubted you. You're back in.")
                # TODO: Ending here. Later, do stuff with sparks.
            elif yorn.lower() in ['n', 'no', '0', '2']:
                badPath = False
            if not badPath:
                raw_input(
                    "\033[0;33;0mEthan:\033[0;0;0m \033[0;33;0mSamantha\033[0;0;0m, you're supposed to bring someone who you think will join when you try to appeal. I just can't work with this. SPARKS! Get them outta here!")
                raw_input("\033[0;33;0mSamantha:\033[0;0;0m Well that didn't work, thanks a lot.")
                raw_input(
                    "\033[0;33;0mSamantha:\033[0;0;0m Ya know, I'm still in the mood to cause trouble. The Elder wizard has a whole library of spells. Ill bring you to it.")
                library()
                raw_input(
                    "\033[0;33;0mSamantha:\033[0;0;0m Ha! It worked! The elder wizard used to be a \033[0;33;0mSparks\033[0;0;0m, so he kinda has a soft spot for them. Thats why we get away with so much. It's a shame we got kicked out though...")
                raw_input(
                    "\033[0;33;0mSamantha:\033[0;0;0m Anyways, learning new spells is a good way to get experience. So you probably can level up!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                # TODO: Ending here. Later, just mess around doing gimicky stuff.
    if badPath:
        spark_init()
        if not badPath:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m \033[0;33;0mSPARKS\033[0;0;0m! Get them outta here!")
            raw_input("You got kicked out of the sparks, and now you have no friends.")
            crew = ["None"]
            while True:
                lonely = raw_input("What would you like to do?\n1)Check on noah  2)Train")
                if lonely == "1":
                    print "You decide to check up on Noah."
                    raw_input("There is another wizard standing over noah, healing him.")
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m Ugh.. What happened?")
                    raw_input("???: Someone defeated you in battle. I'm Thomson and Ill be your healer today.")
                    raw_input("Noah notices you.")
                    raw_input("\033[0;31;0mNoah:\033[0;0;0m Wait a minute, you did this to me " + name + "!")
                    raw_input("\033[0;32;0mThomson:\033[0;0;0m You stay lying down, I'll deal with him.")
                    Enemy("\033[0;32;0mThomson:\033[0;0;0m", 17, "None", "Green", ["Magic Beam", "Heal"])
                    raw_input("Thomson used Revive!")
                    raw_input("\033[0;32;0mThomson:\033[0;0;0m You shouldn't be attacking people you stupid \033[0;33;0mSpark\033[0;0;0m! Everyone is valid!")
                    print "\033[0;32;0mThomson:\033[0;0;0m Why would you do something like that? "
                    why = raw_input("1)I stood no chance against a spark, but I did against Noah. 2)I wanted to be a Spark. 3)He was dumb")
                    if why == "1":
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Oh baloney! I saw you had Lightning!")
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Get outta here kid!")
                    elif why == "2":
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m And how'd that work out for you? I saw that you didn't have the spell Sparks!")
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Get outta here kid!")
                    elif why == "3":
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Well it's not very smart for you to push away other people! Look at you! Now you don't have any friends!")
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Get outta here kid!")
                    else:
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Oh, your ashamed of it. As you should be.")
                        raw_input("\033[0;32;0mThomson:\033[0;0;0m Why don't you make it up to him?")
                        raw_input("You go over to Noah")
                        apology = raw_input("1)I'm sorry. 2)Nerd.")
                        if apology == "1":
                            raw_input("\033[0;31;0mNoah:\033[0;0;0m I know you are. It was a smart move to get on \033[0;33;0mThe Sparks\033[0;0;0m good side.")
                            raw_input("\033[0;31;0mNoah:\033[0;0;0m I think I've recovered now.")
                            raw_input("\033[0;32;0mThomson:\033[0;0;0m That's great! So you two made up?")
                            raw_input("\033[0;31;0mNoah:\033[0;0;0m Yeah.")
                            crew = ["Noah", "Thomson"]
                        elif apology == "2":
                            raw_input("\033[0;31;0mNoah:\033[0;0;0m You deserve this.")
                            raw_input("Noah blasted a fireball into your face! It wasn't very effective, but it still hurt.")
                            raw_input("\033[0;32;0mThomson:\033[0;0;0m Get outta here kid!")
                        else:
                            raw_input("\033[0;31;0mNoah:\033[0;0;0m You don't have anything to say?")
                            raw_input("\033[0;32;0mThomson:\033[0;0;0m Get outta here kid!")
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
    raw_input("\033[0;33;0mEthan:\033[0;0;0m Alright, we have a little Guild station over here. The book is right there, and you can just use the last chalk circle that got used.")
    step1 = raw_input("So, you've decided to become a member of \033[0;33;0mThe Sparks\033[0;0;0m. Well no \033[0;33;0mSpark\033[0;0;0m can exist without the Spell Sparks! Get used to hearing the word sparks, we use it for everything. To cast the spell, you must chant El Yelo Sparkosus. But before you do that, you must swear in to the Sparks. Say \"I solemnly swear to only respect other Sparks.\"\n")
    if step1.lower() not in ["i solemnly swear to only respect other sparks.", "i solemnly swear to only respect other sparks"]:
        raw_input("\033[0;33;0mEthan:\033[0;0;0m NOPE! He is not \033[0;33;0mSpark\033[0;0;0m material!")
        badPath = False
    else:
        step2 = raw_input("You place your " + object1 + " in the worn chalk circle. What must you chant?\n")
        if step2 not in ["El Yelo Sparkosus", "El Yelo Sparkosus!"]:
            raw_input("\033[0;33;0mEthan:\033[0;0;0m NOPE! He is not \033[0;33;0mSpark\033[0;0;0m material!")
            badPath = False
        else:
            step3 = raw_input("How do you call this spell?\n")
            if step3 not in ["Sparks", "Sparks!"]:
                raw_input("\033[0;33;0mEthan:\033[0;0;0m NOPE! He is not \033[0;33;0mSpark\033[0;0;0m material!")
                badPath = False
            else:
                spell_list.append("Sparks")
                print "Successful Enchant!"
                print object1, "has the spells:", spell_list
                if guild != "Yellow":
                    raw_input("\nYou changed to the \033[0;33;0mYellow Guild\033[0;0;0m!\n")
                    guild = "Yellow"
                raw_input("You joined \033[0;33;0mThe Sparks\033[0;0;0m!\n")
                raw_input("\033[0;33;0mEthan:\033[0;0;0m Well, I didn't think you could do it. Welcome to the sparks, in a world of awesome superiority!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                badPath = True
                crew = ["Sparks"]


def elder_wizard():
    Enemy("Elder Wizard", 1000000, "None", "Gold", ["Smite"])
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Ooohhhh...")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m You are very powerful.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Almost... too powerful.")
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Like a Hacker.")
    raw_input("Elder Wizard leveled up! HP +1!")
    raw_input("Elder Wizard regenerated to full health!")
    Enemy("Raged Elder Wizard", 1000001, "None", "Gold", ["Firewall", "Full Regenerate"])
    raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Ngh...")
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
    raw_input("\033[0;33;0mSamantha:\033[0;0;0m I think I hear someone coming!")
    spell_slot = raw_input("What spell slot will you use?\n" + str(spells_found))
    spell = spells_found[int(spell_slot)-1]
    if spell == "Le Grin Medihelios":
        spell_list.append("Heal")
        raw_input("Everyone around you got healed to full health!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Thanks, now we can last longer when the person coming down the hall kills us. Just, play along")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noise!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, you trouble making \033[0;33;0mSparks\033[0;0;0m. Samantha didn't I tell you? This Library is off limits!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Reedos Firon Bulos":
        spell_list.append("Fireball")
        raw_input("A fireball erupted in the middle of the room.")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Great! Now were gonna be in twice as much trouble for property damages!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noise!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Ahh! There's a fire! Water Geyser!")
        raw_input("The fire is put out and there is steam all around.")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Quickly, lets get out of here!")
    elif spell == "Al Bleo Freson":
        spell_list.append("Freeze")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noi-")
        raw_input("You Froze the Elder Wizard!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m That was bold Freezing the Elder Wizard, now lets get out of here before he thaws!")
    elif spell == "El Yelo Lumining":
        spell_list.append("Lightning")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m What the heck did you just do?!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "La Grezz Insivion":
        spell_list.append("Invisibility")
        raw_input("Everyone Around you turned invisible!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Good thinking! now lets get out of here before this spell wears off!")
    elif spell == "El Yelo Sparkosus":
        spell_list.append("Sparks")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Sparks? Do you seriously want to be a \033[0;33;0mSpark\033[0;0;0m in a time like this? But that gives me an idea, just play along")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noise!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, you trouble making \033[0;33;0mSparks\033[0;0;0m. Samantha didn't I tell you? This Library is off limits!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Grezz Maginka Beamos":
        spell_list.append("Magic Beam")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Magic Beam!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m What the heck did you just do?!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Le Grin Raginos Claus":
        spell_list.append("Raged Claws")
        raw_input("You attack Samantha with Raged Claws!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Agh! Why did you do that?!?!?")
        raw_input("The spell made you attack again!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Auughh!")
        raw_input("\033[0;33;0mSamantha\033[0;0;0m was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m My word! What happened here! Broken into the spell room and a defeated body? Both those are off limits!")
        elder_wizard()
    elif spell == "La Grezz Maginka Lessar":
        spell_list.append("Magic Laser")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m What the heck did you just do?!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Aleos Maximon Goludos Smitomiras Infiniron":
        spell_list.append("Smite")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noi- ")
        raw_input("The entire room is obliterated with a Smite from the skies!!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Ngh... Those poor fools. They didn't know what they were messing with.")
        raw_input("Game Over")
        print "You were defeated at level " + str(level) + " with the spells: "
        print spell_list
        quit()
    else:
        raw_input("In your panic, you froze in place, but not like the spell Freeze.")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m what are you doing? Just- just follow my lead.")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Who's in here? I heard noise!")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Oh, just you trouble making \033[0;33;0mSparks\033[0;0;0m. Samantha didn't I tell you? This Library is off limits!")
        raw_input("\033[0;33;0mSamantha:\033[0;0;0m Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("\033[0;35;0mElder Wizard:\033[0;0;0m Just don't get any ideas! Go ahead and get out of here you rascals.")


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
        Enemy("\033[0;34;0mThe Snow Golem\033[0;0;0m", randint(7, 12), "None", "Blue", ["Snowball"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input("You managed to defeat the Snow Golem, but now you're lost.")
    elif path == "3":
        yorn = raw_input("You found a cave! Would you like to enter it?\n(Y)es or (N)o?")
        if yorn.lower() in ["y", "yes"]:
            raw_input("You crawled into the cave.")
            raw_input("Something with red eyes brushed by your legs!")
            Enemy("\033[0;37;0m???\033[0;0;0m", 17, "Invisibile", "Gray", ["Bite", "Raged Claws"])
            raw_input("Level up! Max Hp +1")
            level += 1
            maxHp += 1
            raw_input("But the creature got up and scurried away!")
            leave = raw_input("Leave the cave?\n(Y)es of (N)o?")
            if leave.lower() in ["n", "no"]:
                raw_input("You decide not to leave the cave. That creature doesn't scare you!")
                raw_input("\033[0;37;0m???:\033[0;0;0m oh but we should")
                raw_input("Who said that? How can you read my mind? ...we?")
                raw_input("\033[0;41;0m???:\033[0;0;0m KYYYYYSSSSHHHHAAAAAAAA!!!")
                raw_input("Tha walls around you start to move, the cave closes in, the only light is coming from those red eyes everywhere.")
                while True:
                    Enemy("\033[0;41;0mShadow Swarm\033[0;0;0m", 36, "None", "Gray", ["Bite", "Raged Claws"])
                    raw_input("\033[0;37;0m???:\033[0;0;0m but we get up again.")
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
    raw_input("\033[0;34;0m?\033[0;35;0m??\033[0;0;0m: COOOOORRRAAAAAAAAAHHHHHHHH!")
    raw_input("What was that?")
    raw_input("A Snow Golem with a crown on it's head emerged from the snow! It's the Snow King!")
    raw_input("\033[0;34;0mSnow \033[0;35;0mKing:\033[0;0;0m Your color is Artificial! It must be eliminated!")
    Enemy("\033[0;34;0mSnow \033[0;35;0mKing\033[0;0;0m", 24, "None", "Gold", ["Frost Bite"])
    raw_input("\033[0;34;0mSnow \033[0;35;0mKing:\033[0;0;0m Artificial.. Yet good...")
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1


def forest():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    raw_input("You head out to the Ent Forest")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Alright, there are a few Ents on the border, but that wont get us much experience.")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m I say we sneak through and get to the center to get the stronger enemies")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m There are many paths through the forest, we should choose wisely.")
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
        Enemy("\033[0;32;0mThe Ent\033[0;0;0m", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 4:
        if randint(1, 3) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy("\033[0;32;0mThe Ent\033[0;0;0m", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 5:
        if randint(1, 2) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy("\033[0;32;0mThe Ent\033[0;0;0m", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 6:
        if randint(1, 3) == 1:
            raw_input("Yep, It was an Ent!")
            Enemy("\033[0;32;0mThe Ent\033[0;0;0m", randint(12, 17), "None", "Green", ["Raged Claws"])
        else:
            raw_input("Nope, not an Ent.")
    elif goal == 7:
        raw_input("Nope, not an Ent.")
    raw_input("Other Ents noticed you, and attacked!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Ahh! Theres too many! Try to fend off your side!")
    Enemy("\033[0;32;0mThe Ent\033[0;0;0m", randint(12, 17), "None", "Green", ["Raged Claws"])
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1
    raw_input("\033[0;31;0mNoah:\033[0;0;0m YEAH! I think we're geting them!")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Oh- Oh no.")
    raw_input("\033[0;32;0m?\033[0;35;0m??\033[0;0;0m: ROOOOOAAAAAAHHHH!")
    if guild != "Green":
        Enemy("\033[0;32;0mEnt \033[0;35;0mKing\033[0;0;0m", 25, "None", "Gold", ["Raged Claws"])
        raw_input(
            "Having defeated the Ent King, The other Ents ran off, but they left behind a Spell Book for Raged Claws")
    else:
        raw_input("A giant Ent with a Golden Crown comes out from the trees, and points to you.")
        raw_input("The other Ents grab you, and start dragging you away from your group.")
        raw_input("\033[0;31;0mNoah:\033[0;0;0m Ahhh! The Ent King took " + name + "!")
        raw_input("The Ents made a circle around your group, blocking them off as they took you to the Ent King.")
        raw_input(
            "Ent King: Why have you done this? Are you not a \033[0;32;0mGreen\033[0;0;0m? Why must you attack us with a malicious \033[0;31;0mRed\033[0;0;0m by your side?")
        raw_input("Ent King: Training? For what? To fight the \033[0;33;0mYellow Sparks\033[0;0;0m? My my. That's a new Guild.")
        raw_input("Ent King: 1000 years ago when I was younger, there were only 3 Guilds. \033[0;31;0mRed\033[0;0;0m, \033[0;34;0mBlue\033[0;0;0m, and \033[0;32;0mGreen\033[0;0;0m.")
        raw_input("Ent King: This new Guild must be artificial and unnatural, you said they were like a stronger red?")
        raw_input(
            "Ent King: Hmm. This is concerning. While I musn't leave the forest, I will grant you the spell of out people.")
        raw_input("Ent King: The Spell Book for Raged Claws.")
        raw_input("Ent King: Now go, and stop the evil that is the sparks.")
        raw_input("The Ents dispersed, allowing you and your group to escape.")
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Wow, this forest looks super empty now. Didn't realize quite how many Ents there were")
    raw_input("\033[0;31;0mNoah:\033[0;0;0mBut we gotta learn that new Spell! I imagine it'll be useful when fighting the sparks!")
    raw_input("You cray a circle in the dirt with a stick around your " + object1)
    raw_input("\033[0;31;0mNoah:\033[0;0;0m Alright, to cast Raged Claws you must chant Le Grin Raginos Claus")
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
print "Guild:", guild, "Level:", level, "HP:", maxHp
