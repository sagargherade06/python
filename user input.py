import math
radius=5
class circle():
	def getArea(self):
		return math.pi*radius*radius
	def getcircumference(self):
		return radius*2*math.pi
	def showradius():
		print("radius =",radius)
		showradius()
		c=circle()
		print("Area =",c.getArea())
		print("circumference=",c.getcircumference())
