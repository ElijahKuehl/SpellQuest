from random import randint
maxHp = 10
level = 1
name = ""
scrambled_name = ""
guild = "Gray"


# TODO: maybe you should have a second class for yourself, and have the two classes communicate.
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
            return
        if self.wait == 0:
            Enemy.enemy_turn(self)

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

    def your_turn(self):
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
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


def chapter_one():
    global object1, spell_list, level, maxHp
    start = raw_input("Elder Wizard: Welcome new Wizard, to the Guild of Wizards! (Press enter to continue, or type 'C' to go to a certian point.)")
    if start.lower() == "c":
        return checkpoint()
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
    first_encounter()


def first_encounter():
    global object1, spell_list, level, maxHp
    print "\n", object1, "has the spells:", spell_list
    raw_input("You decide to try out your new spell in the forest")

    Enemy("The Tree", 5, "None", "Green", ["Nothing"])
    raw_input("But what's this?")
    raw_input("That was no tree! It was an Ent! And it's angry!")

    # V This code makes the battle go unscripted, and you will lose. The other code is made so that you get saved.
    # ent = enemy("The Raged Ent", 25, "None", "Green", ["Raged Claws"])

    raw_input("\n\tENCOUNTER: Raged Ent\n")
    ent = 15

    while True:
        print "What spell slot will you use? Equipped Objects: " + object1 + "."
        print "Enemy Health: " + str(ent) + "  Your Health: 10"
        print spell_list
        try:
            spell_use = spell_list[input("Slot Number: ") - 1]
            damage, status, color = spell(spell_use)
            raw_input("You used " + spell_use + " ...")
            raw_input("The Raged Ent lost " + str(damage) + " HP!")
            ent -= damage
            if ent <= 0:
                break
        except Exception:
            raw_input("You don't have a spell in that spell slot!")
        break

    raw_input("The Raged Ent is attacking!")
    raw_input("   'Raged Claws'")
    raw_input("             ???: Fireball!")
    raw_input("             Effective, Double Damage, -10 HP!  Burned! -1 HP!")
    ent -= 11
    if ent > 0:
        raw_input("The Raged Ent recoiled at the attack!\n")
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
        if yorn.lower() in ['y', 'yes', '1']:
            break
    raw_input("Noah: That's an interesting name, I'll be sure to remember that!")
    scrambled_name = name.lower().replace('a', '*').replace('e', '#').replace('i', '$').replace('o', ')').replace('u', '(').replace('*', 'i').replace('#', 'a').replace('$', 'e').replace(')', 'u').replace('(', 'o').capitalize()
    raw_input("Noah: So what were you doing in the Ent Woods, " + scrambled_name + "?")
    raw_input("Noah: Just testing out your first spell? Cool!")
    raw_input("Noah: OH! I got your name wrong didn't I? Yeah I don't have the best memory, but I make up for it in strength!")
    raw_input("Noah: Huh, you don't have a Guild yet. Follow me! I'll show you how to select one!")
    get_guild()


