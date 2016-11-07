from suspect import Suspect
from player import Player
class Engine(object):

	def __init__(self,location_map):
		self.location_map = location_map

	def play(self):
		current_location = self.location_map.opening_location()
		last_location = self.location_map.next_location('animalia')

		while current_location != last_location:
			next_location_name = current_location.enter()
			current_location = self.location_map.next_location(next_location_name)

		current_location.enter()


class Criminal(Suspect):
    def __init__(self, name, speech):
    	super(Criminal, self).__init__(name, speech)

class Location(object):
	def __init__(self, sspct1, sspct2, crmnl, player):
		self.suspect1 = sspct1
		self.suspect2 = sspct2
		self.criminal = crmnl
		self.player = player
	def enter(self):
		print "Hi."
		exit(1)

class TheBurrows(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(TheBurrows, self).__init__(suspect1, suspect2, criminal, player)
	def enter(self):
		print """
One upon a time, there was a squirrel named Sterny.
Sterny was excited because he had just been given a stack of golden acorns from his father,
which had been given to him by his father, which had been given to him by his father and so on.
Unfortunately, one night, when Sterny was asleep, a gang of predators snuck into Sterny's house and stole his acorn stash.
When Sterny awoke the next day, he was devastated.
'MY ACORNS ARE GONE! SOMEONE STOLE THEM!', Sterny said in shock.
'I WILL FIND WHOEVER STOLE THEM AND MAKE THEM PAY!'
			"""
		raw_input("Press any key to continue\n")
		print """
He decided he was going to search the entire city to find his acorns.
He figured he would start where he was, the Burrows.
He suspected three people might be the criminal.
			"""
		raw_input("Press any key to continue\n")
		print """
Suspect #1: Sterny Sr.
When Sterny looked at his drawer, where he kept his acorns, he saw a trail of dandruff leading to his grandpa's room.
			"""
		raw_input("Press any key to continue\n")

		print """
Suspect #2: Sylvia
He remembered catching his sister in his drawer several times without his permission.
			"""
		raw_input("Press any key to continue\n")

		print """
Suspect #3: Stella
His aunt cleans his room on the daily basis and often complains about having financial issues.
She could
			"""

		self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)

		return "downtown"

class Downtown(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(Downtown, self).__init__(suspect1, suspect2, criminal,player)
	def enter(self):
		print """
When Sterny went Downtown, he suspected three people would be the thief.
"""
		raw_input("Press any key to continue\n")

		print """
Suspect #1: Richy Rich
Richy Rich has been eyeing Sterny's acorns for some time now and even offered him $1 million for one.
Unlike other people, Sterny denied his offer and decided to keep them.
Richy Rich became angry, since he had never gotten rejected before.
        """
		raw_input("Press any key to continue\n")

		print """
Suspect #2: Barry the Baboon
Barry has been following Sterny around the city for a long time for no reason.
Barry recently stopped following Sterny after his acorns went missing.
        """

		raw_input("Press any key to continue\n")

		print """
Suspect #3: Peter the Pigeon
Peter is fascinated by acorns and has a large collection of them at home.
He once asked Sterny where he had gotten his from and was denied possession of one.
        """

		self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)

		return "sahara"

class SaharaSquare(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(SaharaSquare, self).__init__(suspect1, suspect2, criminal,player)
	def enter(self):
		print """
Sterny went to Sahara Square and knew there could only be three suspects that would even dare to touch his precious acorns.
        """
		raw_input("Press any key to continue\n")

		print """
Suspect #1: Corey the Camal
Corey needs money to get out of the desert.
He is tired of having to look for water every three weeks to live.
He heard Sterny inherited a sack of acorns, which could probably give him enough money to leave the desert.
        """
		raw_input("Press any key to continue\n")

		print """
Suspect #2: Euphora the Elephant
He is loyal to his family and is willing to do whatever it takes to keep them happy.
        """

		raw_input("Press any key to continue\n")

		print """
Suspect #3: Larry the Lizard
He is known as the theif in town.
He is able to steal anyone's possessions without ever getting caught, with the ability to camouflage with his surroundings.
        """

		self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)

		return "tundra"

