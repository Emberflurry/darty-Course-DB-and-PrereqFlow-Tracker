import py4cytoscape as py4
print(dir(py4))
print(py4.cytoscape_ping())
print(py4.cytoscape_version_info())


# TODO: import .sif file and create cytoscape network graph from it
#import_network
py4.import_network_from_file("C:/Users/John DeForest/Desktop/m74test2.sif")
print("done")
