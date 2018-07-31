from random import randint
# TODO make a main, and break it apart
maxHp = 10
level = 1
name = ""
scrambledName = ""
guild = "Gray"

# TODO: mabye you should have a second class for yourself, and have the two classes communicate.
class enemy(object):
    def __init__(self, name, health, status, color, arsenal):
        self.playerHealth = maxHp  # yours
        self.wait = 0  # enemy's
        self.name = name  # enemy's
        self.health = health  # enemy's
        self.status = status  # enemy's
        self.color = color  # enemy's
        self.arsenal = arsenal  # enemy's
        self.defeated = True  # enemy's
        self.oneGameFreeze = False
        self.fireyRevive = False
        raw_input("\n\tENCOUNTER: " + self.name + "\n")
        enemy.yourTurn(self)

    def attacked(self, damage, attColor, status):
        if damage != 0:
            if self.color == "Blue" and attColor == "Green" or self.color == "Green" and attColor == "Red" or self.color == "Red" and attColor == "Yellow" or self.color == "Yellow" and attColor == "Blue":
                damage = damage*2
                print "Effective, increased Damage!"
            if attColor == "Blue" and self.color == "Green" or attColor == "Green" and self.color == "Red" or attColor == "Red" and self.color == "Yellow" or attColor == "Yellow" and self.color == "Blue":
                damage = damage/2
                damage = round(damage, 0)
                print "Ineffective, decreased damage!"
            self.health -= damage
            raw_input("Dealt " + str(damage) + " damage!")
        enemy.status(self, status)
        if self.health <= 0:
            if self.defeated:
                self.defeated = False
                raw_input(self.name + "'s HP was brought to zero!")
                raw_input(self.name + " was defeated!")
            return
        if self.wait == 0:
            enemy.enemyTurn(self)

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
                enemy.yourTurn(self)
        if self.status == "Frozen":
            if self.health <= 0:
                return
            if self.wait > 0:
                self.wait -= 1
                print self.name + " is frozen for " + str(self.wait) + " more turns!\n"
                enemy.yourTurn(self)
            self.status = "None"

        if status == "Heal":
            originHP = self.playerHealth
            self.playerHealth += 9
            self.status = "None"
            if self.playerHealth >= maxHp:
                self.playerHealth = maxHp
            print "Healed " + str(self.playerHealth - originHP) + " HP!"

    def yourTurn(self):
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        print "Enemy Health: " + str(self.health) + "  Your Health: " + str(self.playerHealth)
        print spell_list
        try:
            spellUse = spell_list[input("Slot Number: ")-1]
            raw_input("You used " + spellUse + " ...")
            damage, status, color = spell(spellUse)
        except Exception:
            raw_input("You don't have a spell in that spell slot!\n")
            enemy.yourTurn(self)
        try:
            enemy.attacked(self, damage, color, status)
        except Exception:
            return

    def enemyTurn(self):
        length = len(self.arsenal) - 1
        attack = self.arsenal[randint(0, length)]
        print self.name + " used " + attack + "!"
        [damage, status, color] = spell(attack)
        if status == "Full Heal" and self.color == "Gold":
            self.health = 1000000
            print "Healed to full health!\n"
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
                    self.playerHealth = 15
                    self.fireyRevive = True
                else:
                    raw_input("Game Over")
                    print "You were defeated at level " + str(level) + " with the spells: "
                    print spell_list
                    quit()
        enemy.yourTurn(self)



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
        return 0, "Stealth", "Gray"
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


