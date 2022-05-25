# The only style I could find that defines character name colors also affects GUI so I am defining the color individually
define Character0 = Character("???", color="#ffffff")
define Character1 = Character("Pomu", color="#ffffff")
define Character2 = Character("[persistent.mcName]", color="#ffffff")
define Character3 = Character("Class President", color="#ffffff")
define Character4 = Character("Oliver", color="#ffffff")
define Character5 = Character("Everyone", color="#ffffff")
define Character6 = Character("Elira", color="#ffffff")
define Character7 = Character("Finana", color="#ffffff")
define Character8 = Character("Emma", color="#ffffff")
define Character9 = Character("Employee", color="#ffffff")

label demo_route:

    scene bg none with fade
    play music audio.bgm_flashback01 fadein 3.0


    "I remember the feeling."


    "The unrelenting heat of the sun."


    "The thundering roar of voices."


    "The resonant beat of my own heart."


    "The feeling of rushing forward.{w} The nervousness.{w} The determination.{w} All of it, so I could see that view."


    play sound audio.sfx_windstrong fadein 2.0

    scene bg sunny sky at sky_zoom with fade

    "Boundless sky with the sun at the center of it all."
    "It felt like I was flying, like the clouds were my second home."
    "It was exhilarating, and it was a feeling I’ll never forget."

    "That is…{w=0.5} until I couldn’t anymore."
    scene bg sunny sky at sky_fall
    play sound [ "<silence 0.7>", audio.sfx_thud01 ]
    pause 0.8

    scene bg none with sshake_m




    "And just like that,{w} everything started to fall apart."
    play sound [ "<silence 0.7>", audio.sfx_ambulance ]
    "My ‘wings’ were taken that day."
    "My precious place in the sky, gone, like the wind."


    "I quit doing all the things that I truly enjoyed doing."
    "The joy, the fun, the excitement, all drowned in my sorrows until my life has become what it is now.{w} A bland mixture of monotony and staleness."


    scene bg mc room night with fade
    stop music fadeout 3.0


    "I wake up with cold sweat dripping from my face.{w} It’s the same dream again."

    "Outside, the sun is yet to be seen."
    "It’s a bit earlier than the time I planned to wake up, but I know I can’t fall back asleep even if I wanted to."

    "A lot of things start to pile up in my mind. It feels like these thoughts would come crashing down at any minute."
    "I have to get away, somewhere, anywhere but here."

    "Without even bothering to change clothes, I grab my jacket and make my way outside."


    scene bg park with slidingblinds

    play sound audio.sfx_birds loop fadein 1.0


    "Soon, I found myself at the park, wandering aimlessly and with no idea how much time had passed."


    "Even though I try to keep my thoughts away from the dream, I end up thinking about it more and more."
    "The feelings become overwhelming and the pain in my arm starts to surface,"
    stop sound fadeout 2.0
    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    play music audio.sfx_heartbeat60 fadein 2.0 volume 2.0
    extend" as if knocking on my mind's door, banging and thrashing and forcing itself in."




    "Before I know it, I’m covered in cold sweat, and my heart is beating so fast, it feels like my chest is about to explode."
    stop music fadeout 2.0
    hide heartdmg with dissolve
    show layer master
    "But suddenly…"




    show pomusuke at center with easeinleft
    Character0 "HISSS!"
    hide pomusuke with easeoutright


    "..."

    Character0 "Get back here!" with sshake_m

    play music audio.bgm_hectic01 fadein 2.0
    scene cg pomu pomusuke ver1 with fade

    "I turn to the source of the commotion and see a blonde girl with a large hair ribbon chasing down her…{w} cat?"
    "But somehow, it looks more like she’s out for blood rather than actually trying to catch it."

    scene cg pomu pomusuke ver2 with fade

    "As the scene in front of me unfolds, I find myself pulled away from my thoughts, and instead taking interest in the somewhat silly chase."
    "They keep running around, going in circles around posts, benches, even through the shrubs. It’s quite the sight."


    "But I guess entertainment is never for free."
    "Soon enough, the cat locks eyes with me and begins barreling straight towards me, ready to smash into me like a bull with a matador in his sights."


    scene cg pomu pomusuke ver1 with fade

    Character0 "Hey you!" with sshake_s
    extend " Catch him!" with sshake_m

    scene bg park with fade
    show pomusuke at center with easeinleft
    "In sort of a daze, I grab the cat with both hands, and lift it up as it starts thrashing about."
    show pomusuke at truecenter with move
    show pomusuke at pomusuke_shake
    "Thankfully it doesn’t try to scratch me, otherwise I’d be bleeding all over my hands."

    play music audio.bgm_pomu01 fadeout 2.0 fadein 2.0
    scene bg park with sweepclock

    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    show pomusuke at pomusuke_caught zorder 50
    with dissolve
    Character0 "Huff. Thanks for helping me catch him."
    show pomusuke at pomusuke_shake
    show pomu school neutral
    "She gives a bright smile as her cat still squirms in her grip. Even after all that running and screaming, she seems fine and not out of breath at all."
    "Does she do this sort of thing everyday?"
    show pomu school happy


    Character1 "I’m Pomu by the way."
    show pomu school neutral

    Character2 "Oh, I’m [persistent.mcName]."
    show pomu school happy
    Character1 "Nice to meet you."
    show pomu school serious
    Character1 "And this silly cat is Pomusuke. I really have no idea how he managed to break his leash."


    Character2 "Seems like he’s quite the trouble maker."
    show pomu school pout at set_aligns(MIDDLE_X_SLOT)
    Character1 "Oh he is. Quite the little goblin."
    Character1 "I take my eyes off him and he does the stupidest things."

    show pomu school neutral at happy_bounce
    "I can’t help but smile as I watch her play with the cat. It feels refreshing and almost lets me forget my troubles. Almost."
    show pomu school neutral at set_aligns(MIDDLE_X_SLOT)
    show pomusuke at pomusuke_caught

    "She glances at me, and a wrinkle of worry forms on her face."


    show pomu school concerned
    Character1 "You… seem to be sweating a lot. Are you okay?"
    Character2 "Oh… I’m fine. Just a bit tired from… trying to catch Pomusuke, yeah."


    "Though I try to brush it off, my strained breathing and tired look is all too clear."
    show pomu school neutral
    Character1 "Well, you certainly seem exhausted."
    Character1 "Here, you should keep yourself hydrated."

    show pomu school happy at nodding
    "She hands me a bottle of water, and though reluctant, I decide to take it and thank her."


    show pomu school neutral
    Character1 "I should go. Still need to take this little goblin back home."


    Character2 "Sure. Thanks again for the water."

    hide pomu
    hide pomusuke
    with slowdissolve
    "And with that, she finally leaves. The further she walks away and the smaller her figure gets, I finally take notice of her clothes."


    "She was wearing my school’s uniform..."


    "School huh. I guess it’s time I get ready for school too."

    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0

    scene bg classroom back view with slidingblinds

    play sound [ "<silence 0.7>", audio.sfx_schoolbell ]
    "At School"

    play sound audio.sfx_doorslide01


    Character3 "Attention everyone! The teacher is here."


    show oliver neutral at set_aligns(MIDDLE_X_SLOT) with dissolve

    Character4 "Good Morning, class."

    Character5 "Good Morning, Professor Oliver!"

    Character4 "Before we start with the lesson, I wish to discuss things regarding club applications."


    Character4 "As you all know, our school is focused on clubs and their development, which means all students are required to at least join one club."
    Character4 "I am sure you are all aware that tomorrow is the final day to hand in your club applications."
    Character4 "However, there are still some of you who have not decided which club to join, so I am here to remind you about this."
    Character4 "I hope you can all decide by today."


    Character4 "Now that I’ve reminded you, let us now proceed to our lessons. Today’s topic is about the…"

    "Club, huh. Do I really have to?"

    scene bg none with sweepclock

    "Classes pass by like a blur. Whether I was listening or not, it really didn't matter."

    "Before I know it, it’s already lunch time."

    play sound [ "<silence 0.7>", audio.sfx_schoolbell ]

    play music audio.sfx_crowdnoise fadeout 2.0 fadein 2.0
    scene bg classroom back view with sweepright


    "I brought lunch with me today. Although, I don’t really feel like eating here in the classroom."
    "Guess I’ll go somewhere quieter."

    stop music fadeout 2.0

    Character0 "Excuse me, [persistent.mcName]. Could I talk to you for a minute?"


    play music "<loop 0.12>{}".format(audio.bgm_elira01) fadein 2.0
    scene cg elira classroom hair tuck with fade

    "I look up to find myself face to face with the class president."
    "I’m surprised for a bit, but I soon find myself staring at her eyes, or well, her eye."
    "I’ve always been curious as to why she hid her other eye behind her hair, but then again, I’m not one to pry."

    scene bg classroom back view with fade
    show elira school neutral at set_aligns(MIDDLE_X_SLOT) with dissolve
    Character2 "What is it, Class President?"
    show elira school straightface
    Character6 "Elira.{w} Call me Elira."
    show elira school sigh
    Character6 "Being called Class President feels…weird."
    show elira school straightface

    Character2 "But…you are the class president."

    show elira school sigh
    Character6 "I know, it’s just…"

    show elira school straightface
    Character2 "Oh uh, okay then…Elira."
    Character2 "So uh, did you need something?"
    show elira school neutral
    Character6 "Oh right. I just wanted to discuss with you about the club applications."
    Character6 "I need to collect those soon, and I see that you’re one of the few people who still hasn’t filled anything out yet."
    Character6 "Are you having any problems?"

    Character2 "I…haven’t decided yet."

    show elira school worried
    Character6 "I see. I know it’s quite soon, but the professor needs the forms by tomorrow so…"


    Character2 "…"
    show elira school serious
    Character6 "But don’t worry, you still have the rest of the day to decide. I can wait until after class to collect yours."


    Character2 "…Yeah… thanks."
    show elira school neutral
    Character6 "Alright."

    show elira school straightface
    "She gives me one last worried look before leaving."
    hide elira with slowdissolve
    "I really don’t want to think about these things right now. Soon, I find myself walking out of the classroom."

    play music audio.sfx_crowdnoise fadeout 2.0 fadein 2.0

    scene bg hallway day with sweepright

    "Do I really have to? Do I have to deal with such expectations again? Why?"


    "My legs move on their own, trying to find a way out of this as if I was escaping a maze, leading me to somewhere where I could have peace and quiet."
    "In the end, I find myself heading for the roof. Perhaps there, I’d be able to eat lunch in peace and gather my thoughts."

    stop music fadeout 2.0

    play sound "<silence 0.5>"
    queue sound audio.sfx_dooropen01

    scene bg school rooftop day with sweepright

    play sound audio.sfx_windstrong fadeout 2.0 fadein 2.0 loop volume 0.75

    "As I open the door, the fresh breeze hits me. I look around and see nobody in sight."
    "It’s quiet, the only sounds I can hear are the wind and the birds."


    Character2 "Finally! A place with nobody in it!!" with sshake_m

    "I shout in exclamation, letting out the feelings that are pent up inside me."

    "I just don’t want to deal with people anymore. But now, I am finally alone and able to ignore everything else."


    stop sound fadeout 2.0
    "...or so I thought."


    "Out the corner of my eye, I notice someone sitting atop the stairwell entrance."

    play music audio.bgm_finana01 fadein 3.0
    scene cg finana rooftop lunch with fade

    "I turn around and lock eyes with a green-haired girl as she eats her lunch with a silent gaze."


    "Though I am surprised at finding someone sitting at such a place, I’m more concerned about what I had just said out loud not too long ago. She definitely must have heard it."


    "After what feels like an eternity of awkward staring, she finally breaks the silence."

    scene bg school rooftop day at rooftop_zoom with fade
    show finana school worried at set_aligns(MIDDLE_X_SLOT) with dissolve
    #show finana at shiver_softer(MIDDLE_X_SLOT)
    Character0 "I-{w}I’m sorry for being in your way{w}, I’ll leave…"

    show finana school embarrassed at set_aligns(MIDDLE_X_SLOT)
    "That made me feel bad."

    "Here I was, barging in and shouting my thoughts without a care, and now I’ve not only disturbed this girl’s lunch, but even made her feel bad for being here first."


    show finana school shocked at bounce_param(LARGE_BOUNCE,0.15)
    Character2 "No no no! {nw}" with sshake_s
    extend " I should be the one apologizing."
    show finana school worried at shiver_softer(MIDDLE_X_SLOT)
    Character2 "I didn’t think anyone was here I-"
    "......"
    Character2 "Sorry,{w} that was rude of me."
    show finana school worried at set_aligns(MIDDLE_X_SLOT)
    Character2 "...I should just go."
    show finana school shocked
    hide finana with slowdissolve
    "..."
    show finana school worried at set_aligns(MIDDLE_X_SLOT) with sshake_s
    Character0 "W-{w}Wait…"

    Character2 "...yes?"
    show finana school embarrassed at fidget
    "She tried to say something, but she only looked away in embarrassment."
    "I’m confused, doesn’t she have the same plan as me? To eat alone and not be disturbed?"

    "Still in silence, I watch as she steals glances at me and my lunch."
    "It seems like she's trying to keep up a cool appearance, but the longer this goes on, the more awkward it becomes."

    "I let out a sigh."
    "Perhaps it’s sympathy I feel, maybe even empathy."
    "Whatever it is, in the end, I choose the option I never thought I’d do."

    show finana school embarrassed at set_aligns(MIDDLE_X_SLOT)
    Character2 "Hey, so uh… there wouldn’t be much time left for lunch if I had to look for another place to eat."
    Character2 "So…{w}would you mind if I ate with you here?"
    Character2 "I won’t give you trouble, promise."

    show finana school shocked at bounce_param
    "The question takes her by surprise."
    "Although she doesn't say anything, her expression is a mixture of bewilderment, confusion, and a hint of appreciation."


    "Did I make the right decision?"

    show finana school worried
    "The silence stretches on to the point that I thought of just leaving."
    show finana school worried at nodding
    "But before I could, she gives me a small nod and I breathe a sigh of relief."


    Character2 "Cool. Give me a minute to get up there then."
    hide finana with dissolve
    scene bg school rooftop day at rooftop_zoom2 with dissolve
    "I don’t know why it never occurred to me that I could just eat at another spot..."
    "..but there I was half-way up the ladder trying to sit beside her which would probably have made her even more nervous."
    "Then, I notice the lack of fences or any safety nets in that area and my arms start to buckle."

    Character2 "Y-{w=0.5}You know what?{w} I think I'll just stay down here…{w} haha…"

    show finana school worried at set_aligns(MIDDLE_X_SLOT) with dissolve
    Character0 "..."


    Character2 "I mean it's just uh…"
    Character2 "I feel like it's a bit dangerous up there."


    Character0 "...{w}I’ll come down if it’s better for you."


    Character2 "That…{w} would be better,{w} yes…{w} thanks…{w} haha…"


    "The whole point was that I was trying to make it up to her, but here I am making her have to compromise for me."
    "What am I even doing…?"

    scene bg school rooftop day with sweepclock

    show finana school neutral at set_aligns(MIDDLE_X_SLOT) with dissolve


    "She makes her way down and we find a spot to sit and eat."

    "Though we sit together side by side, there is nothing but awkward silence between us."
    "I manage to distract myself from the weird atmosphere by concentrating on eating my food, but at that point, I’m not sure what I’m doing anymore."


    Character0 "Um…{w} so what brings you here…?{w} On the rooftop…"


    "I’m surprised how she’s the one to break the ice, considering this probably isn’t what she had planned for lunch."


    Character2 "Nothing much, really."
    Character2 "I just wanted to go to a place where I could think and eat in silence."


    show finana school worried at bounce_param


    "That makes her flinch.{w} Perhaps that wasn’t the best choice of words to use."


    Character2 "No no, I didn’t mean that you were disturbing.{w=0.5} You’re not, you know….{w} ugh."
    Character2 "Let me try this again."


    Character2 "Hi, I’m [persistent.mcName], and I was looking for a quiet place to hang around for lunch."
    Character2 "I didn’t mean to disturb you here, honest. Nor are you disturbing me,{w=0.5} just to put it out there."


    show finana school neutral


    "That seemed to make her relax."


    Character7 "My name’s Finana."
    Character7 "And don’t worry, you’re not disturbing either."


    show finana school happy at bounce_param


    "She lets out a chuckle."


    Character2 "Well that’s good to hear. It’s nice to meet you."

    show finana school neutral
    "We end up making small talk as we get to know each other just a little bit."

    "To my surprise, she’s actually from the same class as me."
    "I’ve never really noticed her, or perhaps my attention was always just elsewhere."
    "That’s how it’s always been with me, anyway. I lose sight of what doesn’t concern me."


    "Before we realize it, lunch is almost over."


    show finana school neutral at bounce_param


    Character7 "I think I'll go on ahead. I'd like to get to class before the halls get…crowded."


    Character2 "Yeah, that’s a good idea. I think I'll take a detour to the bathroom before I go back."

    Character7 "Okay.{w} Oh and um,"
    show finana school happy
    extend " thanks for hanging out with me."


    Character2 "Oh, it was uh my pleasure."
    Character2 "Rather, I'm sorry about the whole barging in thing."


    show finana school neutral


    Character7 "That's alright."

    show finana school happy at bounce_param
    "She lets out a chuckle."

    show finana school neutral
    Character7 "I had fun. Thanks."

    Character2 "Yeah… me too."

    "With a wave and goodbye, we go our separate ways with smiles on our faces."
    hide finana with slowdissolve
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    scene bg hallway day with sweepright

    "Returning to the hallway after my little detour, mobs of students fill the halls as they return to their rooms."
    play sound [ audio.sfx_thud01 ]
    scene bg hallway day with sshake_m
    "I wait for the crowd to start to clear before I proceed, only to accidentally bump into someone going in the opposite direction."

    Character2 "Oh, my bad.{w} I didn’t see you there."


    "In front of me is a familiar shade of blonde that belongs to a certain cat-owner."

    show pomu school neutral at set_aligns(MIDDLE_X_SLOT) with dissolve


    Character1 "It’s fine, I wasn’t really loo-"


    show pomu school surprised at set_aligns(MIDDLE_X_SLOT)
    show pomu at bounce_param
    play music audio.bgm_pomu01 fadeout 1.0 fadein 1.0
    Character1 "Oh, it’s you from this morning!" with sshake_s

    show pomu school neutral
    Character2 "Hi, we meet again."

    Character1 "I didn’t realize you went to this school as well."
    show pomu school happy at bounce_param
    Character1 "Thanks again for helping me out with Pomusuke."

    show pomu school neutral
    Character2 "No worries. It was sort of a spur of the moment."


    Character1 "True."

    show pomu school serious
    Character1 "Wait, if you’re here,{w=0.5} that means you’re in the same class as{nw}"
    show pomu school surprised at bounce_param
    extend " me?!" with sshake_s
    Character1 "I can’t believe I’ve never noticed!"

    show pomu school concerned
    Character2 "Small world indeed."

    play sound [ audio.sfx_schoolbell ]
    "..........."
    show pomu school surprised
    Character1 "Oh no, that’s the bell! I gotta get to class!" with sshake_m

    show pomu school overjoyed
    Character1 "If we’re gonna keep meeting, we gotta stop doing it when I don’t have any time, haha!"

    hide pomu with easeoutleft
    play music audio.bgm_schooltime01 fadeout 1.0 fadein 1.0
    "And once again, she zooms away."
    "What an interesting coincidence it is indeed that she is my classmate as well.{w} Yet again, something that I had failed to notice."


    "And like that, classes just pass by like a breeze."

    stop music fadeout 2.0
    scene bg none with sweepclock
    #scene bg hallway sunset with slidingblinds
    play sound [ audio.sfx_crowdnoise ] fadein 2.0
    "The noise of the crowds of students preparing to go home fills the air."
    "Some have plans, some just want to go straight home, and some decide to stay back.{w} I’m one of the latter."

    "For the others, staying back is for responsible reasons like their club, but for me, I just don’t feel like going home yet, nor anywhere else for that matter."
    "I just want to walk around school with nothing but my thoughts to guide me."
    stop sound fadeout 1.0
    play music audio.bgm_goinghome01 fadein 2.0 volume 1.0
    scene bg track and field day with sweepright


    "Soon, I find myself standing at the outskirts of the track and field."
    "The place is filled with students training hard in multiple physical exercises, determined to prove they could be the best."
    "Seeing it all makes my chest grow tighter."
    "I shouldn’t be here watching, I shouldn’t stay, yet it feels as though my legs knew to take me here and lock themselves in place."

    play sound [ audio.sfx_whistle ]
    show pomu track serious at set_aligns(LEFT_X_SLOT)


    "My attention is caught by the blow of the whistle."
    show pomu track serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    "Before I know it, my eyes are trained to the yellow blur as it runs past."
    hide pomu
    show pomu track serious at set_aligns(MIDDLE_X_SLOT) with easeinleft
    "That same shade of blonde that I’d met this morning is speeding through the track."
    show pomu at focus_stare with dissolve
    show linesov zorder 50 with dissolve
    "The look in her eyes is nothing but determination, ready to break through with a new record."
    hide linesov with dissolve
    show pomu at unfocus_stare with dissolve
    hide pomu with easeoutright

    "...and yet,{w=0.5} it isn’t enough."
    show pomu track sad at set_aligns(LEFT_X_SLOT) with easeinleft
    pause 0.5
    show pomu track sad at set_aligns(MID_LEFT_FOUR_X_SLOT) with ease
    pause 0.5
    show pomu track sad at set_aligns(MIDDLE_X_SLOT) with ease
    "Even though the run ends in disappointment,"
    show linesov zorder 50 with dissolve
    show pomu track serious at focus_stare with dissolve
    extend " the fire of determination never leaves her eyes." with sshake_s
    hide linesov with dissolve
    show pomu at unfocus_stare with dissolve
    hide pomu with easeoutright
    "She’s ready to try again,"
    show pomu track serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu track serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again,"
    show pomu track serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu track serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again,"
    show pomu track serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu track serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again."
    hide pomu
    show pomu track serious at set_aligns(MIDDLE_X_SLOT) with easeinleft
    show pomu at panting
    "It hurts to watch her, not because of how many times she has failed, but because of how many times she chooses to keep going."
    "It stirs the old wound inside me, and I’m afraid seeing any more would make it surface again."
    "Thus, it’s time to leave."
    scene bg black with slowdissolve

    "But before I can walk away, a familiar voice calls out to me."
    scene bg track and field day


    Character6 "Wait! [persistent.mcName]!" with sshake_s


    "I turn around to find our class president huffing as she jogs towards me,{w=0.3} her hands waving back and forth as if signaling me to not move an inch from where I am."
    show elira school neutral at set_aligns(OFFSCREEN_RIGHT_OFFSET)
    show elira school worried at run_tired_elira
    "......."
    show elira school worried at set_aligns(MIDDLE_X_SLOT)
    show elira school worried at panting
    Character2 "Did you need something, Prez?"

    Character6 "I told you…{w}to call me…{w}Elira."
    show elira school sigh at set_aligns(MIDDLE_X_SLOT) with move

    "She takes a moment to catch her breath as she stops in front of me."


    show elira school serious
    Character6 "Calling me ‘Prez’ doesn’t make me any less uncomfortable."

    Character2 "Right, sorry."

    show elira school neutral
    Character6 "Anyway, I need you to come with me back to the classroom. I have some important stuff I need to discuss with you."


    Character2 "Can’t you just tell me here?"

    show elira school straightface
    Character6 "No. Someone else will be joining us in the discussion, and they’re waiting for us there."


    "Seeing as how Pre-…Elira went out of her way to look for me, I assume it's about the club applications, although I honestly wish it was something else."


    "Either way, I don’t really have a choice, so I reluctantly follow Elira back into the classroom."

    play music "<loop 12>{}".format(audio.bgm_trouble01) fadeout 3.0 fadein 3.0
    scene bg classroom back view with sweepright

    show elira school neutral at set_aligns(MIDDLE_X_SLOT)

    "Inside, Elira stands behind the teacher’s desk as she fixes the papers in her hand."
    "She wants to discuss club applications, and more specifically my lack thereof."
    "It must have slipped my mind, or maybe I subconsciously tried to forget."


    "It’s a bit troubling for me, but what I didn’t expect the most was that the supposed other person involved was none other than…"

    show elira school neutral at set_aligns(MID_LEFT_FOUR_X_SLOT) with ease
    show finana school worried at set_aligns(MID_RIGHT_FOUR_X_SLOT) with dissolve

    "...the girl I had lunch with on the rooftop, Finana.{w} What a coincidence."

    show finana at shiver_softer(MID_RIGHT_FOUR_X_SLOT)
    "She sits beside me, her hands shaking as she grips her skirt. She looks even more nervous than before."
    "To somewhat diffuse the tension, I decided to say hi."

    show finana school worried at set_aligns(MID_RIGHT_FOUR_X_SLOT) with ease
    Character2 "Hey, we meet again."

    show finana school worried at nodding
    "She turns to me and nods without making as much of a sound."
    "I guess it’s still a bit awkward between us, but that’s understandable. We’ve only just met today after all."


    show finana school happy

    "Yet when I look at her again, she gives me a cute smile."
    "Perhaps not as awkward as I thought."

    show elira school straightface at focus_sprite zorder 50
    Character6 "Alright, you two."
    show finana school worried
    Character6 "So again, as I’ve mentioned before regarding your club applications, I was going to collect those today."
    Character6 "I do hope you’ve filled them up…{w} you did fill them up, right?"

    show elira school serious at unfocus_sprite zorder 0
    Character2 "…not exactly."

    show elira school worried at focus_sprite zorder 50

    Character6 "Oh…{w} and you, Finana?"

    show finana school worried at focus_sprite zorder 50
    show elira school worried at unfocus_sprite zorder 0
    show finana school worried at shake_head(MID_RIGHT_FOUR_X_SLOT)
    "Finana could only shake her head."

    show elira school worried at focus_sprite zorder 50
    show finana school worried at unfocus_sprite zorder 0
    Character6 "…You know, you two can just join any club."
    Character6 "While it’s not preferred, you don’t even have to be active in it, just as long as you’re in one."

    show elira school neutral at bounce_param


    Character6 "That reminds me."
    Character6 "I’ve looked at your past records and it seems like you used to be part of the pole vaulting club,{w=0.3} so why not?"
    show elira school neutral at unfocus_sprite zorder 0
    "Her gaze is directed at me."
    "Though I understand it isn’t her intention, hearing those words causes strings of pain to slowly creep up my arm."


    "I couldn’t."


    "Not yet."


    "It still hurts."


    "Even if it was just in name, I couldn’t join again."


    "The weight of being a part of that… it has been too long."
    "I don’t wanna return if I can’t contribute anything."


    Character2 "I… no."
    Character2 "I can’t.{w} I won’t."


    show elira school sad


    "She looks at me worriedly. That’s when I notice the cold sweat forming around my face."


    "I wipe my forehead and try to calm down."


    Character2 "Yeah, sorry.{w} I… don’t wanna join that club."

    show elira school worried
    "It feels like she somehow understands, or maybe I just give off an aura of finality as I speak."
    show elira school sad
    "Elira turns to Finana, she asks the same kind of questions regarding the previous club or interest in other clubs,{nw}"
    show finana school worried at shake_head(MID_RIGHT_FOUR_X_SLOT,2) zorder 50
    extend" but she shakes her head to all of them."

    show finana school worried at focus_sprite
    Character7 "I… don’t really feel like I belong anywhere."

    show finana school worried at unfocus_sprite zorder 0
    show elira school sigh

    "Elira could only sigh."
    show elira school sad
    "We certainly were more trouble than she expected."
    stop music

    play sound audio.sfx_doorslide01
    show elira school shocked at bounce_param
    show finana school shocked at bounce_param
    "!" with sshake_l




    "The loud noise of the door being opened catches our attention."
    "Where our eyes turn to look, there stands Pomu by the door frame,{w=0.3} much to our surprise."
    play music audio.bgm_hectic01 fadein 0.1
    scene bg classroom back view
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    show pomu school happy at bounce_param
    Character1 "Sorry, am I disturbing you?"

    hide pomu
    show elira school straightface at set_aligns(MID_LEFT_FOUR_X_SLOT)
    show finana school worried at set_aligns(MID_RIGHT_FOUR_X_SLOT) zorder 25
    show elira school serious at focus_sprite zorder 50
    Character6 "Uh…kinda? Do you need something?"
    show elira school shocked at unfocus_sprite
    show pomu school happy at set_aligns(MIDDLE_X_SLOT) zorder 0 with easeinright
    show elira school shocked at set_aligns(LEFT_X_SLOT) zorder 50 with ease
    show finana school shocked at set_aligns(RIGHT_X_SLOT) zorder 25 with ease
    show pomu school happy at focus_sprite zorder 50
    Character1 "Well, I was on the track doing some laps and I noticed [persistent.mcName] was watching."
    show pomu school neutral
    show finana school worried
    show elira school serious
    Character1 "I figured I’d finish the lap and go say hi, but then you came by and dragged them away."
    Character1 "So right after practice, I went around looking for you and now here we are."

    show pomu school neutral at unfocus_sprite zorder 25
    Character2 "You were looking for us? Why?"

    show pomu school overjoyed at focus_sprite zorder 50
    Character1 "I just explained it!"

    show pomu school neutral at unfocus_sprite zorder 25
    Character2 "…cause you wanted to go say hi to me…?"

    show pomu school overjoyed at focus_sprite zorder 50
    Character1 "Yes! That and cause the Class President dragging you away seemed pretty suspicious..."
    show pomu school serious at set_aligns(MID_LEFT_FOUR_X_SLOT) with ease
    Character1 "Like, real sus."
    show pomu school overjoyed at set_aligns(MIDDLE_X_SLOT) with ease
    Character1 "So anyway, what are you all up to?"
    show pomu school concerned at unfocus_sprite zorder 25
    show elira school sigh at focus_sprite zorder 50
    "There is a bit of confusion, but Elira manages to explain the situation about how Finana and I don’t have clubs yet..."
    "...and how we both are against joining our previous ones or just don’t want to join any in particular."

    show elira school straightface at unfocus_sprite zorder 0

    "As she listens, Pomu’s brows begin to furrow in thought."
    show pomu school excited at bounce_param
    "Then, as if a genius idea formed in her mind, she beams a wide smile."

    show pomu school overjoyed at focus_sprite zorder 50
    stop music fadeout 0.2
    Character1 "If that’s such a problem, why not make a new club then?"

    show pomu school happy at unfocus_sprite zorder 25
    show elira school shocked at bounce_param
    show finana school shocked at bounce_param

    Character2 "…What?"



    play music "<loop 16>{}".format(audio.bgm_clubtime01) fadein 3.0

    show pomu school neutral at focus_sprite zorder 50
    show elira school shocked at unfocus_sprite zorder 0
    show finana school shocked at unfocus_sprite zorder 25
    Character1 "I mean think about it."
    show elira school serious
    show finana school worried
    Character1 "You two don’t want to join any club that’s established already, right?"
    Character1 "Why not just make a new one that fits what you want?"
    Character1 "Like a ‘Going-Home’ club or maybe a ‘Resting’ club or something like that."
    show pomu school neutral at unfocus_sprite zorder 50
    Character2 "…well you have a point, but I don’t think-"
    show pomu school excited at set_aligns(MID_RIGHT_FOUR_X_SLOT) with ease
    show finana school shocked

    "Ignoring the rest of my answer, Pomu grabs Finana’s hands and cups them with excitement."
    "She stares at the shy girl with stars in her eyes, as if anticipating nothing but a positive answer."

    show pomu school excited at bounce_param
    Character1 "You agree too, right?"

    show finana school shocked at shiver_soft(RIGHT_X_SLOT)
    "The poor girl is so nervous, her pupils are visibly shaking."
    show finana school shocked at set_aligns(RIGHT_X_SLOT)
    show finana school nervous at nodding
    "In the end she could only nod to the overwhelming presence in front of her."

    show pomu school overjoyed at set_aligns(MIDDLE_X_SLOT) with ease
    show pomu school overjoyed at focus_sprite zorder 50
    Character1 "See? Everybody’s in agreement. A great solution to your-"


    show elira school angry at focus_sprite zorder 50
    show pomu school surprised at unfocus_sprite zorder 25
    show finana school shocked at set_aligns(RIGHT_X_SLOT)


    Character6 "Wait just a second there!" with sshake_m


    "That makes Pomu freeze mid-sentence."
    show pomu at offscreen_far_right
    show finana at offscreen_far_right
    show elira school angry at set_aligns(MIDDLE_X_SLOT)
    with ease
    show elira school angry at unfocus_sprite zorder 25
    "We turn to Elira who looks just a little bit irritated, perhaps at the ridiculous conclusion this conversation has ended up with."



    Character6 "As much as it would be quite the grand solution, unfortunately, you need 4 members to start up a brand new club!"
    Character6 "Even if [persistent.mcName] and Finana try to form one,{nw}"
    extend " there’s not enough members!" with sshake_m
    show elira at set_aligns(LEFT_X_SLOT)
    show pomu school sad at set_aligns(MIDDLE_X_SLOT)
    show finana school nervous at set_aligns(RIGHT_X_SLOT)
    with ease
    stop music fadeout 0.2
    "An awkward silence fills the room."
    "Of course it wouldn’t work like that. Things are never that easy."
    "In the end, we are still back at square one."


    show pomu school excited at focus_sprite zorder 50

    play music "<loop 16>{}".format(audio.bgm_clubtime01) fadein 1.0
    Character1 "Oho, in that case, how about I join too?"
    Character1 "This school does allow being a member of multiple clubs after all."
    show pomu school overjoyed
    Character1 "We’ve got plenty of members in track who are in other clubs too, so it’s A-OK!"

    show pomu school neutral at unfocus_sprite
    Character2 "Wouldn’t that affect your practice?"

    show pomu school overjoyed at focus_sprite

    Character1 "No worries, I can still practice while popping in from time to time in the new club, right?"
    show pomu school neutral
    Character1 "And it’s not like you guys will actually be doing stuff…"
    show pomu school concerned
    extend " will you?"

    show pomu school neutral at unfocus_sprite zorder 25
    Character2 "…fair enough."

    show elira school serious at focus_sprite zorder 50

    Character6 "Okay okay, that’s good and all, but you’re still short by one member."
    show pomu school concerned
    stop music fadeout 2.0

    show elira school serious at unfocus_sprite zorder 0
    "Another wave of silence."
    "It’s unfortunate, but we can’t do anything about it."
    "The three of us just isn’t enough..."
    "Too bad, I didn’t dislike the atmosphere our little group had…"
    "..."

    "Wait…{w}we do have enough…"

    show pomu at offscreen_far_right
    show finana at offscreen_far_right
    show elira at set_aligns(MIDDLE_X_SLOT)
    with ease
    "I turn towards the figure in front of us. The very one that started this whole conversation."


    Character2 "What about you, Prez?"


    show elira school shocked at bounce_param

    "She seems taken aback by the question."
    "It’s quite an interesting reaction."
    "If my intuition is right, we don’t need to find anyone else."

    Character6 "Wh-{w}What do you mean…?"

    Character2 "Hm…what was your club again, Prez?"

    play music audio.bgm_hectic01 fadein 3.0

    show elira school worried at shiver_softer(MIDDLE_X_SLOT)
    Character6 "Uhh… I…uhh I told you to call me ‘Elira’!"


    Character2 "Pre- Elira, you’re not answering the question."

    Character6 "I-{w} don’t…"


    Character2 "You don’t…?"




    "As if a maiden in distress, she slowly falls to her knees."
    show elira school worried at on_knees with ease
    Character6 "I…don’t have a club…"
    show elira school sad

    "Bingo.{w} We have our fourth member."

    #show elira at set_aligns(LEFT_X_SLOT)
    show finana school angry at set_aligns(RIGHT_X_SLOT)
    with ease
    show elira school shocked
    Character7 "Wait! You didn’t have a club all this time?!" with sshake_m
    show finana school angry at set_aligns(MID_RIGHT_FOUR_X_SLOT)
    show elira school shocked at set_middle_left_four_slot(750)
    with ease
    Character7 "And you kept pestering us about it?!?!?!" with sshake_l

    show pomu school surprised at set_aligns(RIGHT_X_SLOT) zorder 0 with ease


    "The sudden and loud outburst from the normally quiet Finana shocks everyone."
    show elira school sad at shiver_softer(MID_LEFT_FOUR_X_SLOT)

    "Elira could only cover her face in embarrassment."

    show elira school worried at set_middle_left_four_slot(750)
    Character6 "I’m sorry! I just wanted to know what the other club-less students would join, and make a decision after! Maybe even join one of the clubs you would join in. I’m sorry!"

    "Finana could only pout at her. It seems almost like a betrayal."
    show pomu school concerned at set_aligns(MIDDLE_X_SLOT)
    show elira at offscreen_far_left
    show finana at offscreen_far_left
    with ease

    "From the corner of my eye, Pomu has her brows furrowed again in deep thought. Then, as if coming to a conclusion, she turns to Elira and smiles."
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)

    Character1 "You know, for a Class President, you’re not very sociable, huh?"

    hide pomu
    play sound [ "<silence 0.1>", audio.sfx_knifeslash ]
    show elira school worried at set_aligns(MIDDLE_X_SLOT)
    show elira at bounce_param

    Character6 "Ugh…"with sshake_m
    show elira school sad at on_knees with ease
    "Oof. That’s a critical hit."
    hide elira
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    Character1 "In fact, not only the Class President, but everyone in this room here, aside from me, isn’t exactly sociable either. You guys need to touch grass more often."


    hide pomu
    play sound [ "<silence 0.1>", audio.sfx_knifeslash ]
    play voice [ "<silence 0.3>", audio.sfx_knifeslash ]
    show finana school shocked at set_aligns(MIDDLE_X_SLOT)
    show finana school shocked at bounce_param
    Character7 "Ugh…" with sshake_m
    play sound [ "<silence 0.3>", audio.sfx_thud01 ]
    show finana school embarrassed at on_knees with ease
    "Oof."
    show elira school sad at set_left_slot (750)
    show finana school embarrassed at set_right_slot (750)
    show pomu school happy at set_mid_slot
    with dissolve
    "I didn’t expect her words to have an area-of-effect and hit me as well."
    "In the end, we all got called out."

    play music audio.bgm_lazulight01 fadeout 2.0 fadein 5.0
    scene bg black with sweepclock
    scene bg river sunset with sweepright


    show elira school sigh at set_aligns(LEFT_X_SLOT) zorder 50 with dissolve

    Character6 "How did I end up in this situation?"

    show elira school straightface
    "After all the discussions, the four of us ended up deciding to form a new club."
    "Although we came to that conclusion, we still have to iron out the details of how this new club will operate."


    "Before heading home for the day, we decided to stop by the riverside."

    show pomu school happy at set_aligns(MIDDLE_X_SLOT) zorder 0 with easeinleft
    show pomu school overjoyed at focus_sprite zorder 25
    Character1 "So, as I was saying, since you guys don’t really socialize that much, we could just make a ‘Friendship club’!"
    Character1 "Our goal can be helping students work on socialization and interaction with others, of course, starting with our very own members!"

    show pomu school neutral
    Character1 "What do you all think?"

    show pomu at unfocus_sprite zorder 0
    Character2 "I guess.{w} Although I don’t really like the idea of socializing."

    show pomu school overjoyed at focus_sprite zorder 25
    Character1 "You’ll get used to it! Right, Elira?"

    show pomu at unfocus_sprite zorder 0
    show elira school worried at focus_sprite zorder 25

    Character6 "I-I guess…?"

    show elira at unfocus_sprite zorder 0
    show pomu school pout at focus_sprite zorder 25

    Character1 "…you two are hopeless."
    show elira school sad
    "She shakes her head in dismay."

    show pomu at unfocus_sprite zorder 0
    Character2 "So, what are we naming the club?"

    show pomu school concerned
    show elira school worried
    "The three of us start to ponder."
    "As I let my gaze wander around while I think of a name, I notice Finana picking up rocks by the riverbed."

    scene bg river sunset at river_zoom with sweepright
    show finana school happy at set_aligns(RIGHT_X_SLOT)


    "She picks up a small, blue gem-like rock, reminiscent of a dark sapphire crystal, and holds it up towards the sky."

    show finana school neutral
    Character7 "Lazulite…"

    show pomu school concerned at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show elira school worried at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)

    "She murmurs the word as if in a trance, perhaps enticed by the light the stone reflects from the sun."
    scene bg river sunset with sweepleft
    Character2 "How about…{w}‘Lazulite’?"

    #show finana at offscreen_far_right
    show pomu school concerned at set_aligns(MIDDLE_X_SLOT)
    show elira school serious at set_aligns(LEFT_X_SLOT)
    with easeinleft

    "The two turn towards me looking a bit confused."

    show elira school worried at focus_sprite zorder 50
    Character6 "How did you get that name?"

    scene bg river sunset at river_zoom
    show finana school happy at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "I point towards Finana, still examining the stone in her hand."
    scene bg river sunset
    show elira school serious at set_aligns(LEFT_X_SLOT)
    show pomu school concerned at set_aligns(MIDDLE_X_SLOT)
    with dissolve
    show elira school neutral at focus_sprite zorder 50
    Character6 "Oh. I don’t think that’s actually Lazulite."
    Character6 "Lazulite forms by high grade metamorphism of high silica quartz rich rocks and in pegmatites. It usually forms in-"

    show pomu school serious at focus_sprite zorder 50
    show elira school straightface at unfocus_sprite zorder 25

    Character1 "We don’t need to know all that."

    show pomu school excited
    Character1 "But…I do like the name!"
    show pomu at unfocus_sprite zorder 25
    show pomu at happy_bounce
    "She pulls out her phone from her pocket and starts typing down."

    show pomu at set_aligns(MIDDLE_X_SLOT)
    "After a couple of taps, she shows the screen over to us. On it was the word ‘LAZULIGHT’."

    show pomu school neutral at unfocus_sprite zorder 25
    Character2 "It’s spelled ‘Lazulite’,{w=0.3} lite being L-{w=0.5}I-{w=0.5}T-{w=0.5}E."
    show pomu school flustered at focus_sprite zorder 50

    Character1 "Who cares!{w=0.5} It’s cuter this way!" with sshake_s
    show elira school sigh
    show pomu at offscreen_far_right with ease
    "Trying to hide her embarrassment, Pomu heads to Finana and starts talking to her about the club name."

    scene bg river sunset at river_zoom
    show finana school happy at set_aligns(MIDDLE_X_SLOT) zorder 50
    with dissolve
    show pomu school overjoyed at set_aligns(LEFT_X_SLOT) zorder 25
    show elira school neutral at set_aligns(RIGHT_X_SLOT)  zorder 25
    with easeinleft
    "As we all gather around Finana and the stone, a sort of warm feeling starts to surface somewhere deep inside me."
    "It feels familiar, yet also fleeting."
    "But… that’s what makes it feel special."

    scene cg lazulight by the river with fade


    Character6 "Lazulight, huh?"


    Character1 "Sounds pretty good, don’t you think?"


    Character7 "Is it really not Lazulite? I thought it was cause it’s blue and-"


    Character2 "No, it probably isn’t."


    Character2 "But I guess to us…it is now."

    "And so, Lazulight was created."

    stop music fadeout 3.0

    scene bg black with fade
    menu:
        "Play opening? (Opens YouTube in a new browser tab)"
        "Yes":
            $ renpy.run(OpenURL("https://youtu.be/jsJJPGwZpn0"))
            show text "{color=#fff}Click to continue{/color}"
            pause
        "No":
            pass

    scene bg clubroom day with slidingblind
    play music "<loop 16>{}".format(audio.bgm_clubtime01) fadein 3.0

    "Who knew things would proceed so smoothly after that."
    "Before I knew it, there I was inside the newly assigned club room, sitting around with the girls I had just gotten to know."


    "We became ‘Lazulight’, the friendship club, and the first item on our agenda was deciding our very first club activity."


    "Honestly, I’m still not sure how or even why the teachers approved of such a whimsically made club."
    "One of the great mysteries, I suppose."
    show pomu school neutral at set_aligns(MIDDLE_X_SLOT)
    show pomu at bounce_param


    Character1 "Alright, before we start with the discussions, how about we all introduce ourselves?"
    Character1 "We only really know each other’s first names, so I thought we could do a little introduction to get to know each other."
    show pomu at focus_sprite
    "She stands up and pulls our attention towards her."


    Character1 "Alright. I’ll start."
    show pomu school overjoyed at set_aligns(MIDDLE_X_SLOT)


    Character1 "Hello everyone! My name is Pomu Rainpuff."
    Character1 "I know we just kind of made this club up on the spot, but I look forward to having fun and getting to know everyone!"

    show pomu school neutral
    Character1 "That’s all."
    show pomu at unfocus_sprite

    "There is a brief silence, then awkward applause."

    show pomu school overjoyed
    Character1 "Thank you."
    show pomu school neutral
    Character1 "Alright, Miss Class President. Your turn."

    hide pomu with easeoutright
    show elira school straightface at set_aligns(MIDDLE_X_SLOT) with easeinleft
    "She points to the unsuspecting Elira."
    show elira school sigh
    "The poor girl is taken aback, not expecting she’d be the one to go next."


    show elira school serious at focus_sprite


    "She stands up and starts to introduce herself, taking cues from Pomu’s lead."

    show elira school worried
    Character6 "Um, heeeeeeyyy."
    Character6 "I’m Elira Pendora, and uh… seeing as how we’ll be spending time together at the club, I hope you’ll take good care of me."
    show elira school serious
    Character6 "Also, please call me Elira.{w} I’d prefer you call me that over Class President or Prez."
    show pomu school happy at set_aligns(RIGHT_X_SLOT) with easeinright
    Character1 "Great!"
    show pomu at happy_bounce
    "Pomu starts clapping and the rest of us follow."
    show pomu at set_aligns(RIGHT_X_SLOT)
    show elira school neutral at unfocus_sprite
    "Elira sits back down with a subtle smile, finally able to relax."


    Character1 "Next is… Finana!"

    hide elira
    hide pomu
    with easeoutleft
    show finana school nervous at set_aligns(MIDDLE_X_SLOT) with easeinright


    "Our eyes turn towards her, and all she can do is shake her head."
    show finana at shiver_softer(MIDDLE_X_SLOT)
    "I’m almost scared it would fly off with how intensely she’s shaking it."


    Character1 "Go on, Finana. You can do it!"

    show finana at set_aligns(MIDDLE_X_SLOT)
    "The shy girl thinks for a while, then finally decides to stand."
    show finana at focus_sprite
    "Her gaze is low, almost towards the ground."
    "Her hands lock together as if trying to stop each other from shaking in nervousness."


    "Then, a hint of courage."

    show finana school neutral
    Character7 "M-my name is Finana Ryugu…{w} I…{w} I’m not very good at dealing with people…{w} but I’ll try to get along with everyone…"


    "Though not really planned, we let out a collective \"Ohhh\" followed by applause."

    show pomu school happy at set_aligns(LEFT_X_SLOT) with easeinleft

    Character1 "Okay! You can sit down now, Finana."
    show finana at unfocus_sprite

    Character1 "Now we go to the last but not the least. Your turn."
    show finana at set_aligns(RIGHT_X_SLOT)
    show pomu school neutral at set_aligns(MIDDLE_X_SLOT)
    with ease
    show elira school neutral at set_aligns(LEFT_X_SLOT) with easeinleft



    "Their gazes all turn towards me."
    "I’ll admit, it gives me jitters."


    "I stand up and clear my throat, ready to bust out my non-existent social skills."

    Character2 "So uh, my name is [persistent.mcName]."
    Character2 "And uh, I’m still not sure how I ended up here, but I guess uh thanks for the new club?{w} And uh nice to meet all of you."


    "There is applause and a quiet ‘nice to meet you too’. Though, I’m not entirely sure who said it."

    scene bg clubroom day with sweepright
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    show elira school neutral at set_aligns(LEFT_X_SLOT)
    show finana school neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    show pomu school overjoyed at focus_sprite zorder 50
    Character1 "Alright! Now that introductions are out of the way, let’s discuss our club’s first activity!"
    show pomu school neutral
    Character1 "As you all know, we’re a ‘Friendship Club’, so try to think of activities that are in line with ‘Interacting and Socializing’."
    Character1 "We’re gonna need to do these kinds of stuff to be able to get our hands on some budget, after all."
    show pomu school overjoyed
    Character1 "So, any ideas?"

    show pomu school neutral at unfocus_sprite zorder 25
    show finana school nervous
    show elira school straightface
    "There’s silence."
    "Hardly surprising, no one is really into the idea of socializing and interacting."
    "Well, no one except Pomu, I guess."

    show pomu school serious at focus_sprite zorder 50
    Character1 "Hmm. No one?"
    show pomu school neutral
    Character1 "Alright, if you guys aren’t suggesting anything, then I will."

    show pomu school serious
    Character1 "How about….{w} ooh yes."
    show pomu school neutral
    Character1 "When it comes to bonding, it’s gotta be…"
    show pomu school overjoyed
    show finana school worried at bounce_param
    show elira school worried at bounce_param
    Character1 "CAMPING!" with sshake_m

    show pomu school serious at unfocus_sprite zorder 25
    "..."
    show elira school straightface
    show finana school worried at shiver_softer(RIGHT_X_SLOT)
    "Finana and I groan together, in perfect synchronization against our common enemy:{w} touching grass."
    show finana at set_aligns(RIGHT_X_SLOT)
    show pomu school serious at focus_sprite zorder 50
    Character1 "Oh come on, you two."

    show pomu school serious at unfocus_sprite zorder 25
    show elira school worried at focus_sprite zorder 50


    Character6 "Although camping sounds like a great idea, it’d be hard to plan as a first activity, since there’d be a lot of things to prepare, like waivers, tools, location, and a lot of other stuff."

    show pomu school concerned
    Character6 "Plus, since we don’t really have any budget, most of the things we’d need to buy would come from our pockets, which isn’t exactly ideal."
    show pomu school sad
    show elira school sad
    "Pomu looks gloomier and gloomier as Elira explains more and more. She must have really wanted to camp."

    "There are a lot of back-and-forths, suggestions, and rejections of silly ideas, but in the end, we can’t decide on anything."
    "So we opt to instead ask other clubs for help."

    scene bg kitchen with sweepright

    "After a couple of unsuccessful visits to a few other clubs, we soon find ourselves in the school’s home economics classroom where the Cooking Club resides."

    Character0 "Well hello. Need something?"


    "The Cooking Club’s president, Emma, comes up to greet us."
    "Upon explaining our current predicament, she nods as if she has already found a solution to our problems."


    Character8 "I see. Well currently, the cooking club has a planned activity for tomorrow. We will be cooking and serving food for charity by the school’s entrance."
    Character8 "You could participate in it if you want, we’d definitely appreciate extra help."
    Character8 "You’ll also be interacting with a lot of people, so it’s perfect, right?"


    "She’s good. The proposition isn’t bad at all, we’d be able to accomplish our clubs’ aim, while she gets help for her club, how clever."

    show elira school neutral at set_aligns(LEFT_X_SLOT)
    show pomu school neutral at set_aligns(MIDDLE_X_SLOT)
    show finana school neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    show pomu school concerned at focus_sprite zorder 50
    Character1 "What do you guys think?"

    show pomu school concerned at unfocus_sprite zorder 25
    show elira school sigh at focus_sprite zorder 50
    Character6 "Hm. Seeing as how we can’t really decide on anything, it might be best to accept the proposal."

    show elira school straightface at unfocus_sprite zorder 25
    Character2 "I’m okay with it, I guess."
    Character2 "On the plus side, we won't need to prepare too much since the cooking club will take care of most of the preparations for us. We just need to help out."
    show finana school worried at focus_sprite zorder 50
    Character7 "I’m… fine with helping out… {w}but interacting…"
    show finana at unfocus_sprite zorder 25
    show pomu school overjoyed at focus_sprite zorder 50
    Character1 "It’s gonna be good practice, Finana! We’ll be there if you need back-up so you won’t have to worry."
    show pomu school neutral at unfocus_sprite zorder 25
    show finana at focus_sprite zorder 50
    Character7 "Oh…{w} okay."
    show finana at unfocus_sprite zorder 25
    hide pomu
    hide finana
    hide elira
    with dissolve
    Character8 "All aboard? Great!"


    Character8 "Oh right, I need to ask."
    Character8 "How confident are you in your cooking skills?"

    stop music fadeout 4.0
    show elira school murderous at set_aligns(LEFT_X_SLOT)
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    show finana school nervous at set_aligns(RIGHT_X_SLOT)
    with dissolve


    "There's an all too familiar silence."
    "I turn towards the girls, but their gazes are all so far away."
    "You’ve gotta be kidding me."


    Character2 "…do any of you know how to cook, at least…?"


    "The floor, the ceiling, the wall, they’re looking everywhere except at me.{w} Oh no."


    play music audio.bgm_hectic01 fadein 3.0

    Character2 "…you can’t be serious, right…?"
    hide pomu
    hide finana
    hide elira
    with dissolve
    Character2 "…"

    Character2 "Emma, unfortunately… {w}I’m probably the only one."


    Character8 "Eh, well, good enough."
    Character8 "They can just help out with other things, while I’ll be counting on you to help with the cooking!"


    Character8 "Alright, see you guys tomorrow morning by the entrance!"

    "With that, Emma goes back to helping her clubmates prepare."
    show elira school murderous at set_aligns(LEFT_X_SLOT)
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)
    show finana school nervous at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "I turn to the girls, all of them still having that far away gaze."
    "I snap my fingers as if to pull their consciousness back into this plane of existence."


    Character2 "Really? {w}None of you can cook?"

    show pomu school pout at focus_sprite zorder 50

    Character1 "Hey! I can cook, okay?!{w} I’m just…{w=0.3} not confident in serving it to others."
    show pomu at unfocus_sprite zorder 25

    Character2 "That’s… surprising."

    show pomu school concerned at focus_sprite zorder 50


    Character1 "Even I have things I’m not confident in, okay?"
    show pomu school sad at unfocus_sprite zorder 25
    Character2 "Okay okay. And you two?"


    "I turn to the other two who are still silent."
    show elira school murderous at focus_sprite zorder 50


    Character6 "I can bake but… that's about it."
    show elira at unfocus_sprite zorder 25
    Character2 "…"

    Character2 "And you… Finana…?"
    show finana school worried at focus_sprite zorder 50


    Character7 "I-I can..!{w} I can…make…"
    show finana school embarrassed
    extend " spicy noodles."
    show finana at unfocus_sprite zorder 25

    Character2 "Oh…{w} uh,{w=0.5} I don’t think… we can serve that."

    "I could only shake my head in dismay."

    Character2 "I hope we’ll be okay tomorrow…"

    #
    call loading_movie_transition_block

    scene bg school courtyard with slidingblinds
    play sound audio.sfx_crowdnoise loop fadein 2.0


    "Early morning the next day, the cooking club set up stalls at the school entrance, giving out food to the people lining up."
    "It's surprising how many people have shown up."


    stop sound fadeout 2.0
    play music audio.bgm_lazulight01 fadein 3.0


    "I’ve been helping out in the cooking process. It isn’t too difficult, but we still need to take breaks, of course."

    "After a while, I pass off my work to the student taking over."
    "I take a seat at a nearby empty bench. In front of me are crowds of people enjoying their meals and having fun."
    "I don’t think I’ve ever seen a sight like this, it feels heart-warming knowing I’ve helped in creating such an atmosphere."

    "I scan the crowd, looking around for my clubmates."


    show finana school happy at set_aligns(RIGHT_X_SLOT) with dissolve


    "By the stalls, I find Finana serving food with a shy smile."
    "Though still avoiding eye contact at times, she’s doing her best to make the people feel welcomed."
    "Despite all that she’s said, she’s doing a pretty good job of interacting with people."
    "That makes me smile a little."
    scene bg school courtyard with dissolve
    show pomu school happy at set_aligns(LEFT_X_SLOT) with dissolve

    "To the far left is Pomu assisting an elderly woman to a bench as she serves her a warm bowl of soup."
    "I can see the genuine smiles on their faces, almost like they're family hanging out together."
    "That makes me smile a little."

    scene bg school courtyard with dissolve
    show elira school giggle at set_aligns(MIDDLE_X_SLOT) with dissolve

    "Amongst the crowds, surrounded by little kids is Elira, playing around with them like an older sister with her younger siblings."
    "She’s wearing such a gentle expression as she speaks to them, and the kids’ faces are lit up like the sky."
    "That makes me smile a little."

    scene bg school courtyard with dissolve

    "Though we have only really known each other for a little while, I can see their kindness."
    "I don’t know why fate brought us together, but I at least wouldn’t mind being with them a little more."

    "Soon, the activity ends and it’s time for everyone to clean up."
    "Emma approached me to thank us for our help, saying it was a great success with our help."


    Character2 "I think it’s because everyone did their job well and not just us."


    Character8 "Oh just take the compliment."


    Character2 "…okay."


    Character8 "Anyway, I should go help out in cleaning up. I’ll see you in a bit."


    "I look around to see where I could probably help."
    "From afar, I spot my club mates all doing different tasks."


    menu choice0:
        "Help Pomu":
            jump help_pomu
        "Help Elira":
            jump help_elira
        "Help Finana":
            jump help_finana

