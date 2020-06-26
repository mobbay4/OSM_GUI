import pandas as pd
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

        try:
            #Mappingsetup
            tile  = self.comboBox_Maptype.currentText()
            map = folium.Map( tiles= tile,zoom_start = 20,control_scale=True)
            mc  = MarkerCluster()
            if self.markerexistance & self.dataloaded:
                #Auslesen der Markercoordinaten
                i_lat = self.QComboBox_Latetude_val.currentText()
                i_lon = self.QComboBox_Longetude_val.currentText()

                lat = self.df.loc[:][i_lat]
                lon = self.df.loc[:][i_lon]
                if self.checkBox_Marker.isChecked() and len(lat)>3000:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: You have printed a lot of Markers maybe your map will be unstable")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                #vorbereiten der Markercoordinaten
                points = [] #liste für PolyLine
                tool1       = self.comboBox_tooltip_1.currentText()#auslesen der tooltipspalte1
                tool2       = self.comboBox_tooltip_2.currentText()#auslesen der tooltipspalte2
                clustercheck = self.checkBox_cluster.isChecked()#auslesen ob cluster geplottet werden sollen
                markercheck  = self.checkBox_Marker.isChecked()#auslesen ob marker geplottet werden sollen

                for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                    curentpoint = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                    tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                    if markercheck:
                        folium.Marker(curentpoint,tooltip = tooltip).add_to(map)#fügt marker hinzu
                    if clustercheck:
                        mc.add_child(folium.Marker(curentpoint,tooltip = tooltip))#fügt cluster hinzu
                    points.append(tuple(curentpoint))#sammelt punkte für die PolyLine
                if self.checkBox_Polyline.isChecked():
                    folium.PolyLine(points).add_to(map) #erstellen einer PolyLine
                if clustercheck:
                    map.add_child(mc)
                #Zoom auf auf kooridinaten einstellen
                sw = self.df.loc[:,[i_lat, i_lon]].min().values.tolist()
                ne = self.df.loc[:,[i_lat, i_lon]].max().values.tolist()
                map.fit_bounds([sw, ne])

            #Speichern der Karte
            mapname = self.text_Mapname.text()
            map.save(mapname+'.html')

            if self.dataloaded is not True:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("WARNING: No data selected")
                msg.setWindowTitle("WARNING")
                msg.exec_()
        except (IOError,NameError,TypeError,ValueError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Unknown Error, (No IOError, NameError, TypeError or ValueError ")
            msg.setWindowTitle("WARNING")
            msg.exec_()

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
            try:
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

                #Filtern
                if self.checkbox_filter_1.isChecked():
                    x = filtering(op1,self.df,float(arg1),i_par1)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_2.isChecked():
                    x = filtering(op2,self.df,float(arg2),i_par2)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_3.isChecked():
                    x = filtering(op3,self.df,float(arg3),i_par3)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_4.isChecked():
                    x = filtering(op4,self.df,float(arg4),i_par4)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_5.isChecked():
                    x = filtering(op5,self.df,float(arg5),i_par5)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_6.isChecked():
                    x = filtering(op6,self.df,float(arg6),i_par6)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_t1.isChecked():
                    x = filtering(op_t1,self.df,arg_t1,i_time1)
                    del(self.df)
                    self.df=x
                    del(x)
                if self.checkbox_filter_t2.isChecked():
                    x = filtering(op_t2,self.df,arg_t2,i_time2)
                    del(self.df)
                    self.df=x
                    del(x)

                if self.checkBox_filter_repeat.isChecked():
                    self.df.reset_index(drop=True, inplace=True)
                    x = self.df
                    del(self.df)
                    ilat = self.QComboBox_Latetude_val.currentText()
                    ilon = self.QComboBox_Longetude_val.currentText()
                    un= x.loc[:,[ilon,ilat]].drop_duplicates()
                    self.df=x.iloc[un.index,:]
                    del(x)
                self.df.reset_index(drop=True, inplace=True)

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

                if self.checkBox_filter_repeat.isChecked():
                    self.df.reset_index(drop=True, inplace=True)
                    x = self.df
                    del(self.df)
                    ilat = self.QComboBox_Latetude_val.currentText()
                    ilon = self.QComboBox_Longetude_val.currentText()
                    un= x.loc[:,[ilon,ilat]].drop_duplicates()
                    self.df=x.iloc[un.index,:]
                    del(x)
                    
                if self.checkBox_filter_jump.isChecked():
                    self.df.reset_index(drop=True, inplace=True)
                    jumpstring = self.comboBox_markerjump.currentText()
                    jumprate = int(jumpstring[0])
                    goodindex = range(0, len(self.df.index), jumprate)
                    x = self.df
                    del(self.df)
                    self.df = x.iloc[goodindex,:]
                    del(x)

                self.df.reset_index(drop=True, inplace=True)

                if len(self.df.index) == 0:
                    self.markerexistance = False
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: The selected data range is empty")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                else:
                    self.markerexistance = True

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

        elif ~activ:#undo filter Button
            self.df = self.DF
        self.tablefiller()
