from random import shuffle
from tqdm import tqdm

players = []

# Unique-ify list algorithm (f5) taken from this page: https://www.peterbe.com/plog/uniqifiers-benchmark
def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

num_players = int(raw_input("How many players in this league?:  "))
print("")

for i in range(0,num_players):
	entry = raw_input("Enter unique name and entries (format: name, entries):  ").split(",")
	player = entry[0].strip()
	count = entry[1].strip()
	# player_names.append(player)
	for j in range(0, int(count)):
		players.append(player)
	# print (player + " has " + count + " entries")

print("")
shuffle_count = int(raw_input("How many times would you like to shuffle?:  "))
print("")

for i in tqdm(range(0, shuffle_count)):
	shuffle(players)

print(f5(players))
print("")
