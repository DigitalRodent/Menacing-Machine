# # 2026-05-28  
- I have started the Gantt chart and filled out each task for the Paperwork section and will begin work on my class diagrams.   
- No stumbling blocks yet, thankfully!  
- I will begin the code task section of the Gantt chart once the paperwork is filled and we can assign appropriate dates.   
- I am very tired today but I will get the work done as I must.  
- I used excel and a free Gantt chart template provided with a bunch of useful cells.  

# # 2026-06-02
- We have bought the maqueen and begun work on the line following. We made a track with some A3 sheets and duct tape for lines, and developed a track to test its capabilities.
- Right now it struggles to handle sharp turns and intersections. With only two sensors, we can only gather so much information about the track in an instant and can only take a chance on which direction is the best option.
- I will attempt to develop a method for it to "scan" the track when deciding and use a very simple algorithm to choose which way to take.
- Very excited to continue work on this, its a fun problem-solving exercise.
- Used my brain :)

# # 2026-06-4
- Attempted to improve intersection code, tried to experiment with the compass to see if I could get it to follow a heading. No such luck, unfortunately. The compass is simply too unreliable and hard to work with.
- Still strugging with sharp turns and intersections, trying to figure out how it should scan.
- Will continue working hard!
- Little disquieted
- Used my brain :)

# # 2026-07-30
- Began work on object avoidance code, have a working demo but need to tweak some values and compact the code.
- Turns and intersections are solved now, as long as it doesn't encounter a loop =)
- Will tweak avoidance values
- Used my brain :)
# # 2026-08-06
- Fumbled around and found a line-finding algorithm that worked -- due to hardware limitations, the best you can do is make it go in a spiral in an attempt to stumble into the line. If it doesn't find it, just... go again, elsewhere.
- Now all we need to do for the foundation is marry this line following code and object avoidance code into one thing.
- The plan is to make the bot rely on a main line-following algorithm that splits into seperate tasks then returns to line-following.
- Things are looking good
- Used my brain :)

# # 2026-08-08
- After much deliberation, ended up making some classes so that I could get radio code working. To reference the line following script without creating a recursive loop, RoboGobo needs to be a function in a class.
- Need to fix the stopping code so that it actually /stops/.
- Change of plans aswell - The main code will hold all of the radio receiver code, which will be the robot's main interface for starting and stopping.
- Its getting a bit concerning now, but I'm sure it'll work out.
- Used my brain :)

# # 2026-08-09
- Got headlights working
- Not much else to say, goals remain the same.
- Used my brain :)

# # 2026-08-10
- Let me tell you, Jon, how things have transpired in the past 12 hours. It was looking great, wonderful, fantastic even, and then I realised we still lacked working headlights code. This was concerning, as I was sure to have implemented it. Ha, oops, headlight code was never going to work since the light sensors are LEDs and can only measure very bright lights. Oh well! Surely nothing else will happen as a result of this bot's hardware limitations.
- Then, the radio transmitter got haunted. Inexplicably, it started executing code that I'd *never written in my life*. I got 3 people to confirm that, indeed, the bot was outputting things that should never have even been ABLE to occur. Sure, whatever, I'll just re-import main.py. Nope! Doesn't Work! Why? I DONT KNOW??? Replace the batteries with the other maqueen's batteries - Still broken. And the car maqueen doesn't work now, because the radio's batteries were drained. Great. I'll put those batteries back in the car and - Wha. What's this?? The radio works?! Sure! Great! Let's just roll with that.
- This repeats about 4 times. :). I just stopped touching the radio transmitter after a while and left it running for all my updates.
- Then the car got haunted. Every so often, and I can't predict it, when you turn the car on it'll have funky underlights. If you see the underlights, its a 50/50 that they'll drain whatever's left of the batteries you have in the car. On top of that, sometimes it plays a haunting tone and sets all the lights to max brightness, which is a terrifying thing to happen at 2am in your dark room. Again - never programmed that, nothing on the bot to do that. This one still hasn't been solved, I just have to pray it doesn't happen during the class presentation.
- I have a working theory. Thonny, as I've observed over the course of these weeks, seems to execute code from the bot directly in its GUI. I'm not an expert programmer, by any means, but I find it a little concerning that code in loops from a bot that doesn't have an actual on button is able to execute inside a program on my computer. (Sidenote; All of these haunting, supernatural occurrences only started after I tried to run bugged code and I watched the program *bleed*). I've only ever noticed these occurring around the radio function, and I believe that the radio has been sending bugged code back and forth between the bots from demos, code tests, etc. that were never fully realised and since deleted. And whenever it runs into a block, it'll behave like some rogue ai from beyond the Cyberpunk 2077 blackwall and start executing ancient code stored deep in its now cursed memory, to the human operator's horror.
- I'll confess, at one point I even uploaded all of my code to claude. The entire thing. I gave it the error, and I basically begged it to fix everything.
- The response: "That error isn't really about your code logic — i2c.init() on the line right before it runs fine (that name also comes from from microbit import *), so the wildcard import did work overall. It's specifically that pin15 isn't among the names the microbit module exposes on whatever's currently flashed to your board."
- I HAVEN'T FLASHED THE BOARD SINCE WE STARTED
- I DONT KNOW WHAT TO DO ABOUT THIS
- This final github commit, the final push I'll ever make on this damn program, is a miracle. The fact that this code works somewhat reliably might be a slight against whatever terrible will God had against me tonight. I would dare say my special feature is getting the bot to function in spite of Him, but really it's all of the bot's vocalisations and reactions to the world. 
- Good times had by all though. Alongside me, suffering, were Jack and Alex, who were facing almost identical issues with their own ghosts and ghouls in their Microbit machine. Things are looking bleak for us, but we persist.
- Used my brain :)