# 11/24/2021 - 11/28/2021 John DeForest
# create a dictionary of schedule block data -times/etc out of Block objs
# read from csv file-from main excel db (must manually copy to csv if changed, then save and rerun)

from blocktimeclass import Block
inpfile = "C:/Users/John DeForest/Desktop/coursetimesdb1.csv"


# csv data parser for each row in the excel doc of course schedule block/timetable entries
def parse_line(line):
    section_split = line.split(",")
    blockcode = section_split[0].strip()
    ondays = section_split[1].strip()
    starttime = section_split[2].strip()
    endtime = section_split[3].strip()
    typecode = section_split[4].strip()

    return blockcode, ondays, starttime, endtime, typecode


# run this to get a dictionary w the Block objs for the time blocks in the schedule
def load_course_time_blocks(inputfile):
    coursetimesdict = {}
    workingfile = open(inputfile)

    for line in workingfile:
        blockcode, ondays, starttime, endtime, typecode = parse_line(line)
        block_i = Block(blockcode, ondays, starttime, endtime, typecode)
        coursetimesdict[blockcode] = block_i

    workingfile.close()

    return coursetimesdict


# testing:
blocktimesdict = load_course_time_blocks(inpfile)

for item in blocktimesdict:
    print(blocktimesdict[item].blockcode + " | " + blocktimesdict[item].ondays + " | " + blocktimesdict[item].stime
          + " | " + blocktimesdict[item].etime + " | " + blocktimesdict[item].typecode)

# print(blocktimesdict["8S"])  # works!
