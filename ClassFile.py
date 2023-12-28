class File:
    def __init__(self, number=0, name_file=''):
        self.number = number
        self.list_points = []
        self.name_file = name_file

    def set_points(self,point):
        self.list_points.append(point)

    def del_points(self,point):
        self.list_points.pop(point.index)
