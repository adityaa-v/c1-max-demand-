from tkinter import *
from tkinter import ttk

load_groups = ['Appliances (c)', 'Heating/Cooling (d)', 'Instant Water Heaters (e)', 'Storage Water Heaters (f)',
'Spa and swimming pool heaters (g)', 'Communal lighting (h)','Socket (i)', 'Lifts (k)',
'Motors (l)', 'Other Appliances (m)']
sub_lighitng = ["lighting except for communial lighting and <1000W ", 
"Outdoor lighting exceeding a total of 1000 W"]
sub_outlets = ["Socket outlets not exceeding 10 A", 
"One or more 15 A socket outlets",
"One or more 20 A socket outlets"]
sub_appliances = ['Clothes dryers, water heaters, self-heating washing machines, wash boilers', 'Fixed space heating, airconditioning equipment, saunas',
'Spa and swimming pool heaters', 'Charging equipment associated with electric vehicles']
result_list = []

class Application(Frame):
    aValue = bvalue = 0
    bValue = 0
    cValue = 0
    dValue = 0
    eValue = 0
    fValue = 0
    gValue = 0
    hValue = 0
    iValue = 0
    jValue = 0

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.init_window()

    def init_window(self): 

        self.init = Label (master, text="Please enter the number of electrical installations", height=2, width=40)
        self.init.grid(row=1)
        
        self.entry_unit = IntVar()  
        self.entry_unit = Entry (master)
        self.entry_unit.grid(row=2)  

        self.unit_btn = Button(master, text="Calculate", bg="light grey", command=self.unit_redirect)
        self.unit_btn.grid(row = 4)      

    def unit_redirect(self):
        control = Toplevel()
        control.geometry("450x375")
        
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

        #TAB 2 LIGHTING

        self.tab2_living_units = Label (self.tab2, text = self.entry_unit.get(), height=1, width=20, font='Helvetica 12 bold') #Label
        self.tab2_living_units.grid(row=1, columnspan=2)
      
        self.tab2_lbl_options = Label (self.tab2, text = "Options: ", height = 1, width=20)
        self.tab2_lbl_options.grid(row=2, column=0)

        self.cntrl_lighting = StringVar(control) #LIGHTING DROP DOWN BOX
        self.cntrl_lighting.set("-") # default value
        self.om_lighting = OptionMenu(self.tab2, self.cntrl_lighting, *sub_lighitng, )
        self.om_lighting.config(width=35)
        self.om_lighting.grid(row=2, column=1)

        self.tab2_lbl_points = Label (self.tab2, text = "Points", height=1, width=20) #Label
        self.tab2_lbl_points.grid(row=4, column = 0)

        self.tab2_lbl_watts = Label (self.tab2, text = "Watts", height=1, width=20) #Label
        self.tab2_lbl_watts.grid(row=5, column = 0)

        self.tab2_entry_watts = StringVar()  
        self.tab2_entry_watts = Entry (self.tab2) ######## ENTRY BOX
        self.tab2_entry_watts.grid(row=5, column=1)
        
        self.tab2_entry_points = StringVar()  
        self.tab2_entry_points = Entry (self.tab2) ######## ENTRY BOX
        self.tab2_entry_points.grid(row=4, column=1)

        #TAB 3 SOCKET

        self.tab3_living_units = Label (self.tab3, text = self.entry_unit.get(), height=1, width=20, font='Helvetica 12 bold') #Label
        self.tab3_living_units.grid(row=1, columnspan=2)
      
        self.tab3_lbl_options = Label (self.tab3, text = "Options: ", height = 1, width=20)
        self.tab3_lbl_options.grid(row=2, column=0)

        self.cntrl_socket = StringVar(control) #LIGHTING DROP DOWN BOX
        self.cntrl_socket.set("-") # default value
        self.om_socket = OptionMenu(self.tab3, self.cntrl_socket, *sub_outlets)
        self.om_socket.config(width=35)
        self.om_socket.grid(row=2, column=1)

        self.tab3_lbl_points = Label (self.tab3, text = "Points", height=1, width=20) #Label
        self.tab3_lbl_points.grid(row=4, column = 0)

        self.tab3_lbl_watts = Label (self.tab3, text = "Watts", height=1, width=20) #Label
        self.tab3_lbl_watts.grid(row=5, column = 0)

        self.tab3_entry_watts = StringVar()  
        self.tab3_entry_watts = Entry (self.tab3) ######## ENTRY BOX
        self.tab3_entry_watts.grid(row=5, column=1)
        
        self.tab3_entry_points = StringVar()  
        self.tab3_entry_points = Entry (self.tab3) ######## ENTRY BOX
        self.tab3_entry_points.grid(row=4, column=1)

        #TAB 4 APPLIANCES

        self.tab4_living_units = Label (self.tab4, text = self.entry_unit.get(), height=1, width=20, font='Helvetica 12 bold') #Label
        self.tab4_living_units.grid(row=1, columnspan=2)
      
        self.tab4_lbl_options = Label (self.tab4, text = "Options: ", height = 1, width=20)
        self.tab4_lbl_options.grid(row=2, column=0)

        self.cntrl_appliance = StringVar(control) #LIGHTING DROP DOWN BOX
        self.cntrl_appliance.set("-") # default value
        self.om_appliance = OptionMenu(self.tab4, self.cntrl_appliance, *sub_appliances)
        self.om_appliance.config(width=35)
        self.om_appliance.grid(row=2, column=1)

        self.tab4_lbl_points = Label (self.tab4, text = "Points", height=1, width=20) #Label
        self.tab4_lbl_points.grid(row=4, column = 0)

        self.tab4_lbl_watts = Label (self.tab4, text = "Watts", height=1, width=20) #Label
        self.tab4_lbl_watts.grid(row=5, column = 0)

        self.tab4_entry_watts = StringVar()  
        self.tab4_entry_watts = Entry (self.tab4) ######## ENTRY BOX
        self.tab4_entry_watts.grid(row=5, column=1)
        
        self.tab4_entry_points = StringVar()  
        self.tab4_entry_points = Entry (self.tab4) ######## ENTRY BOX
        self.tab4_entry_points.grid(row=4, column=1)

        
        #RESULTS#
        self.lbl_resulta = Label (self.tab5, text = "Lighting (a): ", height = 1, width=20)
        self.lbl_resulta.grid(row=1, column=0)
        self.result_a = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_a.grid(row=1, column=1)
        self.lbl_resultb = Label (self.tab5, text = "Outlets (b): ", height = 1, width=20)
        self.lbl_resultb.grid(row=2, column=0)
        self.result_b = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_b.grid(row=2, column=1)
        self.lbl_resultc = Label (self.tab5, text = "Appliances (c): ", height = 1, width=20)
        self.lbl_resultc.grid(row=3, column=0)
        self.result_c = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_c.grid(row=3, column=1)
        self.lbl_resultd = Label (self.tab5, text = "Heating/Cooling (d): ", height = 1, width=20)
        self.lbl_resultd.grid(row=4, column=0)
        self.result_d = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_d.grid(row=4, column=1)
        self.lbl_resulte = Label (self.tab5, text = "Instant Water Heaters (e): ", height = 1, width=20)
        self.lbl_resulte.grid(row=5, column=0)
        self.result_e = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_e.grid(row=5, column=1)
        self.lbl_resultf = Label (self.tab5, text = "Storage Water Heaters (f): ", height = 1, width=20)
        self.lbl_resultf.grid(row=6, column=0)
        self.result_f = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_f.grid(row=6, column=1)
        self.lbl_resultg = Label (self.tab5, text = "Spa and swimming pool heaters (g): ", height = 1, width=20)
        self.lbl_resultg.grid(row=7, column=0)
        self.result_g = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_g.grid(row=7, column=1)
        self.lbl_resulth = Label (self.tab5, text = "Communal lighting (h): ", height = 1, width=20)
        self.lbl_resulth.grid(row=8, column=0)
        self.result_h = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_h.grid(row=8, column=1)
        self.lbl_resulti = Label (self.tab5, text = "Socket (i): ", height = 1, width=20)
        self.lbl_resulti.grid(row=9, column=0)
        self.result_i = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_i.grid(row=9, column=1)
        self.lbl_resultj = Label (self.tab5, text = "Appliances (j): ", height = 1, width=20)
        self.lbl_resultj.grid(row=10, column=0)
        self.result_j = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_j.grid(row=10, column=1)
        self.lbl_resultk = Label (self.tab5, text = "Lifts (k): ", height = 1, width=20)
        self.lbl_resultk.grid(row=11, column=0)
        self.result_k = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_k.grid(row=11, column=1)
        self.lbl_resultl = Label (self.tab5, text = "Motors (l): ", height = 1, width=20)
        self.lbl_resultl.grid(row=12, column=0)
        self.result_l = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_l.grid(row=12, column=1)
        self.lbl_resultm = Label (self.tab5, text = "Other Appliances (m): ", height = 1, width=20)
        self.lbl_resultm.grid(row=13, column=0)
        self.result_m = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.result_m.grid(row=13, column=1)
        self.total = Label (self.tab5, text = "Total", height = 1, width=20)
        self.total.grid(row=14, column=0)
        self.total = Label (self.tab5, text = "yeet", height = 1, width=20)
        self.total.grid(row=14, column=1)
        self.btn_calculations = Button (self.tab5, text="View Calculations", height=1, width=20)
        self.btn_calculations.grid (row=15, column=0)
        

