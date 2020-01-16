# newsat

from __future__ import annotations
from typing import List, Union

# States
class State(object):
	__slots__ = ("gc", "actual_Start_Time_X", "Start_With_preheat_X", "EndTime_X", "actual_Start_Time_L", "Start_With_preheat_L", "EndTime_L", "JobProvider_L_location", "i_skip", "JobProvider_X_location", "i", "skip")
	
	def copy_to(self, other: State):
		other.gc = self.gc
		other.actual_Start_Time_X = list(self.actual_Start_Time_X)
		other.Start_With_preheat_X = list(self.Start_With_preheat_X)
		other.EndTime_X = list(self.EndTime_X)
		other.actual_Start_Time_L = list(self.actual_Start_Time_L)
		other.Start_With_preheat_L = list(self.Start_With_preheat_L)
		other.EndTime_L = list(self.EndTime_L)
		other.JobProvider_L_location = self.JobProvider_L_location
		other.i_skip = self.i_skip
		other.JobProvider_X_location = self.JobProvider_X_location
		other.i = self.i
		other.skip = self.skip
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.gc == other.gc and self.actual_Start_Time_X == other.actual_Start_Time_X and self.Start_With_preheat_X == other.Start_With_preheat_X and self.EndTime_X == other.EndTime_X and self.actual_Start_Time_L == other.actual_Start_Time_L and self.Start_With_preheat_L == other.Start_With_preheat_L and self.EndTime_L == other.EndTime_L and self.JobProvider_L_location == other.JobProvider_L_location and self.i_skip == other.i_skip and self.JobProvider_X_location == other.JobProvider_X_location and self.i == other.i and self.skip == other.skip
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gc)) & 0xFFFFFFFF
		for x in self.actual_Start_Time_X:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.Start_With_preheat_X:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.EndTime_X:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.actual_Start_Time_L:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.Start_With_preheat_L:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.EndTime_L:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_L_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i_skip)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_X_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.skip)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "gc = " + str(self.gc)
		result += ", actual_Start_Time_X = " + str(self.actual_Start_Time_X)
		result += ", Start_With_preheat_X = " + str(self.Start_With_preheat_X)
		result += ", EndTime_X = " + str(self.EndTime_X)
		result += ", actual_Start_Time_L = " + str(self.actual_Start_Time_L)
		result += ", Start_With_preheat_L = " + str(self.Start_With_preheat_L)
		result += ", EndTime_L = " + str(self.EndTime_L)
		result += ", JobProvider_L_location = " + str(self.JobProvider_L_location)
		result += ", i_skip = " + str(self.i_skip)
		result += ", JobProvider_X_location = " + str(self.JobProvider_X_location)
		result += ", i = " + str(self.i)
		result += ", skip = " + str(self.skip)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ()
	
	def copy_to(self, other: Transient):
		pass
	
	def __eq__(self, other):
		return isinstance(other, self.__class__)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		return result
	
	def __str__(self):
		result = "("
		result += ")"
		return result

