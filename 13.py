# 13

from __future__ import annotations
from typing import List, Union

# States
class State(object):
	__slots__ = ("jobStartTimes_X", "jobEndTimes_X", "counter_X", "jobAccepted_X", "jobStartTimes_U", "jobEndTimes_U", "counter_U", "jobAccepted_U", "gc", "numOfJobsPerformed", "numOfJobsSkipped", "success", "battery_capacity", "jobProvider_X_location", "job_X_location", "internal", "jobProvider_U_location", "job_U_location", "battery_location", "timer_location")
	
	def copy_to(self, other: State):
		other.jobStartTimes_X = list(self.jobStartTimes_X)
		other.jobEndTimes_X = list(self.jobEndTimes_X)
		other.counter_X = self.counter_X
		other.jobAccepted_X = self.jobAccepted_X
		other.jobStartTimes_U = list(self.jobStartTimes_U)
		other.jobEndTimes_U = list(self.jobEndTimes_U)
		other.counter_U = self.counter_U
		other.jobAccepted_U = self.jobAccepted_U
		other.gc = self.gc
		other.numOfJobsPerformed = self.numOfJobsPerformed
		other.numOfJobsSkipped = self.numOfJobsSkipped
		other.success = self.success
		other.battery_capacity = self.battery_capacity
		other.jobProvider_X_location = self.jobProvider_X_location
		other.job_X_location = self.job_X_location
		other.internal = self.internal
		other.jobProvider_U_location = self.jobProvider_U_location
		other.job_U_location = self.job_U_location
		other.battery_location = self.battery_location
		other.timer_location = self.timer_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.jobStartTimes_X == other.jobStartTimes_X and self.jobEndTimes_X == other.jobEndTimes_X and self.counter_X == other.counter_X and self.jobAccepted_X == other.jobAccepted_X and self.jobStartTimes_U == other.jobStartTimes_U and self.jobEndTimes_U == other.jobEndTimes_U and self.counter_U == other.counter_U and self.jobAccepted_U == other.jobAccepted_U and self.gc == other.gc and self.numOfJobsPerformed == other.numOfJobsPerformed and self.numOfJobsSkipped == other.numOfJobsSkipped and self.success == other.success and self.battery_capacity == other.battery_capacity and self.jobProvider_X_location == other.jobProvider_X_location and self.job_X_location == other.job_X_location and self.internal == other.internal and self.jobProvider_U_location == other.jobProvider_U_location and self.job_U_location == other.job_U_location and self.battery_location == other.battery_location and self.timer_location == other.timer_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		for x in self.jobStartTimes_X:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.jobEndTimes_X:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.counter_X)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobAccepted_X)) & 0xFFFFFFFF
		for x in self.jobStartTimes_U:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.jobEndTimes_U:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.counter_U)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobAccepted_U)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gc)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.numOfJobsPerformed)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.numOfJobsSkipped)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.success)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.battery_capacity)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobProvider_X_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.job_X_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.internal)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobProvider_U_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.job_U_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.battery_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.timer_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "jobStartTimes_X = " + str(self.jobStartTimes_X)
		result += ", jobEndTimes_X = " + str(self.jobEndTimes_X)
		result += ", counter_X = " + str(self.counter_X)
		result += ", jobAccepted_X = " + str(self.jobAccepted_X)
		result += ", jobStartTimes_U = " + str(self.jobStartTimes_U)
		result += ", jobEndTimes_U = " + str(self.jobEndTimes_U)
		result += ", counter_U = " + str(self.counter_U)
		result += ", jobAccepted_U = " + str(self.jobAccepted_U)
		result += ", gc = " + str(self.gc)
		result += ", numOfJobsPerformed = " + str(self.numOfJobsPerformed)
		result += ", numOfJobsSkipped = " + str(self.numOfJobsSkipped)
		result += ", success = " + str(self.success)
		result += ", battery_capacity = " + str(self.battery_capacity)
		result += ", jobProvider_X_location = " + str(self.jobProvider_X_location)
		result += ", job_X_location = " + str(self.job_X_location)
		result += ", internal = " + str(self.internal)
		result += ", jobProvider_U_location = " + str(self.jobProvider_U_location)
		result += ", job_U_location = " + str(self.job_U_location)
		result += ", battery_location = " + str(self.battery_location)
		result += ", timer_location = " + str(self.timer_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("R_Succ_Sent_edge_reward", "cost")
	
	def copy_to(self, other: Transient):
		other.R_Succ_Sent_edge_reward = self.R_Succ_Sent_edge_reward
		other.cost = self.cost
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.R_Succ_Sent_edge_reward == other.R_Succ_Sent_edge_reward and self.cost == other.cost
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_Sent_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cost)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "R_Succ_Sent_edge_reward = " + str(self.R_Succ_Sent_edge_reward)
		result += ", cost = " + str(self.cost)
		result += ")"
		return result

