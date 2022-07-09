import openpyxl
import dash
import dash_cytoscape as dcyto
from dash import html as dhtml

dcyto.load_extra_layouts()


def xl2SIFnetworkcreator(xlWbFilePath, sheetIndex, startingRowOfEdgeEntries, columnNumofEdgeEntries,
                         outputSIFnameAndOrPath):
    myWB = openpyxl.load_workbook(xlWbFilePath)
    mySheet = myWB[myWB.sheetnames[sheetIndex]]
    with open(outputSIFnameAndOrPath, 'w') as myOutFile:
        glbOrCtr = 0  # can handle note: INCREASED TO 0-999 (THREE DIGITS CAPACITY FOR ALL GLOBAL ORS/ANDS)
        glbAndCtr = 0  # ^           # note: Only use now if counting # of ors and ands for debugging...

        # FOR outputs to node/edge lists for Dash-Cyto graph visuals, see lines 102-119
        edgeList = []
        nodeList = []

        cumNodeSet = set()  # note: for keeping track of NODES to add/already been added
        lineDuplicateSet = set()  # note: makes sure repeated/duplicate EDGES are not added

        for i in range(startingRowOfEdgeEntries, mySheet.max_row):
            prContents = str(mySheet.cell(row=i, column=columnNumofEdgeEntries).value).strip().split(",")
            if str(prContents) != "['None']":

                for ea in prContents:
                    if str(ea) not in lineDuplicateSet:
                        lineDuplicateSet.add(ea)

                        if "%" in ea:   # NOTE: the id of the OR nodes will be the %### but ill make the labels all OR s
                            glbOrCtr += 1
                            if "%" in ea[4:]:  # if OR->OR, also remap second instance 3: for 2dig, 4: for 3dig?
                                glbOrCtr += 1

                        if "&" in ea:
                            glbAndCtr += 1
                            if "&" in ea[4:]:  # if AND->AND, also remap second instance
                                glbAndCtr += 1


                        # add the lines to the output files for manual checking
                        ea = ea.strip()  # clean
                        myOutFile.write(str(ea))
                        myOutFile.write('\n')

                        # split the line data, then add to the list complex  ( ('src','targ','L'), (etc), (etc)...)

                        a = ea.split(" ")
                        mySrc = a[0]
                        if len(a) == 3:
                            myEdgeLabel = a[1]
                            myTarg = a[2]
                            edgeList.append((mySrc, myTarg, myEdgeLabel))

                            if myTarg not in cumNodeSet:
                                c = (myTarg, myTarg)  # TODO CHANGE SECOND ELEM TO SUM USEFUL LATER??
                                nodeList.append(c)
                                cumNodeSet.add(myTarg)

                        if mySrc not in cumNodeSet:
                            b = (mySrc, mySrc)  # TODO CHANGE SECOND ELEM TO SUM USEFUL LATER??
                            nodeList.append(b)
                            cumNodeSet.add(mySrc)

    # print(nodeList)
    # print(edgeList)
    return nodeList, edgeList


cprqfile = "C:/Users/John DeForest/PycharmProjects/dartyclassdb1/2IntermediateProcessing/xlDBcleaning/deleteTestExportCURRENT3.xlsx"

myNodesLoL, myEdgesLoL = xl2SIFnetworkcreator(cprqfile, 0, 2, 7, 'edgelistOutput3.txt')  # 2nd param: 0 for MATH, 1 for MATH+ENGS
# TODO: this txt writing step^ is for manual checking of the reading from excel process,
#  really can just write straight to list format (as is DONE by the fn)

# print("--")
# print(myNodesLoL)
# print(myEdgesLoL)

"""Section2: testing dash-cyto app"""

myApp = dash.Dash(__name__)
myNodes = [
    {'data': {'id': shortID, 'label': labelID1}, }
    for shortID, labelID1 in myNodesLoL
]
myEdges = [
    {'data': {'source': sourceID, 'target': targetID, 'label': labelID2}}
    for sourceID, targetID, labelID2 in myEdgesLoL
]

# print("i--oi")
# print(myNodes)
# print(myEdges)

myAllElements = myNodes + myEdges
myDefaultStylesheet = [
    {'selector': 'node', 'style': {'label': 'data(id)'}},
    #{'selector': 'edge', 'style': {'label': 'data(label)'}},
    {'selector': 'edge', 'style': {'curve-style': 'bezier'}},
    {'selector': 'edge', 'style': {'mid-target-arrow-color': 'blue',
                                   'mid-target-arrow-shape': 'vee',
                                   'line-color': 'grey', 'arrow-scale': 3.5, }}
]

myApp.layout = dhtml.Div([
    dcyto.Cytoscape(
        id='cytoscape',
        elements=myAllElements,
        stylesheet=myDefaultStylesheet,
        style={'width': '100%', 'height': '800px'},
        # layout choices:
        # ["random",  bad
        # "preset",   If you have preset node locations, good.
        # "circle",   not for this project
        # "concentric", not for this project
        # "grid",       not for this project
        # "breadthfirst",  pretty good
        # "cose",          too bunched
        # added extras:------------------
        # `cose-bilkent` can't use for some reason     https://github.com/cytoscape/cytoscape.js-cose-bilkent
        # `cola`         nasty                         https://github.com/cytoscape/cytoscape.js-cola
        # `euler`        crashes                       https://github.com/cytoscape/cytoscape.js-dagre
        # `spread`       BAD                           https://github.com/cytoscape/cytoscape.js-spread
        # `dagre`        pretty good                   https://github.com/cytoscape/cytoscape.js-dagre
        # `klay`         decent                        https://github.com/cytoscape/cytoscape.js-klay
        layout={'name': 'klay',
                'roots': '[id = "MATH001"]'}
    )
])

if __name__ == '__main__':
    myApp.run_server(debug=True)
