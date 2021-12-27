"""
import sandwiches_module

sandwiches_module.sandwich('salami', 'mustard')
sandwiches_module.sandwich('burger', 'ketchup', 'salad')
sandwiches_module.sandwich('chicken', 'bbq sauce', 'chips', 'pepsi')
##############

from sandwiches_module import sandwich

sandwich('salami', 'mustard')
sandwich('burger', 'ketchup', 'salad')
sandwich('chicken', 'bbq sauce', 'chips', 'pepsi')
####################

from sandwiches_module import sandwich as s

s('salami', 'mustard')
s('burger', 'ketchup', 'salad')
s('chicken', 'bbq sauce', 'chips', 'pepsi')
################

import sandwiches_module as sm

sm.sandwich('salami', 'mustard')
sm.sandwich('burger', 'ketchup', 'salad')
sm.sandwich('chicken', 'bbq sauce', 'chips', 'pepsi')
"""

from sandwiches_module import *

sandwich('salami', 'mustard')
sandwich('burger', 'ketchup', 'salad')
sandwich('chicken', 'bbq sauce', 'chips', 'pepsi')