# Automaton: jobProvider_X
class jobProvider_XAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2]
		self.transition_labels = [[1, 17], [2, 17], [3, 4], [1, 17]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.jobProvider_X_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.jobProvider_X_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.jobProvider_X_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.jobProvider_X_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.jobProvider_X_location
		if location == 0:
			if transition == 0:
				return (state.gc == (state.jobStartTimes_X)[state.counter_X])
			elif transition == 1:
				return ((state.gc < (state.jobStartTimes_X)[state.counter_X]) or (state.gc >= (state.jobEndTimes_X)[state.counter_X]))
		elif location == 1:
			if transition == 0:
				return (state.gc == (state.jobEndTimes_X)[state.counter_X])
			elif transition == 1:
				return (state.gc < (state.jobEndTimes_X)[state.counter_X])
		elif location == 2:
			if transition == 0:
				return (state.counter_X < 1)
			elif transition == 1:
				return (state.counter_X >= 1)
		elif location == 3:
			if transition == 0:
				return (state.gc == (state.jobStartTimes_X)[state.counter_X])
			elif transition == 1:
				return ((state.gc < (state.jobStartTimes_X)[state.counter_X]) or (state.gc >= (state.jobEndTimes_X)[state.counter_X]))
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.jobProvider_X_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.jobProvider_X_location
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
			location = state.jobProvider_X_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobAccepted_X = False
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.counter_X = (state.counter_X + 1)
						target_state.jobAccepted_X = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.jobAccepted_X = False
		elif assignment_index == 2:
			location = state.jobProvider_X_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_X_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_X_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_X_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_X_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_X_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_X_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_X_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_X_location = 3

# Automaton: job_X
class job_XAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 2, 3, 2]
		self.transition_labels = [[1, 5, 17], [1, 17], [6, 17], [2, 17], [1, 5, 17], [7, 17]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.job_X_location = 0
		state.internal = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.job_X_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.job_X_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.job_X_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.job_X_location
		if location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition == 0:
				return (state.internal >= 5)
			elif transition == 1:
				return True
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 3:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition >= 0 and transition < 3:
				return True
		elif location == 5:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.job_X_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.job_X_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
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
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.job_X_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_transient.cost = 1
						target_state.numOfJobsSkipped = (state.numOfJobsSkipped + 1)
				elif transition == 2:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.numOfJobsPerformed = (state.numOfJobsPerformed + 1)
				elif transition == 1:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_transient.cost = 1
						target_state.numOfJobsSkipped = (state.numOfJobsSkipped + 1)
				elif transition == 2:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
			elif location == 5:
				if transition == 1:
					if branch == 0:
						target_state.internal = min((state.internal + 1), 6)
		elif assignment_index == 2:
			location = state.job_X_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.job_X_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.job_X_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.job_X_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.job_X_location = 5

# Automaton: jobProvider_U
class jobProvider_UAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2]
		self.transition_labels = [[8, 17], [9, 17], [10, 11], [8, 17]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.jobProvider_U_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.jobProvider_U_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.jobProvider_U_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.jobProvider_U_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.jobProvider_U_location
		if location == 0:
			if transition == 0:
				return (state.gc == (state.jobStartTimes_U)[state.counter_U])
			elif transition == 1:
				return ((state.gc < (state.jobStartTimes_U)[state.counter_U]) or (state.gc >= (state.jobEndTimes_U)[state.counter_U]))
		elif location == 1:
			if transition == 0:
				return (state.gc == (state.jobEndTimes_U)[state.counter_U])
			elif transition == 1:
				return (state.gc < (state.jobEndTimes_U)[state.counter_U])
		elif location == 2:
			if transition == 0:
				return (state.counter_U < 1)
			elif transition == 1:
				return (state.counter_U >= 1)
		elif location == 3:
			if transition == 0:
				return (state.gc == (state.jobStartTimes_U)[state.counter_U])
			elif transition == 1:
				return ((state.gc < (state.jobStartTimes_U)[state.counter_U]) or (state.gc >= (state.jobEndTimes_U)[state.counter_U]))
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.jobProvider_U_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.jobProvider_U_location
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
			location = state.jobProvider_U_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobAccepted_U = False
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.counter_U = (state.counter_U + 1)
						target_state.jobAccepted_U = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.jobAccepted_U = False
		elif assignment_index == 2:
			location = state.jobProvider_U_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_U_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_U_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_U_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_U_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_U_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_U_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.jobProvider_U_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.jobProvider_U_location = 3

# Automaton: job_U
class job_UAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 3, 2]
		self.transition_labels = [[8, 8, 17], [12, 17], [9, 17], [8, 8, 17], [13, 17]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.job_U_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.job_U_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.job_U_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.job_U_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.job_U_location
		if location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition >= 0 and transition < 2:
				return True
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 3:
			if transition >= 0 and transition < 3:
				return True
		elif location == 4:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.job_U_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.job_U_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
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
			elif transition == 2:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.job_U_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_transient.cost = 1
						target_state.numOfJobsSkipped = (state.numOfJobsSkipped + 1)
				elif transition == 1:
					if branch == 0:
						target_state.numOfJobsPerformed = (state.numOfJobsPerformed + 1)
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_transient.cost = 1
						target_state.numOfJobsSkipped = (state.numOfJobsSkipped + 1)
				elif transition == 1:
					if branch == 0:
						target_state.numOfJobsPerformed = (state.numOfJobsPerformed + 1)
		elif assignment_index == 2:
			location = state.job_U_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.job_U_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.job_U_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.job_U_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.job_U_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.job_U_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.job_U_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.job_U_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.job_U_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.job_U_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.job_U_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.job_U_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.job_U_location = 4

# Automaton: battery
class batteryAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 3, 2]
		self.transition_labels = [[14, 17], [15, 16, 17], [14, 17]]
		self.branch_counts = [[1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.battery_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.battery_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.battery_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.battery_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.battery_location
		if location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.battery_capacity >= 5990400)
		elif location == 1:
			if transition == 0:
				return state.jobAccepted_X
			elif transition == 1:
				return state.jobAccepted_U
			elif transition == 2:
				return ((state.counter_X >= 0) and (state.counter_U >= 0))
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.battery_capacity >= 5990400)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.battery_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.battery_location
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
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.battery_location
			if location == 1:
				if transition == 0:
					if branch == 0:
						target_state.battery_capacity = (11945 * ((state.jobEndTimes_X)[state.counter_X] - (state.jobStartTimes_X)[state.counter_X]))
				elif transition == 1:
					if branch == 0:
						target_state.battery_capacity = ((2630 * (state.jobEndTimes_U)[state.counter_U]) - (state.jobStartTimes_U)[state.counter_U])
		elif assignment_index == 2:
			location = state.battery_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.battery_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.battery_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.battery_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.battery_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.battery_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.battery_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.battery_location = 2