def main():
    global object1, spell_list, level, maxHp
    raw_input("Elder Wizard: Welcome new Wizard, to the Guild of Wizards! (Press enter to continue)")
    raw_input("Elder Wizard: Since it is your first time here, grab an Object and I'll Enchant it for you!")
    object1 = raw_input("Elder Wizard: What will your first object be?\n")
    print "Elder Wizard: So you want a " + object1 + " to be Enchanted?"
    yorn = raw_input("(Y)es or (N)o")
    while yorn.lower() not in ["yes", "y"]:
        object1 = raw_input("What will your first object be?\n")
        print "Elder Wizard: So you want a " + object1 + " to be Enchanted?"
        yorn = raw_input("Yes(Y) or No(N)")
    raw_input("Elder Wizard: Then let it be done! Watch closely now.")
    raw_input("Elder Wizard: First, draw a chalk circle around the Object you want to Enchant. It does not need to be perfect.")
    raw_input("Elder Wizard: Then we will find the Book for a Spell you want to Enchant the Object with.")
    raw_input("Elder Wizard: For now we will give you a basic one, Magic Beam.")
    raw_input("Elder Wizard: From the book, we cast this Spell at the circle. The chalk will then absorb the spell and enchant the Object.")
    raw_input("Elder Wizard:    La Grezz Maginka Beamos!")
    spell_list = ["Magic Beam"]
    raw_input("Elder Wizard: During the time the circle is absorbing the spell, shout what you want to say to cast the spell.")
    raw_input("Elder Wizard:    Magic Beam!")
    raw_input("Elder Wizard: The reason we do this whole process is because some spells take time, and are complex to preform.")
    raw_input("Elder Wizard: It's much easier to just say 'Magic Beam' and point than do specific motions chanting strange words.")
    raw_input("Elder Wizard: Now your " + object1 + " is Enchanted with Magic Beam. Good luck on your Wizard Way!")
    firstEncounter()

def firstEncounter():
    global object1, spell_list, level, maxHp
    print "\n", object1, "has the spells:", spell_list
    raw_input("You decide to try out your new spell in the forest")

    enemy("The Tree", 5, "None", "Green", ["Nothing"])
    raw_input("But what's this?")
    raw_input("That was no tree! It was an Ent! And it's angry!")

    # V This code makes the battle go unscripted, and you will lose. The other code is made so that you get saved.
    # ent = enemy("The Raged Ent", 25, "None", "Green", ["Raged Claws"])

    raw_input("\n\tENCOUNTER: Raged Ent\n")
    ent = 25

    while True:
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        print "Enemy Health: " + str(ent) + "  Your Health: 10"
        print spell_list
        try:
            spellUse = spell_list[input("Slot Number: ") - 1]
            damage, status, color = spell(spellUse)
            raw_input("You used " + spellUse + " ...")
            raw_input("The Raged Ent lost " + str(damage) + " HP!")
            ent -= damage
            if ent <= 0:
                break
        except Exception:
            raw_input("You don't have a spell in that spell slot!")
        break

    raw_input("The Raged Ent is attacking!")
    raw_input("   'Raged Claws'")
    raw_input("             ???: Fireball! FireBall!")
    raw_input("             Effective, Double Damage, -10 HP!  Burned! -1 HP!  Effective, Double Damage, -10 HP!")
    ent -= 21
    if ent > 0:
        raw_input("The Raged Ent recoiled at the attack!\n")
        while True:
            print "What spell slot will you use? Equipped Objects: " + object1 + "."
            print "Enemy Health: " + str(ent) + "  Your Health: 10"
            print spell_list
            try:
                spellUse = spell_list[input("Slot Number: ") - 1]
                damage, status, color = spell(spellUse)
                raw_input("You used " + spellUse + " ...")
                raw_input("The Raged Ent lost " + str(damage) + " HP!\n")
                ent -= damage
                if ent <= 0:
                    break
            except Exception:
                raw_input("You don't have a spell in that spell slot!")
                try:
                    spellUse = spell_list[input("Slot Number: ") - 1]
                    damage, status, color = spell(spellUse)
                    raw_input("You used " + spellUse + " ...")
                    raw_input("The Raged Ent lost " + str(damage) + " HP!\n")
                    ent -= damage
                    if ent <= 0:
                        break
                except Exception:
                    raw_input("You don't have a spell in that spell slot!")
                    raw_input("The Raged Ent is attacking!")
                    raw_input("   'Raged Claws'")
                    raw_input("   Off guard, Increased Damage, -10 HP!")
                    raw_input("Your HP was brought to zero!")
                    raw_input("You have been defeated!")
                    raw_input("Game Over")
                    print "You were defeated at level 1 with the spells: "
                    print spell_list
                    quit()

    raw_input("The Raged Ent's HP was brought to zero!")
    raw_input("The Raged Ent was defeated!")
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1

    raw_input("             ???: Woah! That was a close call!")
    raw_input("Noah: Hey there, I'm Noah, member from the Red Guild!")
    raw_input("Noah: Good thing Red magic is strong against Green creatures, else you would've been toast!")
    while True:
        name = raw_input("Noah: So, what's your name?\n")
        name = name.lower().capitalize()
        yorn = raw_input("Noah: So your name is '" + name + "' huh? (Y)es or (No)")
        if yorn.lower() in ['y', 'yes']:
            break
    raw_input("Noah: That's an interesting name, I'll be sure to remember that!")
    scrambledName = name.lower().replace('a', '*').replace('e', '#').replace('i', '$').replace('o', ')').replace('u', '(').replace('*', 'i').replace('#', 'a').replace('$', 'e').replace(')', 'u').replace('(', 'o').capitalize()
    raw_input("Noah: So what were you doing in the Ent Woods, " + scrambledName + "?")
    raw_input("Noah: Just testing out your first spell? Cool!")
    raw_input("Noah: OH! I got your name wrong didn't I? Yeah I don't have the best memory, but I make up for it in strength!")
    raw_input("Noah: Huh, you don't have a Guild yet. Follow me! i'll show you how to select one!")
    getGuild()

