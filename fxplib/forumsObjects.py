class FxpThread():
	def __init__(self, username, userid, id, title, content,  prefix=''):
		self.username = username
		self.userid = userid

		self.id = id

		self.title = title
		self.content = content
		self.prefix = prefix


class Comment():
	def __init__(self, username, userid, content, threadid, threadtitle, commentid, postsnumber):
		self.username = username
		self.userid = userid

		self.content = content

		self.threadid = threadid
		self.threadtitle = threadtitle
		
		self.id = commentid
		
		self.postsnumber = postsnumber