def get_guild():
    global object1, spell_list, level, maxHp, guild, guild_spell
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
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("Noah: Yay! Now we're in the same guild!!")
                raw_input("\nYou chose the Red Guild!\n")
                guild_spell = ["Fireball", "La Reedos Firon Bulos"]
                break
        elif guild == "Blue":
            yorn = raw_input("Noah: So you want to join the Blue Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("Noah: Yes, good choice!")
                raw_input("\nYou chose the Blue Guild!\n")
                guild_spell = ["Freeze", "Al Bleo Freson"]
                break
        elif guild == "Green":
            yorn = raw_input("Noah: So you want to join the Green Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("Noah: Yes, good choice!")
                raw_input("\nYou chose the Green Guild!\n")
                guild_spell = ["Heal", "Le Grin Medihelos"]
                break
        elif guild == "Yellow":
            yorn = raw_input("Noah: You want to join the Yellow Guild? (Y)es or (N)o.")
            if yorn.lower() in ['y', 'yes', '1']:
                raw_input("Noah: Oh, didn't realize you would be a Yellow.")
                raw_input("\nYou chose the Yellow Guild!\n")
                guild_spell = ["Lightning", "El Yelo Lumining"]
                break
        else:
            raw_input("Noah: I'm not sure " + guild + " is a Guild.")
            yorn = raw_input("Noah: Do you still want to join a Guild? (Y)es or (N)o.")
            if yorn.lower() in ['n', 'no', '0', '2']:
                raw_input("Noah: Oh- okay.")
                raw_input("\nYou didn't choose a guild...\n")
                guild = "Gray"
                guild_spell = ["Magic Laser", "La Grezz Maginka Lessar"]
                break
    second_spell()


def second_spell():
    global badPath, guild, guild_spell
    Enemy.setGuild = guild
    raw_input("Noah: Alright, lets teach you your new spell. The chalk and books are right here, we just have to set it up.")
    while True:
        step1 = raw_input("What do you do with the chalk?\n 1)Draw a circle and point your Object. 2)Draw a circle around your Object. 3)Point the chalk at the Object.")
        if step1 == "2":
            raw_input("Noah: The book says to cast " + guild_spell[0] + " you must chant '" + guild_spell[1] + "!'")
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
    raw_input("\nNoah: Great! You got your second spell!")
    raw_input("Noah: And just in time, here come the local bullies, The Sparks.")
    the_sparks()


def the_sparks():
    global badPath, object1, spell_list, level, maxHp, Noah, Samantha
    raw_input("\n???: Hey look, No-brains is trying to help the newbie with its guild!")
    raw_input("Noah: Buzz off Ethan.")
    raw_input("Ethan: Be quiet loser. What Guild did ya choose newbie?")
    if guild.lower() == "red":
        raw_input("Ethan: You joined the Red Guild? HA! What a loser! You know they're just a weaker version of the Yellow Guild right?")
    elif guild.lower() == "blue":
        raw_input("Ethan: You joined the Blue Guild? Ha! They have the lamest battling style! They make battles drag on and it just gets so boring!")
    elif guild.lower() == "green":
        raw_input("Ethan: The Green Guild? Only wimps join the Green Guild! They're just so fragile!")
    elif guild.lower() == "yellow":
        raw_input("Ethan: Yellow Guild? Nice. Your cool with us. But I wouldn't hang around that Noah kid.")
        raw_input("Ethan: He cant remember a thing you tell him. That's what makes him so great to mess with, you can re-use insults!")
        badPath = True
    else:
        raw_input("Ethan: You didn't choose a Guild? How lame! You're not gonna make any friends like that.")

    if badPath:
        raw_input("Ethan: So wadda ya say, wanna join The Sparks, and actually be part of something important in this world?")
        raw_input("Noah: Don't do it " + scrambled_name + ", you'll regret it.")
        yorn = raw_input("Ethan: Shut it walnut. So? (Y)es or (N)o?")
        if yorn.lower() in ['y', 'yes', '1']:
            raw_input("Ethan: Good good, now take down this bolts-for-brains for me, would ya?")
            Enemy("Noah", 12, "None", "Red", ["Magic Beam", "Fireball"])
        elif yorn.lower() in ['n', 'no', '0', '2']:
            raw_input("Ethan: Oh, how disappointing.")
            badPath = False
        else:
            raw_input("Ethan: Huh? Never mind. Your not getting in.")
            badPath = False
    if not badPath:
        raw_input("Ethan: Hey Samantha, help me deal with these twats. I'll take No-brains, you take the Newbie.")
        raw_input("Samantha: Right away boss.")
        Enemy("Samantha", 13, "None", "Yellow", ["Magic Beam", "Sparks"])
        raw_input("Level up! Max Hp +1")
        level += 1
        maxHp += 1
        raw_input("Samantha: Ahh! I couldn't defeat you.")
        raw_input("Ethan: Get up Samantha! I will not wave a weakling in my gang!")
        raw_input("Samantha: I- I can't...")
        raw_input("Ethan: Pathetic! My Goons do not get defeated! I hereby revoke your title as a Spark. To the rest of you Sparks, lets go.")
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
            raw_input("Elder Wizard: My word! What happened here! A Spark was defeated? Duels are only permitted in the arena! Clean up this mess, I'll work on reviving them")

        elif Samantha:
            raw_input("Samantha: Wow. Helping me more than a friend. I like the way you roll. Don't worry, your friend can be revived, it just takes a lot of magic.")
            raw_input("Samantha: But for now, Invisibility! That should hide him.")
            raw_input("Elder Wizard: My word! What happened here! Its a mess! Duels are only permitted in the arena! Clean up this mess!")
            raw_input("Samantha: Alright, you have fun with that, er, what was your name?")
            raw_input("Samantha: " + name + ", got it. You have fun doing that " + name + ". I'll put in a good word for you with The Sparks. Speaking of which, I gotta see if they'll let me back in. Stop by once your done")
            badPath = False
        else:
            raw_input("Elder Wizard: My word! What happened here! Two people defeated? And your the only person around here. Duels are only permitted in the arena!")
            elder_wizard()
    else:
        raw_input("Noah: Ngh... got me good. I didn't stand a chance.")
        raw_input("Noah: There's a healing potion behind you on that shelf, Heal me " + name + "!")
        raw_input("Ethan: Don't you dare.")
        choice = raw_input("1)Heal 2)Don't Heal")
        if choice == "1":
            raw_input("Ethan: Y'know, I had hopes for ya, you looked strong. But you disappoint me. I'll take that.")
            raw_input("Ethan took the Healing Potion and smashed it on the ground")
            badPath = False
        else:
            raw_input("Ethan: Ha! I knew you had it in ya.")
            badPath = True
        raw_input("Noah: You monster.")
        raw_input("Noah was defeated at level 3 with the spells [\"Magic Beam\", \"Fireball\"]")
        Noah = False
        if badPath:
            raw_input("Ethan: Come on, some other wizards will probably find him and waste their own magic reviving him.")
            raw_input("Ethan: For now, lets get you initiated as an official spark.")
        else:
            raw_input("Ethan: Pathetic! Let's go Sparks.")
            raw_input("Elder Wizard: My word! What happened here! Someone was defeated? Duels are only permitted in the arena! Clean up this mess, then you are EXPELLED!")
            raw_input("The Elder Wizard took your Magic Objects. While leaving, you encountered an Ent in the Ent Forest.")
            object1 = "None"
            spell_list = ["Nothing"]
            Enemy("The Ent", 25, "None", "Green", ["Raged Claws"])
    chapter_two()


def chapter_two():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    if not badPath:
        if Noah and Samantha:
            # You three go around training and trying to get better and defeat the Sparks, the cannon pathway.
            raw_input(
                "The three of you clean up the mess caused by your encounter with the Sparks, and vow to one day defeat them.")
            raw_input(
                "Noah: If were gonna defeat the sparks, were gonna need to get stronger. I say we head back to the Ent woods and level up a bit.")
            raw_input("Samantha: I actually have something a bit more sinister planned.")
            raw_input(
                "Samantha: You see, the Elder Wizard is the most powerful Wizard alive. If you've seen him duel, you'd know what I'm taking about. He is a master of all colored spells.")
            raw_input(
                "Samantha: He has some crazy powerful spells, like FrostBite, a spell that deals 10 damage and freezes the opponent! And I bet the book is still in his room.")
            raw_input("Noah: No way that sounds too dangerous.")
            while True:
                fate = raw_input("Noah: What do you say, " + name + "?\n1)Ent Forest  2)Elder Wizard")
                if fate == "1":
                    raw_input("Samantha: Aw, you guys are lame.")
                    # Train in the forest, encounter a king ent
                    ent_forest()
                    break
                    # TODO: End here

                elif fate == "2":
                    raw_input("Noah: Okay, if you say so " + scrambled_name + ".")
                    raw_input("The three of you go to the Elder Wizard's Lobby, Samantha guiding you.")
                    raw_input("Noah: Woah, that's a huge door.")
                    raw_input("Samantha: And it's even bigger inside. Just look at all the books on the wall!")
                    raw_input("Samantha: We should split up, and look for a powerful spell.")
                    library()
                    raw_input("The three of you narrowly escape")
                    raw_input("Noah: I can't believe we got out of there!")
                    raw_input("Samantha: Honestly neither can I. What did you say your idea was Noah?")
                    raw_input("Noah: I forgot, but I'm panicking too much to want to do anything else than rest.")
                    raw_input("Samantha: But you did get some experience from trying out those spells!")
                    raw_input("Level up! Max Hp +1")
                    level += 1
                    maxHp += 1
                    break
                    # TODO: End here
            crew = ["Noah", "Samantha"]
        elif Noah and not Samantha:
            raw_input("Samantha: You are terrible people! I'm going back to Spark HQ, I will make them Hate you!")
            raw_input(
                "Noah: That cant be good. We should probably train so that were prepared if they attack us again.")
            raw_input("Noah: Lucky for us, we have a perfect training grounds in the form of the Ent Forest!")
            ent_forest()
            # TODO: End here
        elif Samantha and not Noah:
            raw_input(
                "You finish cleaning, and then head off in the direction Samantha went. It isn't long before you encounter a room with constant yellow flashing lights")
            raw_input(
                "Inside you find a large group of people dueling with lightning, in a rectangular arena with lightning rods on each corner.")
            raw_input("Ethan: Hey it's the twat from earlier. What are you doing here.")
            raw_input("Samantha: This twat right here just abandoned his friend to save a Spark.")
            crew = ["Samantha"]
            raw_input("Ethan: Your not a Spark anymore Samantha.")
            raw_input("Samantha: I know, but I thought I'd appeal with " + name + " here.")
            raw_input(
                "Ethan: Alright, " + name + ", lets see if your worthy. The first thing your gonna need to do is change your guild.")
            yorn = raw_input("You think you can do that? (Y)es or (N)o?")
            if yorn.lower() in ['y', 'yes', '1']:
                badPath = True
                spark_init()
                raw_input("Ethan: Samantha, I should have never doubted you. You're back in.")
                # TODO: End here
            elif yorn.lower() in ['n', 'no', '0', '2']:
                badPath = False
            if not badPath:
                raw_input(
                    "Ethan: Samantha, you're supposed to bring someone who you think will join when you try to appeal. I just can't work with this. SPARKS! Get them outta here!")
                raw_input("Samantha: Well that didn't work, thanks a lot.")
                raw_input(
                    "Samantha: Ya know, I'm still in the mood to cause trouble. The Elder wizard has a whole library of spells. Ill bring you to it.")
                library()
                raw_input(
                    "Samantha: Ha! It worked! The elder wizard used to be a Spark, so he kinda has a soft spot for them. Thats why we get away with so much. It's a shame we got kicked out though...")
                raw_input(
                    "Samantha: Anyways, learnig new spells is a good way to get experience. So you probably can level up!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                # TODO: End here
    if badPath:
        spark_init()
        if not badPath:
            raw_input("Ethan: SPARKS! Get them outta here!")
            raw_input("You got kicked out of the sparks, and now you have no friends.")
            crew = ["None"]
            while True:
                lonely = raw_input("What would you like to do?\n1)Check on noah  2)Train")
                if lonely == "1":
                    print "You decide to check up on Noah."
                    break
                elif lonely == "2":
                    print "You decide to train."
                    break
                else:
                    print "You are still undecided."
            # TODO: End Here


def spark_init():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, guild
    raw_input("Ethan: Alright, we have a little Guild station over here. The book is right there, and you can just use the last chalk circle that got used.")
    step1 = raw_input("So, you've decided to become a member of the Sparks. Well no Spark can exist without the Spell Sparks! Get used to hearing the word sparks, we use it for everything. To cast the spell, you must chant El Yelo Sparkosus. But before you do that, you must swear in to the Sparks. Say \"I solemnly swear to only respect other Sparks.\"\n")
    if step1.lower() not in ["i solemnly swear to only respect other sparks.", "i solemnly swear to only respect other sparks"]:
        raw_input("Ethan: NOPE! He is not Spark material!")
        badPath = False
    else:
        step2 = raw_input("You place your " + object1 + " in the worn chalk circle. What must you chant?\n")
        if step2 not in ["El Yelo Sparkosus", "El Yelo Sparkosus!"]:
            raw_input("Ethan: NOPE! He is not Spark material!")
            badPath = False
        else:
            step3 = raw_input("How do you call this spell?\n")
            if step3 not in ["Sparks", "Sparks!"]:
                raw_input("Ethan: NOPE! He is not Spark material!")
                badPath = False
            else:
                spell_list.append("Sparks")
                print "Successful Enchant!"
                print object1, "has the spells:", spell_list
                if guild != "Yellow":
                    raw_input("\nYou changed to the Yellow Guild!\n")
                    guild = "Yellow"
                raw_input("You joined the Sparks!\n")
                raw_input("Ethan: Well, I didn't think you could do it. Welcome to the sparks, in a world of awesome superiority!")
                raw_input("Level up! Max Hp +1")
                level += 1
                maxHp += 1
                badPath = True
                crew = ["Sparks"]


def elder_wizard():
    Enemy("Elder Wizard", 1000000, "None", "Gold", ["Smite"])
    raw_input("Elder Wizard: Ooohhhh...")
    raw_input("Elder Wizard: You are very powerful.")
    raw_input("Elder Wizard: Almost... too powerful.")
    raw_input("Elder Wizard: Like a Hacker.")
    raw_input("Elder Wizard leveled up! HP +1!")
    raw_input("Elder Wizard regenerated to full health!")
    Enemy("Raged Elder Wizard", 1000001, "None", "Gold", ["Firewall", "Full Regenerate"])
    raw_input("Elder Wizard: Ngh...")
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
    raw_input("Samantha: I think I hear someone coming!")
    spell_slot = raw_input("What spell slot will you use?\n" + str(spells_found))
    spell = spells_found[int(spell_slot)-1]
    if spell == "Le Grin Medihelios":
        spell_list.append("Heal")
        raw_input("Everyone around you got healed to full health!")
        raw_input("Samantha: Thanks, now we can last longer when the person coming down the hall kills us. Just, play along")
        raw_input("Elder Wizard: Who's in here? I heard noise!")
        raw_input("Elder Wizard: Oh, you trouble making Sparks. Samantha didn't I tell you? This Library is off limits!")
        raw_input("Samantha: Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("Elder Wizard: Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Reedos Firon Bulos":
        spell_list.append("Fireball")
        raw_input("A fireball erupted in the middle of the room.")
        raw_input("Samantha: Great! Now were gonna be in twice as much trouble for property damages!")
        raw_input("Elder Wizard: Who's in here? I heard noise!")
        raw_input("Elder Wizard: Ahh! There's a fire! Water Geyser!")
        raw_input("The fire is put out and there is steam all around.")
        raw_input("Samantha: Quickly, lets get out of here!")
    elif spell == "Al Bleo Freson":
        spell_list.append("Freeze")
        raw_input("Elder Wizard: Who's in here? I heard noi-")
        raw_input("You Froze the Elder Wizard!")
        raw_input("Samantha: That was bold Freezing the Elder Wizard, now lets get out of here before he thaws!")
    elif spell == "El Yelo Lumining":
        spell_list.append("Lightning")
        raw_input("Elder Wizard: Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input("Samantha: What the heck did you just do?!")
        raw_input("Elder Wizard: Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "La Grezz Insivion":
        spell_list.append("Invisibility")
        raw_input("Everyone Around you turned invisible!")
        raw_input("Samantha: Good thinking! now lets get out of here before this spell wears off!")
    elif spell == "El Yelo Sparkosus":
        spell_list.append("Sparks")
        raw_input("Samantha: Sparks? Do you seriously want to be a Spark in a time like this? But that gives me an idea, just play along")
        raw_input("Elder Wizard: Who's in here? I heard noise!")
        raw_input("Elder Wizard: Oh, you trouble making Sparks. Samantha didn't I tell you? This Library is off limits!")
        raw_input("Samantha: Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("Elder Wizard: Just don't get any ideas! Go ahead and get out of here you rascals.")
    elif spell == "La Grezz Maginka Beamos":
        spell_list.append("Magic Beam")
        raw_input("Elder Wizard: Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Magic Beam!")
        raw_input("Samantha: What the heck did you just do?!")
        raw_input("Elder Wizard: Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Le Grin Raginos Claus":
        spell_list.append("Raging Claws")
        raw_input("You attack Samantha with Raging Claws!")
        raw_input("Samantha: Agh! Why did you do that?!?!?")
        raw_input("The spell made you attack again!")
        raw_input("Samantha: Auughh!")
        raw_input("Samantha was defeated at level 4 with the spells [\"Magic Beam\", \"Sparks\"]")
        raw_input("Elder Wizard: My word! What happened here! Broken into the spell room and a defeated body? Both those are off limits!")
        elder_wizard()
    elif spell == "La Grezz Maginka Lessar":
        spell_list.append("Magic Laser")
        raw_input("Elder Wizard: Who's in here? I heard noi- OOF!")
        raw_input("You hit the Elder Wizard with a Lightning Bolt!")
        raw_input("Samantha: What the heck did you just do?!")
        raw_input("Elder Wizard: Oh, you trouble makers. This Library is off limits!")
        elder_wizard()
    elif spell == "Aleos Maximon Goludos Smitomiras Infiniron":
        spell_list.append("Smite")
        raw_input("Elder Wizard: Who's in here? I heard noi- ")
        raw_input("The entire room is obliterated with a Smite from the skies!!")
        raw_input("Elder Wizard: Ngh... Those poor fools. They didn't know what they were messing with.")
        raw_input("Game Over")
        print "You were defeated at level " + str(level) + " with the spells: "
        print spell_list
        quit()
    else:
        raw_input("In your panic, you froze in place, but not like the spell Freeze.")
        raw_input("Samantha: what are you doing? Just- just follow my lead.")
        raw_input("Elder Wizard: Who's in here? I heard noise!")
        raw_input("Elder Wizard: Oh, just you trouble making Sparks. Samantha didn't I tell you? This Library is off limits!")
        raw_input("Samantha: Yes sir you did but I was just showing the new recruit where all our spell books come from.")
        raw_input("Elder Wizard: Just don't get any ideas! Go ahead and get out of here you rascals.")


def ent_forest():
    global badPath, Noah, Samantha, object1, spell_list, level, maxHp, crew, scrambled_name
    raw_input("You head out to the Ent Forest")
    raw_input("Noah: Alright, there are a few Ents on the border, but that wont get us much experience.")
    raw_input("Noah: I say we sneak through and get to the center to get the stronger enemies")
    raw_input("Noah: There are many paths through the forest, we should choose wisely.")
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
        print " 1      2    "
        print " \ \  / /  "
        print "  \ \/ /   "
        print "   \  /    "
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
        Enemy("Ent", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 4:
        if randint(1, 3) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy("Ent", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 5:
        if randint(1, 2) == 1:
            raw_input("Nope, not an Ent.")
        else:
            raw_input("Yep, It was an Ent!")
            Enemy("The Ent", randint(12, 17), "None", "Green", ["Raged Claws"])
    elif goal == 6:
        if randint(1, 3) == 1:
            raw_input("Yep, It was an Ent!")
            Enemy("The Ent", randint(12, 17), "None", "Green", ["Raged Claws"])
        else:
            raw_input("Nope, not an Ent.")
    elif goal == 7:
        raw_input("Nope, not an Ent.")
    raw_input("Other Ents noticed you, and attacked!")
    raw_input("Noah: Ahh! Theres too many! Try to fend off your side!")
    Enemy("Ent", randint(12, 17), "None", "Green", ["Raged Claws"])
    raw_input("Level up! Max Hp +1")
    level += 1
    maxHp += 1
    raw_input("Noah: YEAH! I think we're geting them!")
    raw_input("Noah: Oh- Oh no.")
    raw_input("???: ROOOOOAAAAAAHHHH!")
    if guild != "Green":
        Enemy("Ent King", 25, "None", "Gold", ["Raged Claws"])
        raw_input(
            "Having defeated the Ent King, The other Ents ran off, but they left behind a Spell Book for Raged Claws")
    else:
        raw_input("A giant Ent with a Golden Crown comes out from the trees, and points to you.")
        raw_input("The other Ents grab you, and start dragging you away from your group.")
        raw_input("Noah: Ahhh! The Ent King took " + name + "!")
        raw_input("The Ents made a circle around your group, blocking them off as they took you to the Ent King.")
        raw_input(
            "Ent King: Why have you done this? Are you not a Green? Why must you attack us with a malicious Red by your side?")
        raw_input("Ent King: Training? For what? To fight the Yellow Sparks? My my. That's a new Guild.")
        raw_input("Ent King: 1000 years ago when I was younger, there were only 3 Guilds. Red, Blue, and Green.")
        raw_input("Ent King: This new Guild must be artificial and unnatural, you said they were like a stronger red?")
        raw_input(
            "Ent King: Hmm. This is concerning. While I musn't leave the forest, I will grant you the spell of out people.")
        raw_input("Ent King: The Spell Book for Raged Claws.")
        raw_input("Ent King: Now go, and stop the evil that is the sparks.")
        raw_input("The Ents dispersed, allowing you and your group to escape.")
    raw_input("Noah: Wow, this forest looks super empty now. Didn't realize quite how many Ents there were")
    raw_input("But we gotta learn that new Spell! I imagine it'll be useful when fighting the sparks!")


def checkpoint():
    print "Where would you like to start?"
    print "0)Quit"
    print "1)Chapter One 2)First fight 3)Choose your Guild 4)Learn your next spell 5)First encounter with the Sparks"
    print "6)Chapter Two 7)Enter the Library 8)Enter the Ent Forest 9)Fight the Elder Wizard"
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
            questions(True, True, True, True, False, False, True, True)
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
            ent_forest()
            break
        elif choice == 9:
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
            allSpells = ["Finished", "Freeze", "Fireball", "Lightning", "Heal", "Magic Beam", "Invisibility", "Raged Claws", "Sparks", "Magic Laser", "Smite", "Firewall", "Full Regenerate"]
            spell = input("\nWhat Spells did you have? Please type one slot number. " + str(spell_list) + "\n     0           1          2           3         4           5             6               7            8           9          10         11             12 \n" + str(allSpells) + "\n")
            if spell != 0:
                spell_list.append(allSpells[spell])
            else:
                break
        if spell_list is []:
            spell_list = ["Nothing"]
    if guildNeed:
        guild = raw_input("What Guild are you in?")
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
            elif yorn.upper() == "N":
                Noah = False
        while True:
            yorn = raw_input("Is Samantha alive? Y/N")
            if yorn.upper() == "Y":
                Samantha = True
            elif yorn.upper() == "N":
                Samantha = False
    if levelNeed:
        level = input("What level were you?")
        maxHp = 9 + level
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