label help_pomu:

    show pomu school neutral at set_aligns(MIDDLE_X_SLOT) with dissolve

    "I catch up to Pomu trying to carry one of the large pots we used for cooking the soup."
    show pomu school happy
    "They seem quite heavy, so I grab one side of it and we carry it together. She seems to appreciate that."
    show pomu school neutral at set_aligns(MIDDLE_X_SLOT)
    "We’re silent as we walk, not really because it’s awkward, but perhaps we’re just a little tired."

    show pomu school overjoyed
    Character1 "So, how’d you find the activity?"
    Character1 "Think it was good enough for our first one as a club?"
    show pomu school neutral
    Character2 "Hm. I think it was okay.{w} We managed to help out."
    Character2 "Oh, and Emma says thanks."
    show pomu school overjoyed


    Character1 "Great! I had a lot of fun too."

    show pomu school happy
    "She has that brilliant smile on her face again."


    Character2 "I saw you helping out an old lady.{w} You seemed to be hitting it off."

    show pomu school concerned at bounce_param
    Character1 "Oh you saw that?"
    Character1 "Well, I guess we did."

    show pomu school neutral
    Character1 "She reminds me of my own grandma."
    show pomu school happy at set_aligns(MIDDLE_X_SLOT)


    Character1 "…"
    show pomu school serious
    Character1 "Okay, maybe not."
    Character1 "She was too kind.{w} My grandma’s insane."


    Character2 "Uh…"

    show pomu school flustered
    Character1 "…nevermind."

    "We continue walking in silence."


    jump continuation

