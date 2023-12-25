import ClassField

cf = ClassField.Field()

btn = 'add_file'        #Нажатие кнопки

if btn == 'add_file':

    cf.add_file('PointCsv.csv')

    print(cf.list_file)