def getGuild():
    global object1, spell_list, level, maxHp, guild, guildSpell
    raw_input("Noah: Here at the Guild of Wizards, we have 4 main guilds.\n")

    raw_input("Noah: Red Guild, the one I'm in, is for people with energy, and Burning passions.")
    raw_input("Noah: In battle, we're just gonna come at you with attacks and never let up.")
    raw_input("\nRed Guild, proficient in Red Magic. Unlocks the spell Fireball.\n")

    raw_input("Noah: Then comes the Blue Guild. It's full of people who are Cool, calm, and collected.")
    raw_input("Noah: In battle, they're always strategizing and planning ahead.")
    raw_input("\nBlue Guild, proficient in Blue Magic. Unlocks the spell Freeze.\n")

    raw_input("Noah: Then there's the Green Guild. They're very positive and always Helping people")
    raw_input("Noah: In battle, they rely on boosting their own and other's abilities with spells.")
    raw_input("\nGreen Guild, proficient in Green Spells. Unlocks the spell Heal.\n")

    raw_input("Noah: Last there's the Yellow Guild. They're quite Shocking in their actions, and not the nicest people.")
    raw_input("Noah: In battle, they have insanely powerful spells, and they pump them out fast!")
    raw_input("\nYellow Guild, proficient in Yellow Spells. Unlocks the spell Lightning.\n")

    raw_input("Noah: Now before you choose a guild, you should know what color spells are stronger against what. Here's a chart:")
    print "\n     Green "
    print "    v      ^ "
    print " Blue      Red "
    print "    v      ^ "
    print "     Yellow \n"
    raw_input("Noah: The arrow points to the side that will be taking twice the damage from the opposing color.")
    while True:
        print "Noah: So, what guild will you choose?"
        guild = raw_input("Red, Blue, Green, or Yellow ")
        guild = guild.lower().capitalize()
        if guild == "Red":
            yorn = raw_input("Noah: You want to join the Red Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes']:
                raw_input("Noah: Yay! Now we're in the same guild!!")
                raw_input("\nYou chose the Red Guild!\n")
                guildSpell = ["Fireball", "La Reedos Firon Bulos"]
                break
        elif guild == "Blue":
            yorn = raw_input("Noah: So you want to join the Blue Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes']:
                raw_input("Noah: Yes, good choice!")
                raw_input("\nYou chose the Blue Guild!\n")
                guildSpell = ["Freeze", "Al Bleo Freson"]
                break
        elif guild == "Green":
            yorn = raw_input("Noah: So you want to join the Green Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes']:
                raw_input("Noah: Yes, good choice!")
                raw_input("\nYou chose the Green Guild!\n")
                guildSpell = ["Heal", "Le Grin Medihelos"]
                break
        elif guild == "Yellow":
            yorn = raw_input("Noah: You want to join the Yellow Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes']:
                raw_input("Noah: Oh, didn't realize you would be a Yellow.")
                raw_input("\nYou chose the Yellow Guild!\n")
                guildSpell = ["Lightning", "El Yelo Lumining"]
                break
        else:
            raw_input("Noah: I'm not sure " + guild + " is a Guild.")
            yorn = raw_input("Noah: Do you still want to join a Guild? (Y)es or (N)o.")
            if yorn.lower() in ['n', 'no']:
                raw_input("Noah: Oh- okay.")
                raw_input("\nYou didn't choose a guild...\n")
                guild = "Gray"
                guildSpell = ["Magic Laser", "La Grezz Maginka Lessar"]
                break
    secondSpell(guildSpell)

def secondSpell(guildSpell):
    global badPath, guild
    enemy.setGuild = guild
    raw_input("Noah: Alright, lets teach you your new spell. The chalk and books are right here, we just have to set it up.")
    while True:
        step1 = raw_input("What do you do with the chalk?\n 1)Draw a circle and point your Object. 2)Draw a circle around your Object. 3)Point the chalk at the Object.")
        if step1 == "2":
            raw_input("Noah: The book says to cast " + guildSpell[0] + " you must chant '" + guildSpell[1] + "!'")
            step2 = raw_input("What must you chant?\n")
            if step2 == guildSpell[1] or step2 == guildSpell[1] + "!":
                step3 = raw_input("How do you call this spell?\n")
                if step3 == guildSpell[0] or step3 == guildSpell[0] + "!":
                    spell_list.append(guildSpell[0])
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
    raw_input("\nNoah: Great! You got your second spell!")
    raw_input("Noah: And just in time, here come the local bullies, The Sparks.")
    theSparks()

def theSparks():
    global badPath, object1, spell_list, level, maxHp, Noah, Samantha
    raw_input("\n???: Hey look, No-brains is trying to help the newbie with its guild!")
    raw_input("Noah: Buzz off Eric.")
    raw_input("Eric: Be quiet loser. What Guild did ya choose newbie?")
    if guild.lower() == "red":
        raw_input("Eric: You joined the Red Guild? HA! What a loser! You know they're just a weaker version of the Yellow Guild right?")
    elif guild.lower() == "blue":
        raw_input("Eric: You joined the Blue Guild? Ha! They have the lamest battling style! They make battles drag on and it just gets so boring!")
    elif guild.lower() == "green":
        raw_input("Eric: The Green Guild? Only wimps join the Green Guild! They're just so fragile!")
    elif guild.lower() == "yellow":
        raw_input("Eric: Yellow Guild? Nice. Your cool with us. But I wouldn't hang around that Noah kid.")
        raw_input("Eric: He cant remember a thing you tell him. That's what makes him so great to mess with, you can re-use insults!")
        badPath = True
    else:
        raw_input("Eric: You didn't choose a Guild? How lame! You're not gonna make any friends like that.")

    if badPath:
        raw_input("Eric: So wadda ya say, wanna join The Sparks, and actually be part of something important in this world?")
        raw_input("Noah: Don't do it " + scrambledName + ", you'll regret it.")
        yorn = raw_input("Eric: Shut it walnut. So? (Y)es or (N)o?")
        if yorn.lower() in ['y', 'yes']:
            raw_input("Eric: Good good, now take down this bolts-for-brains for me, would ya?")
            enemy("Noah", 12, "None", "Red", ["Magic Beam", "Fireball"])
        elif yorn.lower() in ['n', 'no']:
            raw_input("Eric: Oh, how disappointing.")
            badPath = False
        else:
            raw_input("Eric: Huh? Never mind. Your not getting in.")
            badPath = False
    if not badPath:
        raw_input("Eric: Hey Samantha, help me deal with these twats. I'll take No-brains, you take the Newbie.")
        raw_input("Samantha: Right away boss.")
        enemy("Samantha", 13, "None", "Yellow", ["Magic Beam", "Sparks"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input("Samantha: Ahh! I couldn't defeat you.")
        raw_input("Eric: Get up Samantha! I will not wave a weakling in my gang!")
        raw_input("Samantha: I- I can't...")
        raw_input("Eric: Pathetic! My Goons do not get defeated! I hereby revoke your title as a Spark. To the rest of you Sparks, lets go.")
        raw_input("Noah: Ngh... He got me good. I didn't stand a chance.")
        raw_input("Noah: There's a healing potion behind you on that shelf, Heal us!")

        print "Who would you like to heal?"
        choice = raw_input("1)Noah 2)Samantha 3)Self")
        if choice == "1":
            raw_input("Noah: Thanks for that. I have an extra potion, now help Her!")
            Noah = True
            print "Who would you like to heal?"
            choice = raw_input("1)Self 2)Samantha")
            if choice == "2":
                raw_input("Samantha: Wow, even after I attacked you, you saved me? Huh.")
                Samantha = True
            else:
                raw_input("Samantha: You monster.")
                raw_input("Samantha was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
                Samantha = False
        elif choice == "2":
            raw_input("Noah: You monster.")
            raw_input("Noah was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            Samantha = True
        else:
            raw_input("Noah and Samantha: You monster.")
            raw_input("Noah was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
            Noah = False
            raw_input("Samantha was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
            Samantha = False

        if Noah and Samantha:
            raw_input("Noah: Thanks for that. Look on the bright side! We just held off The Sparks!")
            raw_input("Samantha: Speaking of which, I don't think I'm gonna try to join them again. You guys seem pretty strong though. Could I hang with you?")
            raw_input("Noah: Sure! I don't see why not!")
            raw_input("Elder Wizard: My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
        elif Noah:
            raw_input("Noah: Thanks for that, but, why didn't you heal Samantha?")
            raw_input("Elder Wizard: My word! What happened here! Someone was defeated? Duels are only permitted in the arena! Both of you EXPELLED!")
            raw_input("The Elder Wizard took both of your Magic Objects. While leaving, you encountered an Ent in the Ent Forest.")
            try:
                object1 = "None"
                spell_list = ["Nothing"]
                enemy("The Ent", 25, "None", "Green", ["Raged Claws"])
            except Exception:
                raw_input("It didn't end well.")
        elif Samantha:
            raw_input("Samantha: Wow. Helping me more than a friend. I like the way you roll. Don't worry, your friend can be revived, it just takes a lot of magic.")
            raw_input("Samantha: But for now, Invisibility! That should hide him.")
            raw_input("Elder Wizard: My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
            raw_input("Samantha: Alright, you have fun with that, er, what was your name?")
            raw_input("Samantha: " + name + ", got it. You have fun doing that " + name + ". I'll put in a good word for you with The Sparks. Speaking of which, I gotta see if they'll let me back in.")
            badPath = True
        else:
            raw_input("Elder Wizard: My word! What happened here! Two people defeated? And your the only person around here. Duels are only permitted in the arena!")
            enemy("Elder Wizard", 1000000, "None", "Gold", ["Smite"])
            raw_input("Elder Wizard: Ooohhhh...")
            raw_input("Elder Wizard: You are very powerful.")
            raw_input("Elder Wizard: Almost... too powerful.")
            raw_input("Elder Wizard: Like a Hacker.")
            raw_input("Elder Wizard leveled up! HP +1!")
            raw_input("Elder Wizard regenerated to full health!")
            enemy("Raged Elder Wizard", 1000001, "None", "Gold", ["Firewall", "Full Regenerate"])
            raw_input("Elder Wizard: Ngh...")
            raw_input("lder Wizard: you've...")
            raw_input("der Wizard: defeated me.")
            raw_input("er Wizard: Well then, I have no choice")
            raw_input("r Wizard: I hereby grant you...")
            raw_input(" Wizard: The title of Elder Wizard.")
            raw_input("The Wizard faded to dust, leaving no trace. You have gained the title of Elder Wizard!")
    else:
        raw_input("Noah: Ngh... got me good. I didn't stand a chance.")
        raw_input("Noah: There's a healing potion behind you on that shelf, Heal me " + name + "!")
        raw_input("Eric: Don't you dare.")
        Choice = raw_input("1)Heal 2)Don't Heal")
        if Choice == "1":
            raw_input("Eric: Y'know, I had hopes for ya, you looked strong. But you disappoint me. I'll take that.")
            raw_input("Eric took the Healing Potion and smashed it on the ground")
            badPath = False
        else:
            raw_input("Eric: Ha! I knew you had it in ya.")
            badPath = True
        raw_input("Noah: You monster.")
        raw_input("Noah was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
        Noah = False
        if badPath:
            raw_input("Eric: Come on, some other wizards will probably find him and waste their own magic reviving him.")
            raw_input("Eric: For now, lets get you initiated as an official spark.")
        else:
            raw_input("Eric: Pathetic! Let's go Sparks.")
            raw_input("Elder Wizard: My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess, I'll work on reviving your opponent.")
    print "To be continued..."
    print "Are you on the bad path?", badPath
    print "is Noah defeated?", not Noah
    print "Is Samantha defeated?", not Samantha

if __name__ == '__main__':
    main()
    # firstEncounter()  # Needs object1 and spell_list
    # getGuild() # Needs spell_list and object1.
    # secondSpell(guildSpell) # Needs guild, spell_list, and object1.
    # theSparks() # Needs guild, badPath, object1, spell_list.