label help_elira:

    show elira school neutral at set_aligns(MIDDLE_X_SLOT) with dissolve

    "Elira is wiping down the tables we used, making sure they’re clean before folding them up and putting them away."
    "I grab a rag of my own and start wiping the tables along with her."

    show elira school smile

    Character6 "Thanks for the help."

    Character2 "All good."
    show elira school neutral
    Character6 "That was kinda crazy huh?"


    Character2 "You mean the activity?"
    show elira school loudlaugh
    Character6 "Yeah! There were so many people who came. I wasn’t expecting it to be that many!"
    show elira school neutral
    Character2 "True.{w} There was way more than I expected."


    Character2 "You seemed to be having fun though."

    show elira school neutral


    Character6 "I did?"


    Character2 "Yeah, when you were playing around with the kids.{w} You looked like a real reliable older sister."
    show elira school worried
    Character6 "Oh…that I-"

    show elira school blushing
    "She thinks for a moment."

    show elira school sigh
    Character6 "I guess so.{w} Older sister does seem fitting."

    "I wonder what she means by that."


    "We finished cleaning up and went on to bring the tables to storage."

    jump continuation

label help_finana:

    show finana school neutral at set_aligns(RIGHT_X_SLOT) with dissolve

    "From the corner of my eye I see Finana picking up trash with tongs and tossing them into the black bag in her other hand."
    "She’s a bit further away from the rest of the students doing the same job."

    show finana school neutral at set_aligns(MIDDLE_X_SLOT) with fade
    Character2 "Hey. Mind if I join you?"
    show finana school shocked at set_aligns(MIDDLE_X_SLOT)


    "She’s taken by surprise, perhaps not expecting someone would ever approach her." with sshake_s
    show finana school worried
    "I show her my tongs and bag to explain I’m here to help her clean up,"
    show finana school worried at nodding
    extend" to which she nods."

    Character2 "So, what did you think of the activity?"

    "Though I don’t usually start conversations, I‘m curious of what she thinks of the whole thing…{w} or maybe I’m just seeking opinions from someone in the same boat."

    show finana school neutral

    Character7 "I think…{w} it was okay…"


    "I have the same thought as her. It was ‘okay’."
    "I guess it’s really just like that for people who don’t really socialize. But I couldn’t just leave it at that."


    Character2 "You did really well, Finana."
    Character2 "You were smiling a lot, and I think they liked that."

    show finana school shocked

    Character7 "Wh-"
    extend "What?!" with sshake_s

    show finana school worried at shiver_softer(MIDDLE_X_SLOT)

    Character7 "There’s no way that’s true…"

    show finana school nervous at set_aligns(MIDDLE_X_SLOT)
    Character7 "I just… {w}thought I should smile to be polite."


    Character2 "And you have a wonderful smile."
    show finana school shocked at bounce_param
    "This gets her flustered, trying to hide her face with the tongs in her hand. It’s kinda cute."

    show finana school worried
    Character7 "I-{w}I’ll go throw these in the trash can."

    hide finana with slowdissolve
    "With that, she turns and starts to jog away. I couldn’t help but smile."


    Character2 "Hey, wait up, Finana! I’m coming too!"

    "I ran after her and we ended up throwing away the trash in silence."


    jump continuation

