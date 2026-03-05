"""
Supporting inequalities for AR:


The first thing to note is that > and >= are two different inequalities
that pose their own troubles. We want to add angle, length, and ratio
tables for both of these, essentially adding in 6 more matrices(which honestly
shouldn't be too bad because the bottleneck is in DD, not AR).

In our length tables for >/>=, we label things with +/- according to the side
of the inequality they are on(+ is for greater side, - for smaller side). Any addition
is thus a valid operation, BUT subtractions in this ar table are not allowed!!!
Somehow need to find a sol to that(may need to implement custom matrix simplifier?)

In our angle table, the angle1 notation falls apart pretty quickly. We're going to use
angle0 here using the arctan formula given by alphageo2. However, angle0 derivations
in the final result should still stem only from derivation rather than diagram checking.

In our ratio tables, essentially the same notation as length tables, where if we have
a * b > c * d, then a, b are + and c, d are -. This is different from the ratio tables of
alphageo, and the reason I made it this way is because I anticipate there to be more complicated
expressions with ratios in inequalities, so I am putting all terms on single sides.

As for DD, we will add in new rules like triangle inequality, Euler's, Ptolemy's. Still,
I expect most of the work to be done with the equality AR tables, and that the inequality
AR tables use the results of the equality AR tables to deduce further inequalities.


In terms of workflow, we need some sort of way to allow the use of inequality ar tables
ONLY when we have an inequality in the problem statement or target(similar structure for area too).
We will need inequality ar tables to deduce things every N cycles of equality ar tables or
something akin to that, where N could be anywhere from 1 to 5.
"""

import math
import numpy as np
from typing import List, Tuple, Dict, Any, Optional
from ddar import DDAR

class InEqDDAR:    
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        self.ddar = ddar
        self.has_inequalities = has_inequalities

class InEqARGreaterAngle(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.angle_table_greater = {} # TODO: update how we actually store these

class InEqARGreaterLength(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.length_table_greater = {} # TODO: update how we actually store these

class InEqARRatio(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.ratio_table_greater = {} # TODO: update how we actually store these

class InEqARGeqAngle(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.angle_table_geq = {} # TODO: update how we actually store these

class InEqARGeqLength(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.length_table_geq = {} # TODO: update how we actually store these

class InEqARRatioGeq(InEqDDAR):
    def __init__(self, ddar: DDAR, has_inequalities: bool = False):
        super().__init__(ddar, has_inequalities)
        self.ratio_table_geq = {} # TODO: update how we actually store these