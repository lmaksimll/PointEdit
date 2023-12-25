import csv
import ClassPoint
import ClassFile
class Field:
    def add_file(self,name_file):

        self.count_file = self.count_file + 1
        cf = ClassFile.File(number = self.count_file)
        self.list_file.append(cf)

        file = open(name_file, 'r', encoding='utf-8')
        reader = csv.DictReader(file, delimiter=';', quotechar='"')

        i = 0
        for row in reader:
            cp = ClassPoint(x=row.x, y=row.y, index = i, number_file = cf.number)
            cf.set_points(cp)
            i + 1

    def edit_file(self):
        pass

    def delete_point(self):
        pass

    count_file = 0
    list_file = []
