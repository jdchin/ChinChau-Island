class Suspect(object):
	def __init__(self, name, speech):
		self.name = name
		self.speech = speech
	
	def get_name(self):
		return self.name
	
	def get_speech(self):
		return self.speech