label continuation:
    call loading_movie_transition_block
    scene bg clubroom day with slidingblinds
    play music "<loop 16>{}".format(audio.bgm_clubtime01) fadein 3.0

    "A few weeks have passed since then."
    "With how well things went in helping out the cooking club, the other clubs have been asking us for help as well."
    "We’ve been going around fulfilling requests and extending helping hands, and before we knew it, Lazulight has somehow become the club that helps other clubs."
    show pomu school happy at set_aligns(LEFT_X_SLOT) zorder 25
    show finana school happy at set_aligns(RIGHT_X_SLOT) zorder 25
    with dissolve
    "One afternoon, Finana, Pomu, and I are hanging out in the club room like usual,"
    extend " when all of a sudden,{nw}"
    play sound audio.sfx_thud01
    show pomu school surprised
    show finana school shocked
    extend " the door bursts open." with sshake_m

    show elira school smile at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) zorder 0
    show elira school smile at elira_skipping_to_mid
    "It’s Elira, practically skipping in as if she’d won the lottery."
    show pomu school concerned at focus_sprite zorder 50
    show elira school neutral at set_aligns(MIDDLE_X_SLOT)
    show finana school worried
    Character1 "What’s up, Elira?"
    show pomu at unfocus_sprite zorder 25
    "Without losing the smile on her face, she pulls out a piece of paper and dangles it in front of our faces."
    show finana school confused at set_aligns(MID_RIGHT_FOUR_X_SLOT) with ease
    show finana school confused at set_aligns(RIGHT_X_SLOT) with ease
    "Finana takes a closer look and reads the contents aloud."



    show finana at focus_sprite zorder 50
    show finana school shocked
    Character7 "‘Budget for Lazulight Friendship Club’...?!" with sshake_s

    Character7 "Woah, is that real?!"
    show finana school confused at unfocus_sprite zorder 25
    show elira school loudlaugh at focus_sprite zorder 50

    Character6 "Thaaaaat’s right! We finally have a budget!"

    show elira school neutral at unfocus_sprite zorder 25
    Character2 "Hmmm..."
    Character2 "‘In light of all the times the club has helped other clubs in their activities the school has provided a minimal budget for their future activities..."
    Character2 "...provided they submit a report on the breakdown of expenses.’"
    Character2 "Ugh reports… "
    Character2 "Well at least we have money now."
    show elira school loudlaugh at focus_sprite zorder 50
    Character6 "You know what that means, Pomu!"
    show elira school neutral at unfocus_sprite zorder 25
    show pomu school excited at focus_sprite zorder 50

    Character1 "We can finally go camping!!!"
    show pomu at happy_bounce
    Character1 "WOOHOO!!!"
    show elira school loudlaugh at happy_bounce
    show finana school nervous at shiver_softer(RIGHT_X_SLOT)
    "The loud cheers of Pomu and Elira are followed by the exasperated groans of me and Finana."
    show finana school nervous at set_aligns(RIGHT_X_SLOT) with ease
    show elira school neutral at set_aligns(MIDDLE_X_SLOT) with ease
    show pomu school pout at set_aligns(LEFT_X_SLOT) with ease

    show pomu at focus_sprite zorder 50
    Character1 "Oh come on, you two! We’ve talked about this before."
    show pomu at unfocus_sprite zorder 25
    show finana school worried at nodding
    "Finana and I turn to look at each other and come to a silent agreement."


    Character2 "Alright alright, I’ll agree. Just because I know how much you want this, Pomu."

    show pomu school excited

    "If there’s one thing I’ve learned about Pomu it’s that it’s hard to make her back down when it comes to these types of things, especially if it’s something she really wanted."
    "Might as well get it over and done with, I say."
    show pomu school neutral
    show finana school happy at focus_sprite zorder 50


    Character7 "Since it’s with you guys, then I’m okay with it too."
    show finana school worried
    Character7 "Just…{w}don’t go overboard."
    show finana school neutral at unfocus_sprite zorder 25

    Character2 "Agreed."
    Character2 "And I think it would be a nice change of pace from having to help more clubs."

    "Soon after, the clubroom erupts with lots of discussions about camp and everything camp related."
    "Everyone is excited in their own way, trying to think of a good place, and what stuff to bring."


    show finana school worried at focus_sprite zorder 50

    Character7 "Oh, I just realized…{w} I don’t really have stuff for camping."
    show finana at unfocus_sprite zorder 25
    show elira school loudlaugh at focus_sprite zorder 50

    Character6 "I gotchu guuurl."

    show elira school neutral
    Character6 "How about we go shopping for camping supplies this weekend?"

    Character6 "Then, we can set our camping trip for next weekend."
    Character6 "We still need to find a place and prepare, after all."
    show finana school neutral
    Character6 "I think a week is long enough.{w} What do you guys think?"
    show elira at unfocus_sprite zorder 25
    show pomu school excited at focus_sprite zorder 50

    Character1 "I think that’s perfect!"
    show pomu at bounce_param
    Character1 "Oooh, shopping with everyone. Can’t wait!"
    show pomu at unfocus_sprite zorder 25
    "They’re all raring to go with the idea."
    "As for me… well, I thought if I kept quiet and didn’t move, no one would notice and I’d be free."
    show pomu school concerned
    "But alas, Pomu’s gaze shoots straight towards me."
    show pomu school pout at pomu_zoom_face


    Character1 "You ARE coming,{w} right?"

    Character2 "Yes ma’am."
    show pomu school happy at pomu_unzoom
    "........"
    "Figures."

    call loading_movie_transition_block

    scene bg school courtyard with slidingblinds
    play music audio.bgm_morning01 fadein 3.0


    "It’s the weekend."


    "We all promised to meet at the school’s gate since it seemed like the best place for us to converge."
    "I decided to come a little bit early, around 20 minutes before the designated time. That way I can chill for a while before the rest arrive and we leave."

    show elira casual serious at set_aligns(MIDDLE_X_SLOT) with dissolve


    "As I near the school, I notice Elira standing by the gate, quietly reading a book."
    "She seems quite engrossed with it, seeing as how she still hasn’t noticed me."


    "Even on weekends, she reads huh?"
    "As diligent as ever.{w=0.3} Just what you’d expect from the Class President."


    "..."


    "Wait a minute…{w} that book’s title…"
    "‘Larry Potter’…? A fantasy novel?"

    "Hm, interesting."

    Character2 "Hey, Elira."


    "I wave at her just as she lifts her gaze from the book."

    show elira casual loudlaugh at set_aligns(MIDDLE_X_SLOT)


    Character6 "Oh, heyyyyyy~"
    show elira casual neutral
    "She waves back playfully."

    Character2 "Well aren’t you quite the early bird, Elira."

    show elira casual sigh at set_aligns(MIDDLE_X_SLOT)


    Character6 "Oh it’s nothing like that."
    show elira casual straightface
    Character6 "I just don’t trust myself when it comes to appointments, so I just set my alarms earlier instead."
    show elira casual neutral
    Character2 "Huh. I guess that’s one way to work around it."
    Character2 "Well you do you, Elira."

    show elira casual smile

    "She gives me a warm smile."

    show elira casual neutral
    Character6 "You’ve finally gotten used to calling me Elira, huh?"

    Character2 "Oh… yeah, I guess so."

    show elira casual smile
    Character6 "I’m glad.{w=0.5} That makes me feel like we've gotten closer."
    show elira casual neutral
    "Before I could ask what she means by that, a loud voice cuts me off along with my train of thought."

    show pomu casual overjoyed at set_aligns(LEFT_X_SLOT) with easeinleft
    show pomu at focus_sprite zorder 50
    Character1 "Elira! [persistent.mcName]! Hey you two!" with sshake_s
    show pomu casual neutral at unfocus_sprite zorder 25
    show elira casual neutral at focus_sprite zorder 50
    Character6 "Well if it isn’t saucy Pomu."
    show elira at unfocus_sprite zorder 25
    show pomu casual happy at happy_bounce
    "The second one to arrive is Pomu, who is just as energetic as ever."
    show elira casual smile at happy_bounce
    "Conversations ensued as we waited for the last member to arrive."
    "And yet even after waiting 20 minutes past the meet-up time, Finana is nowhere to be found."

    play music "<loop 12>{}".format(audio.bgm_trouble01) fadeout 2.0 fadein 2.0

    scene bg school courtyard with sweepclock
    show pomu casual concerned at set_aligns(LEFT_X_SLOT)
    show elira casual sad at set_aligns(MIDDLE_X_SLOT)
    with dissolve
    show pomu at focus_sprite zorder 50
    play music "<loop 12>{}".format(audio.bgm_trouble01) fadeout 2.0 fadein 2.0
    Character1 "Where is that girl?"
    show pomu at unfocus_sprite zorder 25
    show elira casual worried at focus_sprite zorder 50


    Character6 "I hope she’s okay..."
    Character6 "You don’t think she got into an accident, do you?"
    Character6 "Please tell me that’s not what happened."
    show elira casual sad at unfocus_sprite zorder 25
    Character2 "Calm down, Elira.{w} I’m sure she’s fine."
    show pomu at focus_sprite zorder 50
    Character1 "Do you think we should call her?"
    show pomu at unfocus_sprite zorder 25

    stop music fadeout 0.5

    Character2 "It might be best that you do. Just so we can get a situation upda-"

    show pomu casual surprised
    show elira casual shocked
    Character7 "Waaaait!" with sshake_m
    Character7 "I’m heeeere!"

    play music audio.bgm_hectic01 fadein 2.0
    "The high pitched wail cut me off before I could finish speaking."


    hide elira
    hide pomu
    with easeoutleft
    show finana casual embarrassed at set_aligns(MIDDLE_X_SLOT) with easeinright
    show finana casual embarrassed at panting
    "From across the road, Finana is shouting to us, her face beaded in sweat, her breathing rapid."
    hide finana with easeoutleft
    show pomu casual concerned at set_aligns(LEFT_X_SLOT)
    show elira casual worried at set_aligns(MIDDLE_X_SLOT)
    with dissolve
    show finana casual embarrassed at set_aligns(RIGHT_X_SLOT) with easeinright
    "As she finally approaches us, she takes a deep breath."
    show finana casual embarrassed at focus_scream zorder 50


    Character7 "I’M SO SORRY I’M LATE!!!" with sshake_xl
    show finana at unfocus_sprite zorder 25
    show elira casual shocked
    show pomu casual surprised


    "I never could’ve imagined she was capable of shouting so loudly."
    "And seeing the reaction of the other two, they’re probably thinking the same."
    show elira casual sad at focus_sprite zorder 50
    show pomu casual concerned

    Character6 "Don’t worry about it."
    show elira casual worried
    Character6 "More importantly, are you okay? Nothing bad happened to you, right?"
    show elira casual sad at unfocus_sprite zorder 25
    show finana casual nervous at focus_sprite zorder 50
    Character7 "No, I’m fine. I just…"
    show finana casual sleepy
    extend" overslept."
    show finana casual confused
    Character7 "I was up playing ga-{nw}"
    show finana casual embarrassed at bounce_param(MED_BOUNCE)
    Character7 "Uhh I mean, I couldn’t sleep."
    show finana at unfocus_sprite zorder 25
    show pomu casual happy at focus_sprite zorder 50

    Character1 "Got too excited for shopping, huh? I can understand."
    show pomu casual neutral at unfocus_sprite zorder 25
    show finana casual nervous at focus_sprite zorder 50
    Character7 "Yeah….{w} let’s go with that."
    show finana at unfocus_sprite zorder 25
    "Hm... smells fishy."
    show pomu casual happy
    show elira casual smile
    show finana casual happy
    "Now that we’re all here, it’s time for us to proceed to the station."

    stop music fadeout 2.0
    play sound [ audio.sfx_train ]

    scene bg streets day with sweepright

    "The place we are going to is quite a few stops away, nonetheless, it’s a quick trip."


    play sound audio.sfx_crowdnoise loop fadein 2.0

    "Stepping off and leaving the station, we find ourselves surrounded by buildings, most of which seem like they touch the sky with how tall they are."
    "The streets are crawling with people moving through their busy day."

    stop sound fadeout 2.0

    play music audio.bgm_shopping01 fadeout 2.0 fadein 2.0

    show elira casual neutral at set_aligns(RIGHT_X_SLOT)
    show pomu casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual nervous at set_aligns(MIDDLE_X_SLOT)
    with dissolve

    "For Pomu and Elira, this probably seems like a normal day of shopping in a big city, but for Finana, I fear she may be feeling a little bit overwhelmed."

    show elira casual smile at set_aligns(RIGHT_HAND_X_SLOT)
    show pomu casual happy at set_aligns(LEFT_HAND_X_SLOT)
    with ease
    "As if understanding the situation, Pomu and Elira each grab one of Finana’s hands, reassuring her as they move towards the crowd."
    show finana casual happy at bounce_param
    "I follow right behind them, trying to hide the smile that is forming on my lips."

    scene bg mall with sweepright
    show elira casual neutral at set_aligns(RIGHT_X_SLOT)
    show pomu casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT)
    with dissolve
    "We opt for the mall as the diversity of shops will provide us with a greater range of choices."
    show elira casual smile
    show pomu casual concerned
    show finana casual confused
    "Looking around we manage to find a store that sells camping supplies and other outdoor necessities."
    show elira casual loudlaugh
    show pomu casual excited
    show finana casual happy
    "They have these cute little tents with interesting designs that can fit a single person, and the girls really like them so we head into the shop to buy them."
    show elira casual smile
    show pomu casual concerned
    show finana casual confused
    "We also pick up some tools, food… and a fishing rod? As well as a whole bunch of other things we need for the trip..."
    show elira casual neutral
    show pomu casual neutral
    show finana casual neutral
    "In the end, we find and buy most of what we need from there, but seeing as it’s a bit too early to go home, we decide to check out some other shops and stores."


    Character2 "Which one should we go for?"

    menu choice1:
        "GameStonks":
            jump gamestonks
        "Bobalicious":
            jump bobalicious
        "T.R.A.P.":
            jump trap

