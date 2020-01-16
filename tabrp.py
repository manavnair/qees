# tabrp

from __future__ import annotations
from typing import List, Union, Optional

class VariableInfo(object):
	__slots__ = ("name", "component", "type", "minValue", "maxValue")
	
	def __init__(self, name: str, component: Optional[int], type: str, minValue = None, maxValue = None):
		self.name = name
		self.component = component
		self.type = type
		self.minValue = minValue
		self.maxValue = maxValue

# States
class State(object):
	__slots__ = ("success", "failure", "coll", "waiting", "Sender_location", "c", "n", "Channel_location", "c_1", "Channel_location_1", "c_2", "Receiver_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.success
		elif variable == 1:
			return self.failure
		elif variable == 2:
			return self.coll
		elif variable == 3:
			return self.waiting
		elif variable == 4:
			return self.Sender_location
		elif variable == 5:
			return self.c
		elif variable == 6:
			return self.n
		elif variable == 7:
			return self.Channel_location
		elif variable == 8:
			return self.c_1
		elif variable == 9:
			return self.Channel_location_1
		elif variable == 10:
			return self.c_2
		elif variable == 11:
			return self.Receiver_location
	
	def copy_to(self, other: State):
		other.success = self.success
		other.failure = self.failure
		other.coll = self.coll
		other.waiting = self.waiting
		other.Sender_location = self.Sender_location
		other.c = self.c
		other.n = self.n
		other.Channel_location = self.Channel_location
		other.c_1 = self.c_1
		other.Channel_location_1 = self.Channel_location_1
		other.c_2 = self.c_2
		other.Receiver_location = self.Receiver_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.success == other.success and self.failure == other.failure and self.coll == other.coll and self.waiting == other.waiting and self.Sender_location == other.Sender_location and self.c == other.c and self.n == other.n and self.Channel_location == other.Channel_location and self.c_1 == other.c_1 and self.Channel_location_1 == other.Channel_location_1 and self.c_2 == other.c_2 and self.Receiver_location == other.Receiver_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.success)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.failure)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.coll)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.waiting)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Sender_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.n)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Channel_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Channel_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Receiver_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "success = " + str(self.success)
		result += ", failure = " + str(self.failure)
		result += ", coll = " + str(self.coll)
		result += ", waiting = " + str(self.waiting)
		result += ", Sender_location = " + str(self.Sender_location)
		result += ", c = " + str(self.c)
		result += ", n = " + str(self.n)
		result += ", Channel_location = " + str(self.Channel_location)
		result += ", c_1 = " + str(self.c_1)
		result += ", Channel_location_1 = " + str(self.Channel_location_1)
		result += ", c_2 = " + str(self.c_2)
		result += ", Receiver_location = " + str(self.Receiver_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("R_Succ_Wait_rate_reward", "R_Succ_Sent_edge_reward", "sent")
	
	def copy_to(self, other: Transient):
		other.R_Succ_Wait_rate_reward = self.R_Succ_Wait_rate_reward
		other.R_Succ_Sent_edge_reward = self.R_Succ_Sent_edge_reward
		other.sent = self.sent
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.R_Succ_Wait_rate_reward == other.R_Succ_Wait_rate_reward and self.R_Succ_Sent_edge_reward == other.R_Succ_Sent_edge_reward and self.sent == other.sent
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_Wait_rate_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_Sent_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.sent)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "R_Succ_Wait_rate_reward = " + str(self.R_Succ_Wait_rate_reward)
		result += ", R_Succ_Sent_edge_reward = " + str(self.R_Succ_Sent_edge_reward)
		result += ", sent = " + str(self.sent)
		result += ")"
		return result

# Automaton: Sender
class SenderAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 3, 3, 1]
		self.transition_labels = [[1, 8], [2, 3, 8], [1, 9, 8], [8]]
		self.branch_counts = [[1, 1], [1, 1, 1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Sender_location = 0
		state.c = 0
		state.n = 2
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Sender_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Sender_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Sender_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Sender_location
		if location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.n <= 0)
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c >= 7)
			elif transition == 2:
				return (state.c < 7)
		elif location == 2:
			if transition == 0:
				return (state.n > 0)
			elif transition == 1:
				return (state.n == 0)
			elif transition == 2:
				return ((state.n <= 0) and (state.n != 0))
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Sender_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Sender_location
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
			elif transition == 2:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Sender_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.n = (state.n - 1)
						if target_state.n < 0:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is less than the lower bound of 0 for variable \"n\".")
						target_transient.sent = 1
						target_state.waiting = True
				elif transition == 1:
					if branch == 0:
						target_state.c = min((state.c + 1), 8)
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.success = True
						target_state.waiting = False
						target_state.n = 0
				elif transition == 1:
					if branch == 0:
						target_state.waiting = False
						target_state.c = 0
				elif transition == 2:
					if branch == 0:
						target_state.c = min((state.c + 1), 8)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.n = (state.n - 1)
						if target_state.n < 0:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is less than the lower bound of 0 for variable \"n\".")
						target_transient.sent = 1
						target_state.waiting = True
				elif transition == 1:
					if branch == 0:
						target_state.failure = True
						target_state.n = 0
				elif transition == 2:
					if branch == 0:
						target_state.c = min((state.c + 1), 8)
		elif assignment_index == 2:
			location = state.Sender_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Sender_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Sender_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
						target_state.Sender_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Sender_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Sender_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Sender_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.c = 0
						target_state.Sender_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.Sender_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Sender_location = 3

