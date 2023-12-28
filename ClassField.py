import csv
import ClassPoint
import ClassFile
class Field:
    def __init__(self):
        self.count_file = 0
        self.list_file = []

    def add_file(self,name_file):

        self.count_file += 1
        cf = ClassFile.File(number = self.count_file, name_file = name_file)
        self.list_file.append(cf)

        file = open(name_file, 'r', encoding='utf-8')
        reader = csv.DictReader(file, delimiter=';', quotechar='"')

        i = 0
        for row in reader:
            cp = ClassPoint.Point(x=row['x'], y=row['y'], index=i, number_file=cf.number)
            cf.set_points(cp)
            i + 1

    def edit_file(self,cf):

        file = open(cf.name_file,'w',encoding='utf-8',newline='')

        writer = csv.DictWriter(file, fieldnames=['x','y'], delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

        for p in cf.list_points:
            writer.writerow({'x': p.x, 'y': p.y})

    def delete_point(self, del_list_points):

        for file in self.list_file:
            for point in file.list_points:
                if point in del_list_points:
                    file.del_points(point)