label gamestonks:
    scene bg mall with sweepright
    show elira casual neutral at set_aligns(RIGHT_X_SLOT)
    show pomu casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT)
    with easeinright

    "Once we enter what seems to be a den of glowing lights and RGB streaks,{nw}"
    show elira casual shocked at bounce_param
    show pomu casual surprised at bounce_param
    show finana casual shocked at bounce_param
    extend " we’re all in awe."
    show elira casual straightface
    show pomu casual concerned
    show finana casual nervous
    "Shelves are lined with a multitude of video games, from different years and genres."
    "Different well known gaming consoles from different years and generations are all displayed in glass cases, all yours for the taking, if you could handle the expense."


    "Keyboards, mice, headsets, graphics cards, accessories, they have just about everything, even the newest ones in the market that seem so hard to get nowadays."
    "For a ‘game shop’, the place really feels high end."
    hide pomu with easeoutleft
    hide elira with easeoutright
    hide finana with dissolve


    show finana casual confused at finana_staring with slowdissolve
    "While we're exploring the shop, I catch a glimpse of Finana staring intently at the gaming peripherals when we're caught off guard by a sudden screech."
    show finana casual shocked




    Character6 "OH MY GOD!" with sshake_l
    hide finana with easeoutleft
    show elira casual shocked at set_aligns(MIDDLE_X_SLOT) zorder 50 with easeinright
    extend" Is that an Ages Uranus?!"

    show pomu casual concerned at set_aligns(LEFT_X_SLOT) with easeinleft
    show finana casual nervous at set_aligns(RIGHT_X_SLOT) with easeinleft
    show pomu at focus_sprite zorder 50
    Character1 "Sorry, a what now?"
    show pomu at unfocus_sprite zorder 25
    show elira casual loudlaugh at focus_sprite zorder 50
    Character6 "An AGES URANUS!"
    show elira casual smile at unfocus_sprite zorder 25
    "Inside the glass is an old, box-shaped console in all black."
    "It has that distinct retro looking style that you could tell at a glance."

    show finana casual confused at focus_sprite zorder 50

    Character7 "What’s an… Ages Ur{w=0.5}anus…?"
    show finana at unfocus_sprite zorder 25
    show elira casual loudlaugh at focus_sprite zorder 50


    Character6 "It was a super popular game console back in the day. It’s where I played a lot of my favorite childhood classics."
    show elira casual smile at bounce_param
    Character6 "Oh that makes me feel so nostalgic!"
    show elira at unfocus_sprite zorder 25

    Character2 "Back in the day…?"
    Character2 "Sorry, how old are you again, Elira?"

    show elira casual straightface at focus_sprite zorder 50

    Character6 "Yow…"
    show elira casual sad
    extend " you ain’t gotta do me dirty like that."
    show elira at unfocus_sprite zorder 25
    Character2 "Uh…my bad."
    show elira casual loudlaugh at happy_bounce
    "Ages Uranus aside, we spend a lot of time just browsing and watching Elira react to the older consoles."
    "I swear she sounds like she’s a million years old when she talks about the past."


    jump continuation2