class TundraTown(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(TundraTown, self).__init__(suspect1, suspect2, criminal,player)
	def enter(self):
		print """
Sterny has arrived to Tundra Town in search for his acorns.
        """
		raw_input("Press any key to continue\n")

		print """
Suspect #1: Pablo the Polar Bear
Polar Bear was mad with Sterny for leaving his stranded in the Tundra Town.
"""
		raw_input("Press any key to continue\n")

		print """
Suspect #2: Penelope the Penguin
Penelope is a kind young lady and has been nothing but nice to Sterny.
She invited Sterny over to her house for a slumber party.
However, it has been said that when she's around things go missing.
        """
		raw_input("Press any key to continue\n")

		print """
Suspect #3: Mobey the Moose
Mobey is a calm guy and has never been accused of stealing anything.
In fact, people trust him to watch over their house when they go on vacation.
However, some people still can't be trusted.
        """

		self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)

		return "rainforest"
class Rainforest(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(Rainforest, self).__init__(suspect1, suspect2, criminal, player)

	def enter(self):
		print "You enter the rainforest, home to millions of plants and biotic species."
		print "You realize that Sniper the Snake always slithers around the Tree of Life."
		print "You also realize that Tom the Toucan enjoys stealing shiny things."
		print "Finally, you remember that Mitch the Monkey likes collecting yellow objects (especially bananas!)"
		print "Who would you like to investigate? Or, choose a criminal. (%s, %s, %s, choose)?" % (self.suspect1.get_name(),
		self.suspect2.get_name(), self.criminal.get_name())

		action = raw_input("> ")
		choice = True

		while choice:
			if action == self.suspect1.get_name():
				self.player.investigate(self.suspect1)
				print "You find Sniper's journal lying next to his snake hole."
				print "You read that he was sniping animal terrorists the day your acorns were stolen."
				print "He worked at the Tree of Life lately and found that one animal has been stealing something."
				print "What would you like to do next, choose the criminal or investigate another suspect? (choose, %s, %s)" % (self.suspect2.get_name(),
				self.criminal.get_name())
				action = raw_input("> ")
			elif action == self.suspect2.get_name():
				self.player.investigate(self.suspect2)
				print "You enter Tom's birdhouse during the midst of day."
				print "All around, you see a plethora of fine dining utensils, from forks to spoons to fancy knives."
				print "Nothing golden however, but in the corner your eye, you see a safe."
				print "It seems too big to hold an acorn, but who knows?"
				print "What would you like to do next, choose the criminal or investigate another suspect? (choose, %s, %s)" % (self.suspect1.get_name(),
				self.criminal.get_name())
				action = raw_input("> ")
			elif action == self.criminal.get_name():
				self.player.investigate(self.criminal)
				print "You enter Mitch's crib. The place looks sketchy and dilapidated."
				print "Right in the middle, you see a fountain of bananas."
				print "You also see pineapples. Do monkeys even like pineapples?"
				print "There are also golden apples, but no acorn."
				print "Nice try Mitch, but I see a small golden acorn nested within everything."
				print "What would you like to do next, choose the criminal or investigate another suspect? (choose, %s, %s)" % (self.suspect1.get_name(),
				self.suspect2.get_name())
				action = raw_input("> ")
			elif action == "choose":
				self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)
				choice = False
			else:
				print "That is not a suspect!"
				print "What would you like to do next, choose the criminal or investigate another suspect? (choose, %s, %s, %s)" % (self.suspect1.get_name(), self.suspect2.get_name(), self.criminal.get_name())
				action = raw_input("> ")

		return "docks"