# Automaton: timer
class timerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1]
		self.transition_labels = [[18, 17], [17]]
		self.branch_counts = [[1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.timer_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.timer_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.timer_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.timer_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.timer_location
		if location == 0:
			if transition == 0:
				return (state.gc == 10)
			elif transition == 1:
				return (state.gc < 10)
		elif location == 1:
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.timer_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.timer_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.timer_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.success = True
		elif assignment_index == 2:
			location = state.timer_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.timer_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.timer_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.timer_location = 1

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[17, 18]]
		self.branch_counts = [[1, 1]]
	
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
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.gc = min((state.gc + 1), 11)
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.R_Succ_Sent_edge_reward = transient.cost

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
	
	def __init__(self, label = 0, transitions = [-1, -1, -1, -1, -1, -1, -1]):
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "transition_labels", "sync_vectors", "properties", "aut_jobProvider_X", "aut_job_X", "aut_jobProvider_U", "aut_job_U", "aut_battery", "aut_timer", "aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "available_X", 2: "not_available_X", 3: "updateCounter_X", 4: "finishedCounting_X", 5: "performSlewing_X", 6: "performJob_X", 7: "skipJob_X", 8: "available_U", 9: "not_available_U", 10: "updateCounter_U", 11: "finishedCounting_U", 12: "performJob_U", 13: "skipJob_U", 14: "b_update", 15: "b_update_X", 16: "b_update_U", 17: "tick", 18: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, -1, 0, 0], [3, -1, -1, -1, -1, -1, 18, 3], [4, -1, -1, -1, -1, -1, 18, 4], [-1, 5, -1, -1, -1, -1, 18, 5], [-1, 6, -1, -1, -1, -1, 18, 6], [-1, 7, -1, -1, -1, -1, 18, 7], [1, 1, -1, -1, -1, -1, 18, 1], [2, 2, -1, -1, -1, -1, 18, 2], [-1, -1, 10, -1, -1, -1, 18, 10], [-1, -1, 11, -1, -1, -1, 18, 11], [-1, -1, -1, 12, -1, -1, 18, 12], [-1, -1, -1, 13, -1, -1, 18, 13], [-1, -1, 8, 8, -1, -1, 18, 8], [-1, -1, 9, 9, -1, -1, 18, 9], [-1, -1, -1, -1, 14, -1, 18, 14], [-1, -1, -1, -1, 15, -1, 18, 15], [-1, -1, -1, -1, 16, -1, 18, 16], [-1, -1, -1, -1, -1, 18, 18, 0], [17, 17, 17, 17, 17, 17, 17, 17]]
		self.properties = [Property("R_Succ_Sent", PropertyExpression("xmin", [0, PropertyExpression("ap", [1])]))]
		self.aut_jobProvider_X = jobProvider_XAutomaton(self)
		self.aut_job_X = job_XAutomaton(self)
		self.aut_jobProvider_U = jobProvider_UAutomaton(self)
		self.aut_job_U = job_UAutomaton(self)
		self.aut_battery = batteryAutomaton(self)
		self.aut_timer = timerAutomaton(self)
		self.aut_GlobalSync = GlobalSyncAutomaton(self)
	
	def get_initial_state(self) -> State:
		state = State()
		state.jobStartTimes_X = [2, 7]
		state.jobEndTimes_X = [3, 9]
		state.counter_X = 0
		state.jobAccepted_X = False
		state.jobStartTimes_U = [2, 4]
		state.jobEndTimes_U = [3, 5]
		state.counter_U = 0
		state.jobAccepted_U = False
		state.gc = 0
		state.numOfJobsPerformed = 0
		state.numOfJobsSkipped = 0
		state.success = False
		state.battery_capacity = 149760000
		self.aut_jobProvider_X.set_initial_values(state)
		self.aut_job_X.set_initial_values(state)
		self.aut_jobProvider_U.set_initial_values(state)
		self.aut_job_U.set_initial_values(state)
		self.aut_battery.set_initial_values(state)
		self.aut_timer.set_initial_values(state)
		self.aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.R_Succ_Sent_edge_reward = 0
		transient.cost = 0
		self.aut_jobProvider_X.set_initial_transient_values(transient)
		self.aut_job_X.set_initial_transient_values(transient)
		self.aut_jobProvider_U.set_initial_transient_values(transient)
		self.aut_job_U.set_initial_transient_values(transient)
		self.aut_battery.set_initial_transient_values(transient)
		self.aut_timer.set_initial_transient_values(transient)
		self.aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "R_Succ_Sent_edge_reward")
		elif expression == 1:
			return state.success
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.R_Succ_Sent_edge_reward
		elif expression == 1:
			return state.success
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		result = self.aut_jobProvider_X.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_job_X.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_jobProvider_U.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_job_U.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_battery.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_timer.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		if transient_variable == "R_Succ_Sent_edge_reward":
			return 0
		elif transient_variable == "cost":
			return 0
		return None
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_jobProvider_X = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_jobProvider_X.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_jobProvider_X.get_guard_value(state, i):
				trans_jobProvider_X[self.aut_jobProvider_X.get_transition_label(state, i)].append(i)
		trans_job_X = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_job_X.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_job_X.get_guard_value(state, i):
				trans_job_X[self.aut_job_X.get_transition_label(state, i)].append(i)
		trans_jobProvider_U = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_jobProvider_U.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_jobProvider_U.get_guard_value(state, i):
				trans_jobProvider_U[self.aut_jobProvider_U.get_transition_label(state, i)].append(i)
		trans_job_U = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_job_U.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_job_U.get_guard_value(state, i):
				trans_job_U[self.aut_job_U.get_transition_label(state, i)].append(i)
		trans_battery = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_battery.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_battery.get_guard_value(state, i):
				trans_battery[self.aut_battery.get_transition_label(state, i)].append(i)
		trans_timer = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_timer.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_timer.get_guard_value(state, i):
				trans_timer[self.aut_timer.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self.aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for sv in self.sync_vectors:
			synced = [[-1, -1, -1, -1, -1, -1, -1, -1]]
			# jobProvider_X
			if synced is not None:
				if sv[0] != -1:
					if len(trans_jobProvider_X[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_jobProvider_X[sv[0]][0]
						for i in range(1, len(trans_jobProvider_X[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_jobProvider_X[sv[0]][i]
			# job_X
			if synced is not None:
				if sv[1] != -1:
					if len(trans_job_X[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_job_X[sv[1]][0]
						for i in range(1, len(trans_job_X[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_job_X[sv[1]][i]
			# jobProvider_U
			if synced is not None:
				if sv[2] != -1:
					if len(trans_jobProvider_U[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_jobProvider_U[sv[2]][0]
						for i in range(1, len(trans_jobProvider_U[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_jobProvider_U[sv[2]][i]
			# job_U
			if synced is not None:
				if sv[3] != -1:
					if len(trans_job_U[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_job_U[sv[3]][0]
						for i in range(1, len(trans_job_U[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_job_U[sv[3]][i]
			# battery
			if synced is not None:
				if sv[4] != -1:
					if len(trans_battery[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_battery[sv[4]][0]
						for i in range(1, len(trans_battery[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_battery[sv[4]][i]
			# timer
			if synced is not None:
				if sv[5] != -1:
					if len(trans_timer[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_timer[sv[5]][0]
						for i in range(1, len(trans_timer[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_timer[sv[5]][i]
			# GlobalSync
			if synced is not None:
				if sv[6] != -1:
					if len(trans_GlobalSync[sv[6]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][6] = trans_GlobalSync[sv[6]][0]
						for i in range(1, len(trans_GlobalSync[sv[6]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][6] = trans_GlobalSync[sv[6]][i]
			if synced is not None:
				for sync in synced:
					sync[7] = sv[7]
				transitions.extend(filter(lambda s: s[-1] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][7], transitions[i])
			del transitions[i].transitions[7]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self.aut_jobProvider_X.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self.aut_jobProvider_X.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self.aut_jobProvider_X.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self.aut_job_X.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self.aut_job_X.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self.aut_job_X.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self.aut_jobProvider_U.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self.aut_jobProvider_U.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self.aut_jobProvider_U.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self.aut_job_U.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self.aut_job_U.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self.aut_job_U.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self.aut_battery.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self.aut_battery.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self.aut_battery.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self.aut_timer.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self.aut_timer.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self.aut_timer.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
				probs[i] *= probability
		if transition.transitions[6] != -1:
			existing = len(combs)
			branch_count = self.aut_GlobalSync.get_branch_count(state, transition.transitions[6])
			for i in range(1, branch_count):
				probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[6], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][6] = i
					probs.append(probs[j] * probability)
			probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[6], 0)
			for i in range(existing):
				combs[i][6] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 3):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self.aut_jobProvider_X.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self.aut_job_X.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self.aut_jobProvider_U.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self.aut_job_U.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self.aut_battery.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self.aut_timer.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			if transition.transitions[6] != -1:
				self.aut_GlobalSync.jump(state, transient, transition.transitions[6], branch.branches[6], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
