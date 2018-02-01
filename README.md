# FXaPi
Fxp python api


## Example
```python
import time
from fxplib import *

@FxpEvents.on('newcomment')
def on_newcomment_handle(data):
	print ('New comment')
	print (data)

@FxpEvents.on('newpm')
def on_newpm_handle(data):
	print ('New pm')

@FxpEvents.on('newthread')
def on_newtread_handle(data):
	print ('New thread')
	
user = fxp('FXP-USERNAME','FXPֹֹֹ-PASSWORD')

if user.login():
	print ('[*] Login success - %s' % user.username)

	live = user.livefxp.connect(debug=False)
	if live == False:
		print ('[*] Error while creating live connection')
	else:
		user.livefxp.addForum(21)
		while True:
			time.sleep(1)

```