label bobalicious:
    scene bg mall with dissolve
    Character2 "How about that place? Bobalicious."

    show finana casual confused at set_aligns(MIDDLE_X_SLOT) zorder 30 with easeinleft

    Character7 "Booba?"

    show pomu casual concerned at set_aligns(LEFT_X_SLOT) with easeinleft
    show pomu at focus_sprite zorder 50
    Character1 "Finana…"
    show pomu at unfocus_sprite zorder 25
    show elira casual serious at set_aligns(RIGHT_X_SLOT) zorder 0 with easeinleft
    show elira at focus_sprite zorder 25
    Character6 "Boba,{w=0.3} Finana."
    show elira casual annoyed
    extend " BOBA."
    show elira casual sigh
    Character6 "The stuff you find in Bubble Tea."
    show elira casual straightface at unfocus_sprite zorder 25

    show finana casual embarrassed at focus_sprite zorder 50

    Character7 "Oh…"
    show finana at unfocus_sprite zorder 25
    hide pomu
    hide finana
    hide elira
    with fade
    "Bobalicious is a nice, little bubble tea shop."
    "The atmosphere is very calming and the staff are all very nice."


    show elira casual neutral at set_aligns(MIDDLE_X_SLOT) with dissolve


    Character6 "What flavor did you get?"


    menu choice2:
        "Taro":
            jump taro_hazelnut
        "Hazelnut":
            jump taro_hazelnut
        "Lova Palooza":
            jump lova_palooza

label taro_hazelnut:
    show elira casual smile
    Character6 "Nice."

    show elira casual neutral
    Character6 "I got Thai tea."
    show elira casual loudlaugh at bounce_param
    extend" I just love that flavor!"
    show elira casual neutral zorder 30

    show pomu casual happy at set_aligns(LEFT_X_SLOT) with easeinleft
    show pomu at focus_sprite zorder 50
    Character1 "Raspberry for me!"
    show pomu at unfocus_sprite zorder 25
    show finana casual happy at set_aligns(RIGHT_X_SLOT)zorder 0 with easeinleft
    show finana at focus_sprite zorder 25
    Character7 "I got Matcha!"
    show finana at unfocus_sprite zorder 25

    jump sub_continuation

label lova_palooza:

    show elira casual worried


    Character6 "…what?"
    show elira casual sad zorder 30

    show pomu casual concerned at set_aligns(LEFT_X_SLOT)with easeinleft
    show pomu at focus_sprite zorder 50
    Character1 "What even IS that flavor?"
    show pomu at unfocus_sprite zorder 25
    show finana casual confused at set_aligns(RIGHT_X_SLOT)with easeinleft
    show finana at focus_sprite zorder 50
    Character7 "Sounds kinda sus."
    show finana at unfocus_sprite zorder 25

    "It does, in fact, taste pretty sus."
    "Like a mixture of rainbow sprinkles, rubber, and toothpaste."
    "Not picking that one next time."

    jump sub_continuation

label sub_continuation:

    scene bg mall with sweepclock
    show pomu casual overjoyed at set_aligns(LEFT_X_SLOT)
    show elira casual loudlaugh at set_aligns(MIDDLE_X_SLOT)
    show finana casual happy at set_aligns(RIGHT_X_SLOT)
    with dissolve
    show pomu at happy_bounce
    show elira at happy_bounce
    show finana at happy_bounce
    "We sat down at a table with our drinks in hand, talking about a multitude of topics and ideas while laughing and goofing around."
    "Overall, I’d say it was time well spent."

    jump continuation2

label trap:

    scene bg mall with sweepright
    Character9 "Welcome to T.R.A.P.! What are you looking for today?"
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with easeinright
    "We are greeted by the staff as soon as we enter the shop."
    show elira casual smile
    show pomu casual happy
    show finana casual happy
    "Apparently, this place is a clothing store selling their own designs and brands."
    show elira casual neutral
    show pomu casual neutral
    show finana casual neutral
    "There is a wide range of fashion assortment, from formal and elegant, to casual and comfortable."
    show pomu casual excited
    "They even have character shirts from different types of media like anime and movies."

    show pomu casual neutral at focus_sprite zorder 50

    Character1 "So…"
    show pomu casual concerned
    extend " what does T.R.A.P. stand for?"
    show pomu at unfocus_sprite zorder 25

    "Pomu asks the employee the question we all have in mind."
    hide pomu
    hide elira
    hide finana
    with dissolve

    Character9 "It stands for this store’s very motto."
    Character9 "The very sole vision that the owner, Mister Kiro, had set his mind on as he built this brand from the ground up!"
    Character9 "Yes, it stands for"
    extend " ‘Thighs" with sshake_s
    extend " Really" with sshake_m
    extend " Are" with sshake_l
    extend " Passion’!" with sshake_xl


    "I might have imagined it, but there seems to be sparkles and glowing lights shining out of their eyes."

    show elira casual straightface at set_aligns(LEFT_X_SLOT)
    show pomu casual surprised at set_aligns(MIDDLE_X_SLOT)
    show finana casual shocked at set_aligns(RIGHT_X_SLOT)
    with dissolve
    show finana at focus_sprite zorder 50
    Character7 "What the feesh…?"
    show finana at unfocus_sprite zorder 25
    show elira casual sigh at focus_sprite zorder 50

    Character6 "I can’t believe that’s a thing."
    show elira casual straightface at unfocus_sprite zorder 25
    show pomu casual concerned
    scene bg mall with sweepclock
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "Time passes as we listen to the employee’s enthusiastic explanations and descriptions of the store’s legacy while browsing through their selection."
    show finana casual confused
    "From the corner of my eye, I notice the infamous virgin-killing sweater, a piece of clothing so scandalous, it took the internet by storm."
    "Who knew they’d be selling such a unique item here?"
    show elira casual loudlaugh at bounce_param
    show pomu casual overjoyed  at bounce_param
    show finana casual happy at bounce_param

    "Although it’s a bit of an odd experience, we have some fun talking and laughing together."
    "It’s definitely a memory that’s gonna be hard to forget."


    jump continuation2

label continuation2:
    scene bg streets day with sweepright
    "Before heading back home, we decided to stop by one last place."

    play music audio.bgm_hangout01 fadeout 2.0 fadein 3.0
    scene bg karaoke with sweepright

    show pomu casual excited at set_aligns(MIDDLE_X_SLOT)

    Character1 "Let’s go!!!" with sshake_m
    show pomu casual overjoyed at happy_bounce
    extend " This is ‘Kami Knows’!"
    show pomu casual happy at set_aligns(MIDDLE_X_SLOT)
    show pomu casual happy at pomu_sing
    "Everyone cheers as the music plays and Pomu starts to sing."
    show pomu casual overjoyed at happy_bounce
    "Her voice is powerful, like the chorus of a hundred fairies singing the same tune, but somehow, I feel like she’s still holding back."
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT) with ease
    "The roar of the beat finally comes to an end,{nw}"
    show pomu casual happy at nodding
    extend " and Pomu gives us a bow."
    show pomu casual overjoyed at bounce_param
    Character1 "Alright, Elira. You’re next."
    hide pomu with easeoutright
    show elira casual sigh  at set_aligns(MIDDLE_X_SLOT) with easeinleft
    "With a little reluctance, Elira picks up the microphone as the sound of lapping waves fills the room."
    show elira casual neutral
    "There’s a pause,"
    show elira casual giggle
    extend " and from her lips comes a giggle."
    show elira casual neutral
    Character6 "Spirit Girl by TokimoP"
    show elira casual smile at elira_sing
    "The song sounds relaxing, but also melancholic."
    show elira casual sigh
    "Elira’s soft and sweet voice has a tremble in it, perhaps from nervousness or a lack of confidence."
    show elira casual giggle
    "But the way she sings felt like a lullaby luring you into the dreams that you’ve so desperately sought for."
    show elira casual neutral at set_aligns(MIDDLE_X_SLOT) with ease

    "Before I realize it, the sounds of bells are ringing and the song has ended."
    hide elira with easeoutleft
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT) with easeinright
    "Elira passes on the microphone to Finana and gives her a wink."

    show elira casual giggle at set_aligns(LEFT_X_SLOT) with easeinleft
    Character6 "All yours, Finana."
    hide elira with easeoutleft
    show finana casual happy
    "Though Finana has gotten quite used to hanging out with us, I was still expecting her to be at least a little nervous, especially since it’s karaoke."
    show finana casual confused
    "Yet there she is standing quite confident as she holds the microphone up."


    "Then the most unexpected song came on."

    show finana casual neutral
    Character7 "Feeshney Spears… Noxic"
    show finana casual happy at finana_sing

    "The beat comes down and it is intense, and also…seductive?"
    "It feels so out of left field but somehow, also kind of fitting."
    "Oh are we in for a ride."
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT) with ease
    show finana at bounce_param
    "I couldn’t help but applaud as the amazing performance came to an end."
    show finana casual happy
    "Never have I imagined Finana would be singing such a song, but she did and it was so good."

    show finana casual neutral
    Character7 "Your turn."

    show finana at nodding
    "She smiles as she hands me the microphone."
    hide finana with dissolve
    "Now… which song to sing…"

    scene bg karaoke

    menu choice3:
        "Always Gonna Give You Up by Rock Ridley":
            jump always_gonna_give_you_up_by_rock_ridley
        "Like an Idiot by Ryu Kazama":
            jump like_an_idiot_by_ryu_kazama
        "Take On You by U-hu":
            jump take_on_you_by_u_hu

label always_gonna_give_you_up_by_rock_ridley:


    play music audio.bgm_karaokea fadeout 2.0 fadein 2.0

    show pomu casual concerned at set_aligns(MIDDLE_X_SLOT)
    show elira casual murderous at set_aligns(LEFT_X_SLOT)
    show finana casual confused at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "The funky beat starts to roll, and the sound of a thousand disappointed sighs ring as the tune of the very famous song starts to fill the room."
    show pomu casual pout
    show elira casual annoyed
    show finana casual sleepy
    "I move my body from side to side, just like how Rock Ridley did in his music video. Swaying, jamming, tapping, I’m in my element."
    "Nothing could ever be better than pulling off a Rock Roll in front of your friends."
    show elira casual sigh

    "It’s… perfect."

    jump continuation3

label like_an_idiot_by_ryu_kazama:

    play music audio.bgm_karaokeb fadeout 2.0 fadein 2.0
    show pomu casual concerned at set_aligns(MIDDLE_X_SLOT)
    show elira casual sigh at set_aligns(LEFT_X_SLOT)
    show finana casual shocked at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "As soon as the sad melody starts, I am in my element."
    show pomu casual sad
    show elira casual worried
    show finana casual nervous
    "The feelings of someone drowning in sorrow and heartache as they drank their sadness away fills me."
    show elira casual sad
    "Longing for the other person’s love, but seemingly doing the dumbest things at the most crucial moments."
    "So deep in love that I couldn’t think straight."
    "Truly, I’ve been a fool."


    "It’s so melancholic, but oh so perfect."


    jump continuation3


label take_on_you_by_u_hu:

    play music audio.bgm_karaokec fadeout 2.0 fadein 2.0

    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "The jolly beats come up, and I am jumping on my toes."
    show pomu casual happy at bounce_param
    show elira casual smile at bounce_param
    show finana casual happy at bounce_param
    "Everything seems to distort into a black and white painting as I interact with it."
    "The lines that make up myself feel darker and bolder as the song went on, and I could feel the hype filling my soul."
    "I sing with such power that I feel like I could take on the world, that I could take on me."
    show pomu casual overjoyed
    show elira casual loudlaugh
    show finana casual happy

    "It’s a blast, and the hype is perfect."

    jump continuation3


label continuation3:

    play music audio.bgm_goinghome01 fadeout 2.0 fadein 3.0

    scene bg streets sunset with sweepclock
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "As the day nears its end, we find ourselves smiling as we stop at the street where we’d all have to go our separate ways back home."
    "The day has been so fun and so full of memories that it feels a little hard to go."
    show pomu casual happy
    show elira casual smile
    show finana casual happy
    "After a little reminder of the things we still need to do for the camping trip, we all head home with smiles on our faces and new memories to remember."

    call loading_movie_transition_block

    play music sfx_crowdnoise fadein 3.0
    scene bg classroom back view with slidingblinds

    "As the weekdays come, the monotonous feeling of going to school starts to sink in."
    "Classes pass by like a blur."
    "The lessons, the notes, the writings of chalk on the board."
    "They all melt into the back of my subconsciousness, as I dwell in the feeling of excitement for the trip that is to come at the end of the week."


    play music ["<silence 1>","<loop 16>{}".format(audio.bgm_clubtime01)] fadeout 2.0 fadein 2.0

    scene bg clubroom day with sweepclock
    show elira school neutral at set_aligns(MIDDLE_X_SLOT)
    show pomu school neutral at set_aligns(LEFT_X_SLOT)
    show finana school neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "Of course, there are still club activities after school."
    "I’m not sure when it started, but the little time I’ve spent with these girls has become the highlight of my days."
    "Always looking forward to seeing them,{w} always wondering what silly things we’d do next,{w} always wanting to…"

    show elira school worried at focus_sprite zorder 50


    Character6 "You okay?"
    show elira school sad at unfocus_sprite zorder 25

    "The question catches me off guard."


    Character2 "Yeah, I’m fine.{w} I was just… thinking about stuff."


    "Do I have a frown on my face while in deep thought?"
    "Maybe.{w} Elira’s always been sensitive to those things."

    show pomu school concerned at set_aligns(LEFT_X_SLOT)
    show pomu at focus_sprite zorder 50
    Character1 "What’s up? Something going on here?"
    show pomu at unfocus_sprite zorder 25

    "Even Pomu joins in."
    "If she ever hears someone is down in spirits, she’d always find a way to cheer them up.{nw}"
    show pomu school happy
    extend" That’s just how she is."

    show finana school worried at set_aligns(RIGHT_X_SLOT)
    show finana at focus_sprite zorder 50
    Character7 "Um, if you need help with anything, I’ll do my best!"
    show finana school happy at unfocus_sprite zorder 25

    "Hearing the shy Finana cheer me on, I can’t help but smile."
    "The way she gives effort at even the smallest of things is something I’ve always liked about her."
    show elira school neutral
    show pomu school neutral
    show finana school neutral
    "Spending all this time with the girls, I've started to learn more about them, their likes and dislikes, their humor, their kindness…"


    "But… {w}could I say the same for me?"


    Character2 "Thanks for worrying, but really,{w=0.3} I’m fine."

    show elira school smile at set_aligns(MIDDLE_X_SLOT)
    show pomu school happy at set_aligns(LEFT_X_SLOT)
    show finana school happy at set_aligns(RIGHT_X_SLOT)

    "The gentle smiles they all hold cast a ray of light into the shadow of my doubts."
    "Maybe there isn’t anything to worry about in the first place."


    "Wouldn’t that be great?"

    call loading_movie_transition_block

    play music audio.bgm_lazulight01 fadein 3.0

    scene bg school courtyard with slidingblinds

    "The weekend comes and we yet again meet up at the school’s entrance."
    "Somehow, the spot just becomes the usual meeting place for us."
    show elira casual straightface at set_aligns(MIDDLE_X_SLOT) zorder 50
    with dissolve

    "Elira is yet again the first to arrive, quietly reading another book as she stands by the gate."
    show elira casual neutral
    show pomu casual happy at set_aligns(LEFT_X_SLOT)
    show finana casual embarrassed at set_aligns(RIGHT_X_SLOT)
    with easeinright
    "We chat for a bit until Pomu arrives, this time together with Finana."
    "Probably picked her up so she isn’t late again."
    show elira casual neutral
    show pomu casual neutral
    show finana casual neutral

    "Then, we all make our way towards the station."

    play sound [ audio.sfx_train ]
    scene bg camping spot by river day with slidingblinds
    show elira casual neutral at set_aligns(MIDDLE_X_SLOT)
    show pomu casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "We arrive at the camping spot, a lush area just beside a snaking river."
    "The air feels fresh and cool, and the weather isn’t too hot."
    "Suffice to say, it’s a pretty good place to camp in."

    show pomu casual happy at bounce_param
    show elira casual smile at bounce_param
    show finana casual happy at bounce_param
    "Though we have planned some activities, we all just end up playing around in the river."


    "Before we realize it, it’s already time for lunch."

    scene bg camping spot by river day with sweepclock
    show elira casual neutral at set_aligns(MIDDLE_X_SLOT) with dissolve
    show elira at bounce_param
    Character6 "Alright everyone, I’ll be assigning you tasks to prepare for lunch!"
    show elira casual serious
    Character6 "[persistent.mcName], you’ll be in charge of cooking."


    Character2 "Alright."
    show pomu casual concerned at set_aligns(LEFT_X_SLOT) with dissolve
    show elira at focus_sprite zorder 50
    Character6 "Pomu,{w} you’re assistant chef."
    show elira at unfocus_sprite zorder 25
    show pomu casual happy at bounce_param
    show pomu at focus_sprite zorder 50
    Character1 "Roger that!"
    show pomu at unfocus_sprite zorder 25
    show finana casual sleepy at set_aligns(RIGHT_X_SLOT) with dissolve
    show elira at focus_sprite zorder 50
    Character6 "Finana, you’re with me.{w} We’ll gather firewood and set up the table."
    show elira at unfocus_sprite zorder 25
    show finana casual confused at focus_sprite zorder 50
    Character7 "O-okay"
    show finana at unfocus_sprite zorder 25
    show elira casual neutral at focus_sprite zorder 50

    Character6 "Lazulight,"
    show elira casual annoyed
    extend " to battle stations!" with sshake_m
    hide pomu with easeoutleft
    hide finana
    hide elira
    with easeoutright
    scene bg camping spot by river day with sweepclock
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT) with dissolve

    "We each head to do our own work."
    "I end up doing most of the cooking,{nw}"
    show pomu casual happy
    extend " but Pomu helps out with stuff like cutting and washing."

    "Soon, everything is set up, and the feast is ready."
    scene bg camping spot by river day with sweepclock
    show elira casual neutral at set_aligns(MIDDLE_X_SLOT)
    show pomu casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve

    "We were having good ol' curry with rice as well as some barbeque on the side. A hearty meal for us would-be-adventurers for the day."
    show elira casual smile
    show pomu casual happy
    show finana casual happy
    "Fortunately, everybody seems to like the food that I made."
    show elira casual loudlaugh at happy_bounce
    show pomu casual overjoyed at happy_bounce
    show finana casual happy at happy_bounce
    "Laughs and chuckles fill the air as we eat and enjoy our lunch, until we finish our plates empty."

    stop music fadeout 2.0
    scene bg camping spot by river day with sweepclock

    "After cleaning up, we're free to do whatever we want."

    "Now then, I wonder what I should do to pass the time?"


    menu choice4:
        "Stone skipping with Pomu":
            jump stone_skipping_with_pomu
        "Fishing with Elira":
            jump fishing_with_elira
        "Wading in the water with Finana":
            jump wading_in_the_water_with_finana

