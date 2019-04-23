from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserListView
from functools import partial
from kivy.lang import Builder
import webbrowser

class UIManager(FloatLayout):
	fselection = []
	fcselection = []

	def __init__(self, **kwargs):
		super(UIManager, self).__init__(**kwargs)
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="TIGRE", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Medical Imaging Framework", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#ct button
		ct = Button(text=' Tomographic\nReconstruction', pos_hint={'x':.15, 'center_y': .6}, size_hint=(.2, None), font_size=25)
		ct.bind(on_press=self.UnderConstruction)

		#ct blurb
		ctBlurb = Label(text="Under Construction", font_size=15, pos_hint={'x':-.25, 'center_y': .5}, outline_color=[0,0,0,1], outline_width=1)

		#thermography button
		therm = Button(text='Thermography', pos_hint={'x':.65, 'center_y': .6}, size_hint=(.2, None), font_size=25)
		therm.bind(on_press=self.Thermo)

		#therm blurb
		thermBlurb = Label(text="Under Construction", font_size=15, pos_hint={'x':.25, 'center_y': .5}, outline_color=[0,0,0,1], outline_width=1)

		#about button
		about = Button(text='About', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None), font_size=25)
		about.bind(on_press=self.TIGREhub, on_release=self.Menu)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(ct)
		layout.add_widget(ctBlurb)
		layout.add_widget(therm)
		layout.add_widget(thermBlurb)
		layout.add_widget(about)
		layout.add_widget(exit)

	def Close(self, button):
		###closes TIGRE
		self.clear_widgets()
		App.get_running_app().stop()

	def TIGREhub(self, button):
		webbrowser.open("https://github.com/nlaluzerne/TIGRE")

	def Menu(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="TIGRE", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Medical Imaging Framework", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#ct button
		ct = Button(text=' Tomographic\nReconstruction', pos_hint={'x':.15, 'center_y': .6}, size_hint=(.2, None), font_size=25)
		ct.bind(on_press=self.UnderConstruction)

		#ct blurb
		ctBlurb = Label(text="Under Construction", font_size=15, pos_hint={'x':-.25, 'center_y': .5}, outline_color=[0,0,0,1], outline_width=1)

		#thermography button
		therm = Button(text='Thermography', pos_hint={'x':.65, 'center_y': .6}, size_hint=(.2, None), font_size=25)
		therm.bind(on_press=self.Thermo)

		#therm blurb
		thermBlurb = Label(text="Under Construction", font_size=15, pos_hint={'x':.25, 'center_y': .5}, outline_color=[0,0,0,1], outline_width=1)

		#about button
		about = Button(text='About', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None), font_size=25)
		about.bind(on_press=self.TIGREhub, on_release=self.Menu)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(ct)
		layout.add_widget(ctBlurb)
		layout.add_widget(therm)
		layout.add_widget(thermBlurb)
		layout.add_widget(about)
		layout.add_widget(exit)


	def UnderConstruction(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#background image
		background = AsyncImage(source='TIGRE_Oops.jpg')
		
		#page description
		desc = Label(text="Oops! Page Under Construction", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#return button
		ret = Button(text='Return to Menu', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None))
		ret.bind(on_press=self.Menu)

		###adding widgets to the layout
		layout.add_widget(background)
		layout.add_widget(desc)
		layout.add_widget(ret)


	def Thermo(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="Thermo TIGRE", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Medical Thermographic Analysis", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#breast cancer analysis button
		bca = Button(text='Breast Cancer Analysis', pos_hint={'x':.3, 'center_y': .5}, size_hint=(.4, None), font_size=25)
		bca.bind(on_press=self.ImageSelectfc)

		#breast cancer analysis blurb
		bcaBlurb = Label(text="The only option available as of now, but expandable", font_size=15, pos_hint={'x':0, 'center_y': .6}, outline_color=[0,0,0,1], outline_width=1)

		#Help button
		help = Button(text='Help', pos_hint={'x':.15, 'y': .1}, size_hint=(.2, None), font_size=25)
		help.bind(on_press=self.UnderConstruction)

		#Learn More button
		learn = Button(text='Learn More', pos_hint={'x':.65, 'y': .1}, size_hint=(.2, None), font_size=25)
		learn.bind(on_press=self.UnderConstruction)

		#back button
		back = Button(text='Back', pos_hint={'x':0, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		back.bind(on_press=self.Menu)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(bca)
		layout.add_widget(bcaBlurb)
		layout.add_widget(help)
		layout.add_widget(learn)
		layout.add_widget(back)
		layout.add_widget(exit)


	def ImageSelectfc(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="Image Select", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Select a Cooled Image", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#file chooser
		fchooser = FileChooserListView(pos_hint={'x':.25, 'y': .175}, size_hint=(.5, .6))

		#results button
		results = Button(text='Next', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None), font_size=25)
		results.bind(on_press=partial(self.loadfcImage, fchooser), on_release=self.ImageSelectf)

		#back button
		back = Button(text='Back', pos_hint={'x':0, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		back.bind(on_press=self.Thermo)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(fchooser)
		layout.add_widget(results)
		layout.add_widget(back)
		layout.add_widget(exit)

	def loadfcImage(self, filechooser, button):
		self.fcload(filechooser.selection)
	def fcload(self, selection):
		global fcselection
		fcselection = selection


	def ImageSelectf(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="Image Select", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Select a not Cooled Image", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#file chooser
		fchooser = FileChooserListView(pos_hint={'x':.25, 'y': .175}, size_hint=(.5, .6))

		#results button
		results = Button(text='Next', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None), font_size=25)
		results.bind(on_press=partial(self.loadfImage, fchooser), on_release=self.ImgCrop)

		#back button
		back = Button(text='Back', pos_hint={'x':0, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		back.bind(on_press=self.Thermo)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(fchooser)
		layout.add_widget(results)
		layout.add_widget(back)
		layout.add_widget(exit)

	def loadfImage(self, filechooser, button):
		self.fload(filechooser.selection)
	def fload(self, selection):
		global fselection
		fselection = selection


	def ImgCrop(self, button):
		###page setup
		global fcselection
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="Image Crop", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Crop any extra space/extremities.", font_size=50, pos_hint={'x':0, 'center_y': .8}, outline_color=[0,0,0,1], outline_width=1)

		#image 1
		wimg = Image(source=fcselection[0])

		#results button
		results = Button(text='Next', pos_hint={'x':.4, 'y': .05}, size_hint=(.2, None), font_size=25)
		results.bind(on_press=self.Results)

		#back button
		back = Button(text='Back', pos_hint={'x':0, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		back.bind(on_press=self.Thermo)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(wimg)
		layout.add_widget(results)
		layout.add_widget(back)
		layout.add_widget(exit)

	def Results(self, button):
		###page setup
		self.clear_widgets()
		layout = FloatLayout()
		self.add_widget(layout)

		###widgets setup

		#page title
		title = Label(text="Results", font_size=100, pos_hint={'x':0, 'center_y': .9}, outline_color=[0,0,0,1], outline_width=1)

		#page desc
		desc = Label(text="Our classifier indicates a 85% chance of a tumor.", font_size=35, pos_hint={'x':0, 'y': 0}, outline_color=[0,0,0,1], outline_width=1)

		#Export PDF button
		pdf = Button(text='Export PDF', pos_hint={'x':.15, 'y': .1}, size_hint=(.2, None), font_size=25)
		pdf.bind(on_press=self.UnderConstruction)

		#Export CSV button
		csv = Button(text='Export CSV', pos_hint={'x':.65, 'y': .1}, size_hint=(.2, None), font_size=25)
		csv.bind(on_press=self.UnderConstruction)

		#back button
		back = Button(text='Back', pos_hint={'x':0, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		back.bind(on_press=self.Thermo)

		#exit button
		exit = Button(text='Exit', pos_hint={'x':.95, 'bottom_y': 1}, size_hint=(.05, .05), font_size=20)
		exit.bind(on_press=self.Close)

		###adding widgets to layout
		layout.add_widget(title)
		layout.add_widget(desc)
		layout.add_widget(pdf)
		layout.add_widget(csv)
		layout.add_widget(back)
		layout.add_widget(exit)



class TIGREApp(App):
	def build(self):
		self.root = root = UIManager()
		root.bind(size=self._update_rect, pos=self._update_rect)
		with root.canvas.before:
			Color(.5647, .5647, .5647, 1) #background colour
			self.rect = Rectangle(size=root.size, pos=root.pos)
		return root

	def _update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size

if __name__ == "__main__":
	Window.fullscreen = 'auto' #if wanting fullscreen
	TIGREApp().run()
