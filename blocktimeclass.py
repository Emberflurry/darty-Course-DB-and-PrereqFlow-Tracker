# 11/24/2021 - 11/28/2021 John DeForest
# for storing info about ea named time block
# for storage as objs in dictionary to reference/use for class compatibility/scheduling


class Block:
    def __init__(self, blockcode, ondays, stime, etime, typecode):
        self.blockcode = str(blockcode)
        self.ondays = str(ondays)
        self.stime = str(stime)
        self.etime = str(etime)
        self.typecode = str(typecode)  # 0=reg, 1=Xhr, 2=lab (unofficial) maybe make INT?

        # MAYBE add a class duration instance var? (calc w/in ea block obj or when/if used?)

    def __str__(self):
        return self.blockcode + " | " + self.ondays + " | " + self.stime+"-"+self.etime + " | " + self.typecode
