from tkinter import *
import time
import Visualizer

class App:

	def __init__(self, master):

		frame = Frame(master)
#		frame.pack()

		self.master = master
		
		self.var = StringVar(master)
		self.var.set("uniform") # initial value

		self.k_slider = Scale(master, from_=1, to=50, orient=HORIZONTAL, label='K Value', length=300)
		self.k_slider.grid(row=0,column=0, columnspan=2)
		#self.k_slider.pack()

		self.mesh_slider = Scale(master, from_=0.1, to=1.0, orient=HORIZONTAL, label='Mesh Resolution', resolution=0.05, length=300)
		self.mesh_slider.grid(row=1,column=0, columnspan=2)
		#self.mesh_slider.pack()

		self.refresh = Button(master, text="Refresh", command=self.refresh)
		self.refresh.grid(row=2, column=0, columnspan=2)
		#self.refresh.pack(side=LEFT)

		## Define 6 Input Fields

		features = ['pelvic_incidence', 'pelvic_tilt', 'lumbar_lordosis_angle' , 'sacral_slope', 'pelvic_radius', 'degree_spondylolisthesis']

		Label(text='pelvic_incidence', relief=RIDGE,width=30).grid(row=3,column=0)
		self.pelvic_incidence = Entry(relief=SUNKEN,width=8)
		self.pelvic_incidence.grid(row=3,column=1)

		Label(text='pelvic_tilt', relief=RIDGE,width=30).grid(row=4,column=0)
		self.pelvic_tilt = Entry(relief=SUNKEN,width=8)
		self.pelvic_tilt.grid(row=4,column=1)

		Label(text='lumbar_lordosis_angle', relief=RIDGE,width=30).grid(row=5,column=0)
		self.lumbar_lordosis_angle = Entry(relief=SUNKEN,width=8)
		self.lumbar_lordosis_angle.grid(row=5,column=1)

		Label(text='sacral_slope', relief=RIDGE,width=30).grid(row=6,column=0)
		self.sacral_slope = Entry(relief=SUNKEN,width=8)
		self.sacral_slope.grid(row=6,column=1)

		Label(text='pelvic_radius', relief=RIDGE,width=30).grid(row=7,column=0)
		self.pelvic_radius = Entry(relief=SUNKEN,width=8)
		self.pelvic_radius.grid(row=7,column=1)

		Label(text='degree_spondylolisthesis', relief=RIDGE,width=30).grid(row=8,column=0)
		self.degree_spondylolisthesis = Entry(relief=SUNKEN,width=8)
		self.degree_spondylolisthesis.grid(row=8,column=1)

		Label(text='weighting algorithm', width=30).grid(row=9, column=0)
		self.weights = OptionMenu(master, self.var, "uniform", "distance")
		self.weights.grid(row=9, column =1)

	def refresh(self):
		new_entry = [
			float(self.pelvic_incidence.get()),
			float(self.pelvic_tilt.get()),
			float(self.lumbar_lordosis_angle.get()),
			float(self.sacral_slope.get()),
			float(self.pelvic_radius.get()),
			float(self.degree_spondylolisthesis.get())
		]

		print(self.var.get())

		Visualizer.makeGraph(self.k_slider.get(), self.mesh_slider.get(), new_entry, self.var.get())

root = Tk()
app = App(root)
app.master.title("Spinal Classifier Control Panel")

root.mainloop()
