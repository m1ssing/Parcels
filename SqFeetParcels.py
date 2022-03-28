import arcpy
import time

start = time.time()
tempTable = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\_Projects\\Major Projects\\Parcels\\Data\\BCAD\\BCAD_Prelim2021.gdb\\impr_detail"
fields = ["prop_id", "Imprv_det_type_cd", "imprv_det_area"]
sqft_dict = {0:"test"}
lstMA = ['MA', 'MA2.0', 'MA3.0', 'MA4.0']
with arcpy.da.SearchCursor(tempTable, fields) as Scur:
    for row in Scur:
        if row[0] in sqft_dict.keys():
            if row[1] in lstMA:
                sqft_dict[row[0]].append(row[2])
        else:
            if row[1] in lstMA:
                sqft_dict[row[0]] = [row[2]]
lstTable = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\_Projects\\Major Projects\\Parcels\\Data\\BCAD\\BCAD_Prelim2021.gdb\\impr_detail_plswork"
lstfields = ["prop_id", "imprv_det_area"]
if arcpy.Exists(lstTable):
    arcpy.TruncateTable_management(lstTable)

Icur = arcpy.da.InsertCursor(lstTable, lstfields)
for key,value in sqft_dict.items():
    print(value)
    if key != 0:
        Icur.insertRow((key, sum(value)))
    else:
        pass
end= time.time()
elapse = end - start 
print(elapse/60)
print(".")
