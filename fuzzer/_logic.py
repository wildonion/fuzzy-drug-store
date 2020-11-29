





__all__ = ['Antecedent', 'ControlSystem', 'Rule', 'ControlSystemSimulation']



class Antecedent(dict):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__dict__ = self

	def view(self):
		for key in self.__dict__.keys():
			if key == "low":
				print(self.__dict__[key])


class ControlSystem:
	def __init__(self):
		pass


class Rule:
	def __init__(self):
		pass


class ControlSystemSimulation:
	def __init__(self):
		pass