class Docks(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(Docks, self).__init__(suspect1, suspect2, criminal,player)
	def enter(self):
		print "As you walk out the humid rainforest, you spot a large docking area out towards the shore."
		print "Out in the distance you spot the docks to the left, the dam out towards the right, and the beach straight ahead."
		print "At the docks you spot Pete the Pelican scurrying place to place as he hands out the mail form his bill"
		print "At the dam you spot Bucky the Beaver shouting at his workers as he paces left to right to check on things."
		print "By the beach you spot a whales coming up the shore one by one in order to catch a breath. Surely Walter the Whale will come up soon."
		print "Would you like to investigate %s, %s, %s or choose the criminal?" % (self.suspect1.get_name(), self.suspect2.get_name(),
		self.criminal.get_name())


		action = raw_input("> ")
		done = True
		while (done):
		# Player either chooses a suspect to investigate or chooses the suspect he/she
		# thinks is the criminal.
			if action == self.suspect1.get_name():
				self.player.investigate(self.suspect1)
				print "You approach Pete the Pelican hand mail to the workers at the dock."
				print "Looking at his bill, you see that Pete takes out mail quickly."
				print "After observing his habits, you see his bill get smaller and smaller until it looks flappy and empty."
				print "As soon as you finished observing his actions, you walk up to him and asked him to give his testimony for the current case."
				print "As Pete turned around, he flew straight towards the direction of the mail post."
				action = raw_input("> ")
			elif action == self.suspect2.get_name():
				print" Walking up the stairs you spot Bucky shouting and flapping his tail feverishly."
				print "As soon as he was done, you see him anxiously walk back to his office in order to check things"
				print "Two minutes later, you see him walk towards a different section of the dam."
				print "Bucky later shouts at the workers at the different post"
				print "During your ten minute observation, you see Bucky repeat these same actions but in different locations of the dam"
				print "Since you did not know why he was walking back towards his office, you figured that it would be best to ask him"
				print "As soon as you finished observing his actions, you walk up to him and asked him to give his testimony for the current case."
				print "Walking away disappointed with the way he acted, you left him off to do his work."
				print "What would you like to do next?(%s, %s, %s, choose)" % (self.suspect1.get_name(),self.suspect2.get_name(),self.criminal.get_name())
				action = raw_input("> ")
			elif action == self.criminal.get_name():
				print " Walking straight up the shore, you spot the whale family taking their turns to come up the surface."
				print "As they shot up out the surface, you observe the individuals that are coming up"
				print "In your head you keep track of the whales."
				print "Wally, Wilma, Wendy, Warren, and Wanda"
				print "Five minutes later, you noticed that no one else had come up for air"
				print "Why would Walter's whole family pop up for air expect for himself"
				print " Swimming out towards the shore, you decide to ask Walter for his testimony with your best whale call."
				print "Swimming back to the shore, you think to yourself how it is odd with the fact that Walter would need to come up at least once for air"
				print "Since whales are mammals, he would normally come up for air."
				print "What would you like to do next? (%s, %s, %s, choose)" % (self.suspect1.get_name(),self.suspect2.get_name(),self.criminal.get_name())
				action = raw_input("> ")
			elif action == "choose":
				self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)
				done = False
			else:
				print "Please choose an action to take."
				action = raw_input("> ")



		return "outback island"

