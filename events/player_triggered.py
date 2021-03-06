import re

from standard_pattern import player

class player_triggered:
	# "[SC-UBW] Don<2273><BOT><TERRORIST>" triggered "Got_The_Bomb"
	pattern = re.compile(player()+" triggered \"(?P<event>[A-Za-z0-9_]*)\"")

	@staticmethod
	def isMatch(instr):
		return (player_triggered.pattern.match(instr) != None)

	def __init__(self,instr):
		obj = player_triggered.pattern.match(instr)
                self.name = obj.group("name")
                self.uniqueid = obj.group("uniqueid")
                self.steamid = obj.group("steamid")
		self.team = obj.group("team")
		self.event = obj.group("event")
	
	def __str__(self):
		return "player %s (%s) triggered event %s" % (self.name,self.steamid,self.event)

from eventhandler import eventhandler
eventhandler.registerEvent(player_triggered)
