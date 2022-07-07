# darty-Course-DB-and-PrereqFlow-Tracker

trying to make sense of Dartmouth's ORC and create a useful database of courses and prereqs (required/recommended/concurrent/etc) as well as other important info

undergrad ORC home: http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate


# Node Network testing:
## (7/7/22) Converted! Dash-Cytoscape running, reworking some backend stuff to optimize and clean up the graph a bit (Math 22/24 stuff and the like), but can now associate course attributes with various interactive features as I want. below is a basic viz of the Math dept - not much has changed visually since previous updates but the data linkage + capability(s) have improved enormously:
![image](https://user-images.githubusercontent.com/87039043/177697199-4dde685e-e563-4bff-8aac-19fe1d612d34.png)

## (7/6/22) Moving to Dash-Cytoscape for interactive visualization given successful tests in Cytoscape for Math and Engineering departments
requires mods to xl-2-graph scripts, may take a bit to convert to .js-friendly format

## (6/28/22) Network Exports: still may work on aesthetics and readability (and ofc interactivity), but ANDs/ORs all work!
![testExp sif](https://user-images.githubusercontent.com/87039043/176257254-527033d9-3827-434c-afb2-e389e005a400.png)
see xlRead2SIFWrite1.py for excel DB -> .SIF file (then opened and organized for aesthetics in Cytoscape)

## (6/26-28/22) BIG CHANGE: switched to .SIF-based Cytoscape visualization for future interactivity flexibility and for simplicity and functionality of database (most important). Note: need to open and run Cytoscape desktopApp before executing xlRead2SIFWrite1.py

still porting over all the data formats to CSV entries in ea excel row (readable to SIF format via my XL2SIF parser^), but here is a mini-network as proof of concept:

![image](https://user-images.githubusercontent.com/87039043/176141378-525a8104-0ee2-4e9f-9e46-c27983e23571.png)

(phew, after *many* tries with jsongraph and other libs and data structure/storage/viz options, got one to work)

## (6/24/22) UPDATE! Got complex AND/OR prereqs sorted and Full Math Department conversion, cleaning/fixing for DB, and most importantly, PREREQ VIZ!:
![image](https://user-images.githubusercontent.com/87039043/175492070-3af15bf3-85bf-45d0-8070-7594085b1a15.png)

^ugly as all hell but thats not my fault. okay, maybe it is a little bit. later on will mess around with physics algos to get nicer distribution and clustering of nodes and other aesthetics

## (6/23/22) current progress (in coursePrereqGraphTesting1.py) on handling complex ORs and ANDs on course subset (2 lol):
![image](https://user-images.githubusercontent.com/87039043/175473854-5da14f66-567e-40ca-af9e-354737d971f2.png)

^rough, using matplotlib, but has all the correct connections...now to add objects/edge/node info...

## (6/21/22) getting situated with the NetworkX package, need to test for lots of properties of nodes and edges for complex prereqs but should be fine
functionality testing w autogen nodes complete:
![image](https://user-images.githubusercontent.com/87039043/174941663-25838a5b-5643-408c-bc08-2caaab3e22f3.png)


# allwebstripr3.py 
(1/4/22) current "working" webscraper (on all of the ORC department subpages, rather impressively), output file still needs serious manual checking and cleaning, separation of fields, etc
may require serious rewriting of the scraping logic to get things sorted out, if ever...the ORC pages are not at all consistent in their HTML/CSS elements which makes finding things a royal...once I clean things/sort out manually the viz comes along quite nicely...see above (edited 6/24/22)