label stone_skipping_with_pomu:

    scene bg camping spot by river day with sweepright

    "A little further downstream from where we had set up camp, the sound of consecutive splashes of water can be heard."
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT) with dissolve
    play music audio.bgm_pomu01 fadein 3.0
    show pomu at pomu_stone_skip
    "I arrive just in time to see Pomu managing to make a rock skip five times before it sinks."


    Character2 "Nice throw."

    show pomu casual happy at bounce_param

    "She turns to me with a huge smile on her face."
    show pomu casual neutral

    Character1 "I’m pretty good, huh?"


    Character2 "Yeah, I guess so."
    Character3 "Can I have a try?"

    show pomu casual happy
    Character1 "Sure, go ahead."

    "I search around the riverbed until I find a decent flat stone."
    "With a tight grip around it, I take a step back, throw back my arm, and slingshot that stone towards the water, letting it leave my hand with a notable spin around its longer side."

    show pomu casual concerned
    "The spinning stone hits the surface of the water and bounces back up as if it was deflected, skipping one, two, three, four, five times until it loses all momentum and sinks."

    show pomu casual overjoyed at bounce_param
    Character1 "Hey, you’re pretty good too!"

    show pomu casual neutral
    Character2 "Thanks."

    Character2 "So…{w} contest?"
    show pomu casual excited at bounce_param
    Character1 "You’re on!"
    show pomu casual neutral at pomu_stone_skip_repeat

    "Soon we are throwing tons of stones, waiting for that one throw to break the skipping record we had."
    "In the end, Pomu managed to get one to skip seven times, while I couldn’t go more than five."


    scene bg camping spot by river day with sweepclock
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT) with dissolve
    show pomu at nodding

    "We sit down by the riverside. Tired from our little contest, we are now just tossing the stones randomly into the river."


    "It’s peaceful, being able to just relax like this. The breeze feels particularly great as it blows past us."

    show pomu at focus_stare with dissolve
    "I soon find myself staring at Pomu, particularly at her blonde hair that flows freely as the wind combs through the strands."
    show pomu casual happy with dissolve
    "The sun’s rays shining upon her make her seem magical, like a fairy crowned in nature’s evergreen beauty."


    "She takes notice of my stare and raises her brow in question."
    show pomu at unfocus_stare with dissolve
    show pomu casual concerned at set_aligns(MIDDLE_X_SLOT)
    show pomu at bounce_param

    Character1 "What?"

    show pomu casual neutral
    Character2 "Nothing."
    show pomu casual serious
    Character1 "You’re weird."

    show pomu casual neutral
    Character2 "Right back at you."

    show pomu casual serious
    Character1 "…"
    show pomu casual pout
    Character2 "…"


    show pomu casual overjoyed at bounce_param
    "We could only laugh at our silly conversation."

    show pomu casual neutral
    Character2 "I still can’t believe I’m out here, camping together with you."

    show pomu casual concerned
    Character1 "What? You don’t like it?"

    show pomu casual neutral
    Character2 "On the contrary, I’m quite thankful."
    show pomu casual surprised at bounce_param
    Character2 "Especially to you, Pomu."

    Character1 "Wh-"
    show pomu casual concerned
    extend "Why me, specifically?"


    Character2 "Because it’s thanks to you that Lazulight came to be."


    Character2 "It was your idea to make this club, after all.{w} And it’s been real fun."

    show pomu casual surprised at bounce_param
    Character2 "So… thank you, Pomu."

    show pomu casual flustered with dissolve
    show pomu at shiver_softer(MIDDLE_X_SLOT)
    "She turns her face away from me, though I could still see her ears turn red from behind."



    show pomu casual serious at set_aligns(MIDDLE_X_SLOT)
    show pomu at bounce_param
    Character1 "I-I just did what I wanted to do, okay? I didn’t do it for anyone."

    Character1 "I didn’t do it for you either…{w=0.5}"
    show pomu casual pout at bounce_param
    extend " idiot."
    show pomu casual concerned
    "I laugh, much to her surprise."
    "I truly am grateful to have gotten to know them."
    extend " And to have gotten to know the girl named Pomu."

    show pomu casual sad
    Character2 "Come on, let’s go back and see what the others are up to."
    show pomu casual concerned
    Character1 "O-Okay?"


    jump continuation4

label fishing_with_elira:

    play sound sfx_river loop fadein 3.0

    scene bg camping spot by river day with sweepclock

    "A little bit further upstream, I start setting up my seat."
    "Seeing that fishing pole back when we went shopping got me interested and curious about fishing, so I ended up doing some research and even bought some basic gear."


    "With the bait hooked, I swing the pole towards the river, and the line flies off."
    "I stick the pole between a rock and the leg of my seat, and wait for the catch."


    "This activity requires patience, or so I’ve read."
    "Waiting for the right moment, the right time when that fish snags onto that hook."
    "And then, bam, you pull at it with nothing but your strength and sheer willpower."
    "It’s you versus the fish fighting for its life.{w} Nothing sounds more epic than that."

    scene bg camping spot by river day with sweepclock

    "Minutes later, I find myself consumed by boredom."
    "Never have I expected for such an activity to require this much patience."
    "Bored out of my mind, I start to pick up pebbles and toss them into the water for no particular reason other than it seems more amusing than waiting for a fish to bite."
    "But even that doesn’t last long."


    "Just as I’m about to give up and start packing up my things, a familiar voice calls out to me."

    stop sound fadeout 2.0

    show elira casual smile at set_aligns(LEFT_X_SLOT) with easeinleft
    play music "<loop 0.12>{}".format(audio.bgm_elira01) fadein 3.0

    Character6 "Hey there. What are you up to?"

    show elira casual neutral
    Character2 "Achieving the epitome of pain and suffering."

    show elira casual worried at set_aligns(MIDDLE_X_SLOT) with ease


    Character6 "…what?"

    show elira casual sad
    Character2 "Sorry, it’s nothing."
    Character2 "I’m uhh, actually trying to fish right now."
    Character2 "Keyword is ‘trying’."

    show elira casual worried

    Character6 "Oh. "
    show elira casual neutral
    extend "Mind if I join you then?"


    Character2 "Sure go ahead. Here, you can take my chair."
    show elira casual neutral

    Character6 "No, it’s alright. "
    show elira casual smile
    extend "You need that more than I do since you’re, you know,{w=0.5} fishing."

    show elira casual neutral
    Character6 "I’ll just sit over here on this rock. That way I can also dip my feet in the water."

    Character2 "Alright then."
    show elira casual smile at set_aligns(LEFT_X_SLOT) with ease
    show elira casual giggle at set_aligns(LEFT_X_SLOT,650) with ease

    "We end up engaging in idle chatter as we sit around doing nothing."
    show elira casual loudlaugh
    "I find it so much more enjoyable than fishing that for a good minute, I forgot all about the pole in my hand."
    "And in just those few moments when I loosen my grip, something begins to pull on the line."

    hide elira with dissolve
    "Surprised and shocked, I freak out as the pole begins to bend."
    "Thankfully I stuck it in a pretty tight place, otherwise it would have gone flying by now."


    "Realizing what is happening, I jump up, grab the pole and kick my seat, pulling like my life depended on it."
    "I’m trying to reel it in, but the fish has such impressive strength that I could barely keep my feet planted on the ground." with vpunch


    show elira casual shocked at set_aligns(LEFT_X_SLOT) with easeinleft


    Character6 "Holy- Are you okay??{w} Do you need help???" with sshake_s

    Character2 "Yes."
    extend " YES I DO." with sshake_m

    show elira casual worried at set_aligns(MIDDLE_X_SLOT) with ease
    "Elira runs towards me and grabs a part of the pole."
    show elira at elira_fishing
    "Together we keep pulling, and reeling, and pulling without rest, but the prey is fighting for its dear life."


    "The next split second is a blur. We pull as hard as we can, and in one last ditch effort, I jump back, putting all my weight into it."


    "The feeling of tension in my hands grows weak, and before I know it..."
    play sound [ "<silence 0.5>", audio.sfx_thud01 ]
    hide elira with easeoutleft
    "I am on the ground staring up at the sky." with sshake_m
    scene bg black with fade

    scene bg camping spot by river day with fade
    Character2 "Damn… {w}Elira, are you okay?"


    show elira casual sigh at set_aligns(MIDDLE_X_SLOT,650) with dissolve


    Character6 "Yeah, I’m fine."
    show elira casual sad

    "She managed to land on my arm. Thankfully, that means I managed to cushion her fall, at least."

    show elira casual worried at set_aligns(MIDDLE_X_SLOT) with ease

    Character6 "What about you? Are you okay?"
    show elira casual sad

    Character2 "Yeah, I’m fine too. Just a little tired."

    "After confirming we are both okay, she starts to pout."


    show elira casual annoyed


    Character6 "We are {nw}"
    extend "NEVER{nw}" with sshake_s
    extend " doing that again."

    Character2 "I one hundred percent agree with you."


    show elira casual worried


    Character6 "So what happened, did we… did we manage to catch it?"
    show elira casual sad
    Character2 "Well…"

    show elirafish at fish_slight_right with easeinbottom
    "I prop the pole up, and there it is."
    show elirafish at fish_shake
    "Dangling on the end of the line, hook inside its mouth, is the glorious catch, a grey-scaled fish known as Tilapia{w=0.3} a.k.a. St. Peter’s Fish."

    show elira casual shocked
    Character6 "EEEKKKK!" with sshake_m
    show elira casual shocked at set_aligns(LEFT_X_SLOT) with ease

    "The sudden scream catches me by surprise."

    Character6 "IT LOOKS SO GROSS! EUGHHH!!" with sshake_m
    show elirafish at fish_slight_right with ease
    show elira casual worried
    Character2 "Elira, calm down, it’s a fish."
    show elirafish at fish_center with ease
    "I move it closer towards her and she starts freaking out even more."
    show elira casual shocked
    Character6 "GETITAWAYGETITAWAYGETITAWAYGETITAWAYGETITAWAY{nw}" with sshake_m
    hide elira with easeoutleft
    Character6 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"with sshake_xl


    "I’m not sure why she is freaking out so much, but I know that scream is a scream of pure terror."
    "I quickly grab the cooler box and dump in the fish, closing the lid as fast as I can."
    hide elirafish with easeoutbottom

    Character2 "There we go.{w} No more fish."
    Character2 "It’s okay now, Elira."

    show elira casual murderous at set_aligns(MIDDLE_X_SLOT,850) with dissolve

    "She’s crouching down a few feet away,{nw}"
    show elira at shiver_softer(MIDDLE_X_SLOT)
    extend " her hands covering her eyes as she trembles."
    "I lean over and place my hand on her back."

    Character2 "Elira…{w} are you okay?"
    show elira casual murderous at set_aligns(MIDDLE_X_SLOT,850) with ease
    #show elira at nodding(870,850) ##doesn't work
    "She nods quietly."


    Character2 "I’ve already put the fish away."

    Character6 "…okay."

    show elira casual sad with dissolve
    show elira at shiver_softer(MIDDLE_X_SLOT)
    "She finally removes her hands from her face and looks up to me."
    "Her eyes are teary and her mouth trembles."
    "Something about that fish must have really shaken her up."

    show elira casual sigh at set_aligns(MIDDLE_X_SLOT) with ease
    "I held out my hand to her, which she took, as I pulled her up."

    show elira casual worried
    Character6 "I’m… sorry about that."

    show elira casual sad
    Character2 "No, I should be the one apologizing.{w} I shouldn’t have pushed it closer to you."


    Character6 "…mhm."


    Character2 "So uh… are you okay now?"

    show elira casual serious

    Character6 "Yeah, I’ll be fine. I just…{w=0.5}"
    show elira casual sad
    extend " need some time to settle my nerves."
    show elira casual sigh at panting

    "I am curious, very curious in fact, about why she freaked out so much, but I realize it would be rude to ask."

    show elira casual sad at set_aligns(MIDDLE_X_SLOT)
    show elira casual sigh at set_aligns(MIDDLE_X_SLOT,650) with ease
    "We sit back down somewhere a bit further away from the river."

    "I let her have the chair and give her a bottle of water to help her calm down."


    show elira casual sad

    Character6 "The truth is…{w=0.5}"
    show elira casual worried
    extend" I’m actually scared of fish."

    show elira casual sad
    "Her sudden confession is unexpected."


    Character2 "So like, all the fish?"

    show elira casual serious
    Character6 "Kinda."
    show elira casual worried
    Character6 "I just… I can’t stand looking at them. I feel like I’d pass out."
    show elira casual sad

    Character2 "I see."


    Character2 "…wait. If you’re so scared of fish… why would you join me while I’m fishing?"


    show elira casual sigh


    Character6 "I thought you’d just be catching the smaller kinds of fish."
    show elira casual serious
    Character6 "Those I can stand at least."
    Character6 "I’m still scared of them, but they’re a lot better than…"
    show elira casual sad
    extend " what you caught."


    Character2 "Oh Elira…"


    Character2 "Well, I’m just glad you’re fine now."
    Character2 "I almost had a heart attack when you started freaking out and screaming in terror."


    show elira casual worried


    Character6 "…sorry."

    show elira casual sad
    "I let out a sigh."


    Character2 "Now you know, if it’s an activity that involves something you’re scared of, don’t join in, okay?"
    show elira casual worried
    Character6 "Okay…"
    show elira casual sad
    Character2 "Alright then. We should head back to the others. You can rest some more in the tent."
    show elira casual worried
    Character6 "What about the fish…?"
    show elira casual sad
    Character2 "We’re gonna grill it for dinner."


    show elira casual smile

    Character6 "You’re joking,{w=0.5} right?"
    show elira casual murderous
    extend " RIGHT?"with sshake_m


    "The murderous look in her eyes sends chills down my spine."


    Character2 "Haha y-{w=0.3}yeah…{w=0.5}it’s just a joke..."


    show elira casual sigh with dissolve

    "She lets out a sigh of relief."
    show elira casual smile

    Character6 "Okay then. That’s good."
    show elira casual neutral
    "Guess we’re not having grilled fish for dinner…"

    jump continuation4

