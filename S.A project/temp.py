from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox,QPushButton
import matplotlib.pyplot as plt
import numpy
import time
import math
import pandas as pd
from csv import reader
import csv
import statistics
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

file=pd.read_csv(r'Corona_Death.csv')

class Salah(QMainWindow):
    
    #dras scatter plot
    def Scatter_Plot(self):
        file=pd.read_csv(r'WebDevelopment2.csv')
        x = file['price']
        y = file['NumberOfLectures']
        X=sorted(x)
        plt.scatter(X,y)
        plt.show()
      
      
    def Histogram(self):
      with open('HistoCSV.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        plt.hist(list_of_rows[0],bins=int(math.sqrt(len(list_of_rows[0])))+1)
        plt.show()
    
    def histo2(self):

        # Read CSV into pandas 
        data = pd.read_csv(r'WebDevelopment2.csv') 
        data.head() 
        df = pd.DataFrame(data) 
  
        name = df['title'].head(50) 
        price = df['price'].head(50)    
  
# Figure Size 
        fig, ax = plt.subplots(figsize =(16, 9)) 
  
        # Horizontal Bar Plot 
        ax.barh(name, price) 
  
        # Remove axes splines 
        for s in ['top', 'bottom', 'left', 'right']: 
           ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
        ax.xaxis.set_ticks_position('none') 
        ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
        ax.xaxis.set_tick_params(pad = 5) 
        ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
        ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
        ax.invert_yaxis() 
  
# Add annotation to bars 
        for i in ax.patches:
           plt.text(i.get_width()+0.2, i.get_y()+0.5,  
           str(round((i.get_width()), 2)), 
           fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
        ax.set_title('Web development courses from udemy', 
             loc ='right', ) 
  
# Add Text watermark 
        fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.7) 
  
# Show Plot 
        plt.show() 
    
    def CalMean(self):
       file=pd.read_csv(r'HistoCSV.csv')
       mean1=file['height'].mean()
       QMessageBox.about(self,"Mean","the mean = "+str(mean1))
      
      
    def CalMode(self):
         x=[1,2,3,4,3,3,9,9,9,9]
         QMessageBox.about(self,"Mode","the Mode = "+str(statistics.mode(x)))
    
    def CalMedain(self):
         #x=[1,2,3,4,3,3]
         file=pd.read_csv(r'HistoCSV.csv')
         medain1=file['height'].median()
         QMessageBox.about(self,"Median","the Median = "+str(medain1))
    #Bar graph
    def BarGraph(self):
        data=file['Day']
        label=file['Country']
        
        objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        
        y_pos = np.arange(len(label))
        performance = [10,8,6,4,2,1]
        
        plt.bar(label, data,width=0.1, alpha=0.5)
        plt.xticks(y_pos, label)
        plt.ylabel('Death')
        plt.title('Corona Death')
        plt.show()
        
    def Pie(self):
       data=file['Day']
       label=file['Country']
       
       fig = plt.figure(figsize =(100, 70)) 
       plt.pie(data, labels = label) 
       plt.show() 
       
    def BoxPlot(self) :
    
        np.random.seed(10)
        collectn_1 = np.random.normal(100, 10, 200)
        collectn_2 = np.random.normal(80, 30, 200)
        collectn_3 = np.random.normal(90, 20, 200)
        collectn_4 = np.random.normal(70, 25, 200)
        files=pd.read_csv(r'HistoCSV.csv')
        
        data=files['height']
        
        data_to_plot=[data]
        # Create a figure instance
        fig = plt.figure(1, figsize=(2, 3))
        ax = fig.add_subplot(111)
        bp = ax.boxplot(data_to_plot)
        plt.show()
        
        
   
         
    def __init__(self):
        super(Salah,self).__init__()  
        self.setGeometry(400,400,800,800)
        self.setWindowTitle("Statistical Analysis")
        
        #Scatter plot
        self.ScatterButton=QtWidgets.QPushButton(self)
        self.ScatterButton.setText("Scatter plot")
        self.ScatterButton.clicked.connect(self.Scatter_Plot)
        
        #Histogram
        self.HistogramButton=QtWidgets.QPushButton(self)
        self.HistogramButton.setText("Histogram ")
        self.HistogramButton.move(0,20)
        self.HistogramButton.clicked.connect(self.Histogram)
        
        #Mean
        self.MeanButton=QtWidgets.QPushButton(self)
        self.MeanButton.setText("Mean")
        self.MeanButton.move(0,50)
        self.MeanButton.clicked.connect(self.CalMean)
        
        #Mode
        self.ModeButton=QPushButton('Mode',self)
        self.ModeButton.clicked.connect(self.CalMode)
        self.ModeButton.move(0,80)
        
        #Median
        self.MedainButton=QPushButton('Median',self)
        self.MedainButton.clicked.connect(self.CalMedain)
        self.MedainButton.move(0,110)
        
        #Bar chart
        self.BarButton=QPushButton('Bar graph',self)
        self.BarButton.clicked.connect(self.BarGraph)
        self.BarButton.move(0,140)
        
        #pie graph
        self.PieButton=QPushButton('pie graph',self)
        self.PieButton.clicked.connect(self.Pie)
        self.PieButton.move(0,170)
        
        #Box polt
        self.BoxPlotButton=QPushButton('Box Plot',self)
        self.BoxPlotButton.clicked.connect(self.BoxPlot)
        self.BoxPlotButton.move(0,200)
        
        #Histo2
        self.histo=QPushButton('Histo2',self)
        self.histo.clicked.connect(self.histo2)
        self.histo.move(0,250)
        
       
    

#main
app=QApplication(sys.argv)
w=Salah()
w.show()
sys.exit(app.exec_())

x=34
name='salah'
name=str(input("Enter your name"))
