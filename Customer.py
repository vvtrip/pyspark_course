class Customer:
 title = ""
 fname = ""
 lname = ""
 isblacklisted = 0
 
 def __init__(self):
  self.title = ""
 
 def __str__(self):
  return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted
 
 def setIsblacklisted(self,isblacklisted):
  self.isblacklisted = isblacklisted
 
 def isblacklisted(self):
  return self.isblacklisted
 
 def setTitle(self,title):
  self.title = title
 
 def getTitle(self):
  return self.title
 
 def setFname(self,fname):
  self.fname = fname
 
 def getFname(self):
  return self.fname
 
 def setLname(self,lname):
  self.lname = lname

 def getLname(self):
  return self.lname

