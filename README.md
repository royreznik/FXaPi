# FXaPi
Fxp python api

## About
I created the api for my own personal use, i made bots and some other cool stuff.

## Basics
```python
#user = fxp from fxplib
```

```python
#Login
#try login and return True if successed or False if failed
user.login()
```

```python
#createThread
#create new thread in certain forum
user.createThread(TITLE, CONTENT, FORUM_ID)
```

```python
#comment
#comment on thread
user.comment(THREAD_ID, CONTENT)

#editComment
#edit your comment
#if ADD is True app will add the CONTENT to the existing CONTENT
user.editComment(COMMENT_ID, CONTENT, ADD)

#reply
#reply message CommentClass
user.reply(CommentClass, ReplyData, spamPrevention=False):
```

```python
#like
#like comment, return True if successed or False if failed
user.like(COMMENT_ID)
```

```python
#createPrivateChat
#start chat with username
user.createPrivateChat(TO_USERNAME, TITLE, CONTENT)

#sendPrivateChat
#send message to existing chat
usser.sendPrivateChat(TO_USERNAME, FIRST_PM_ID, CONTENT)
```

```python
#updateProfileImage
#update user profile picture, IMG_PATH could be a url or system path
user.updateProfileImage(IMG_PATH)
```

## Live Events System
```python
@FxpEvents.on('newcomment')
def on_newcomment_handle(comment):
	#comment is is Class object that contain username, userid, content, threaid, threadtitle, id 
```

```python
@FxpEvents.on('newthread')
def on_newnewthread_handle(fxpThread):
	#fxpThread is is Class object that contain username, userid, id, title, content, prefix
```

```python
@FxpEvents.on('newpm')
def on_newpm_handle(data):
	#data is a dict object
```

## Example
```python
import time
from fxplib import *

@FxpEvents.on('newcomment')
def on_newcomment_handle(comment):
	print ('New comment')
	print (data)

@FxpEvents.on('newpm')
def on_newpm_handle(data):
	print ('New pm')

@FxpEvents.on('newthread')
def on_newtread_handle(data):
	print ('New thread')
	
user = fxp('FXP_USERNAME','FXPֹֹֹ_PASSWORD')

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

## Todo List
- [x] Finish the base
- [ ] Organize my code
- [ ] Add more web interface features
- [ ] fxpLive class rewriting

## Screenshots
![Console](https://image.prntscr.com/image/_ZhGSXDmTPquViv0wQOgUA.png)