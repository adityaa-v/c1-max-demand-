from tkinter import *
from tkinter import ttk
import xlsxwriter

load_groups = ['(a) Lighting (please select one below)',' (i) Lighting except for communial lighting and <1000W',' (ii) Outdoor lighting exceeding a total of 1000W', '(b) Sub-outlets',
' (i) Socket outlets not exceeding 10 A',' (ii) 1 or more 15 A socket outlets',' (iii) 1 or more 20 A socket outlets',  
'Appliances (c)', '(d) Heating/Cooling', '(e) Instant Water Heaters', '(f) Storage Water Heaters',
'(g) Spa and swimming pool heaters', '(h) Communal lighting','(i) Socket','(j) Appliances (please select one below)',' (i) clothes dryer, water heaters, self-heating washing machines, wash boilers',
' (ii) Fixed space heating, airconditioning equipment, saunas',' (iii) Spa and swimming pool heaters',' (iv) Charging equipment associated with electric vehicles',  '(k) Lifts',
'(l) Motors', '(m) Other Appliances']
load_groupsc2 = ['(a) Lighting other than in load group (f)', '(b) sockets',' (i) Not exceeding 10A',' (ii) Not exceeding 10 A in areas with permanent heating/cooling equipment'
,' (iii) Exceeding 10 A', '(c) ',' (i) Appliances for cooking, heating and cooling', ' (ii) Electric vehicles charging', '(d) Motors','(e) Lifts', '(f) Fuel dispensing units',
'(g) Heating elements', '(h) Welding machines','(i) X-ray equipment','(j) Other equipment' ] 
groupc2_options=['Residential institutions, hotels, boarding houses, hospitals, accommodation houses, motels',
'Factories, shops, stores, offices, business premises, schools and churches']

result_list = []