label wading_in_the_water_with_finana:


    scene bg camping spot by river day with sweepright
    play music audio.bgm_finana01 fadein 3.0
    show finana casual happy at set_aligns(MIDDLE_X_SLOT) with dissolve
    show finana at elira_sing
    "Just near our camping spot, I find Finana, barefoot and wading through the shallow water."
    "She seems to be looking for and picking up small rocks, a sight that looks quite familiar."


    Character2 "Hey Finana. What are you up to?"
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT) with ease

    show finana at bounce_param
    Character7 "Oh! Hey there."
    show finana casual happy

    "She gives me a wide smile."

    show finana casual neutral
    Character7 "I’m uh picking up rocks that look pretty."


    Character2 "Oh, kinda like when we all went to the river together the first time. You really like doing that, huh?"
    show finana casual happy
    Character7 "Ehehe..."

    show finana casual neutral
    Character2 "Now that I think about it, it’s because of you that we went with the name ‘Lazulight’."
    show finana casual confused
    Character2 "So you’re basically like the group’s godmother or something."
    show finana casual shocked at bounce_param
    pause 1.0
    show finana casual embarrassed with dissolve

    Character7 "Wh-{w}What?!{w} N-{w=0.1}no, that can’t be…"
    show finana casual shocked
    Character7 "I was just saying stupid things!" with sshake_s
    extend " The rock wasn’t even lazulite!" with sshake_m

    Character2 "I know, but we can’t deny it’s still because of you."

    show finana casual confused with dissolve

    Character7 "Oh stop teasing me."
    show finana casual angry
    extend " You’re such a meanie!" with sshake_s

    "The small pout that forms on her lips is adorable."

    show finana casual sleepy
    Character2 "Okay okay, I’ll stop."


    show finana casual neutral


    "We both take a seat on some large rocks on the side of the river,{nw}"
    show finana casual neutral at set_aligns(MIDDLE_X_SLOT,SITTING) with ease
    extend" dipping our feet in the water as we talk."

    show finana casual happy
    "It’s interesting to see how much Finana’s improved in regards to talking with people. Well, mainly with us, but progress is still progress."


    Character2 "Say, Finana…"

    show finana casual neutral
    Character7 "Yeah?"


    Character2 "Do you like hanging out with us?"
    show finana casual shocked  at set_aligns(MIDDLE_X_SLOT,500) with ease
    Character7 "Huh? Of course! I love hanging out with everyone."
    show finana casual nervous
    Character7 "But… why do you ask?"

    show finana casual confused
    Character2 "No reason in particular."
    Character2 "I’m just kind of amazed how our little impromptu group managed to hold up."
    Character2 "And now here we are, camping outside when you and I were so against it when it was first mentioned."

    show finana casual nervous at fidget
    Character7 "I mean, I’m still kinda not very fond of it."
    show finana casual happy at set_aligns(MIDDLE_X_SLOT)
    show finana casual happy at bounce_param
    Character7 "But I think it’s because I’m together with everyone in Lazulight that I feel like things would work out."

    show finana casual neutral
    Character2 "Really? Does that mean we’re special to you?"


    show finana casual shocked at bounce_param

    Character7 "No!" with sshake_s
    show finana casual nervous
    extend " I mean, yes but-{w=0.5} I-{w=0.5}"
    show finana casual angry
    Character7 "Oh… you’re so mean."

    show finana casual confused
    "I try and fail to hold back my laughter."
    show finana casual sleepy
    "Her reactions are always so amusing and adorable that I can’t help but tease her."
    show finana casual confused
    Character2 "Well, to us,"
    extend" you’re special too."
    show finana casual shocked with sshake_s
    pause 1.0
    show finana casual embarrassed with dissolve
    Character7 "…"


    "The silence is a lot longer than I expected."

    "Curious, I turn towards her,"
    show finana casual angry at finana_splashing
    play sound [ "<silence 0.8>", audio.sfx_splash ] volume 2.0
    extend "but what greets me instead is a splash of {nw}"
    extend "water." with sshake_s


    Character2 "Wha-"
    extend " HEY!" with sshake_m

    play sound [ audio.sfx_splash, audio.sfx_splash ] volume 2.0
    play voice [ "<silence 0.5>", audio.sfx_splash ] volume 2.0
    play audio [ "<silence 0.8>", audio.sfx_splash ] volume 2.0

    show finana casual angry at finana_splashing2(3)

    "Without saying a word, she keeps on splashing water on me."
    "I fight back, sending a shower of droplets her way."
    "Soon it turns into a full on water fight, and we are soaked from head to toe."


    show finana casual happy at set_aligns(MIDDLE_X_SLOT)


    "As it ends, we can only laugh at the silliness of our actions which led to nothing but us getting wet."
    show finana casual neutral

    Character2 "…we should go back and dry ourselves before the other two return."


    show finana casual happy at set_aligns(MIDDLE_X_SLOT)
    show finana at bounce_param

    Character7 "Yeah…I’m drenched down to my underwear."

    show finana casual neutral
    Character2 "Woah, too much info there, Finana."


    show finana casual happy at set_aligns(MIDDLE_X_SLOT)
    show finana at bounce_param
    Character7 "Ehehe…"


    jump continuation4



label continuation4:

    scene bg none with sweepclock

    stop music fadeout 2.0
    "Time passes and it’s soon night."
    "Right after dinner, we set up a small campfire and toast some s’mores over the flames."

    play sound audio.sfx_campfire loop
    play music audio.bgm_soft01 fadein 3.0

    scene cg lazulight camping night ver2 with fade

    "Everyone is quiet. There’s only the crackling of the fire, and the crickets chirping in the distance."


    "Though no one makes any attempts to speak, the silence isn’t awkward or discomforting."
    "It’s relaxing and calming, a release from the day’s exhaustive activities."
    "But silence also stirs emotions that surface in the quiet of the night."


    Character1 "…I really like campfires."


    "Though she speaks in a low voice, it cuts through the silence much to our surprise"


    Character1 "You get to sit around them and feel warm, you can even roast s'mores like this, and you can talk about random stuff with others."


    Character1 "The reason why I really wanted to do camping as our first activity… it’s because I really like getting to know people by the warmth of the fire."


    Character1 "This was exactly what I had in mind when I thought of it."
    Character1 "All of us gathered here, together, as we all talk and get to know each other more."


    "In the shadows of the fire, we all let out a small smile."

    play sound audio.sfx_campfire loop fadeout 2.0 fadein 2.0 volume 0.75
    scene cg lazulight camping night with fade

    Character7 "I-{w} I really love cosplay!"

    "Finana’s sudden confession catches us off guard."
    "Though a bit sudden, it feels like a response to Pomu’s words, sharing what she likes so we learn more about her."
    "I guess we all just didn’t expect it to start from her."


    "Noticing our reactions, she turns away, flustered, but Pomu urges her on."

    "She starts describing how she likes both fashion and anime, and that led to her loving cosplay and even cosplaying some of her favorite characters before."
    "This sparks the rest of the conversation, and soon, they are all sharing their likes, dislikes, and even stories of how those came to be."


    "Elira goes on to talk about her love of the Larry Potter books, and Pomu shares stories of dealing with her troublesome cat, Pomusuke."

    "As the talk dies down, they turn towards me with eager eyes."


    scene cg lazulight camping night ver3 with fade


    Character1 "Well, it’s your turn, right?"


    "I always feel it."
    "That although I know so much about these girls, they barely know anything about me."
    "I'm not really trying to avoid telling them, but I can’t deny that I never actively pursue it either."
    "Perhaps… it is time to do so."


    Character2 "I… don’t really have anything I like or dislike in particular, so I guess I’ll just talk about stuff that I used to do?"

    Character1 "That’s okay. We’re all ears."


    Character2 "Back when I was a lot younger, I uh… used to play the violin."


    Character6 "V-Violin?!"

    Character2 "Yeah. But I kinda stopped playing after a couple of years though."


    Character2 "I… got into track and field, and I really liked it there, so I stayed for a long while."


    Character2 "I used to be part of our school’s pole-vaulting team, you know. I was even winning medals and all that."


    Character1 "Oh! So that’s why I felt like I’ve seen you before when we first met."
    Character1 "I used to see you on the field during club hours."

    Character2 "I guess."


    Character2 "Unfortunately, I got into an accident last year."
    Character2 "I shattered my elbow as I hit the ground. A small mistake in my jump cost me everything."


    Character2 "I was hospitalized. Had some minor injuries as well that kept me in there for a long while."
    Character2 "Ever since then, I… haven’t been able to go back."


    Character7 "Are you… okay now?"


    Character2 "Okay…? Physically, I am I guess."
    Character2 "But… sometimes, I get these random bouts of pain from my arm. Sometimes it leads to weird panic attacks and I-"


    Character2 "Just…{w}nevermind."


    "They are all silent with serious looks on their faces."
    "It’s probably hard for them to react to such a heavy story."


    "I don’t usually talk about these things with others."
    "Being at that campfire with those girls made me open up more than I usually would have."


    "It almost felt like fairy magic had taken over me and set my words free."

    Character6 "I… think that’s really brave of you."


    "Elira suddenly speaks out in a soft, comforting voice."


    Character6 "I don’t know how I would have felt had I been in your situation."
    Character6 "But seeing that you’re here now, living your life rather than wallowing in sorrow, I think that’s really strong of you, and I think you’re doing great."


    "I never expected that Elira would comfort me, but I also feel like no one could’ve done such a thing better than her."


    "The kindness of her words feels like the peaceful warmth of the sun as it flows over me and washes away my doubt."


    Character7 "I… also think you’re doing an amazing job."

    "Finana says those words with a surprising vigor."


    Character7 "Even when you have such troubles, you still go out of your way to be kind to someone like me."
    Character7 "I really enjoy being together with you and everyone in Lazulight."
    Character7 "I love spending time with all of you!"
    Character7 "So I’ll do my best…{w} to try to talk more and share more…{w} so you can share all your problems with me as well.{w} Okay?"


    "Finana seems to look tired after that, as if it took all her strength just to get that out clearly to everybody."


    "Though it may seem insignificant to other people, to me, the courage she displayed right then is like a gentle sea breeze that softly urges me onward."


    "I couldn’t help but smile, smile at these wonderful people that I have met."


    "As the night grows older, the flames of the campfire start to die down, and soon, it is time for us to sleep."
    stop sound fadeout 2.0

    scene bg black with fade
    call loading_movie_transition_block(slidingblind)

    play music audio.bgm_morning01 fadeout 2.0 fadein 2.0

    scene bg camping spot by river day with slidingblinds

    show pomu casual happy at set_aligns(MIDDLE_X_SLOT)
    with dissolve

    "Morning dawns and we all wake up early to see the sunrise."
    "While Pomu is up and about with plenty of energy..."
    show elira casual sigh at set_aligns(LEFT_X_SLOT)
    show finana casual sleepy at set_aligns(RIGHT_X_SLOT)
    with slowdissolve
    extend" Finana and Elira on the other hand are still rubbing their eyes trying to shake the sleepiness away."
    show pomu casual happy at bounce_param
    show elira casual smile at bounce_param
    show finana casual happy at bounce_param
    "Soon, the orange glow falls on our faces and we greet the morning with smiles and laughter."
    scene bg camping spot by river day with sweepclock

    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    "After having a quick breakfast, we all pack up our things and get ready to leave for home."
    show pomu casual happy at bounce_param
    show elira casual smile at bounce_param
    show finana casual happy at bounce_param

    "There are the usual shenanigans, the usual talks,{w=0.5} and then the usual goodbyes."
    scene bg river day with sweepright
    show pomu casual neutral at set_aligns(MIDDLE_X_SLOT)
    show elira casual neutral at set_aligns(LEFT_X_SLOT)
    show finana casual neutral at set_aligns(RIGHT_X_SLOT)
    with dissolve
    show pomu casual happy at focus_sprite zorder 50

    Character1 "Well, see you all at school, I guess?"
    show pomu casual neutral at unfocus_sprite zorder 25

    show elira casual smile at focus_sprite zorder 50


    Character6 "Yeah, see you there."
    show elira casual neutral at unfocus_sprite zorder 25

    show finana at focus_sprite zorder 50


    Character7 "Bye bye."
    show finana at unfocus_sprite zorder 25


    Character2 "Bye."


    hide pomu with slowdissolve
    hide elira with slowdissolve
    hide finana with slowdissolve
    "As we go our separate ways, I can’t help but feel a little sad."
    scene bg park with sweepright

    "On the way home, I find myself passing by the park."


    "This was where I first met Pomu."
    "It’s where it all started."
    "Then I got to know Finana on the school’s rooftop, oh and Elira was already pestering me about the club applications in the classroom."
    "Then we founded Lazulight, and that silly name came from that silly rock."


    "All these great things have been happening to me, and it’s been amazing and a lot of fun."
    "Yet somehow…{w=0.5} something still feels…{w=0.5} incomplete."

    "Then, it finally comes."

    stop music fadeout 2.0
    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    play sound [ audio.sfx_heartbeat60 ] loop volume 2.0

    "A sharp pain creeps up from my elbow, and my arm starts to feel numb."


    "I rest at a nearby bench, just until the pain subsides."
    stop sound fadeout 2.0
    hide heartdmg with dissolve
    show layer master
    "I could never get a break from this stupid pain."
    "But why?{w} What else am I missing?{w} What do I need to do to get rid of it?"


    "I try to push those thoughts away as I stand and make my way back home."

    stop sound fadeout 2.0
    scene bg mc room night with slidingblinds

    "Night has already fallen as I lie in my bed,{w} those same thoughts still persisting like little flies inside my brain."


    "It’s back to school tomorrow, but I guess that isn’t so bad."
    "It means having time to hangout with everyone again."
    "That is the only comfort in the otherwise monotonous days of school."
    "In the dark of the night, something catches my eye."
    scene bg mc room night with flash
    "Something is glowing on top of my study table."

    scene cg magic rock with fade

    "As I approach, I realize it’s the rock Finana had found in the river, the blue gem-like rock that led us to the name ‘Lazulight’."


    "On its surface are three lights of different colors."
    "A warm yellow,{w} a soft purple,{w} and a gentle green."

    "The lights look familiar."
    "I am sure I’ve seen them before,{w=0.5} but where exactly?"


    "As I take hold of it, a familiar warmth spreads throughout my body, and then… it’s gone."


    "Confused, I decide to return to bed and close my eyes."

    scene bg mc room night with fade

    "Soon, I find myself drifting to sleep."

    scene bg black with fade
    menu:
        "Play ending? (Opens YouTube in a new browser tab)"
        "Yes":
            $ renpy.run(OpenURL("https://youtu.be/dQw4w9WgXcQ"))
            show text "{color=#fff}Click to continue{/color}"
            pause
        "No":
            pass

    $ persistent.endings.add("demo")

return