# Automaton: Channel
class ChannelAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 3, 1, 3]
		self.transition_labels = [[4, 4, 8], [9, 4, 8], [8], [5, 4, 8]]
		self.branch_counts = [[1, 1, 1], [1, 1, 1], [1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Channel_location = 0
		state.c_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Channel_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Channel_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Channel_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Channel_location
		if location == 2:
			return True
		elif location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition == 0:
				return (state.c_1 >= 1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.c_1 < 3)
		elif location == 3:
			if transition == 0:
				return (state.c_1 >= 1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.c_1 < 3)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Channel_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Channel_location
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
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Channel_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.c_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.c_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.coll = True
				elif transition == 2:
					if branch == 0:
						target_state.c_1 = min((state.c_1 + 1), 4)
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.c_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.coll = True
				elif transition == 2:
					if branch == 0:
						target_state.c_1 = min((state.c_1 + 1), 4)
		elif assignment_index == 2:
			location = state.Channel_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Channel_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_1 = 0
						target_state.Channel_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_1 = 0
						target_state.Channel_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location = 3

# Automaton: Channel
class ChannelAutomaton_1(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 3, 1, 3]
		self.transition_labels = [[4, 4, 8], [9, 4, 8], [8], [5, 4, 8]]
		self.branch_counts = [[1, 1, 1], [1, 1, 1], [1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Channel_location_1 = 0
		state.c_2 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Channel_location_1
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Channel_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Channel_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Channel_location_1
		if location == 2:
			return True
		elif location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition == 0:
				return (state.c_2 >= 1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.c_2 < 3)
		elif location == 3:
			if transition == 0:
				return (state.c_2 >= 1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.c_2 < 3)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Channel_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Channel_location_1
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
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Channel_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.c_2 = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_2 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.c_2 = 0
				elif transition == 1:
					if branch == 0:
						target_state.coll = True
				elif transition == 2:
					if branch == 0:
						target_state.c_2 = min((state.c_2 + 1), 4)
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.c_2 = 0
				elif transition == 1:
					if branch == 0:
						target_state.coll = True
				elif transition == 2:
					if branch == 0:
						target_state.c_2 = min((state.c_2 + 1), 4)
		elif assignment_index == 2:
			location = state.Channel_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Channel_location_1 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_2 = 0
						target_state.Channel_location_1 = 2
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location_1 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location_1 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Channel_location_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.c_2 = 0
						target_state.Channel_location_1 = 2
				elif transition == 2:
					if branch == 0:
						target_state.Channel_location_1 = 3

# Automaton: Receiver
class ReceiverAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1]
		self.transition_labels = [[6, 8], [7]]
		self.branch_counts = [[1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Receiver_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Receiver_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Receiver_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Receiver_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Receiver_location
		if location == 1:
			return True
		elif location == 0:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Receiver_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Receiver_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 2:
			location = state.Receiver_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Receiver_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Receiver_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Receiver_location = 0

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[8, 9]]
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
		if assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_transient.R_Succ_Wait_rate_reward = (1 if state.waiting else 0)
				elif transition == 1:
					if branch == 0:
						target_transient.R_Succ_Sent_edge_reward = transient.sent

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
	__slots__ = ("sync_vector", "label", "transitions")
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Sender", "_aut_Channel", "_aut_Channel_1", "_aut_Receiver", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "snd_data", 2: "rcv_ack", 3: "timeout", 4: "snd", 5: "rcv", 6: "rcv_data", 7: "snd_ack", 8: "tick", 9: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, 0], [-1, -1, 0, -1, -1, 0], [-1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, 0, 0], [3, -1, -1, -1, 9, 3], [1, 4, -1, -1, 9, 1], [2, -1, 5, -1, 9, 2], [-1, 5, -1, 6, 9, 6], [-1, -1, 4, 7, 9, 7], [9, -1, -1, -1, 9, 0], [-1, 9, -1, -1, 9, 0], [-1, -1, 9, -1, 9, 0], [8, 8, 8, 8, 8, 8]]
		self.properties = [Property("E_Succ", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])), Property("E_Fail", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [1])])])), Property("R_Succ_Sent", PropertyExpression("xmin", [2, PropertyExpression("ap", [0])])), Property("R_Succ_Wait", PropertyExpression("xmin", [3, PropertyExpression("ap", [0])]))]
		self.variables = [VariableInfo("success", None, "bool"), VariableInfo("failure", None, "bool"), VariableInfo("coll", None, "bool"), VariableInfo("waiting", None, "bool"), VariableInfo("Sender_location", 0, "int", 0, 3), VariableInfo("c", 0, "int", 0, 8), VariableInfo("n", 0, "int", 0, 2), VariableInfo("Channel_location", 1, "int", 0, 3), VariableInfo("c", 1, "int", 0, 4), VariableInfo("Channel_location", 2, "int", 0, 3), VariableInfo("c", 2, "int", 0, 4), VariableInfo("Receiver_location", 3, "int", 0, 1)]
		self._aut_Sender = SenderAutomaton(self)
		self._aut_Channel = ChannelAutomaton(self)
		self._aut_Channel_1 = ChannelAutomaton_1(self)
		self._aut_Receiver = ReceiverAutomaton(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Sender, self._aut_Channel, self._aut_Channel_1, self._aut_Receiver, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.success = False
		state.failure = False
		state.coll = False
		state.waiting = False
		self._aut_Sender.set_initial_values(state)
		self._aut_Channel.set_initial_values(state)
		self._aut_Channel_1.set_initial_values(state)
		self._aut_Receiver.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.R_Succ_Wait_rate_reward = 0
		transient.R_Succ_Sent_edge_reward = 0
		transient.sent = 0
		self._aut_Sender.set_initial_transient_values(transient)
		self._aut_Channel.set_initial_transient_values(transient)
		self._aut_Channel_1.set_initial_transient_values(transient)
		self._aut_Receiver.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return state.success
		elif expression == 1:
			return state.failure
		elif expression == 2:
			return self.network._get_transient_value(state, "R_Succ_Sent_edge_reward")
		elif expression == 3:
			return self.network._get_transient_value(state, "R_Succ_Wait_rate_reward")
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return state.success
		elif expression == 1:
			return state.failure
		elif expression == 2:
			return transient.R_Succ_Sent_edge_reward
		elif expression == 3:
			return transient.R_Succ_Wait_rate_reward
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Sender.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Channel.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Channel_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Receiver.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Sender = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Sender.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Sender.get_guard_value(state, i):
				trans_Sender[self._aut_Sender.get_transition_label(state, i)].append(i)
		trans_Channel = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Channel.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Channel.get_guard_value(state, i):
				trans_Channel[self._aut_Channel.get_transition_label(state, i)].append(i)
		trans_Channel_1 = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Channel_1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Channel_1.get_guard_value(state, i):
				trans_Channel_1[self._aut_Channel_1.get_transition_label(state, i)].append(i)
		trans_Receiver = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Receiver.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Receiver.get_guard_value(state, i):
				trans_Receiver[self._aut_Receiver.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1]]
			# Sender
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Sender[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Sender[sv[0]][0]
						for i in range(1, len(trans_Sender[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Sender[sv[0]][i]
			# Channel
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Channel[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Channel[sv[1]][0]
						for i in range(1, len(trans_Channel[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Channel[sv[1]][i]
			# Channel
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Channel_1[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Channel_1[sv[2]][0]
						for i in range(1, len(trans_Channel_1[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Channel_1[sv[2]][i]
			# Receiver
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Receiver[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Receiver[sv[3]][0]
						for i in range(1, len(trans_Receiver[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Receiver[sv[3]][i]
			# GlobalSync
			if synced is not None:
				if sv[4] != -1:
					if len(trans_GlobalSync[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_GlobalSync[sv[4]][0]
						for i in range(1, len(trans_GlobalSync[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_GlobalSync[sv[4]][i]
			if synced is not None:
				for sync in synced:
					sync[-1] = sv[-1]
					sync.append(svi)
				transitions.extend(filter(lambda s: s[-2] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][-1], transitions[i][-2], transitions[i])
			del transitions[i].transitions[-1]
			del transitions[i].transitions[-1]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Sender.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Sender.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Sender.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Channel.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Channel.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Channel.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Channel_1.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Channel_1.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Channel_1.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Receiver.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Receiver.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Receiver.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
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
				self._aut_Sender.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Channel.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Channel_1.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Receiver.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