class Application(Frame):
    light_points = 0
    light_watts = 0
    outlets_points = 0
    outlets_watts = 0
    subappliances_points = 0
    subappliances_watts = 0
    general_points = 0
    general_watts = 0

    aValue = 0
    bValue = 0
    cValue = 0
    dValue = 0
    eValue = 0
    fValue = 0
    gValue = 0
    hValue = 0
    iValue = 0
    jValue = 0

    a2Value=0
    b2Value=0
    c2Value=0
    d2Value=0
    e2Value=0


    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.init_window()

    def init_window(self): 
        
        nb = ttk.Notebook(master)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.homeTab = ttk.Frame(nb) #tab 1 creation
        nb.add(self.homeTab, text='Home Menu')    
        self.resultTab = ttk.Frame(nb) 
        nb.add(self.resultTab, text='Summary')    

        self.projname_lbl = Label (self.homeTab,font="Helvetica 16 bold", justify=CENTER, text="Home Menu")
        self.projname_lbl.grid(rowspan=1, columnspan=2)

        self.projname_lbl = Label (self.homeTab, text="Project Name:", height=2, width=25)
        self.projname_lbl.grid(row=2)

        self.projname_entry = IntVar()  
        self.projname_entry = Entry (self.homeTab)
        self.projname_entry.grid(row=2, column=2)  

        self.projno_lbl = Label (self.homeTab, text="Project Number:", height=2)
        self.projno_lbl.grid(row=3)
        
        self.projno_entry = IntVar()  
        self.projno_entry = Entry (self.homeTab)
        self.projno_entry.grid(row=3, column=2)

        self.date_lbl = Label (self.homeTab, text="Data Completed:", height=2)
        self.date_lbl.grid(row=4)
        
        self.date_entry = IntVar()  
        self.date_entry = Entry (self.homeTab)
        self.date_entry.grid(row=4, column=2)

        self.completed_lbl = Label (self.homeTab, text="Filled by:", height=2)
        self.completed_lbl.grid(row=5)
        
        self.completed_entry = IntVar()  
        self.completed_entry = Entry (self.homeTab)
        self.completed_entry.grid(row=5, column=2)

        self.reviewed_lbl = Label (self.homeTab, text="Reviewed by:", height=2)
        self.reviewed_lbl.grid(row=6)
        
        self.reviewed_entry = IntVar()  
        self.reviewed_entry = Entry (self.homeTab)
        self.reviewed_entry.grid(row=6, column=2)

        self.init = Label (self.homeTab, text="Please enter the number of\n electrical installations (units):", height=2)
        self.init.grid(row=7)
        
        self.entry_unit = IntVar()  
        self.entry_unit = Entry (self.homeTab)
        self.entry_unit.grid(row=7, column=2) 

        self.init = Label (self.homeTab, text="Please select which non-domestic\n electrical installations applies:", height=2).grid(row=8)

        self.groupc2 = StringVar(master)
        self.groupc2.set("-") # default value
        self.om_groupc2 = OptionMenu(self.homeTab, self.groupc2, *groupc2_options, )
        self.om_groupc2.config(width=25)
        self.om_groupc2.grid(row=8, column=2)
            

        self.c1_btn = Button(self.homeTab, text="C1", bg="light grey", command=self.unit_redirect, width=5).grid(row=9, column=0)    

        self.c2_btn = Button(self.homeTab, text="C2", bg="light grey", command=self.c2_redirect, width=5).grid(row = 9, column=1)

        self.c3_btn = Button(self.homeTab, text="C3", bg="light grey", command=self.c3_redirect, width=5).grid(row =9, column=2)

        self.lbl_resulta = Label (self.resultTab, text = "Lighting (a): ", height = 1, width=20).grid(row=1, column=0)
        self.result_a = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=1, column=1)
        self.lbl_resultb = Label (self.resultTab, text = "Outlets (b): ", height = 1, width=20).grid(row=2, column=0)
        self.result_b = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=2, column=1)
        self.lbl_resultc = Label (self.resultTab, text = "Appliances (c): ", height = 1, width=20).grid(row=3, column=0)
        self.result_c = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=3, column=1)
        self.lbl_resultd = Label (self.resultTab, text = "Heating/Cooling (d): ", height = 1, width=20).grid(row=4, column=0)
        self.result_d = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=4, column=1)
        self.lbl_resulte = Label (self.resultTab, text = "Instant Water Heaters (e): ", height = 1, width=20).grid(row=5, column=0)
        self.result_e = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=5, column=1)
        self.lbl_resultf = Label (self.resultTab, text = "Storage Water Heaters (f): ", height = 1, width=20).grid(row=6, column=0)
        self.result_f = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=6, column=1)
        self.lbl_resultg = Label (self.resultTab, text = "Spa and swimming pool heaters (g): ", height = 1, width=20).grid(row=7, column=0)
        self.result_g = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=7, column=1)
        self.lbl_resulth = Label (self.resultTab, text = "Communal lighting (h): ", height = 1, width=20).grid(row=8, column=0)
        self.result_h = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=8, column=1)
        self.lbl_resulti = Label (self.resultTab, text = "Socket (i): ", height = 1, width=20).grid(row=9, column=0)
        self.result_i = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=9, column=1)
        self.lbl_resultj = Label (self.resultTab, text = "Appliances (j): ", height = 1, width=20).grid(row=10, column=0)
        self.result_j = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=10, column=1)
        self.lbl_resultk = Label (self.resultTab, text = "Lifts (k): ", height = 1, width=20).grid(row=11, column=0)
        self.result_k = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=11, column=1)
        self.lbl_resultl = Label (self.resultTab, text = "Motors (l): ", height = 1, width=20).grid(row=12, column=0)
        self.result_l = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=12, column=1)
        self.lbl_resultm = Label (self.resultTab, text = "Other Appliances (m): ", height = 1, width=20).grid(row=13, column=0)
        self.result_m = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=13, column=1)
        self.total = Label (self.resultTab, text = "Total", height = 1, width=20).grid(row=14, column=0)
        self.total = Label (self.resultTab, text = "yeet", height = 1, width=20).grid(row=14, column=1)

        def xlsx_test():
            workbook = xlsxwriter.Workbook('please-work.xlsx')
            worksheet = workbook.add_worksheet()

            worksheet.set_column('A:A', 20)

            worksheet.write('A1', 'Number of Units')
            worksheet.write('B1', int(self.entry_unit.get()))

            worksheet.write('A2', 'Load Group')
            worksheet.write('B2', 'Watts')
            worksheet.write('C2', 'Points')
            worksheet.write('D2', 'Amperes')

            worksheet.write('A3', 'Lighting (a)')
            worksheet.write('B3', int(self.light_watts))
            worksheet.write('C3', int(self.light_points))
            worksheet.write('D3', int(self.aValue))

            worksheet.write('A4', 'Outlets (b)')
            worksheet.write('B4', int(self.outlets_watts))
            worksheet.write('C4', int(self.outlets_points))
            worksheet.write('D4', int(self.bValue))

            worksheet.write('A5', 'Appliances (c)')
            worksheet.write('B5', int(self.general_watts))
            worksheet.write('C5', int(self.general_points))
            worksheet.write('D5', int(self.cValue))

            worksheet.write('A6', 'Heating/Cooling (d)')
            worksheet.write('B6', int(self.general_watts))
            worksheet.write('C6', int(self.general_points))
            worksheet.write('D6', int(self.dValue))

            worksheet.write('A7', 'Heating/Cooling (e)')
            worksheet.write('B7', int(self.general_watts))
            worksheet.write('C7', int(self.general_points))
            worksheet.write('D7', int(self.eValue))

            worksheet.write('A8', 'Heating/Cooling (f)')
            worksheet.write('B8', int(self.general_watts))
            worksheet.write('C8', int(self.general_points))
            worksheet.write('D8', int(self.fValue))

            worksheet.write('A9', 'Heating/Cooling (g)')
            worksheet.write('B9', int(self.general_watts))
            worksheet.write('C9', int(self.general_points))
            worksheet.write('D9', int(self.gValue))

            worksheet.write('A10', 'Heating/Cooling (f)')
            worksheet.write('B10', int(self.general_watts))
            worksheet.write('C10', int(self.general_points))
            worksheet.write('D10', int(self.fValue))

            


            workbook.close()

        def update ():
            total_sum = self.aValue + self.bValue + self.cValue + self.dValue + self.eValue + self.fValue 

            self.total.config(text = total_sum,bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)



        self.btn_calculations = Button (self.resultTab, text="Update", height=1, width=20, command=update).grid (row=15,column=1)

        self.btn_calculations = Button (self.resultTab, text="Write to excel", command=xlsx_test, height=1, width=20).grid (row=15, column=0)

        

    def unit_redirect(self):
        control = Toplevel()
        control.geometry("450x375")
        control.title("TABLE C1")
        
        nb = ttk.Notebook(control)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.tab1 = ttk.Frame(nb) #tab 1 creation
        nb.add(self.tab1, text='Load Groups')       
        self.tab2 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.tab2, text='Lighting (a)')
        self.tab3 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.tab3, text='Outlets (b)')
        self.tab4 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.tab4, text='Applainces (j)')
        self.tab5 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.tab5, text='Results')

        self.living_units = Label (self.tab1, text = self.entry_unit.get(), height=1, width=20, font='Helvetica 12 bold') #Label
        self.living_units.grid(rowspan=1, columnspan=2)

        self.lbl_load= Label (self.tab1, text = "Type of Load", height=1, width=20) #Label
        self.lbl_load.grid(row=2, column = 0)

        self.cntrl_loadgroup = StringVar(control)
        self.cntrl_loadgroup.set("-") # default value
        self.om_loadgroup = OptionMenu(self.tab1, self.cntrl_loadgroup, *load_groups, )
        self.om_loadgroup.config(width=35)
        self.om_loadgroup.grid(row=2, column=1)

        self.lbl_points = Label (self.tab1, text = "Points", height=1, width=20) #Label
        self.lbl_points.grid(row=4, column = 0)
        
        self.entry_points = StringVar()  
        self.entry_points = Entry (self.tab1) ######## ENTRY BOX
        self.entry_points.grid(row=4, column=1)

        self.lbl_watts = Label (self.tab1, text = "Watts", height=1, width=20) #Label
        self.lbl_watts.grid(row=5, column = 0)

        self.entry_watts = StringVar()  
        self.entry_watts = Entry (self.tab1) ######## ENTRY BOX
        self.entry_watts.grid(row=5, column=1)



        
        #RESULTS#
        self.lbl_resulta = Label (self.resultTab, text = "Lighting (a): ", height = 1, width=20)
        self.lbl_resulta.grid(row=1, column=0)
        self.result_a = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_a.grid(row=1, column=1)
        self.lbl_resultb = Label (self.resultTab, text = "Outlets (b): ", height = 1, width=20)
        self.lbl_resultb.grid(row=2, column=0)
        self.result_b = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_b.grid(row=2, column=1)
        self.lbl_resultc = Label (self.resultTab, text = "Appliances (c): ", height = 1, width=20)
        self.lbl_resultc.grid(row=3, column=0)
        self.result_c = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_c.grid(row=3, column=1)
        self.lbl_resultd = Label (self.resultTab, text = "Heating/Cooling (d): ", height = 1, width=20)
        self.lbl_resultd.grid(row=4, column=0)
        self.result_d = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_d.grid(row=4, column=1)
        self.lbl_resulte = Label (self.resultTab, text = "Instant Water Heaters (e): ", height = 1, width=20)
        self.lbl_resulte.grid(row=5, column=0)
        self.result_e = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_e.grid(row=5, column=1)
        self.lbl_resultf = Label (self.resultTab, text = "Storage Water Heaters (f): ", height = 1, width=20)
        self.lbl_resultf.grid(row=6, column=0)
        self.result_f = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_f.grid(row=6, column=1)
        self.lbl_resultg = Label (self.resultTab, text = "Spa and swimming pool heaters (g): ", height = 1, width=20)
        self.lbl_resultg.grid(row=7, column=0)
        self.result_g = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_g.grid(row=7, column=1)
        self.lbl_resulth = Label (self.resultTab, text = "Communal lighting (h): ", height = 1, width=20)
        self.lbl_resulth.grid(row=8, column=0)
        self.result_h = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_h.grid(row=8, column=1)
        self.lbl_resulti = Label (self.resultTab, text = "Socket (i): ", height = 1, width=20)
        self.lbl_resulti.grid(row=9, column=0)
        self.result_i = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_i.grid(row=9, column=1)
        self.lbl_resultj = Label (self.resultTab, text = "Appliances (j): ", height = 1, width=20)
        self.lbl_resultj.grid(row=10, column=0)
        self.result_j = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_j.grid(row=10, column=1)
        self.lbl_resultk = Label (self.resultTab, text = "Lifts (k): ", height = 1, width=20)
        self.lbl_resultk.grid(row=11, column=0)
        self.result_k = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_k.grid(row=11, column=1)
        self.lbl_resultl = Label (self.resultTab, text = "Motors (l): ", height = 1, width=20)
        self.lbl_resultl.grid(row=12, column=0)
        self.result_l = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_l.grid(row=12, column=1)
        self.lbl_resultm = Label (self.resultTab, text = "Other Appliances (m): ", height = 1, width=20)
        self.lbl_resultm.grid(row=13, column=0)
        self.result_m = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.result_m.grid(row=13, column=1)
        self.total = Label (self.resultTab, text = "Total", height = 1, width=20)
        self.total.grid(row=14, column=0)
        self.total = Label (self.resultTab, text = "yeet", height = 1, width=20)
        self.total.grid(row=14, column=1)

        def update ():
            total_sum = self.aValue + self.bValue + self.cValue + self.dValue + self.eValue + self.fValue 

            self.total.config(text = total_sum,bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
        
    

        def calculations():

            def getUnit(self): #get values
                self.x = int(self.entry_unit.get())                   
                return self.x

            def getLoadgroup(self):
                self.x = self.cntrl_loadgroup.get()
                return self.x
            def getPoints(self):
                self.x = int(self.entry_points.get())
                self.general_points = self.x
                return self.x
            def getWatts(self):
                self.x = int(self.entry_watts.get())
                self.general_watts = self.x
                return self.x  
            
            def lighting(self):
                self.amps = 0
                
                if (getLoadgroup(self)==load_groups[1]):
                    if (getUnit(self)==1):

                        if (getPoints(self)<=20):
                            self.amps = (self.amps + 3)/3
                            self.aValue = self.amps
                            return str(self.amps)

                        if (getPoints(self)>=40):
                            self.amps = (self.amps + 5)/3
                            self.aValue = self.amps
                            return str(self.amps)
                            if (getPoints(self)>=60):
                                self.amps = (self.amps + 2)/3
                                self.aValue = self.amps
                                return str(self.amps)
                                if (getPoints(self)>=80):
                                    self.amps = (self.amps + 2)/3
                                    self.aValue = self.amps
                                    return str(self.amps)
                                    if (getPoints(self)>=100):
                                        self.amps = (self.amps + 2)/3
                                        self.aValue = self.amps
                                        return str(self.amps)
                        
                    if (getUnit(self)>=2 and getUnit(self)<=5):#2-5

                        self.aValue = 6
                        return '6'                    
                    
                    if (getUnit(self)>=6 and getUnit(self)<=20):#6-20

                        self.excess = getUnit(self) - 6
                        self.amps = ((self.excess * 0.25) + 5)/3     
                        self.aValue = self.amps
                        return str(self.amps)  

                    if (getUnit(self)>=21):#21+
                        self.excess = getUnit(self) - 21
                        self.amps = (self.excess * 0.25)   
                        self.aValue = self.amps         
                        return str(self.amps)  
                             
                if (getLoadgroup(self)==load_groups[2]):
                    if(getUnit(self)==1):
                        self.amps = getWatts(self) * 0.75
                        self.aValue = self.amps
                        return str(self.amps)

                else:
                    return 'lighting error'

            if (lighting(self)!='lighting error'):
                      
                self.light_result = Label (self.tab5, text = ""+lighting(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=1, column=1)

                self.amps = Label (self.tab1, text = lighting(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)
            

            def b(self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[4]):

                    if (getUnit(self)==1):

                        if (getPoints(self)<=20):
                                self.amps = self.amps + 10
                                self.bValue = self.amps
                                return str(self.amps)

                        if (getPoints(self)>=40):
                            self.amps = self.amps + 15
                            self.bValue = self.amps
                            return str(self.amps)
                            if (getPoints(self)>=60):
                                self.amps = self.amps + 5
                                self.bValue = self.amps
                                return str(self.amps)
                                if (getPoints(self)>=80):
                                    self.amps = self.amps + 5
                                    self.bValue = self.amps
                                    return str(self.amps)
                                    if (getPoints(self)>=100):
                                        self.amps = self.amps + 5
                                        self.bValue = self.amps
                                        return str(self.amps)
                        
                    if (getUnit(self)>=2 and getUnit(self)<=5):#2-5

                        if (getUnit(self)==2):
                            self.amps = 10
                            self.bValue = self.amps
                            return str(self.amps)
                        if(getUnit(self)>=3 and getUnit(self)<=5):
                            self.amps = (getUnit(self) - 1 ) *  5
                            self.amps = self.amps +10
                            self.bValue = self.amps
                            return str(self.amps)
                        else: 
                            return "you is a bum"
                    
                    
                    if (getUnit(self)>=6 and getUnit(self)<=20):#6-20

                        if (getUnit(self)==6):
                            self.amps = 15
                            self.bValue = self.amps
                            return str(self.amps)
                        if(getUnit(self)>=7 and getUnit(self)<=20):
                            self.amps = (getUnit(self) - 1 ) *  3.75
                            self.amps = self.amps = 15
                            self.bValue = self.amps
                            return str(self.amps)
                        else: 
                            return "you is a bum"

                    if (getUnit(self)>=21):#21+
                        if (getUnit(self)==21):
                            self.amps = 50
                            self.bValue = self.amps
                            return str(self.amps)
                        if(getUnit(self)>=22):
                            self.amps = (getUnit(self) - 1 ) *  1.9
                            self.amps = self.amps + 50
                            self.bValue = self.amps
                            return str(self.amps)
                        else: 
                            return "you is a bum"
                             
                if (getLoadgroup(self)==load_groups[5]):
                    self.bValue = 10
                    return "10"
                if (getLoadgroup(self)==load_groups[6]):
                    self.bValue = 15
                    return "15"
                
                else:
                    return 'yeet'
            if (b(self)!='yeet'):          
                self.light_result = Label (self.tab5, text = ""+b(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=2, column=1)              
                self.amps = Label (self.tab3, text = b(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)           
                             
            def c(self): #WORKS
                self.amps = 0
                self.cValue = 0

                if (getLoadgroup(self)==load_groups[7]):

                    if (getUnit(self)==1):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.cValue = self.amps
                        return str(self.amps)

                    if (getUnit(self)>1 and getUnit(self)<=5):
                        self.amps= 15
                        self.cValue = self.amps
                        return str(self.amps)
                        
                    if (getUnit(self)>= 6):
                        self.amps= getUnit(self) * 2.8
                        self.cValue = self.amps
                        return str(self.amps)
                
                else:
                    return 'yeet1'
            if (c(self)!='yeet1'):
                
                self.light_result = Label (self.tab5, text = ""+c(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=3, column=1)

                self.amps = Label (self.tab1, text = c(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            def d (self):#WORKS
                self.amps = 0
                self.dValue = 0

                if (getLoadgroup(self)==load_groups[8]):

                    if (getUnit(self)==1):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.dValue = self.amps
                        return str(self.amps)

                    if (getUnit(self)>=2 and getUnit(self)<=5):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.dValue = self.amps
                        return str(self.amps)

                    if (getUnit(self)>= 6 and getUnit(self)<=20):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.dValue = self.amps
                        return str(self.amps)

                    if(getUnit(self)>=21):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.dValue = self.amps
                        return str(self.amps)

                else:
                    return 'yeet2'
            if (d(self)!='yeet2'):
                self.light_result = Label (self.tab5, text = ""+d(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=4, column=1)

                self.amps = Label (self.tab1, text = d(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)
            
            def e (self): #WORKS
                self.amps = 0
                self.eValue = 0
                if (getLoadgroup(self)==load_groups[8]):
                    if (getUnit(self)==1):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.333
                        self.eValue = self.amps
                        return str(self.amps)
                    if (getUnit(self)>=2 and getUnit(self)<=5):
                        self.amps = 6 * getUnit(self)
                        self.eValue = self.amps
                        return str(self.amps)
                    if (getUnit(self)>= 6 and getUnit(self)<=20):
                        self.amps = 6 * getUnit(self)   
                        self.eValue = self.amps                             
                        return str(self.amps)
                    if(getUnit(self)>=21):
                        self.amps = (getUnit(self) * 0.8) + 100
                        self.eValue = self.amps
                        return str(self.amps)
                else:
                    return 'yeet3'

            if (e(self)!='yeet3'):
                self.light_result = Label (self.tab5, text = ""+e(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=5, column=1)

                self.amps = Label (self.tab1, text = e(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            def f (self):
                self.amps = 0
                self.fValue = 0

                if (getLoadgroup(self)==load_groups[9]):

                    if (getUnit(self)==1):

                        return "full load connected"

                    if (getUnit(self)>=2 and getUnit(self)<=5):
                        self.amps = 6 * getUnit(self)
                        self.fValue = self.amps
                        return str(self.amps)

                    if (getUnit(self)>= 6 and getUnit(self)<=20):
                        self.amps = 6 * getUnit(self)
                        self.fValue = self.amps
                        return str(self.amps)

                    if(getUnit(self)>=21):
                        self.amps = (getUnit(self) * 0.8) + 100
                        fValue = self.amps
                        return str(self.amps)

                else:
                        return 'yeet4'

                if (f(self)!='yeet4' or f(self)=='full load connected'):
                    self.light_result = Label (self.tab5, text = ""+f(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                    self.light_result.grid(row=6, column=1)

                    self.amps = Label (self.tab1, text = f(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                    self.amps.grid(rowspan=7, columnspan=2)
                
            def g (self):#SPAAAA??? HOW TO DO THIS ONE WHAT DO HECK 
                self.amps = 0

                if (getLoadgroup(self)==load_groups[10]):
                    if (getUnit(self)==1):
                        
                        return str(self.amps)
                    if (getUnit(self)>=2 and getUnit(self)<=5):
                        return str(self.amps)
                    if (getUnit(self)>= 6 and getUnit(self)<=20):
                        return str(self.amps)
                    if(getUnit(self)>=21):
                        return str(self.amps)
                else:
                        return 'yeet5'

                if (g(self)!='yeet5'):
                    self.light_result = Label (self.tab5, text = ""+g(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                    self.light_result.grid(row=7, column=1)

                    self.amps = Label (self.tab1, text = g(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                    self.amps.grid(rowspan=7, columnspan=2)

                
            def h (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[11]):
                    if (getUnit(self)==1):
                        return "N/A"
                    if (getUnit(self)>=2):
                        return "full connected laod"        
                else:
                    return 'yeet6'

            if (h(self)!='yeet6'):
                self.light_result = Label (self.tab5, text = ""+h(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=8, column=1)

                self.amps = Label (self.tab1, text = h(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)      

            def i (self):
                self.amps = 0 
                iValue = 0
                if (getLoadgroup(self)==load_groups[12]):
                    if (getUnit(self)==1):
                        return "N/A"
                        return str(self.amps)
                    if (getUnit(self)>=2):
                        self.amps = getUnit(self) * 2
                        iValue = self.amps
                        if self.amps >=15:
                            return "Value exceeded"
                    else:
                        return str(self.amps) 

                else:
                    return 'yeet7'

            if (i(self)!='yeet7'):
                self.light_result = Label (self.tab5, text = ""+i(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=9, column=1)

                self.amps = Label (self.tab1, text = i(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)     
            
            def appliances(self):
                self.amps = 0
                self.aValuejValue = 0
                             
                if (getLoadgroup(self)==load_groups[13] or getLoadgroup(self)==load_groups[1] or getLoadgroup(self)==load_groups[2]):
                    if (getUnit(self) == 1):
                        return "Not applicable"

                if (getLoadgroup(self)==sub_appliances[14]):
                    if (getUnit(self) == 1):
                        return "Fully connected load"

                if (getLoadgroup(self) ==sub_appliances[15]):
                    if getUnit(self)>=2:
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.5
                        self.jValue = self.amps
                        return str(self.amps)
                
                if (getLoadgroup(self) ==sub_appliances[16]):
                    if getUnit(self)>=2:
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.jValue = self.amps
                        return str(self.amps)
                
                if (getLoadgroup(self) == sub_appliances[17]):

                    if (getUnit(self)>=2 and getUnit(self)<=5):#2-5
                        return "100% connected load"
                
                    if (getUnit(self)>=6 and getUnit(self)<=20):#6-20
                        return "90% connected load"

                    if (getUnit(self)>=21):#21+
                        return "75% connected load"
 
                else:
                    return 'yeet'

            if (appliances(self)!='yeet'):          

                self.appliance_result = Label (self.tab5, text = ""+appliances(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appliance_result.grid(row=2, column=1)

                self.amps = Label (self.tab4, text = appliances(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)


            def k (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[18]):
                    if (getUnit(self)==1):
                        
                        return str(self.amps)
                    if (getUnit(self)>=2 and getUnit(self)<=5):
                        return str(self.amps)
                    if (getUnit(self)>= 6 and getUnit(self)<=20):
                        return str(self.amps)
                    if(getUnit(self)>=21):
                        return str(self.amps)  
                else:
                    return 'yeet8'

            if (k(self)!='yeet8'):
                self.light_result = Label (self.tab5, text = ""+k(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=10, column=1)

                self.amps = Label (self.tab1, text = k(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)     

    def c2_redirect(self):
        control = Toplevel()
        control.geometry("450x375")
        control.title("TABLE C2")
        
        nb = ttk.Notebook(control)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.c2tab = ttk.Frame(nb) #tab 1 creation
        nb.add(self.c2tab, text='Load Groups')       
        self.c2tab1 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.c2tab1, text='Results')

        self.living_unitsc2 = Label (self.c2tab, text = self.groupc2.get(), height=1, width=20, font='Helvetica 12 bold') #Label
        self.living_unitsc2.grid(rowspan=1, columnspan=2)

        self.lbl_loadc2= Label (self.c2tab, text = "Type of Load", height=1, width=20) #Label
        self.lbl_loadc2.grid(row=2, column = 0)

        self.cntrl_loadgroupc2 = StringVar(control)
        self.cntrl_loadgroupc2.set("-") # default value
        self.om_loadgroupc2 = OptionMenu(self.c2tab, self.cntrl_loadgroupc2, *load_groupsc2)
        self.om_loadgroupc2.config(width=35)
        self.om_loadgroupc2.grid(row=2, column=1)

        self.lbl_wattsc2 = Label (self.c2tab, text = "Watts", height=1, width=20) #Label
        self.lbl_wattsc2.grid(row=3, column = 0)

        self.entry_wattsc2 = StringVar()  
        self.entry_wattsc2 = Entry (self.c2tab) ######## ENTRY BOX
        self.entry_wattsc2.grid(row=3, column=1)

        self.lbl_outletc2 = Label (self.c2tab, text = "Number of Outlets: ", height=1, width=20) #Label
        self.lbl_outletc2.grid(row=4, column = 0)

        self.entry_outletc2 = StringVar()  
        self.entry_outletc2 = Entry (self.c2tab) ######## ENTRY BOX
        self.entry_outletc2.grid(row=4, column=1)

        def calculationsc2():
    
            def getGroup(self): #get values
                self.x = self.groupc2.get()                   
                return self.x
            def getLoadgroup(self):
                self.x = self.cntrl_loadgroupc2.get()
                return self.x
            def getOutlet(self):
                self.x = int(self.entry_outletc2.get())
                return self.x
            def getWatts(self):
                self.x = int(self.entry_wattsc2.get())
                self.general_watts = self.x
                return self.x  
            
            def a(self):
                self.amps = 0
                if (getLoadgroup(self)==load_groupsc2[0]): #load group lighting
                    if (getGroup(self)==groupc2_options[0]):
                        self.amps = getWatts(self) * 0.75
                        a2Value = self.amps
                        return str(self.amps)
                    if (getGroup(self)==groupc2_options[1]):
                        self.amps = getWatts(self)
                        a2Value = self.amps
                        return str(self.amps)
                else:
                    return 'c2a'
            if (a(self)!='c2a'):                     
                self.c2light_result = Label (self.c2tab1, text = ""+a(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.c2light_result.grid(row=1, column=1)
                self.c2amps = Label (self.c2tab, text = a(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.c2amps.grid(rowspan=7, columnspan=2)
            
            def b(self):
                self.amps = 0
                if (getLoadgroup(self)==load_groupsc2[2]): #load group lighting
                    if (getGroup(self)==groupc2_options[0]):
                        if(getOutlet(self) ==1):
                            self.amps = 1000
                            b2Value = self.amps
                            return str(self.amps)
                        if(getOutlet(self) > 1 ):
                            self.amps = getOutlet(self) - 1
                            self.amps = self.amps * 400
                            self.amps = self.amps + 1000
                            b2Value = self.amps
                            return str(self.amps)
                    if (getGroup(self)==groupc2_options[1]):
                        if(getOutlet(self) == 1):
                            self.amps = 1000
                            b2Value = self.amps
                            return str(self.amps)
                        if(getOutlet(self) > 1 ):
                            self.amps = getOutlet(self) - 1
                            self.amps = self.amps * 750
                            self.amps = self.amps + 1000
                            b2Value = self.amps
                            return str(self.amps)
                else:
                    return 'c2b'

            if (b(self)!='c2b'):                     
                self.c2socket_result = Label (self.c2tab1, text = ""+b(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.c2socket_result.grid(row=1, column=1)
                self.c2amps = Label (self.c2tab, text = b(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.c2amps.grid(rowspan=7, columnspan=2)
            
            def c(self):
                self.amps = 0
                if (getLoadgroup(self)==load_groupsc2[3]):
                    if (getGroup(self)==groupc2_options[0] or groupc2_options[1]): #load group lighting
                        if (getOutlet(self) == 1):
                            self.amps = 1000
                            c2Value = self.amps
                            return str(self.amps)
                        if(getOutlet(self)>=2 ):
                            self.amps = getOutlet(self) - 1
                            self.amps = self.amps * 100 + 1000
                            c2Value = self.amps
                            return str(self.amps)
                else:
                    return 'c2c'
            if (c(self)!='c2c'):                     
                self.c2bii_result = Label (self.c2tab1, text = ""+c(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.c2bii_result.grid(row=1, column=1)
                self.c2biiamps = Label (self.c2tab, text = c(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.c2biiamps.grid(rowspan=7, columnspan=2)

            # def d(self):
            #     self.amps = 0
            #     if (getLoadgroup(self)==load_groupsc2[4]):
            #         if (getGroup(self)==groupc2_options[0] or groupc2_options[1]): #load group lighting
            #             if (getOutlet(self) == 1):
            #                 self.amps = 1000
            #                 c2Value = self.amps
            #                 return str(self.amps)
            #             if(getOutlet(self)>=2 ):
            #                 self.amps = getOutlet(self) - 1
            #                 self.amps = self.amps * 100 + 1000
            #                 c2Value = self.amps
            #                 return str(self.amps)
            #     else:
            #         return 'c2d'
            # if (d(self)!='c2d'):                     
            #     self.c2biii_result = Label (self.c2tab1, text = ""+d(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
            #     self.c2biii_result.grid(row=1, column=1)
            #     self.c2biiiamps = Label (self.c2tab, text = d(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
            #     self.c2biiiamps.grid(rowspan=7, columnspan=2)

            



                        
        self.c2add = Button(self.c2tab, text="Add", bg="light grey", command=calculationsc2) #ADD BUTTON
        self.c2add.grid(row = 6,column=1)   



                


    def c3_redirect(self):
        control = Toplevel()
        control.geometry("450x375")
        control.title("TABLE C3")

        nb = ttk.Notebook(control)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.c3tab = ttk.Frame(nb) #tab 1 creation
        nb.add(self.c3tab, text='Energy Demand')       
        self.c3tab1 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.c3tab1, text='Results')

        self.living_unitsc3 = Label (self.c3tab, text = "test", height=1, width=20, font='Helvetica 12 bold') #Label
        self.living_unitsc3.grid(rowspan=1, columnspan=2)

        self.lbl_loadc3= Label (self.c3tab, text = "Type of Load", height=1, width=20) #Label
        self.lbl_loadc3.grid(row=2, column = 0)

        # self.cntrl_loadgroupc3 = StringVar(control)
        # self.cntrl_loadgroupc3.set("-") # default value
        # self.om_loadgroupc3 = OptionMenu(self.c3tab, self.cntrl_loadgroupc3, *load_groupsc3)
        # self.om_loadgroupc3.config(width=35)
        # self.om_loadgroupc3.grid(row=2, column=1)

        self.lbl_wattsc3 = Label (self.c3tab, text = "Watts", height=1, width=20) #Label
        self.lbl_wattsc3.grid(row=3, column = 0)

        self.entry_wattsc3 = StringVar()  
        self.entry_wattsc3 = Entry (self.c3tab) ######## ENTRY BOX
        self.entry_wattsc3.grid(row=3, column=1)

        self.lbl_outletc3 = Label (self.c3tab, text = "Number of Outlets: ", height=1, width=20) #Label
        self.lbl_outletc3.grid(row=4, column = 0)

        self.entry_outletc3 = StringVar()  
        self.entry_outletc3 = Entry (self.c3tab) ######## ENTRY BOX
        self.entry_outletc3.grid(row=4, column=1)




    
    def update ():
        total_sum = self.aValue + self.bValue + self.cValue + self.dValue + self.eValue + self.fValue 

        self.total.config(text = total_sum,bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)

    def xlsx_test():
        workbook = xlsxwriter.Workbook('please-work.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.set_column('A:A', 20)

        worksheet.write('A1', 'Number of Units')
        worksheet.write('B1', int(self.entry_unit.get()))

        worksheet.write('A2', 'Load Group')
        worksheet.write('B2', 'Watts')
        worksheet.write('C2', 'Points')
        worksheet.write('D2', 'Amperes')

        worksheet.write('A3', 'Lighting (a)')
        worksheet.write('B3', int(self.light_watts))
        worksheet.write('C3', int(self.light_points))
        worksheet.write('D3', int(self.aValue))

        worksheet.write('A4', 'Outlets (b)')
        worksheet.write('B4', int(self.outlets_watts))
        worksheet.write('C4', int(self.outlets_points))
        worksheet.write('D4', int(self.bValue))

        worksheet.write('A5', 'Appliances (c)')
        worksheet.write('B5', int(self.general_watts))
        worksheet.write('C5', int(self.general_points))
        worksheet.write('D5', int(self.cValue))

        worksheet.write('A6', 'Heating/Cooling (d)')
        worksheet.write('B6', int(self.general_watts))
        worksheet.write('C6', int(self.general_points))
        worksheet.write('D6', int(self.dValue))

        worksheet.write('A7', 'Heating/Cooling (e)')
        worksheet.write('B7', int(self.general_watts))
        worksheet.write('C7', int(self.general_points))
        worksheet.write('D7', int(self.eValue))

        worksheet.write('A8', 'Heating/Cooling (f)')
        worksheet.write('B8', int(self.general_watts))
        worksheet.write('C8', int(self.general_points))
        worksheet.write('D8', int(self.fValue))

        worksheet.write('A9', 'Heating/Cooling (g)')
        worksheet.write('B9', int(self.general_watts))
        worksheet.write('C9', int(self.general_points))
        worksheet.write('D9', int(self.gValue))

        worksheet.write('A10', 'Heating/Cooling (f)')
        worksheet.write('B10', int(self.general_watts))
        worksheet.write('C10', int(self.general_points))
        worksheet.write('D10', int(self.fValue))

        


        workbook.close()


        #ADD BUTTONS#

        self.add_load = Button(self.tab1, text="Add", bg="light grey", command=calculations) #ADD BUTTON
        self.add_load.grid(row = 6,column=1) 

        self.btn_calculations = Button (self.tab5, text="Update", height=1, width=20, command=update)
        self.btn_calculations.grid (row=15,column=1)

        self.btn_calculations = Button (self.tab5, text="Write to excel", command=xlsx_test, height=1, width=20)
        self.btn_calculations.grid (row=15, column=0)
        #ADD BUTTONS#


        
        

        #TOOLBARS#  
        def doNothing():
            print("yes boss")
        


        
        menu = Menu(control)
        control.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label='New', command=doNothing)
        subMenu.add_separator()
        subMenu.add_command(label='Exit', command=doNothing)

        editMenu = Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Redo', command=doNothing)
      




master = Tk()
master.title("Home")
master.geometry("500x350")
app = Application(master)

master.mainloop()