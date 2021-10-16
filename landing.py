import kivy
from kivy.app import App
from kivy.uix.label import Label

# button tiem
from kivy.uix.button import Button

# boxLayout
from kivy.uix.boxlayout import BoxLayout


kivy.require('2.0.0')

# class HelloWorld(App):

# 	def build(self):
# 		return Label(text = "HIIIIIIIIIIIII")


# HelloWorld().run()

class LargestBox(App):
	# for the largest container that 
	def build(self):

		superBox = BoxLayout(orientation='vertical')


		