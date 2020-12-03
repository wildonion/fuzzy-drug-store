


import matplotlib.pyplot as plt


__all__ = ['Antecedent', 'Consequent', 'ControlSystem', 'Rule', 'ControlSystemSimulation']



class Antecedent(dict): # input
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__dict__ = self

	def view(self):
		for key in self.__dict__.keys():
			if key == "name" or key == "range":
				continue
			plt.ylabel('Membership')
			plt.legend()
			plt.ylim(self.__dict__["range"])
			plt.plot(self.__dict__[key], label=key)
		plt.show()


class Consequent(dict): # output
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__dict__ = self

	def view(self):
		pass


class ControlSystem:
	def __init__(self):
		pass


class Rule:
	def __init__(self):
		pass

	def view(self):
		pass


class ControlSystemSimulation:
	def __init__(self):
		pass