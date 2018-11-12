#  Copyright 2018 Bridger Herman

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import bpy
from mathutils import Vector

from glyph import Glyph

# glyphs: a map of `tuple => Glyph` obtained from a `.distribute_poisson()`
# method call
# Returns the maximum value in the data
def task_1(glyphs):
    max_glyph = Glyph(0.0, Vector((0.0, 0.0, 0.0)))
    max_location = (0.0, 0.0, 0.0)

    for location in glyphs:
        if glyphs[location].value > max_glyph.value:
            max_glyph = glyphs[location]
            max_location = location

    return Vector(max_location)

# mesh: the mesh to find the steepest slope (from a sphere) on
# Returns the location of the steepest slope
def task_3(obj):
    min_dot_difference = 1.0
    steepest = Vector((0.0, 0.0, 0.0))
    for v in obj.data.vertices:
        dot = v.co.normalized().dot(v.normal.normalized())
        if dot < min_dot_difference:
            min_dot_difference = dot
            steepest = v.co
    return steepest

