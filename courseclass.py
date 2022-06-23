# 11/24/2021 John DeForest

# may need multiple classes for all of the course info?
# also how to store the per-term info? do we even try to?


class Course:
    def __init__(self, dept, coursenum, coursetitle="", profs="", pastterms="", curfutterms="", xlist="", prereqs="", prereqnotes="", xtrafee=False,
                 distribs="", nroelig=True, typicalblocks="", crn="", coursetype="", worldcults="", assocLab=False, coursecredits=""):
        # ADD =[] to LISTS^ (when applicable lol)

        self.dept = str(dept)  # 4dig
        self.number = str(coursenum)  # 3dig or 1dig.2dig or 2dig.2dig

        # not required:
        self.title = str(coursetitle)  # duh
        self.profs = str(profs)    # eventually a list
        self.pastterms = str(pastterms)  # eventually a list
        self.curfutterms = str(curfutterms)  # eventually a list
        self.xlist = str(xlist)    # eventually a list
        self.prereqs = str(prereqs)  # eventually a list
        self.prereqnotes = str(prereqnotes)
        self.xtrafee = bool(xtrafee)  # boolean
        self.distribs = str(distribs)  # eventually a list?
        self.isNROelig = bool(nroelig)  # boolean
        self.typicalblocks = str(typicalblocks)  # eventually a list
        self.CRN = str(crn)  # eventually an INT. course reg number? might b term specific...
        self.coursetype = str(coursetype)  # 3dig: lec vs lab
        self.worldcults = str(worldcults)  # world culture distribs, eventually a list
        self.hasAssocLab = bool(assocLab)  # boolean
        self.credits = coursecredits  # int or float

    # earlier version of toString method, may have things that depend on it but oh well for now (6/22/22)
    # def __str__(self):
    #     return self.dept + self.number + ": "+self.title+",xlist(" + str(self.xlist) + "),prqs(" + \
    #            str(self.prereqs) + ")"
    def __str__(self):
        return self.dept + self.number