# Automaton: JobProvider_L
class JobProvider_LAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 3, 2, 2]
		self.transition_labels = [[1, 6], [2, 3, 6], [4, 6], [5, 6]]
		self.branch_counts = [[1, 1], [1, 1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.JobProvider_L_location = 0
		state.i_skip = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.JobProvider_L_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.JobProvider_L_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.JobProvider_L_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.JobProvider_L_location
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return (state.gc == (state.Start_With_preheat_L)[0])
			elif transition == 1:
				return (state.gc >= (state.Start_With_preheat_L)[0])
			elif transition == 2:
				return ((state.gc < (state.Start_With_preheat_L)[0]) or (state.gc >= (state.Start_With_preheat_L)[0]))
		elif location == 2:
			if transition == 0:
				return (state.gc == (state.actual_Start_Time_L)[0])
			elif transition == 1:
				return (state.gc < (state.actual_Start_Time_L)[0])
		elif location == 3:
			if transition == 0:
				return (state.gc == (state.EndTime_L)[0])
			elif transition == 1:
				return (state.gc < (state.EndTime_L)[0])
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.JobProvider_L_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.JobProvider_L_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.JobProvider_L_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_L_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_L_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_L_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.i_skip = (state.i_skip + 1)
						target_state.JobProvider_L_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.JobProvider_L_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_L_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_L_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.i_skip = (state.i_skip + 1)
						target_state.JobProvider_L_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_L_location = 3

# Automaton: JobProvider_X
class JobProvider_XAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 3, 2, 2]
		self.transition_labels = [[1, 6], [2, 3, 6], [4, 6], [5, 6]]
		self.branch_counts = [[1, 1], [1, 1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.JobProvider_X_location = 0
		state.i = 0
		state.skip = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.JobProvider_X_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.JobProvider_X_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.JobProvider_X_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.JobProvider_X_location
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return (state.gc == (state.Start_With_preheat_X)[0])
			elif transition == 1:
				return (state.gc >= (state.Start_With_preheat_X)[0])
			elif transition == 2:
				return ((state.gc < (state.Start_With_preheat_X)[0]) or (state.gc >= (state.Start_With_preheat_X)[0]))
		elif location == 2:
			if transition == 0:
				return (state.gc == (state.actual_Start_Time_X)[0])
			elif transition == 1:
				return (state.gc < (state.actual_Start_Time_X)[0])
		elif location == 3:
			if transition == 0:
				return (state.gc == (state.EndTime_X)[0])
			elif transition == 1:
				return (state.gc < (state.EndTime_X)[0])
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.JobProvider_X_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.JobProvider_X_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.JobProvider_X_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_X_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_X_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_X_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_state.skip = (state.skip + 1)
						target_state.JobProvider_X_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.JobProvider_X_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_X_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_X_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						target_state.JobProvider_X_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_X_location = 3

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[6]]
		self.branch_counts = [[1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.gc = min((state.gc + 1), 1)

class PropertyExpression(object):
	__slots__ = ("op", "args")
	
	def __init__(self, op: str, args: List[Union[int, PropertyExpression]]):
		self.op = op
		self.args = args
	
	def __str__(self):
		result = self.op + "("
		needComma = False
		for arg in self.args:
			if needComma:
				result += ", "
			else:
				needComma = True
			result += str(arg)
		return result + ")"

class Property(object):
	__slots__ = ("name", "exp")
	
	def __init__(self, name: str, exp: PropertyExpression):
		self.name = name
		self.exp = exp
	
	def __str__(self):
		return self.name + ": " + str(self.exp)

class Transition(object):
	__slots__ = ("label", "transitions")
	
	def __init__(self, label = 0, transitions = [-1, -1, -1]):
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "transition_labels", "sync_vectors", "properties", "aut_JobProvider_L", "aut_JobProvider_X", "aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "start_p", 2: "preheat", 3: "skip", 4: "available", 5: "not_available", 6: "tick" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0], [1, 1, -1, 1], [2, 2, -1, 2], [3, 3, -1, 3], [4, 4, -1, 4], [5, 5, -1, 5], [6, 6, 6, 6]]
		self.properties = []
		self.aut_JobProvider_L = JobProvider_LAutomaton(self)
		self.aut_JobProvider_X = JobProvider_XAutomaton(self)
		self.aut_GlobalSync = GlobalSyncAutomaton(self)
	
	def get_initial_state(self) -> State:
		state = State()
		state.gc = 0
		state.actual_Start_Time_X = [14, 20]
		state.Start_With_preheat_X = [14, 18]
		state.EndTime_X = [20, 24]
		state.actual_Start_Time_L = [16, 24]
		state.Start_With_preheat_L = [14, 19]
		state.EndTime_L = [18, 28]
		self.aut_JobProvider_L.set_initial_values(state)
		self.aut_JobProvider_X.set_initial_values(state)
		self.aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self.aut_JobProvider_L.set_initial_transient_values(transient)
		self.aut_JobProvider_X.set_initial_transient_values(transient)
		self.aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		result = self.aut_JobProvider_L.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_JobProvider_X.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		return None
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_JobProvider_L = [[], [], [], [], [], [], []]
		transition_count = self.aut_JobProvider_L.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_JobProvider_L.get_guard_value(state, i):
				trans_JobProvider_L[self.aut_JobProvider_L.get_transition_label(state, i)].append(i)
		trans_JobProvider_X = [[], [], [], [], [], [], []]
		transition_count = self.aut_JobProvider_X.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_JobProvider_X.get_guard_value(state, i):
				trans_JobProvider_X[self.aut_JobProvider_X.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], []]
		transition_count = self.aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self.aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for sv in self.sync_vectors:
			synced = [[-1, -1, -1, -1]]
			# JobProvider_L
			if synced is not None:
				if sv[0] != -1:
					if len(trans_JobProvider_L[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_JobProvider_L[sv[0]][0]
						for i in range(1, len(trans_JobProvider_L[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_JobProvider_L[sv[0]][i]
			# JobProvider_X
			if synced is not None:
				if sv[1] != -1:
					if len(trans_JobProvider_X[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_JobProvider_X[sv[1]][0]
						for i in range(1, len(trans_JobProvider_X[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_JobProvider_X[sv[1]][i]
			# GlobalSync
			if synced is not None:
				if sv[2] != -1:
					if len(trans_GlobalSync[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_GlobalSync[sv[2]][0]
						for i in range(1, len(trans_GlobalSync[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_GlobalSync[sv[2]][i]
			if synced is not None:
				for sync in synced:
					sync[3] = sv[3]
				transitions.extend(filter(lambda s: s[-1] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][3], transitions[i])
			del transitions[i].transitions[3]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self.aut_JobProvider_L.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self.aut_JobProvider_L.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self.aut_JobProvider_L.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self.aut_JobProvider_X.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self.aut_JobProvider_X.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self.aut_JobProvider_X.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self.aut_GlobalSync.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 1):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self.aut_JobProvider_L.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self.aut_JobProvider_X.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self.aut_GlobalSync.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
