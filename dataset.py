from roboflow import Roboflow
rf = Roboflow(api_key="OFcjwhoeGI2aE4NA0ox8")
project = rf.workspace("gryffindor-gk5ny").project("feature-extraction-jk4ua")
version = project.version(2)
dataset = version.download("yolov12")
                