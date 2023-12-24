class File:
    def __init__(self,number):
        self.number = number

    def set_points(self,point):
        self.list_points.append(point)

    def del_points(self,point):
        self.list_points.pop(point.index)


    list_points = []


