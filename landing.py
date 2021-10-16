import kivy
from kivy.app import App
from kivy.uix.label import Label

# button tiem
from kivy.uix.button import Button

# boxLayout
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')
class LargestBox(App):
	# for the largest container that 
	def build(self):

		superBox = BoxLayout(orientation='vertical')

		# code to show how to use nested boxlayouts.
# class in which we are creating the button by using boxlayout
# defining the App class
class BoxLayoutApp(App):
	
	def build(self):

		# To position oriented widgets again in the proper orientation
		# use of vertical orientation to set all widgets
		superBox = BoxLayout(orientation ='vertical')
		

		camBox = BoxLayout(orientation = 'vertical')
		btncam = Label(text ="yo face")

		camBox.add_widget(btncam)

		# To position widgets next to each other,
		# use a horizontal BoxLayout.
		bottomBox = BoxLayout(orientation ='horizontal')
		resultLabel = Label(text ="Left/Right")
		btn2 = Button(text ="Start")

		# HB represents the horizontal boxlayout orientation
		# declared above
		bottomBox.add_widget(resultLabel)
		bottomBox.add_widget(btn2)

		# To position widgets above/below each other,
		# use a vertical BoxLayout.
		# superbox used to again align the oriented widgets
		superBox.add_widget(camBox)
		superBox.add_widget(bottomBox)

		return superBox

# creating the object root for BoxLayoutApp() class
root = BoxLayoutApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
if __name__ == "__main__":
	root.run()

