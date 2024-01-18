import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class DialogueOptions:
    def __init__(self,name):
        #all sprite options
        self.playerSprite = PlayerDialSprites(name) #Main character dialogue sprite object
        self.RMSprite = RMDialSprites() #Ring Master dialogue sprite object
        self.DDSprite = DDDialSprites() #DareDevil dialogue sprite object
        self.LTSprite = LTDialSprites() #Lion Tamer dialogue sprite object
        self.CSprite = CDialSprites() #Contortionist dialogue sprite object
        self.VSprite = VDialSprites() #Ventriloquist dialogue sprite object

        #all scenes and required information
        self.dialogueList = [(False, True, "I look around to see other pedrestians minding their own business and going about their days.", self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, "Am I just like them? Just another random person in this world? Will I ever amount to anything?", self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, ("I am lost in thought. I trip over some rubbish that the lady on the corner left out days ago."), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, True, ("This is the third time this has happened this week... and now I'm covered in rubbish yet again."), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, True, ("And now I have no choice but to return back home and change. All I want to do is go to the shops."), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, True, ("The whole way home I fret about which clothes to change into. I really should be more aware of my surroundings..."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("I continue walking, and accidentally bump into someone on the way."), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, True, ("Sorry! I really didn't mean it!"), self.playerSprite, self.playerSprite.ImageList[1], self.playerSprite.colour),
        (False, False, ("You should watch your step."), self.playerSprite,self.RMSprite, self.playerSprite.ImageList[1], self.RMSprite.ImageList[0], self.RMSprite.colour),
        (False, False, ("You're right. I'm sorry, I should have been walking backwards or something so I could see where I'm going."), self.playerSprite,self.RMSprite, self.playerSprite.ImageList[1], self.RMSprite.ImageList[0], self.playerSprite.colour),
        (False, False, ("I'll try to be better for next time."), self.playerSprite,self.RMSprite, self.playerSprite.ImageList[1], self.RMSprite.ImageList[0], self.playerSprite.colour),
        (False, True, ("What a rude man."), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, True, ("He walks off into the other direction. I hope I never see him again."), self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, ("It's people like him who really get me annoyed. They don't care about other people."), self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, ("I sigh. I'm getting too irritated over a little thing like that."), self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, ("Although, if I was bumped into by someone covered in mysterious subtances, I'd be kind of annoyed too."), self.playerSprite, self.playerSprite.ImageList[3], "White"),
        (False, True, ("I guess it is a nice day out. It's nice to see so many friendly faces out and about today."), self.playerSprite, self.playerSprite.ImageList[5], "White"),
        (False, True, ("...Huh? Is that a baby crying? It's in an alleyway too..."), self.playerSprite, self.playerSprite.ImageList[3], self.playerSprite.colour),
        (True, 2, "Approach the baby?", "Yes", "No"),
        (False, True, ("I should try and be smart about this."), self.playerSprite, self.playerSprite.ImageList[3], self.playerSprite.colour),
        (False, True, ("There is nothing not suspicious about a random baby in an alleyway. I'm not dumb."), self.playerSprite, self.playerSprite.ImageList[3], self.playerSprite.colour),
        (False, True, ("Yeah. Especially not after Tao got kidnapped. I'm not falling for these tricks."), self.playerSprite, self.playerSprite.ImageList[3], self.playerSprite.colour),
        (False, True, (""), self.playerSprite, self.playerSprite.ImageList[6], "White"),
        (False, True, ("Hello? Is anyone here?"), self.playerSprite, self.playerSprite.ImageList[1], self.playerSprite.colour),
        (False, True, ("I still hear the sound of a baby crying."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("Why am I trying to talk to a baby anyway?"), self.playerSprite, self.playerSprite.ImageList[2], self.playerSprite.colour),
        (False, True, ("I move further into the alleyway. There is no sign of a baby."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("I sigh."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("There is no way I'm not about to get kidnapped or something right now."), self.playerSprite, self.playerSprite.ImageList[3], self.playerSprite.colour),
        (False, True, ("This is like what Tao must have done. Walked into a suspicious alleyway only to see nothing."), self.playerSprite, self.playerSprite.ImageList[5], "White"),
        (False, True, ("Even more suspicious."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("And then... !"), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, (""), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("INSTANT KIDNAPPING!"), self.playerSprite, self.playerSprite.ImageList[7], "White"),
        (False, True, (""), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("I should leave before that actually turns into a reality though."), self.playerSprite, self.playerSprite.ImageList[5], "White"),
        (False, True, ("I continue to make my way home."), self.playerSprite, self.playerSprite.ImageList[0], "White"),
        (False, True, ("There's a cloth over my mouth...! I can't breathe..."), self.playerSprite, self.playerSprite.ImageList[6], self.playerSprite.colour),
        (False, True, ("Everything is fading to black..."), self.playerSprite, self.playerSprite.ImageList[6], self.playerSprite.colour),
        (False, True,(""),self.playerSprite, self.playerSprite.ImageList[1],"White"),
        (False, True, ("I slowly regain my consciousness... How long has it been...?"), self.playerSprite, self.playerSprite.ImageList[1],"White"),
        (False, True, ("I look around at my new environment."), self.playerSprite, self.playerSprite.ImageList[3],"White"),
        (False, True, ("...is this..."), self.playerSprite, self.playerSprite.ImageList[7], "White"),
        (False, True, (" ...A CIRCUS?"), self.playerSprite, self.playerSprite.ImageList[7], "White"),
        (False, True, ("As cool as this may be... this is completely weird."), self.playerSprite, self.playerSprite.ImageList[1], "White"),
        (False, True, ("Why would a person kidnap me, a random guy on the street, and take him to a circus?"), self.playerSprite, self.playerSprite.ImageList[2], "White"),
        (False, False, ("Hello, our new member."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[1],  self.DDSprite.colour),
        (False, False, ("Just woke up?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[1],  self.DDSprite.colour),
        (False, False, ("Who are you?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[1],  self.playerSprite.colour),
        (False, False, ("She looks cool, I guess."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[3],  "White"),
        (False, False, ( "Oh, I'm only the most talented member of this troupe. You're speaking to the star of the show, the main attraction."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[1],  self.DDSprite.colour),
        (False, False, ("I take that back."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[2],  "White"),
        (False, False, ("Wow, I hadn't realised I'd been greeted by such greatness!"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.playerSprite.colour),
        (False, False, ("But really, your Majesty, who are you actually?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[4],  self.playerSprite.colour),
        (False, False, ("I'm the one who makes sparks fly in the show. I can handle anything that my flames throw my way!"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Really?? This tells me nothing...."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[2],  "White"),
        (False, False, ("I'm the fearless fire dancer of this circus..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[5],  self.DDSprite.colour),
        (False, False, ("I am the DAREDEVIL"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Finally an answer!"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[7],  self.playerSprite.colour),
        (False, False, ("So, what am I doing here??"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[3],  self.playerSprite.colour),
        (False, False, ("I'm sorry to break the news..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[1],  self.DDSprite.colour),
        (False, False, ("... but you's been kidnapped."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[4], self.playerSprite.colour),
        (False, False, ("Yeah, I got that already."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[4],  "White"),
        (False, False, ("But trust me, it's for a good cause. We're going to make you a star, just like me."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[3],  self.DDSprite.colour),
        (False, False, ("Do you ever stop bragging about yourself? You talk so much, I'm just going to head back to sleep."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[3],self.playerSprite.ImageList[2],  self.playerSprite.colour),
        (False, False, ("Bragging? Nonsense! My dear, everything I say is the absolute truth!"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("And if you're not interested in hearing it, well, that's your loss."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("Well, I guess I do want to know the truth..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.playerSprite.colour),
        (False, False, ("Out with it then. It's not every day you get to speak to such talent like me."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Who kidnapped me? And why do they want to make me a part of this?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[3],  self.playerSprite.colour),
        (False, False, ("That'll be none other than the Head of this Circus."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("He looks for people who don't have any purpose in life to come and join the circus."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("He lets us discover our skills. So I guess he saw some hidden talent within you too... although I don't think sarcasm would get you far here."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("Skills, huh..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.playerSprite.colour),
        (False, False, ("And as for why he wants to make you a star... I don't know."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("Clearly the performers are not chosen well. None of them other than me have any talent at all."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("But that's all they truly need."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Isn't that rude to your cast? Theyre not here right now, why insult them?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[2],  self.playerSprite.colour),
        (False, False, ("Oh, you'll see soon.."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Then... do you what role I'll take in the circus"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.playerSprite.colour),
        (False, False, ("I think your outfit says it all."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, True, ("She points me to a puddle on the floor. Do you these people not own a single mirror??"), self.playerSprite, self.playerSprite.ImageList[1],  "White"),
        (False, True, ("I take a look at my reflection.."), self.playerSprite,self.playerSprite.ImageList[1],  "White"),
        (False, True, ("I dressed as a clown..."), self.playerSprite, self.playerSprite.ImageList[2],  "White"),
        (False, True, ("Seriously? A clown?? A clown!"), self.playerSprite, self.playerSprite.ImageList[4],  "White"),
        (False, True, ("Why am I a clown? It doesn't even fit.."), self.playerSprite, self.playerSprite.ImageList[0],  "White"),
        (False, True, ("Why is DareDevil laughing at my reaction..."), self.playerSprite, self.playerSprite.ImageList[4],  "White"),
        (False, True, ("...I'm a clown..."), self.playerSprite, self.playerSprite.ImageList[7],  "White"),
        (False, False, ("I guess clown college wasn't for you. You're already a professional."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[4],  self.DDSprite.colour),
        (False, False, ("..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[4],  self.playerSprite.colour),
        (False, False, ("...not funny."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[4],  self.playerSprite.colour),
        (False, False, ("Wasn't trying to be. That's your job, isn't it?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[2],  self.DDSprite.colour),
        (False, False, ("HOW COULD THIS HAPPEN TO ME????"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[4],  self.playerSprite.colour),
        (False, False, ("..."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[0],  self.playerSprite.colour),
        (False, False, ("Well, what do I do now?"), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[0],  self.playerSprite.colour),
        (False, False, ("I guess you could meet the other troupe members."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("They're truly an amazing group of people."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Okay then, They're all boring to me. I guess taht's obvious since they're not on my level."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("Perhaps you'll fit right in."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[4],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, True, ("We both walk over to the other troupe members."), self.playerSprite, self.playerSprite.ImageList[0],  "White"),
        (False, False, ("Well, well, well look who decided to grace us with his presence. And who might you be, little man?"), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, True, ("Little man, LITTLE MAN??"), self.playerSprite, self.playerSprite.ImageList[2],  "White"),
        (False, False, ("I am " + self.playerSprite.name + ". Apparently I'm a new member of this troupe."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.playerSprite.colour),
        (False, False, ("I see a young boy in the corner with a puppet..."), self.VSprite, self.playerSprite, self.VSprite.ImageList[0],self.playerSprite.ImageList[3],  "White"),
        (False, False, ("...Next to a girl who won't even look at me. Weird?"), self.CSprite, self.playerSprite, self.CSprite.ImageList[0],self.playerSprite.ImageList[3],  "White"),
        (False, False, ("Hello there... I think you look funny with your short legs."), self.VSprite, self.playerSprite, self.VSprite.ImageList[1],self.playerSprite.ImageList[7],  self.VSprite.colour),
        (False, True, ("Did this kid speak through a puppet?"), self.playerSprite, self.playerSprite.ImageList[7],  "White"),
        (False, False, ("SHORT LEGS? I just met these people, why are they insulting me so much..."), self.VSprite, self.playerSprite, self.VSprite.ImageList[0],self.playerSprite.ImageList[2],  "White"),
        (False, False, ("I think they give me character."), self.VSprite, self.playerSprite, self.VSprite.ImageList[0],self.playerSprite.ImageList[5],  self.playerSprite.colour),
        (False, False, ("Oh, how cute. The new guy thinks he's got character."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[3],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("Well, let me tell you something kid."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("You're going to need more than short legs to make it in this troupe."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[1],self.playerSprite.ImageList[1],  self.LTSprite.colour),
        (False, True, ("I didn't want to join this troupe. I was kidnapped. Why doesn't this old man understand?"), self.playerSprite, self.playerSprite.ImageList[2],  "White"),
        (False, False, ("Leave him alone. He is a newcomer..."), self.CSprite, self.playerSprite, self.CSprite.ImageList[0],self.playerSprite.ImageList[0],  self.CSprite.colour),
        (False, False, ("Stop wasting tiem and introduce yourselves to our new member."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[0],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("I am the Lion-Tamer, the second most senior member of this illustrious troupe."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[2],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("I have been performing for many years, and I only expect the best from my fellow performers!"), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[2],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("IF you think of your perfromers as the best, then you all have a lot of work to do."), self.DDSprite, self.playerSprite, self.DDSprite.ImageList[1],self.playerSprite.ImageList[0],  self.DDSprite.colour),
        (False, False, ("I am Contortionist. And he is Ventriloquist."), self.CSprite, self.playerSprite, self.CSprite.ImageList[0],self.playerSprite.ImageList[0],  self.VSprite.colour),
        (False, True, ("I assume she's speaking about the little kid? He looks creepy that's for sure."), self.playerSprite, self.playerSprite.ImageList[3],  "White"),
        (False, True, ("Cortortionist seems to be looking for something... like something bad is about to happen."), self.playerSprite, self.playerSprite.ImageList[1],  "White"),
        (False, True, ("So, about this Head of Circus, when does he show up?"), self.playerSprite, self.playerSprite.ImageList[3],  self.playerSprite.colour),
        (False, False, ("Oh, you're looking for them, are you? Well, I hate to disappoint, but you're stuck with me now."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[3],self.playerSprite.ImageList[2],  self.LTSprite.colour),
        (False, False, ("As for when he will arrive, that is not for me to say. We all have our own obilgations, you know."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[3],self.playerSprite.ImageList[2],  self.LTSprite.colour),
        (False, False, ("At this point you'll have to answer to me."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("You could have just said 'I don't know' and I would've understood."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[2],  self.playerSprite.colour),
        (False, False, ("Ah, sorry about that. I guess I like to hear myself talk sometimes."), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("But, hey, now you know who the most senior member of the troupe is, right?"), self.LTSprite, self.playerSprite, self.LTSprite.ImageList[0],self.playerSprite.ImageList[0],  self.LTSprite.colour),
        (False, False, ("Oh, just stop talking old man. We all know that it's me..."), self.LTSprite, self.DDSprite, self.LTSprite.ImageList[0],self.DDSprite.ImageList[3],  self.DDSprite.colour),
        (False, False, ("The only thing you've got going for yourself, and it's you're age, and barely that."), self.LTSprite, self.DDSprite, self.LTSprite.ImageList[1],self.DDSprite.ImageList[3],  self.DDSprite.colour),
        (False, False, ("Yeah, Yeah. You have talent. SO what? I guided and shaped this troupe. What have you done?"), self.LTSprite, self.DDSprite, self.LTSprite.ImageList[3],self.DDSprite.ImageList[3],  self.LTSprite.colour),
        (False, True, ("Nobody cares. Let's just practise."), self.CSprite, self.CSprite.ImageList[0], self.CSprite.colour),
        (False, True, ("She's right. Practise makes perfect."), self.DDSprite, self.DDSprite.ImageList[0], self.DDSprite.colour),
        (False, True, ("...did DareDevil just argee on something??"), self.playerSprite, self.playerSprite.ImageList[7],  "White"),
        (False, True, ("We all begin to practise. As expected, I am horrible. I just can't seem to get anything right."), self.playerSprite, self.playerSprite.ImageList[2],  "White"),
        (False, True, ("What is even my purpose here..."), self.playerSprite, self.playerSprite.ImageList[2],  "White"),
        (False, True, ("When I wake up the next day, I feel exhausted..."), self.playerSprite, self.playerSprite.ImageList[0],  "White"),
        (False, True, ("Practise with Daredevil is something I will avoid for the rest of my life."), self.playerSprite, self.playerSprite.ImageList[0],  "White"),
        (False, True, ("However, I have some free-time..."), self.playerSprite, self.playerSprite.ImageList[0],  "White"),
        (False, True, ("I need to get out of here..."), self.playerSprite, self.playerSprite.ImageList[5],  "White")
        ]
    
    def returnDialogueInfo(self, currentScene): #returning the list of information from the main list
        return self.dialogueList[currentScene]

class DialogueScene:
    def __init__(self, keyboard, canvasWidth, canvasHeight, frame, name ='MC'):
        #the default name for the player is MC
        self.keyboard = keyboard
        self.dialogueOptions = DialogueOptions(name) 

        self.tempPlayer = PlayerDialSprites(name)
        
        self.currentSceneInfo = None

        self.character1 = self.tempPlayer
        self.character2 = None
        self.dialogueText = "I look around to see other pedrestians minding their own business and going about their days."
        self.currentDialogue = 0
        self.name1 = ""
        self.name2 = ""
        self.place = "Town"
        self.menu = False

        self.expression1 = ""
        self.expression2 = ""

        self.textBoxColour = "White"

        self.option1 = ""
        self.option2 = ""

        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.delay = simplegui.create_timer(100,self.delay_handler)
        self.delay.start()
        self.delayBool = False

        self.finished = False

        #adding the controls to the sidepanel
        frame.add_label('') 
        frame.add_label('Next Scene = Space bar') 
        frame.add_label('Left Option = 1')
        frame.add_label('Right Option = 2')
        frame.add_label('')

        #setting up the background and event handlers
        frame.set_canvas_background('Black')
        frame.set_keydown_handler(self.keyboard.keyDown)
        frame.set_keyup_handler(self.keyboard.keyUp)

    #timer handler used to prevent the keyboard from being too responsive
    def delay_handler(self):
        self.delayBool = False

    def update(self):
        if (len(self.dialogueOptions.dialogueList) < self.currentDialogue): #checking whether the list containing all the scene information has reached the end
            self.finished = True #stopping the dialogue scene
        else:
            if (self.finished == False): #checking if we have made it to the end of the cutscene
                if self.delayBool == False: #adding a delay to the next button
                    self.delayBool = True #restarting the delay
                    if ((self.keyboard.next == True) or (self.keyboard.option1 == True) or (self.keyboard.option2 == True) ) and ((self.currentDialogue == 18) or (self.currentDialogue == 22) or (self.currentDialogue == 38)): #creating jump statement for specfic cases or if the user has presses any buttons
                        if self.currentDialogue == 18: #option menu
                            if(self.keyboard.option1 == True): #option for yes
                                self.currentDialogue =23 #jumping to the continuation for this option of the story
                            elif(self.keyboard.option2 == True): #option for no
                                self.currentDialogue += 1
                                self.delay.start()
                        elif self.currentDialogue == 22: #reaching the end of option 1
                            self.currentDialogue = 34 #jumpging to the continuation of the story
                            self.delay.start()
                        elif self.currentDialogue == 38: #switching the scene of the character
                            self.place = "BackStage"
                            self.currentDialogue += 1
                            self.delay.start()
                    else:
                        if(self.keyboard.next == True): # checking if the next button is pressed
                            self.currentDialogue += 1 #moving onto the next scene
                            self.delay.start()
                    
                    if (len(self.dialogueOptions.dialogueList) <= self.currentDialogue): #checking if the end of the list has been reached
                        self.delay.stop()
                        self.finished = True

                    if(self.finished == False): #fetching the new information for the current scene
                        self.currentSceneInfo = self.dialogueOptions.returnDialogueInfo(self.currentDialogue) #setting the new scene
                        if(self.currentSceneInfo[0] == True): #If the scene is a menu
                            #setting up menu variables
                            self.menu = True #changing the scene format for a menu
                            if(self.currentSceneInfo[1] == 2):
                                self.dialogueText = self.currentSceneInfo[2]
                                self.option1 = self.currentSceneInfo[3]
                                self.option2 = self.currentSceneInfo[4]

                        else: #if the scene contains characters
                            self.menu = False #resetting the scene format
                            if(self.currentSceneInfo[1] == True): #checking how many people are in the scene
                            #setting up variables for one character
                                self.dialogueText = self.currentSceneInfo[2]
                                self.character1 = self.currentSceneInfo[3]
                                self.expression1 = self.currentSceneInfo[4]
                                self.character2 = None
                                self.textBoxColour = self.currentSceneInfo[5]
                            else:
                                #setting up variables for two characters
                                self.dialogueText = self.currentSceneInfo[2]
                                self.character1 = self.currentSceneInfo[3]
                                self.character2 = self.currentSceneInfo[4]
                                self.expression1 = self.currentSceneInfo[5]
                                self.expression2 = self.currentSceneInfo[6]
                                self.textBoxColour = self.currentSceneInfo[7]

    def drawBase(self, canvas): #drawing the base for the scene for any characters present
        canvas.draw_polygon([(20,(self.canvasHeight)-25),((self.canvasWidth)-25,(self.canvasHeight)-25),((self.canvasWidth)-25,(self.canvasHeight)-185),(20,(self.canvasHeight)-185)], 1, self.textBoxColour, self.textBoxColour)
        canvas.draw_polygon([(20,(self.canvasHeight)-186),((self.canvasWidth)-750,(self.canvasHeight)-186),((self.canvasWidth)-750,(self.canvasHeight)-215),(20,(self.canvasHeight)-215)], 1,'Red', 'Red')
        canvas.draw_polygon([(20,50),(250,50),(250,20),(20,20)], 1,'Red', 'Red')
        canvas.draw_text(self.dialogueText,((25,(self.canvasHeight)-105)),20, 'Black')
        canvas.draw_text(self.place,((20,45)),30, 'Black')
        canvas.draw_text(self.character1.name,[20,425],30, 'Black')

    def drawMenuBase(self, canvas): #drawing the base for the scene for a manu
        canvas.draw_polygon([(20,(self.canvasHeight)-25),((self.canvasWidth)-25,(self.canvasHeight)-25),((self.canvasWidth)-25,(self.canvasHeight)-185),(20,(self.canvasHeight)-185)], 1,'White', 'White')
        canvas.draw_text(self.dialogueText,((20,(self.canvasHeight)-105)),20, 'Black')
        if (self.currentSceneInfo[1] == 2): #drawing the scene for a menu with two options
            canvas.draw_circle(((self.canvasWidth/3)-30,(self.canvasHeight/4)*2), 60, 1, 'Blue', 'Red')
            canvas.draw_text(self.option1,(((self.canvasWidth/3)-50,(self.canvasHeight/4)*2)),30, 'Black')
            canvas.draw_circle((((self.canvasWidth/3)*2)-30,((self.canvasHeight/4)*2)), 60, 1, 'Red', 'Blue')
            canvas.draw_text(self.option2,((((self.canvasWidth/3)*2)-50,(self.canvasHeight/4)*2)),30, 'Black')
        canvas.draw_text(self.place,((20,45)),50, 'Black')

    def draw(self,canvas):
        self.update()
        if(self.finished == False): # checking if the scene has finished
            if self.menu == False:
            #scene to draw for one character, only check for the second character
                if self.character2 == None: #for one character
                    canvas.draw_circle((self.canvasWidth/2, self.canvasHeight/2), 50, 1, self.character1.colour, self.character1.colour) #drawing character1 to the scene
                    canvas.draw_text(self.expression1,[(self.canvasWidth/2)-25,(self.canvasHeight/2)+5],20, 'Black')
                    self.drawBase(canvas)
                #scene to draw for two character
                else: #for two characters
                    #for character 1
                    canvas.draw_circle((self.canvasWidth/3-60, self.canvasHeight/2), 60, 1, self.character1.colour, self.character1.colour) #drawing character1 to the scene
                    canvas.draw_text(self.expression1,[(self.canvasWidth/3)-100,self.canvasHeight/2],20, 'Black')
                    #for character 2
                    canvas.draw_polygon([(self.canvasWidth-255,(self.canvasHeight)-186),((self.canvasWidth)-25,(self.canvasHeight)-186),((self.canvasWidth)-25,(self.canvasHeight)-215),(self.canvasWidth-255,(self.canvasHeight)-215)], 1,'Red', 'Red') # 
                    canvas.draw_text(self.character2.name,[self.canvasWidth-245,(self.canvasHeight)-196],20, 'Black')
                    canvas.draw_circle((((self.canvasWidth/3)*2)+50, self.canvasHeight/2), 60, 1, self.character2.colour, self.character2.colour) #drawing character2 to the scene
                    canvas.draw_text(self.expression2,[((self.canvasWidth/3)*2)+20,self.canvasHeight/2],20, 'Black')
                    #drawing the base
                    self.drawBase(canvas)
            else: #for a menu
                self.drawMenuBase(canvas) #drawing the menu to the screen
        else:
            self.delay.stop()#stoping the timer

class CDialSprites:
    def __init__(self):
        self.name = "Contortionist" #for the nametag
        
        self.colour = "#cebdf9" #the colour of the textbox
        
        self.currentImage = 0 #the current image to be drawn to the screen

        self.cWorried = "Worried" # Case 0

        self.ImageList = [self.cWorried] #list of all the contortionist sprites

class DDDialSprites:
    def __init__(self):
        self.name = "DareDevil" #for the nametag
        
        self.colour = "#de4201" # the colour of the textbox
        
        self.currentImage = 0 #the current image to be drawn to the screen

        self.dDConfident = "Confident" # Case 0
        self.dDSmug = "Smug" # Case 1
        self.dDAnnoyed = "Annoyed" # Case 2
        self.dDAngry = "Angry" # Case 3
        self.dDismissive = "Dismissive" # Case 4

        self.ImageList = [self.dDConfident, self.dDSmug, self.dDAnnoyed, self.dDAngry, self.dDismissive] #list of all the daredevil sprites

class LTDialSprites:
    def __init__(self):
        self.name = "Lion Tamer" #for the nametag
        
        self.colour = "#ab8036" #the colour of the textbox
        
        self.currentImage = 0 #the currrent image to be drawn to the screen

        self.lTLightHearted = "Light-Hearted" # Case 0
        self.lTSerious = "Serious" # Case 1
        self.lTConfident = "Confident" # Case 2
        self.lTDismissive = "Dismissive" # Case 3

        self.ImageList = [self.lTLightHearted, self.lTSerious, self.lTConfident, self.lTDismissive] #list of all the lion tamer sprites

class PlayerDialSprites:
    def __init__(self, name):
        self.name = name#for the nametag
        
        self.colour = "#dad3d1" #the colour of the textbox
        
        self.currentImage = 0 #the current image to be drawn to the screen

        self.mCBored = "Bored" # Case 0
        self.mCWorried = "Worried" # Case 1
        self.mCAnnoyed = "Annoyed" # Case 2
        self.mCQuestion = "Question" # Case 3
        self.mCAngry = "Angry" # Case 4
        self.mCThoughtful = "Thoughtful" # Case 5
        self.mCKidnapped = "Kidnapped" # Case 6
        self.mCSurprised = "Surprised" # Case 7

        self.ImageList = [self.mCBored, self.mCWorried, self.mCAnnoyed, self.mCQuestion, self.mCAngry, self.mCThoughtful, self.mCKidnapped, self.mCSurprised] #list of all the player sprites

class RMDialSprites:
    def __init__(self):
        self.name = "Ring Master" #for the nametag
        
        self.colour = "#6C0255" #the colour of the textbox
        
        self.currentImage = 0 #thhe current image to be drawn to the screen

        self.rMAngry = "Angry" # Case 0

        self.ImageList = [self.rMAngry] #list of all the ring master sprites

class VDialSprites:
    def __init__(self):
        self.name = "Ventriloquist" #for the nametag
        
        self.colour = "#1D1E3E" #the colour of the textbox
        
        self.currentImage = 0 #the current image to be drawn to the screen

        self.vTalking = "Talking" # Case 0
        self.vIdle = "Idle" # Case 1

        self.ImageList = [self.vTalking, self.vIdle] #list of all the ventriloquist sprites