class Outback_Island(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(Outback_Island, self).__init__(suspect1, suspect1, criminal, player)
	def enter(self):
		return "animalia"

class Animalia(Location):
	def __init__(self, suspect1, suspect2, criminal, player):
		super(Animalia, self).__init__(suspect1, suspect2, criminal, player)

	def enter(self):
		print"""
You have arrived to the Animalia Stadium, the location where all criminals get
executed! However, you know that there is at least one more missing golden acorn.
You see Remi the Rat scurrying across the popcorn stand with a super large popcorn
bag. You also see Luster the Lion with the mic, ready to recite a speech for the
next set of criminal executions. Lastly you see Gia the Giraffe ordering some food
from the herbivore stand.
Would you like to investigate %s, %s, %s or choose the criminal?
(%s, %s, %s, choose)
		""" % (self.suspect1.get_name(), self.suspect2.get_name(),
		self.criminal.get_name(), self.suspect1.get_name(), self.suspect2.get_name(),
		self.criminal.get_name())

		action = raw_input("> ")

		done = True
		while (done):
		# Player either chooses a suspect to investigate or chooses the suspect he/she
		# thinks is the criminal.
			if action == self.suspect1.get_name():
				self.player.investigate(self.suspect1)
				print "What would you like to do next?"
				action = raw_input("> ")
			elif action == self.suspect2.get_name():
				self.player.investigate(self.suspect2)
				print "What would you like to do next?"
				action = raw_input("> ")
			elif action == self.criminal.get_name():
				self.player.investigate(self.criminal)
				print "What would you like to do next?"
				action = raw_input("> ")
			elif action == "choose":
				self.player.choose(self.suspect1, self.suspect2, self.criminal, self.player)
				done = False
			else:
				print "Please choose an action to take."
				action = raw_input("> ")

		print self.player.get_sus_list()
		return self.end_game()

	def end_game(self):
		#Method for printing the Police Report, a file that is written based off the player's suspect list, then read to the player.
		print"""
You have reached the final destination of Zootopia.
		"""
		crim_list = ['Sylvia', 'Richy', 'Lary', 'Penelope', 'Mitch', 'Walter',  'Remi']
		report = open("polport.txt", 'w')
		acorns = 0
		for elem in crim_list:
			if elem in self.player.get_sus_list():
				acorns = acorns + 1
		report.write("Greetings Sterny,\n\n")
		report.write("Here is your police report.\n\n")
		report.write("Out of the 7 golden acorns you have inherited, you were able to retrieve %d.\n" % (acorns))
		report.write("""
If you were able to correctly capture all of the
criminals, congratulations! However, if you have falsely accused an animal, note
that it is your fault that he/she is on death row.
"""
		)
		report.close()
		report = open ("polport.txt")
		print report.read()
		report.close()
class Map(object):
	Squirrel = Player([])
	#Bunny Burrows
	sterny_jr = Suspect("Sterny Jr", "Hello")
	sylvia = Suspect("Sylvia", "Helloiuhuiohi")
	stella = Suspect("Stella", "Hellohjjytyj ")
	#Downtown
	richy = Suspect("Richy", "Hello")
	barry = Suspect("Barry", "Helloiuhuiohi")
	peter = Suspect("Peter", "Hellohjjytyj ")
	#SaharaSquare
	corey = Suspect("Corey", "Hello")
	euphora = Suspect("Euphora", "Helloiuhuiohi")
	lary = Suspect("Lary", "Hellohjjytyj ")
	#TundraTown
	pablo = Suspect("Pablo", "Hello")
	penelope = Suspect("Penelope", "Helloiuhuiohi")
	mobey = Suspect("Mobey", "Hellohjjytyj ")
	#Rainforest
	sniper = Suspect("Sniper", "Hi, I'm Sniper the Snake.")
	tom = Suspect("Tom", "Hi, I'm Tom the Toucan.")
	mitch = Suspect("Mitch", "Hi, I'm Mitch the Monkey.")
	#Docks
	pete = Suspect("Pete", "")
	bucky = Suspect("Bucky", "Helloiuhuiohi")
	walter = Suspect("Walter", "Hellohjjytyj ")
	#Outback_Island
	todd = Suspect("Todd", "Hello")
	danielle = Suspect("Danielle", "Helloiuhuiohi")
	willy = Suspect("Willy", "Hellohjjytyj ")
	#Animalia
	luster = Suspect("Luster", "You see Luster the Lion concentrating on memorizing his speech. He takes his job as Mayor very seriously.")
	gia = Suspect("Gia", "You see Gia the Giraffe leaving the herbivore stand with a bunch of herbivore food in she popcorn bag.\n You watch Gia as she walks next to the entrance of the indoor stadium and starts looking around. \n It seems like she is searching for someone...")
	remi = Suspect("Remi", "You watch Remi the Rat as he tries to jump on the popcorn stand. \nSuddenly, he misses the jump and falls, dropping the popcorn bag spilling the popcorn. \nWait a second... You notice that the popcorn is not actually popcorn,\nbut actually some unique small objects that seem rare and expensive.")

	crim_list = [sylvia, richy, lary, penelope, mitch, walter, todd, remi]

	locations = {
	'burrows' : TheBurrows(sterny_jr, sylvia, stella, Squirrel),
	'downtown' : Downtown(richy, barry, peter, Squirrel),
	'sahara' : SaharaSquare(corey, euphora, lary, Squirrel),
	'tundra' : TundraTown(pablo, penelope, mobey, Squirrel),
	'rainforest' : Rainforest(sniper, tom, mitch, Squirrel),
	'docks' : Docks(pete, bucky, walter, Squirrel),
	'outback island' : Outback_Island(todd, danielle, willy, Squirrel),
	'animalia' : Animalia(luster, gia, remi, Squirrel),
	}
	def __init__(self,start_location):
		self.start_location = start_location

	def next_location(self, location_name):
		loc = Map.locations.get(location_name)
		return loc

	def opening_location(self):
		return self.next_location(self.start_location)

"""squirrel = Player()
sniper_the_snake = Suspect("Sniper", "Hi, I'm Sniper the Snake.")
tom_the_toucan = Suspect("Tom", "Hi, I'm Tom the Toucan.")
mitch_the_monkey = Suspect("Mitch", "Hi, I'm Mitch the Monkey.")
animal = Rainforest(sniper_the_snake, tom_the_toucan, mitch_the_monkey, squirrel)
animal.enter()"""

zoo_map = Map('burrows')
zootopia = Engine(zoo_map)
zootopia.play()
