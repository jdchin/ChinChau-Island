class Player(object):
	def __init__(self, sus_list):
		self.sus_list = sus_list
		
	def investigate(self, suspect):
		print suspect.get_speech()
	
	def add_to_list(self, suspect):
		self.sus_list.append(suspect)
	
	def choose(self, suspect1, suspect2, criminal, player):
		choose_crim = True
		
		while choose_crim:
			print "Who is the criminal? (%s, %s, %s)?" % (suspect1.get_name(), suspect2.get_name(), criminal.get_name())
			crim = raw_input("> ")
			while( crim != suspect1.get_name() and crim != suspect2.get_name() and crim != criminal.get_name()):
				print "That's not a suspect!"
				crim = raw_input("> ")
			print "You have added %s to your criminal list" % (crim)
			player.add_to_list(crim)
			choose_crim = False
		
	def get_sus_list(self):
		return self.sus_list
