from tkinter import *
from tkinter import ttk

load_groups = ["Lighting (a)", 'Outlets (b)', 'Appliances (c)', 'Heating/Cooling (d)', 'Instant Water Heaters (e)', 'Storage Water Heaters (f)',
'Spa and swimming pool heaters (g)', 'Communal lighting (h)','Socket (i)', 'Appliances (j)', 'Lifts (k)',
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
        control.geometry("600x375")
        
        nb = ttk.Notebook(control)
        nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.tab1 = ttk.Frame(nb) #tab 1 creation
        nb.add(self.tab1, text='Load Groups')       
        self.tab2 = ttk.Frame(nb) #tab 2 creation
        nb.add(self.tab2, text='Results')

        self.living_units = Label (self.tab1, text = self.entry_unit.get(), height=1, width=20, font='Helvetica 9 bold') #Label
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

        
        
        #RESULTS#
        self.lbl_resulta = Label (self.tab2, text = "Lighting (a): ", height = 1, width=20)
        self.lbl_resulta.grid(row=1, column=0)
        self.result_a = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_a.grid(row=1, column=1)
        self.lbl_resultb = Label (self.tab2, text = "Outlets (b): ", height = 1, width=20)
        self.lbl_resultb.grid(row=2, column=0)
        self.result_b = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_b.grid(row=2, column=1)
        self.lbl_resultc = Label (self.tab2, text = "Appliances (c): ", height = 1, width=20)
        self.lbl_resultc.grid(row=3, column=0)
        self.result_c = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_c.grid(row=3, column=1)
        self.lbl_resultd = Label (self.tab2, text = "Heating/Cooling (d): ", height = 1, width=20)
        self.lbl_resultd.grid(row=4, column=0)
        self.result_d = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_d.grid(row=4, column=1)
        self.lbl_resulte = Label (self.tab2, text = "Instant Water Heaters (e): ", height = 1, width=20)
        self.lbl_resulte.grid(row=5, column=0)
        self.result_e = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_e.grid(row=5, column=1)
        self.lbl_resultf = Label (self.tab2, text = "Storage Water Heaters (f): ", height = 1, width=20)
        self.lbl_resultf.grid(row=6, column=0)
        self.result_f = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_f.grid(row=6, column=1)
        self.lbl_resultg = Label (self.tab2, text = "Spa and swimming pool heaters (g): ", height = 1, width=20)
        self.lbl_resultg.grid(row=7, column=0)
        self.result_g = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_g.grid(row=7, column=1)
        self.lbl_resulth = Label (self.tab2, text = "Communal lighting (h): ", height = 1, width=20)
        self.lbl_resulth.grid(row=8, column=0)
        self.result_h = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_h.grid(row=8, column=1)
        self.lbl_resulti = Label (self.tab2, text = "Socket (i): ", height = 1, width=20)
        self.lbl_resulti.grid(row=9, column=0)
        self.result_i = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_i.grid(row=9, column=1)
        self.lbl_resultj = Label (self.tab2, text = "Appliances (j): ", height = 1, width=20)
        self.lbl_resultj.grid(row=10, column=0)
        self.result_j = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_j.grid(row=10, column=1)
        self.lbl_resultk = Label (self.tab2, text = "Lifts (k): ", height = 1, width=20)
        self.lbl_resultk.grid(row=11, column=0)
        self.result_k = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_k.grid(row=11, column=1)
        self.lbl_resultl = Label (self.tab2, text = "Motors (l): ", height = 1, width=20)
        self.lbl_resultl.grid(row=12, column=0)
        self.result_l = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_l.grid(row=12, column=1)
        self.lbl_resultm = Label (self.tab2, text = "Other Appliances (m): ", height = 1, width=20)
        self.lbl_resultm.grid(row=13, column=0)
        self.result_m = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.result_m.grid(row=13, column=1)
        self.total = Label (self.tab2, text = "Other Appliances (m): ", height = 1, width=20)
        self.total.grid(row=14, column=0)
        self.total = Label (self.tab2, text = "yeet", height = 1, width=20)
        self.total.grid(row=14, column=1)
        self.btn_calculations = Button (self.tab2, text="View Calculations", height=1, width=20)
        self.btn_calculations.grid (row=15, column=0)
        self.btn_calculations = Button (self.tab2, text="Update", height=1, width=20)
        self.btn_calculations.grid (row=15,column=1)

        def sub_menu():
            subcontrol = Toplevel()
            subcontrol.geometry("300x250")

            self.lbl_subLight = Label (subcontrol, text = "Lighting (a)", height = 1, width=20)
            self.lbl_subLight.grid(row=0, column=0)

            self.cntrl_loadgroup = StringVar(control)
            self.cntrl_loadgroup.set("-") # default value
            self.om_loadgroup = OptionMenu(subcontrol, self.cntrl_loadgroup, *sub_lighitng)
            self.om_loadgroup.config(width=25)
            self.om_loadgroup.grid(row=0, column=1)
                
        self.add_sub = Button (self.tab1, text = "Sub Option", height=1, width=20, command=sub_menu) #Label
        self.add_sub.grid(row=3, column = 1)
        
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
                     
            def lighting(self):

                if (getLoadgroup(self)=="Lighting (a)"):

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

                else:
                    return 'hello boss'
                
            def appliances (self):
                if (getLoadgroup(self)=="Appliances (c)"):
    
                    if (getUnit(self)==1):
                        self.amps = 0
                        

            self.light_result = Label (self.tab2, text = ""+lighting(self), bg='firebrick1', borderwidth="2", relief="sunken", height = 1, width=20)
            self.light_result.grid(row=1, column=1)

            self.amps = Label (self.tab1, text = lighting(self)+ " A is required for "+ getLoadgroup(self), height=1) #Label
            self.amps.grid(rowspan=7, columnspan=2)
            
                    
            

        self.add_lighting = Button(self.tab1, text="Add", bg="light grey", command=calculations) #ADD BUTTON
        self.add_lighting.grid(row = 6,column=1)        
        
        #RESULTS    

        
            
        
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