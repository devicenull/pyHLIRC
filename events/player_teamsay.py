import re

from standard_pattern import player

class player_teamsay:
	# "[SC-UBW] Mike<2277><BOT><TERRORIST>" say_team "wtf?"
	pattern = re.compile(player()+" say_team \"(?P<message>.*)\"")

	@staticmethod
	def isMatch(instr):
		return (player_teamsay.pattern.match(instr) != None)

	def __init__(self,instr):
		obj = player_teamsay.pattern.match(instr)
		self.name = obj.group("name")
		self.uniqueid = obj.group("uniqueid")
		self.steamid = obj.group("steamid")
		self.message = obj.group("message")
	
	def __str__(self):
		return "%s team says %s" % (self.name,self.message)

from eventhandler import eventhandler
eventhandler.registerEvent(player_teamsay)
