from tkinter import *
from tkinter import ttk

load_groups = ['Appliances (c)', 'Heating/Cooling (d)', 'Instant Water Heaters (e)', 'Storage Water Heaters (f)',
'Spa and swimming pool heaters (g)', 'Communal lighting (h)','Socket (i)', 'Lifts (k)',
'Motors (l)', 'Other Appliances (m)']
sub_lighitng = ["lighting except for communial lighting and <1000W ", 
" Outdoor lighting exceeding a total of 1000 W"]
sub_outlets = ["Socket outlets not exceeding 10 A", 
" Outdoor lighting exceeding a total of 1000 W"]
result_list = []

class Application(Frame):

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
      
        self.tab2_lbl_options = Label (self.tab2, text = "Options: ", height = 1, width=20)
        self.tab2_lbl_options.grid(row=1, column=0)

        self.cntrl_lighting = StringVar(control) #LIGHTING DROP DOWN BOX
        self.cntrl_lighting.set("-") # default value
        self.om_lighting = OptionMenu(self.tab2, self.cntrl_lighting, *sub_lighitng, )
        self.om_lighting.config(width=35)
        self.om_lighting.grid(row=1, column=1)

        self.tab2_lbl_points = Label (self.tab2, text = "Points", height=1, width=20) #Label
        self.tab2_lbl_points.grid(row=4, column = 0)
        
        self.tab2_entry_points = StringVar()  
        self.tab2_entry_points = Entry (self.tab2) ######## ENTRY BOX
        self.tab2_entry_points.grid(row=4, column=1)

        self.tab2_lbl_watts = Label (self.tab2, text = "Watts", height=1, width=20) #Label
        self.tab2_lbl_watts.grid(row=5, column = 0)

        self.tab2_entry_watts = StringVar()  
        self.tab2_entry_watts = Entry (self.tab2) ######## ENTRY BOX
        self.tab2_entry_watts.grid(row=5, column=1)

        
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
        self.btn_calculations = Button (self.tab5, text="Update", height=1, width=20)
        self.btn_calculations.grid (row=15,column=1)

        # def sub_menu():
        #     subcontrol = Toplevel()
        #     subcontrol.geometry("300x250")

        #     self.lbl_subLight = Label (subcontrol, text = "Lighting (a)", height = 1, width=20)
        #     self.lbl_subLight.grid(row=0, column=0)

        #     self.cntrl_loadgroup = StringVar(control)
        #     self.cntrl_loadgroup.set("-") # default value
        #     self.om_loadgroup = OptionMenu(subcontrol, self.cntrl_loadgroup, *sub_lighitng)
        #     self.om_loadgroup.config(width=25)
        #     self.om_loadgroup.grid(row=0, column=1)
                
        # self.add_sub = Button (self.tab1, text = "Sub Option", height=1, width=20, command=sub_menu) #Label
        # self.add_sub.grid(row=3, column = 1)
        
        def calculations(): ## SPECIFICALLY FOR LOAD GROUP

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
                                   
            def c (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[2]):
                    if (getUnit(self)==1):
                        self.amps= getWatts(self) * 0.5
                        return str(self.amps)
                    if (getPoints(self)>=2 and getPoints(self)<=5):
                        self.amps = 15
                        return str(self.amps)
                    if (getPoints(self)>= 6 and getPoints(self)<=20):
                        self.amps = 2.8 * getUnit(self)
                        return str(self.amps)
                    if(getPoints(self)>=21):
                        self.amps = 2.8 * getUnit(self)
                        return str(self.amps)
                
            def d (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[3]):
                    if (getUnit(self)==1):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        return str(self.amps)
                    if (getPoints(self)>=2 and getPoints(self)<=5):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        return str(self.amps)
                    if (getPoints(self)>= 6 and getPoints(self)<=20):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        return str(self.amps)
                    if(getPoints(self)>=21):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.75
                        return str(self.amps)
            def e (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[4]):
                    if (getUnit(self)==1):
                        self.amps = getWatts(self)                       
                        self.amps= self.amps * 0.333
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            self.amps = 6 * getUnit(self)
                            return str(self.amps)
                            if (getPoints(self)>= 6 and getPoints(self)<=20):
                                self.amps = 6 * getUnit(self)                                
                                return str(self.amps)
                                if(getPoints(self)>=21):
                                    self.amps = (getUnit(self) * 0.8) + 100
                                    return str(self.amps)
            def f (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[5]):
                    if (getUnit(self)==1):
                        return "full load connected"
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            self.amps = 6 * getUnit(self)
                            return str(self.amps)
                            if (getPoints(self)>= 6 and getPoints(self)<=20):
                                self.amps = 6 * getUnit(self)
                                return str(self.amps)
                                if(getPoints(self)>=21):
                                    self.amps = (getUnit(self) * 0.8) + 100
                                    return str(self.amps)
            def g (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[6]):
                    if (getUnit(self)==1):
                        
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            return str(self.amps)
                            if (getPoints(self)>= 6 and getPoints(self)<=20):
                                return str(self.amps)
                                if(getPoints(self)>=21):
                                    return str(self.amps)
            def h (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[7]):
                    if (getUnit(self)==1):
                        return "N/A"
                        return str(self.amps)
                        if (getPoints(self)>=2):
                            return "full connected laod"
            def i (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[8]):
                    if (getUnit(self)==1):
                        return "N/A"
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            self.amps = getUnit(self) * 2
                            if self.amps >=15:
                                return "Value exceeded"
                            else:
                                return str(self.amps)

            def k (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[9]):
                    if (getUnit(self)==1):
                        
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            return str(self.amps)
                            if (getPoints(self)>= 6 and getPoints(self)<=20):
                                return str(self.amps)
                                if(getPoints(self)>=21):
                                    return str(self.amps)
            def l (self):
                self.amps = 0
                if (getLoadgroup(self)==load_groups[10]):
                    if (getUnit(self)==1):
                        
                        return str(self.amps)
                        if (getPoints(self)>=2 and getPoints(self)<=5):
                            return str(self.amps)
                            if (getPoints(self)>= 6 and getPoints(self)<=20):
                                return str(self.amps)
                                if(getPoints(self)>=21):
                                    return str(self.amps)    
            
            
            if getLoadgroup(self)==load_groups[0]:            
                self.appli_result = Label (self.tab5, text = c(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=3, column=1)

                self.amps = Label (self.tab1, text = int(c(self)) + " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[1]:            
                self.appli_result = Label (self.tab5, text = d(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=4, column=1)

                self.amps = Label (self.tab1, text =d(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[2]:            
                self.appli_result = Label (self.tab5, text = d(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=5, column=1)

                self.amps = Label (self.tab1, text =d(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[3]:            
                self.appli_result = Label (self.tab5, text = e(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=6, column=1)

                self.amps = Label (self.tab1, text =e(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[4]:            
                self.appli_result = Label (self.tab5, text = f(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=7, column=1)

                self.amps = Label (self.tab1, text =f(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[5]:            
                self.appli_result = Label (self.tab5, text = g(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=8, column=1)

                self.amps = Label (self.tab1, text =g(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)

            if getLoadgroup(self)==load_groups[6]:      

                self.appli_result = Label (self.tab5, text = h(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=9, column=1)

                self.amps = Label (self.tab1, text =h(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)
            if getLoadgroup(self)==load_groups[7]:            
                self.appli_result = Label (self.tab5, text = i(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
                self.appli_result.grid(row=10, column=1)

                self.amps = Label (self.tab1, text = i(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)
            
            else :
                self.amps = Label (self.tab1, text = "false son", height=1) #Label
                self.amps.grid(rowspan=7, columnspan=2)
            
                    
        def lighting():

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

            if (getLoadgroup(self)=="lighting except for communial lighting and <1000W "):
    
                if (getUnit(self)==1):
                    self.amps = 0

                    if (getPoints(self)<=20):
                        self.amps = self.amps + 3
                        return str(self.amps)

                    if (getPoints(self)>=40):
                        self.amps = self.amps + 5
                        if (getPoints(self)>=60):
                            self.amps = self.amps + 2
                            if (getPoints(self)>=80):
                                self.amps = self.amps + 2
                                if (getPoints(self)>=100):
                                    self.amps = self.amps + 2
                        return str(self.amps)

                    else:
                        return "ooga booga"
                    
                if (getUnit(self)>=2 and getUnit(self)<=5):#2-5

                    result_list.append(6)
                    return '6'                    
                
                if (getUnit(self)>=6 and getUnit(self)<=20):#6-20

                    self.excess = getUnit(self) - 6
                    self.amps = (self.excess * 0.25) + 5     
                    result_list.append(self.amps)                  
                    return str(self.amps)  

                if (getUnit(self)>=21):#21+
                    self.excess = getUnit(self) - 21
                    self.amps21 = (self.excess * 0.25)            
                    result_list.append(self.amps21)                  
                    return str(self.amps21)  


            self.appli_result = Label (self.tab5, text = lighting(), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
            self.appli_result.grid(row=1, column=1)
            
            self.amps = Label (self.tab2, text = lighting () + "A is required for" + lighting(), height=1)
            self.amps.grid(row=8, columnspan=2)

        # self.light_result = Label (self.tab5, text = ""+lighting(), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
        # self.light_result.grid(row=1, column=1)
        
        self.add_load = Button(self.tab1, text="Add", bg="light grey", command=calculations) #ADD BUTTON
        self.add_load.grid(row = 6,column=1)
        
        self.add_lighting = Button(self.tab2, text="Add", bg="light grey", command=lighting) #ADD BUTTON
        self.add_lighting.grid(row = 6,column=1)
        #RESULTS    
       
        menu = Menu(control)
        control.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label='New')
        subMenu.add_separator()
        subMenu.add_command(label='Exit')

        editMenu = Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Redo')

        

master = Tk()
master.title("TABLE C1")
master.geometry("300x100")
app = Application(master)

master.mainloop()