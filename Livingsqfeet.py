import arcpy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
PID = []
layer = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\2020PrelimParcels.gdb\\BCAD_Final2"
fields = ['PID_1']
with arcpy.da.SearchCursor(layer, fields) as Scur:
    for row in Scur:
        if row[0] != None:
            PID.append(row[0])
for x in PID:
    driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe")
    lst = []
    page = driver.get('https://propaccess.trueautomation.com/ClientDB/Property.aspx?cid=51&prop_id={}'.format(x))
    buyer = driver.find_element_by_xpath('//*[@id="improvementBuilding"]').click() 
    buyers = driver.find_elements_by_xpath('/html/body/form/div/div[5]/div[9]/table[1]/tbody/tr/td[3]')
    time.sleep(7)
    for node in buyers:
        if node.text in lst:
            pass
        else:
            lst.append(node.text)
    driver.close()
    print(lst)
    if lst == []or lst == ['sqft']:
       continue
    lst = lst[0].split("\n")
    split_string = lst[0].split(" ", 1)
    layer_new = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\2020PrelimParcels.gdb\\PID_sqfeet"
    field_new = ['PID', 'SqFt']
    with arcpy.da.InsertCursor(layer_new, field_new) as Ucur:
        lst = []
        Ucur.insertRow((x, int(float(split_string[0]))))
        print("update")
    print(x, int(float(split_string[0])))


print(PID)
print(".")