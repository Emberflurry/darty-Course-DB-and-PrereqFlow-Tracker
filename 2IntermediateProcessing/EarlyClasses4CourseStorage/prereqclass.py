# 11/24/2021 - 11/28/2021 John DeForest
# possible use of prereq class objects for managing complex ands/ors prereq networks...
# many questions(choices) about how to store prereqs/credits for classes...


class Prereq:
    def __init__(self, required, ors_combos):
        self.required = required  # ez to check, but only store courses required regardless of combo
        self.ors_combos = ors_combos  # HOW TF DO WE DO THIS? -- does a Course object have 1 prereq object or multiple?
        # maybe use pointers to other Course objects? multiple dictionaries?-where created?

        # OR use an ordered (regular) list of (all) of the required course credit(s) --would require full backchaining
        # and keeping track of all course credits for an indiv (which might have to do anyways)

        # OR use list of lists w indicator?,ieCHEM040req: MATH008 and (PHYS013 or PHYS015 or (PHYS003 and PHYS004)) and (CHEM006 or CHEM010)
        # (math8,   "+",   (phys13, "o", phys15, "o", (phys3, "+", phys4)),   "+",   (chem6, "o", chem10))
        # ^ might require some decent work on the driver side (interpreting), but idk



class Orprq:
    def __init__(self, courses):
        self.courses = courses

class Andprq:
    def __init__(self, courses):
        self.courses = courses



