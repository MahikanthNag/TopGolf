import subprocess
import time
import json

# op = os.system("curl 'https://www.sevenrooms.com/api-yoa/availability/widget/range?venue=topgolfsanjose&time_slot=13:15&party_size=2&halo_size_interval=32&start_date=06-03-2021&num_days=1&channel=SEVENROOMS_WIDGET'")
counter = 1

while(True):
	op = subprocess.run(["curl 'https://www.sevenrooms.com/api-yoa/availability/widget/range?venue=topgolfsanjose&time_slot=13:15&party_size=2&halo_size_interval=32&start_date=11-12-2021&num_days=1&channel=SEVENROOMS_WIDGET'"], shell=True, stdout=subprocess.PIPE).stdout
	op = op.decode('utf-8')
	op = json.loads(op)
	available = False
	for slot in op['data']['availability']['2021-11-12'][0]['times']:
		print(slot)
		if "confirmation_include_end_time" in slot:
			available = True
			break
		# else:
		# 	subprocess.run(["say 'Not Available  Now'"], shell=True, stdout=subprocess.PIPE)

	if available:
		subprocess.run(["say 'Available  Now'"], shell=True, stdout=subprocess.PIPE)
	# else:
	# 	subprocess.run(["say 'Not Available  Now'"], shell=True, stdout=subprocess.PIPE)
	#
	# if (op['data']['availability']['2021-05-29'][0]['times'] is not None) or len(op['data']['availability']['2021-05-29']['times']) > 0:
	# 	subprocess.run(["say 'Available  Now'"], shell=True, stdout=subprocess.PIPE)
	# else:
	# 	subprocess.run(["say 'Not Available  Now'"], shell=True, stdout=subprocess.PIPE)
	print(counter)
	counter+=1
	time.sleep(10)
