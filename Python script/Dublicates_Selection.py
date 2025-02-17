# Created by Ruslan Huseynov

import arcpy

import zipfile

import itertools

import random

import re



Layer = str(arcpy.GetParameterAsText(0))

Field = str(arcpy.GetParameterAsText(1))

arcpy.env.scratchWorkspace = "c:/projects/Scratch/scratch.gdb"

# dublicate script

tekrar = []

def dublicate (deyer):
    if deyer in tekrar:
        return 1

    else:
        tekrar.append(deyer)
        return 0


featureclass = Layer

field_names = [f.name for f in arcpy.ListFields(featureclass)]


    

arcpy.AddMessage("Tamamlandi {} eded".format(arcpy.GetCount_management(Layer)))
# add Field

Feature_data = Layer

Field_Name = "Dublicate"

Field_Type = "DOUBLE"

Field_Deyer = 'NULLABLE'


arcpy.AddField_management(Feature_data, Field_Name, Field_Type, '#', '#', '#', '#', Field_Deyer, 'NON_REQUIRED', '#')


arcpy.CalculateField_management(Layer, 'Dublicate',
                                'dublicate(!{}!)'.format(Field),
                                'PYTHON_9.3',
                                r'tekrar = []\n\ndef dublicate (deyer):\n    if deyer in tekrar:\n        return 1\n\n    else:\n        tekrar.append(deyer)\n        return 0')


Selection_type = 'NEW_SELECTION'

Sql_query = 'Dublicate = 1'

arcpy.SelectLayerByAttribute_management(Layer, Selection_type, Sql_query)




Delete_field = 'Dublicate'

arcpy.DeleteField_management(Layer, Delete_field)