###### LIGHTING BEGIN

        def calculationsAll(): #LIGHTING
    
            def getUnit(self): #get values
                self.x = int(self.entry_unit.get())
                return self.x
            def getLoadgroup(self):
                self.x = self.cntrl_lighting.get()
                return self.x
            def getPoints(self):
                self.x = int(self.tab2_entry_points.get())
                return self.x
            def getWatts(self):
                self.x = int(self.tab2_entry_watts.get())
                return self.x  
                     
            def lighting(self):
                self.amps = 0
                
                if (getLoadgroup(self)==sub_lighitng[0]):
                    if (getUnit(self)==1):

                        if (getPoints(self)<=20):
                                self.amps = self.amps + 3
                                self.aValue = self.amps
                                return str(self.amps)

                        if (getPoints(self)>=40):
                            self.amps = self.amps + 5
                            self.aValue = self.amps
                            return str(self.amps)
                            if (getPoints(self)>=60):
                                self.amps = self.amps + 2
                                self.aValue = self.amps
                                return str(self.amps)
                                if (getPoints(self)>=80):
                                    self.amps = self.amps + 2
                                    self.aValue = self.amps
                                    return str(self.amps)
                                    if (getPoints(self)>=100):
                                        self.amps = self.amps + 2
                                        self.aValue = self.amps
                                        return str(self.amps)
                        
                    if (getUnit(self)>=2 and getUnit(self)<=5):#2-5

                        self.aValue = 6
                        return '6'                    
                    
                    if (getUnit(self)>=6 and getUnit(self)<=20):#6-20

                        self.excess = getUnit(self) - 6
                        self.amps = (self.excess * 0.25) + 5     
                        self.aValue = self.amps
                        return str(self.amps)  

                    if (getUnit(self)>=21):#21+
                        self.excess = getUnit(self) - 21
                        self.amps = (self.excess * 0.25)   
                        self.aValue = self.amps         
                        return str(self.amps)  
                             
                if (getLoadgroup(self)==sub_lighitng[1]):
                    if(getUnit(self)==1):
                        self.amps = getWatts(self) * 0.75
                        self.aValue = self.amps
                        return str(self.amps)

                else:
                    return 'yeet'
                      
            self.light_result = Label (self.tab5, text = ""+lighting(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
            self.light_result.grid(row=1, column=1)

            self.amps = Label (self.tab2, text = lighting(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
            self.amps.grid(rowspan=7, columnspan=2)

###### LIGHTING END

###### socket BEGIN

        def calculationsB():
    
            def getUnit(self): #get values
                self.x = int(self.entry_unit.get())
                return self.x
            def getLoadgroup(self):
                self.x = self.cntrl_socket.get()
                return self.x
            def getPoints(self):
                self.x = int(self.tab3_entry_points.get())
                return self.x
            def getWatts(self):
                self.x = int(self.tab3_entry_watts.get())
                return self.x  
                     
            def sockets(self):
                self.amps = 0


                if (getLoadgroup(self)==sub_outlets[0]):

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
                             
                if (getLoadgroup(self)==sub_outlets[1]):
                    self.bValue = 10
                    return "10"
                if (getLoadgroup(self)==sub_outlets[2]):
                    self.bValue = 15
                    return "15"
                
            

                else:
                    return 'yeet'
            if (sockets(self)!='yeet'):          
                self.light_result = Label (self.tab5, text = ""+sockets(self), bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)
                self.light_result.grid(row=2, column=1)
                
                
                self.amps = Label (self.tab3, text = sockets(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

###### socket END

######appliance begin
 
        def calculationsJ():
        
            def getUnit(self): #get values
                self.x = int(self.entry_unit.get())
                return self.x
            def getLoadgroup(self):
                self.x = self.cntrl_appliance.get()
                return self.x
            def getPoints(self):
                self.x = int(self.tab4_entry_points.get())
                return self.x
            def getWatts(self):
                self.x = int(self.tab4_entry_watts.get())
                return self.x  
                     
            def appliances(self):
                self.amps = 0
                self.aValuejValue = 0
                             
                if (getLoadgroup(self)==sub_appliances[0] or getLoadgroup(self)==sub_appliances[1] or getLoadgroup(self)==sub_appliances[2]):
                    if (getUnit(self) == 1):
                        return "Not applicable"

                if (getLoadgroup(self)==sub_appliances[3]):
                    if (getUnit(self) == 1):
                        return "Fully connected load"

                if (getLoadgroup(self) ==sub_appliances[0]):
                    if getUnit(self)>=2:
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.5
                        self.jValue = self.amps
                        return str(self.amps)
                
                if (getLoadgroup(self) ==sub_appliances[1]):
                    if getUnit(self)>=2:
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        self.jValue = self.amps
                        return str(self.amps)
                
                if (getLoadgroup(self) == sub_appliances[3]):

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

###### LIGHTING END

###### OTHERS BEGIN 

        def calculations():

            def getUnit(self): #get values
                self.x = int(self.entry_unit.get())                   
                return self.x
            def getLoadgroup(self):
                self.x = self.cntrl_loadgroup.get()
                return self.x
            def getPoints(self):
                self.x = int(self.entry_points.get())
                return self.x
            def getWatts(self):
                self.x = int(self.entry_watts.get())
                return self.x  
                     
            def c(self): #WORKS
                self.amps = 0
                self.cValue = 0

                if (getLoadgroup(self)==load_groups[0]):

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

                if (getLoadgroup(self)==load_groups[1]):

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
                if (getLoadgroup(self)==load_groups[2]):
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

                if (getLoadgroup(self)==load_groups[3]):

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

                if (getLoadgroup(self)==load_groups[4]):
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
                if (getLoadgroup(self)==load_groups[5]):
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
                if (getLoadgroup(self)==load_groups[6]):
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

            def k (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[7]):
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
###### OTHERS END
                
                
        def update ():
            total_sum = self.aValue + self.bValue + self.cValue + self.dValue + self.eValue + self.fValue 

            self.total.config(text = total_sum,bg='green2', borderwidth="2", relief="sunken", height = 1, width=20)


        #ADD BUTTONS#
        self.add_socket = Button(self.tab4, text="Add", bg="light grey", command=calculationsJ) #ADD BUTTON
        self.add_socket.grid(row = 6,column=1)  

        self.add_socket = Button(self.tab3, text="Add", bg="light grey", command=calculationsB) #ADD BUTTON
        self.add_socket.grid(row = 6,column=1)  

        self.add_lighting = Button(self.tab2, text="Add", bg="light grey", command=calculationsAll) #ADD BUTTON
        self.add_lighting.grid(row = 6,column=1)        

        self.add_load = Button(self.tab1, text="Add", bg="light grey", command=calculations) #ADD BUTTON
        self.add_load.grid(row = 6,column=1)  

        self.btn_calculations = Button (self.tab5, text="Update", height=1, width=20, command=update)
        self.btn_calculations.grid (row=15,column=1)
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
master.title("")
master.geometry("300x100")
app = Application(master)

master.mainloop()