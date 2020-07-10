import pandas as pd
import numpy as np
#from openpyxl.workbook import Workbook
import folium
from folium.plugins import MarkerCluster
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem, QProgressDialog
from PyQt5 import QtCore, QtGui, QtWidgets



        self.bt_Mapping.clicked.connect(self.mapping_bt)
        self.bt_fileread.clicked.connect(self.readfile_bt)
        self.bt_cleardata.clicked.connect(self.cleardata_bt)
        self.bt_applyfilter.clicked.connect(lambda:self.filteroptions(activ=True))
        self.bt_undofilter.clicked.connect(lambda:self.filteroptions(activ=False))
        self.bt_sort.clicked.connect(self.sort_bt)
        self.bt_savefiltered.clicked.connect(self.savefiltered_bt)
        self.markerexistance = False
        self.dataloaded      = False

    def savefiltered_bt(self):
        try:
            name=self.text_datasave_filename.text()
            self.df.reset_index(drop=True, inplace=True)
            if self.comboBox_datasave_format.currentText() == ".csv":
                name      = name + ".csv"
                seperator = self.text_datasave_seperator.text()
                if len(seperator)==1:

                    self.df.to_csv(name,index=True,sep=seperator)

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("seperator shoult have length=1")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
            elif self.comboBox_datasave_format.currentText() == ".xlsx":
                name      = name + ".xlsx"
                self.df.to_excel(name)

        except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            msg.setWindowTitle("WARNING")
            msg.exec_()

    def cleardata_bt(self):
        #clears data
        self.QComboBox_Longetude_val.clear()       # delete all items from comboBox
        self.QComboBox_Latetude_val.clear()       # delete all items from comboBox
        self.comboBox_filter_par1.clear()
        self.comboBox_filter_par2.clear()
        self.comboBox_filter_par3.clear()
        self.comboBox_filter_par4.clear()
        self.comboBox_filter_par5.clear()
        self.comboBox_filter_par6.clear()
        self.comboBox_filter_time1.clear()
        self.comboBox_filter_time2.clear()
        self.comboBox_tooltip_1.clear()
        self.comboBox_tooltip_2.clear()
        self.comboBox_tooltip_1.clear()
        self.comboBox_tooltip_2.clear()
        self.df=pd.DataFrame()
        self.tablefiller()
        self.markerexistance = False
        self.dataloaded      = False

    def tablefiller(self):
        #fills the TableWidget with current Data
        self.df.reset_index(drop=True, inplace=True)
        columnames=self.df.columns
        indexnames=self.df.index
        self.lcdNumber.display(len(indexnames))
        self.TableWidget.setColumnCount(len(columnames))
        if len(indexnames)>100:
            self.TableWidget.setRowCount(100)
            indexlaenge=100
        else:
            self.TableWidget.setRowCount(len(indexnames))
            indexlaenge=len(indexnames)
        horHeaders=[]
        for i in range(0,indexlaenge):
            for j in range(0,len(columnames)):
                horHeaders.append(columnames[j])
                a=(self.df.loc[indexnames[i]][columnames[j]])
                self.TableWidget.setItem(i,j,QTableWidgetItem(str(a)))
        self.TableWidget.setHorizontalHeaderLabels(horHeaders)

    def readfile_bt(self):
        try:
            path = self.text_filepath.text()
            raw_path = fr"{path}"
            self.DF = pd.read_csv(raw_path)
            self.textfilter=[]

            self.QComboBox_Longetude_val.clear()       # delete all items from comboBox
            self.QComboBox_Latetude_val.clear()       # delete all items from comboBox
            self.comboBox_filter_par1.clear()
            self.comboBox_filter_par2.clear()
            self.comboBox_filter_par3.clear()
            self.comboBox_filter_par4.clear()
            self.comboBox_filter_par5.clear()
            self.comboBox_filter_par6.clear()
            self.comboBox_filter_time1.clear()
            self.comboBox_filter_time2.clear()
            self.comboBox_tooltip_1.clear()
            self.comboBox_tooltip_2.clear()

            #befüllen der latitude/longitude Comboboxen
            for i in self.DF.axes[1]:
                if i == 'timestamp':
                    self.QComboBox_Timstamp.addItem('timestamp')
                    self.comboBox_tooltip_1.addItem("timestamp")
            for i in self.DF.axes[1]:
                self.QComboBox_Longetude_val.addItem(i)
                self.QComboBox_Latetude_val.addItem(i)
                self.comboBox_filter_par1.addItem(i)
                self.comboBox_filter_par2.addItem(i)
                self.comboBox_filter_par3.addItem(i)
                self.comboBox_filter_par4.addItem(i)
                self.comboBox_filter_par5.addItem(i)
                self.comboBox_filter_par6.addItem(i)
                self.comboBox_filter_time1.addItem(i)
                self.comboBox_filter_time2.addItem(i)
                self.comboBox_tooltip_2.addItem(i)
                if i == 'timestamp':
                    self.DF = self.DF.sort_values(by=['timestamp'])
                else:
                    self.QComboBox_Timstamp.addItem(i)
                    self.comboBox_tooltip_1.addItem(i)
            #set working frame
            self.DF.reset_index(drop=True, inplace=True)
            self.df = self.DF
            #check if no error ocured
            self.markerexistance = True
            self.dataloaded      = True
        except (IOError,NameError,FileNotFoundError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("WARNING")
            msg.setText("Unknown Error, (No IOError, FileNotFoundError ")
            msg.exec_()
        self.tablefiller()

    def sort_bt(self):
        try:
            sortname  = self.QComboBox_Timstamp.currentText()
            self.DF = self.DF.sort_values(by=[sortname])
            self.df = self.df.sort_values(by=[sortname])
            self.df.reset_index(drop=True, inplace=True)
            self.DF.reset_index(drop=True, inplace=True)
            self.tablefiller()
        except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            msg.setWindowTitle("WARNING")
            msg.exec_()

    def mapping_bt(self):

        # try:
            #Mappingsetup
            tile  = self.comboBox_Maptype.currentText()
            map = folium.Map( tiles= tile,zoom_start = 20,control_scale=True)

            if self.markerexistance & self.dataloaded:
                mc  = MarkerCluster()#initialisieren der MarkerCluster
                #Auslesen der Markercoordinaten
                i_lat = self.QComboBox_Latetude_val.currentText()#auslesen der lat lon indizes im Dataframe
                i_lon = self.QComboBox_Longetude_val.currentText()

                if self.checkBox_jump.isChecked():#für den Jumpratefilter (just keep every [Jumprate] Marker)
                    self.df.reset_index(drop=True, inplace=True)#stellt sicher dass Indizes fortlaufend nummeriert sind
                    jumprate = int(self.text_jumprate.text())#auslesen der Jumprate
                    goodindex = range(0, len(self.df.index), jumprate)
                    x = self.df
                    del(self.df)
                    self.df = x.iloc[goodindex,:]
                    del(x)

                lat = self.df.loc[:][i_lat]#auslesen der lat lon kooridinaten
                lon = self.df.loc[:][i_lon]

                if self.checkBox_Marker.isChecked() and len(lat)>3000:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: You have printed over 3000 Markers maybe your map will be unstable try using MarkerClusters or the Jumpfilter")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()#waring for to much Markers
                #vorbereiten der Markercoordinaten

                tool1           = self.comboBox_tooltip_1.currentText()#auslesen der tooltipspalte1
                tool2           = self.comboBox_tooltip_2.currentText()#auslesen der tooltipspalte2
                clustercheck    = self.checkBox_cluster.isChecked()#auslesen ob cluster geplottet werden sollen
                markercheck     = self.checkBox_Marker.isChecked()#auslesen ob marker geplottet werden sollen
                jumpcheck       = self.checkBox_jumpborder_mark.isChecked()#auslesen ob markersprünge markiert werden sollen
                points          = [] #liste für PolyLine
                polylinecheck   = self.checkBox_Polyline.isChecked()#auslesen ob polyline geplottet werden soll

                if jumpcheck:
                    jumpborder = self.text_map_jumpborder_mark.text()
                    jumpframe = self.findjumps(jumpborder)#Dataframe with jumps between next neighbours over 60km
                    print("jumpframe=",jumpframe)
                    jumpindex = jumpframe.loc[:,"oldindex"]#indizes of self.df for the jumppoints
                    print("jumpindex=",jumpindex)
                    if jumpindex.empty:
                        jumpindex.loc[0]=2000000000000000000
                    for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                        for jk in jumpindex:
                            if jk == i:
                                curentpoint_jp = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                                tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                                folium.Marker(curentpoint_jp,tooltip = "This marker has a jump",popup=tooltip,icon=folium.Icon(color='red')).add_to(map)

                if markercheck:#fügt marker zu der map hinzu
                    for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                        curentpoint = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                        tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                        folium.Marker(curentpoint,tooltip = tooltip).add_to(map)#fügt marker hinzu

                if clustercheck: #erstellt clustermarker
                    for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                        curentpoint = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                        tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                        mc.add_child(folium.Marker(curentpoint,tooltip = tooltip))#fügt cluster hinzu
                    map.add_child(mc)

                if polylinecheck & len(points)>0:#erstellt PolyLine
                    if jumpcheck:
                        for i in lat.index:
                            for jk in jumpindex:
                                if jk != i:
                                    points.append(tuple(curentpoint_jp.loc[i]))#sammelt punkte für die PolyLine
                    else:
                        for i in lat.index:
                            curentpoint = [lat.loc[i],lon.loc[i]]
                            points.append(tuple(curentpoint))#sammelt punkte für die PolyLine
                    print("pointslen = ",len(points))
                    folium.PolyLine(points).add_to(map) #erstellen einer PolyLine

                #Zoom auf auf kooridinaten einstellen
                sw = self.df.loc[:,[i_lat, i_lon]].min().values.tolist()
                ne = self.df.loc[:,[i_lat, i_lon]].max().values.tolist()
                map.fit_bounds([sw, ne])

                #Darstellen der filtersettings mithilfe eines mittig plazierten markers
                s= self.textfilter
                if len(s)>0:
                    for i in range(0,len(s)):
                       popfiltertext = ''.join([str(elem)+"<br>" for elem in s])
                    infopos     = [(sw[0]+ne[0])/2,(sw[1]+ne[1])/2]
                    infomarker  = folium.Marker(infopos,tooltip="filtersettings",icon=folium.Icon(color='red', icon='info-sign'))
                    pop         = folium.map.Popup(html=popfiltertext, max_width=200,min_width=200).add_to(infomarker)
                    infomarker.add_to(map)

            #Speichern der Karte
            mapname = self.text_Mapname.text()
            map.save(mapname+'.html')

            if self.dataloaded is not True:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("WARNING: No data selected")
                msg.setWindowTitle("WARNING")
                msg.exec_()
        # except (IOError,NameError,TypeError,ValueError) as e:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText(str(e))
        #     msg.setWindowTitle("WARNING")
        #     msg.exec_()
        # except:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText("Unknown Error, (No IOError, NameError, TypeError or ValueError ")
        #     msg.setWindowTitle("WARNING")
        #     msg.exec_()

    def filteroptions(self,activ):
        #Filter the data as said by the Filteroptions
        #Input Parameter:
        #activ....[bolian] if True ->filteroptions get aplyed
        #                  if False ->filteroptions get undone

        if activ: #Apply filter button
                self.df = self.DF

                def filtering(operator, DataFr, argument,i_par):
                    #translate Filteroptions into boolians
                    if operator=='<':
                        x=DataFr.loc[DataFr[i_par]<argument]
                        return x
                    elif operator == '>':
                        x=DataFr.loc[DataFr[i_par]>argument]
                        return x
                    elif operator == '<=':
                        x=DataFr.loc[DataFr[i_par]<=argument]
                        return x
                    elif operator == '>=':
                        x=DataFr.loc[DataFr[i_par]>=argument]
                        return x
                    elif operator == '==':
                        x=DataFr.loc[DataFr[i_par]==argument]
                        return x
                    elif operator == '!=':
                        x=DataFr.loc[DataFr[i_par]!=argument]
                        return x
            # try:
                #Auslesen der Datenfelder
                i_par1 = self.comboBox_filter_par1.currentText() #Spaltenauswahl
                i_par2 = self.comboBox_filter_par2.currentText()
                i_par3 = self.comboBox_filter_par3.currentText()
                i_par4 = self.comboBox_filter_par4.currentText()
                i_par5 = self.comboBox_filter_par5.currentText()
                i_par6 = self.comboBox_filter_par6.currentText()
                i_time1 = self.comboBox_filter_time1.currentText()
                i_time2 = self.comboBox_filter_time2.currentText()
                op1 = self.comboBox_filter_op1.currentText() #Operatorauswahl
                op2 = self.comboBox_filter_op2.currentText()
                op3 = self.comboBox_filter_op3.currentText()
                op4 = self.comboBox_filter_op4.currentText()
                op5 = self.comboBox_filter_op5.currentText()
                op6 = self.comboBox_filter_op6.currentText()
                op_t1 = self.comboBox_filter_op_t1.currentText()
                op_t2 = self.comboBox_filter_op_t2.currentText()
                arg1 = self.text_filter_par1.text() #Filterargument
                arg2 = self.text_filter_par2.text()
                arg3 = self.text_filter_par3.text()
                arg4 = self.text_filter_par4.text()
                arg5 = self.text_filter_par5.text()
                arg6 = self.text_filter_par6.text()
                #Timefilter
                arg_t1 = self.text_filter_time1.text()
                arg_t2 = self.text_filter_time2.text()
                #cutoff Filtern
                first = self.text_filter_firstrow.text()
                last  = self.text_filter_cutoff.text()


                #Filtersettings prealocate
                self.textfilter=[]

                #Filtern
                if self.checkbox_filter_1.isChecked():
                    x = filtering(op1,self.df,float(arg1),i_par1)#filter data
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par1+" "+op1+" "+arg1)#save text for filtersettings.txt
                if self.checkbox_filter_2.isChecked():
                    x = filtering(op2,self.df,float(arg2),i_par2)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par2+" "+op2+" "+arg2)
                if self.checkbox_filter_3.isChecked():
                    x = filtering(op3,self.df,float(arg3),i_par3)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par3+" "+op3+" "+arg3)
                if self.checkbox_filter_4.isChecked():
                    x = filtering(op4,self.df,float(arg4),i_par4)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par4+" "+op4+" "+arg4)
                if self.checkbox_filter_5.isChecked():
                    x = filtering(op5,self.df,float(arg5),i_par5)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par5+" "+op5+" "+arg5)
                if self.checkbox_filter_6.isChecked():
                    x = filtering(op6,self.df,float(arg6),i_par6)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par6+" "+op6+" "+arg6)
                if self.checkbox_filter_t1.isChecked():#Timestamp Filter
                    x = filtering(op_t1,self.df,arg_t1,i_time1)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_time1+" "+op_t1+" "+arg_t1)
                if self.checkbox_filter_t2.isChecked():#Timestamp Filter
                    x = filtering(op_t2,self.df,arg_t2,i_time2)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_time2+" "+op_t2+" "+arg_t2)
                self.df.reset_index(drop=True, inplace=True) #reset index for potential filtering
                if self.checkBox_filter_jumppoints.isChecked():
                    jumpborder = float(self.text_filter_jumpborder.text()) #[km] #set classification for a jump
                    jumppoints = self.findjumps(jumpborder)
                    deadindex = jumppoints.loc[:,"oldindex"]
                    for i in jumppoints.loc[:,"oldindex"]:
                        self.df=self.df.drop(i)
                    self.df.reset_index(drop=True, inplace=True)
                    self.textfilter.append("jumpfilter = True, jumpborder = "+str(jumpborder)+"km")

                if self.checkBox_filter_repeat.isChecked():#Filter for repeating Datapoints
                    self.df.reset_index(drop=True, inplace=True)
                    x = self.df
                    del(self.df)
                    ilat = self.QComboBox_Latetude_val.currentText()
                    ilon = self.QComboBox_Longetude_val.currentText()
                    un= x.loc[:,[ilon,ilat]].drop_duplicates()
                    self.df=x.iloc[un.index,:]
                    del(x)
                    self.textfilter.append("repeatfilter = True")
                #Cutoff Filter Cuts at firstrow and at lastrow
                if self.checkBox_filter_firstrow.isChecked() | self.checkBox_filter_cutoff.isChecked():
                    if (self.checkBox_filter_firstrow.isChecked()):
                        firstrow = int(first)
                    else:
                        firstrow = 1
                    if (self.checkBox_filter_cutoff.isChecked()):
                        lastrow = int(last)
                    else:
                        lastrow = len(self.df.index)

                    if (firstrow)<(lastrow):
                        if lastrow<=len(self.df.index):
                            x = self.df
                            del(self.df)
                            self.df = x.iloc[firstrow:lastrow,:]
                            del(x)
                            self.textfilter.append("firstrow = " +str(firstrow))
                            self.textfilter.append("lastrow = "+str(lastrow))
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("ERROR: lastrow > data length")
                            msg.setWindowTitle("ERROR")
                            msg.exec_()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("ERROR: firstrow >= lastrow")
                        msg.setWindowTitle("ERROR")
                        msg.exec_()

                self.df.reset_index(drop=True, inplace=True)#resets indexes of the Dataframe to 1,2,3,4,...

                #gives a waring if you have Filtered all points and swich markers off
                if len(self.df.index) == 0:
                    self.markerexistance = False
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: The selected data range is empty")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                else:#if filtered data is not empty shich markers on
                    self.markerexistance = True

            # except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Warning)
            #     msg.setText(str(e))
            #     msg.setWindowTitle("WARNING")
            #     msg.exec_()
            # except:
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Warning)
            #     msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            #     msg.setWindowTitle("WARNING")
            #     msg.exec_()

        elif ~activ:#undo filter Button, resets Dataset
                    self.df = self.DF
                    self.textfilter=[]
        self.tablefiller()

    def findjumps(self,jumpborder):
        ilat = self.QComboBox_Latetude_val.currentText()
        ilon = self.QComboBox_Longetude_val.currentText()
        gps  = self.df.loc[:,[ilat,ilon]]#build working dataframe
        gps.loc[:,"oldindex"] = range(0,len(gps.loc[:,ilat]))#save current index
        lat  = gps.loc[:,[ilat,"oldindex"]]#build Latitude
        lon  = gps.loc[:,[ilon,"oldindex"]]#build Longitude

        #setting 2 dataframes for next neighbours
        lat_i  = lat.iloc[range(1,len(lat),2),:]
        lat_ii = lat.iloc[range(0,len(lat),2),:]
        lat_i.reset_index(drop=True, inplace=True)#resetting indexes nessesary to subtrackting 2 frames
        lat_ii.reset_index(drop=True, inplace=True)
        if len(lat_i)!=len(lat_ii):#check if lat_i and lat_ii have same length
            if len(lat_i)<len(lat_ii):
                lat_ii=lat_ii.loc[0:len(lat_i)]
            elif len(lat_i)>len(lat_ii):
                lat_i=lat_i.loc[0:len(lat_ii)]
        delta_lat = lat_i[ilat].sub(lat_ii[ilat])#subtrackting next neighbours

        lon_i  = lon.loc[range(1,len(lon),2),:]
        lon_ii = lon.loc[range(0,len(lon),2),:]
        lon_i.reset_index(drop=True, inplace=True)
        lon_ii.reset_index(drop=True, inplace=True)
        if len(lon_i)!=len(lon_ii):#check if lon_i and lon_ii have same length
            if len(lon_i)<len(lon_ii):
                lon_ii=lon_ii.loc[0:len(lon_i)]
            elif len(lon_i)>len(lon_ii):
                lon_i=lon_i.loc[0:len(lon_ii)]
        delta_lon = lon_i[ilon] - lon_ii[ilon]

        #create distance vector and detect jumps
        R               = np.sqrt(delta_lat**2 + delta_lon**2)#build a distance vector
        jumpborder_grad = jumpborder/11.3 #km to ° maybe better convert faktor
        jumps           = R[R>jumpborder_grad]# find jump
        print(jumps)
        #build dataframe with jumppoints
        lat                    = pd.concat([lat_i.loc[jumps.index.values,:],lat_ii.loc[jumps.index.values,:]])
        lon                    = pd.concat([lon_i.loc[jumps.index.values,:],lon_ii.loc[jumps.index.values,:]])
        jumppoints             = lat
        jumppoints.loc[:,ilon] = lon.loc[:,ilon]
        return jumppoints
