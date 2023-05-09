# -*- coding: utf-8 -*-
"""project2menu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12G0DrGkFsSwJKZ8fvbd-_QeQuacbtAer
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
xl = pd.ExcelFile("/content/TableauSalesData.xlsx")
SalesData = xl.parse("Orders")

"""Menu 1:"""

#def for menu 1
def RegionsProfSales():
  RegionsProfSales = SalesData[["Region","Profit","Sales"]].groupby(by="Region").sum().sort_values(by="Sales",ascending = False)
  print('Profits and sales by region:')
  display(RegionsProfSales) 

def StateSales():
  RegionData = SalesData[["Sub-Category","Sales","Region","State"]]
  SouthData = RegionData[SalesData["Region"]== "South"]
  StateSales = SouthData.groupby(by="State").sum(numeric_only=True).sort_values(by="Sales",ascending =False)
  display(StateSales)

def SubCat_sc():
  RegionData = SalesData[["Sub-Category","Sales","Region","State"]]
  SC_Data = RegionData[SalesData["State"]=="South Carolina"]
  SubCat_sc = SC_Data.groupby(by= "Sub-Category").sum(numeric_only=True).sort_values(by="Sales",ascending = False)
  print("Sales by Sub-Category in SC")
  display(SubCat_sc)

def SC_StorageProdSales():
  sc_storage = SalesData[(SalesData['State'] == 'South Carolina') & (SalesData['Sub-Category'] == 'Storage')]
  ProdSales = sc_storage.groupby('Product Name')['Sales'].agg('sum')
  SC_StorageProdSales = ProdSales.sort_values(ascending=False)
  print("These are the product names and sales from the Storage sub-category in SC:")
  print(SC_StorageProdSales)

def plot_SC_StorageProdSales():
    sc_storage = SalesData[(SalesData['State'] == 'South Carolina') & (SalesData['Sub-Category'] == 'Storage')]
    ProdSales = sc_storage.groupby('Product Name')['Sales'].agg('sum')
    SC_StorageProdSales = ProdSales.sort_values(ascending=False)
    
    SC_StorageProdSales.plot.bar(figsize=(10,6))
    plt.title('Sales by Product in South Carolina - Storage Category')
    plt.xlabel('Product Name')
    plt.ylabel('Sales')
    plt.show()

def Returntomenu():
  print('Thank you for using the office solution data analytics system')

#menu 1
def salesmenu():
  print('Welcome to the Sales Analytics System.')
  print('\n Enter 1 to see the Profit and Sales by region'+
          '\n Enter 2 to see the Sales by States in the South Region' +
          '\n Enter 3 to see the total sales by Sub-Categories in South Carolina' +
          '\n Enter 4 to see the sales of Storage items in South Carolina' +
          '\n Enter 5 to see a Bar Chart of the Sales by Product - Storage, SC' +
          '\n Enter 6 to return to main menu\n')
  choice = input('Please enter your selection here:')
  print('\n')
  if choice == '1':
    RegionsProfSales()
    salesmenu()
  elif choice == '2':
    StateSales()
    salesmenu()
  elif choice == '3':
    SubCat_sc()
    salesmenu()
  elif choice == '4':
    SC_StorageProdSales()
    salesmenu()
  elif choice =='5':
    plot_SC_StorageProdSales()
    salesmenu()
  elif choice == '6':
    Returntomenu()
    menu()
  else: 
    print('You have entered an invalid option, please select from one of the options provided:')
    salesmenu()
salesmenu()

"""Menu 2: """

#menu 2
def discountmenu():
  print('Welcome to the Discount Analytics System')
  print('\n Enter 1 to see total profits and average discount for each region' + 
        '\n Enter 2 to see yearly regional furnishings discounts for 2017-2020'+
        '\n Enter 3 to see total profits and average discounts in five sub-categories for Central region'+
        '\n Enter 4 to quit\n')
  choice = input('Please enter you selection here:')
  print('\n')
  if choice == '1':
    RegionProfDis = SalesData[["Region", "Profit", "Discount"]].groupby(by="Region").agg({"Profit":'sum', "Discount":'mean'}).sort_values(by="Profit", ascending = False)
    display(RegionProfDis)
    discountmenu()
  elif choice == '2':
    JustFurnishings = SalesData.loc[SalesData["Sub-Category"]=="Furnishings"]
    JustFurnishingsYear = JustFurnishings.copy()
    JustFurnishingsYear["Year"] = JustFurnishingsYear["Order Date"].dt.year
    Years = JustFurnishingsYear.Year.unique()
    RegJustFurnishingsYear = JustFurnishingsYear[["Region","Year","Discount"]]
    for year in Years:
      OneYear = RegJustFurnishingsYear.loc[RegJustFurnishingsYear["Year"]==year]
      NoYear = OneYear[["Region","Discount"]]
      YearlyRegDiscount = NoYear.groupby("Region").mean()

      print("\nRegional furnishings discounts for the year: " + str(year))
      display(YearlyRegDiscount)
      print("*" * 40)
    discountmenu()
  elif choice == '3': 
    TablesReg = SalesData[["Sub-Category", "Region", "Profit", "Discount"]]
    CentralFurn = TablesReg.loc[TablesReg["Region"]=="Central"]
    CentralProfDis = CentralFurn.groupby(by="Sub-Category").agg({"Profit":"sum", "Discount":"mean"}).sort_values(by="Profit")
    display(CentralProfDis.head(5))
    discountmenu()
  elif choice == '4':
    print('Thank you for using the Office Solution Data Analystics System')
  else:
    print('You have entered an invalid option, please select from one of the options provided: ')
    discountmenu()
    
menu()

"""**Menu 3**"""

def SubCatsProfits():
  SubCatsProfits = SalesData[["Sub-Category","Profit","Sales"]]
  TotalSubCatProfits = SubCatsProfits.groupby(by= "Sub-Category").sum().sort_values(by="Profit",ascending = True)
  display(TotalSubCatProfits)

def TableRegion():
  JustTables = SalesData.loc[SalesData["Sub-Category"]=="Tables"]
  TableRegion = JustTables[['Region','Profit']]
  RegionTotalProf = TableRegion.groupby(by ='Region').sum().sort_values(by = 'Profit')
  display(RegionTotalProf) 

def TableSegRegionProd():
  JustTables = SalesData.loc[SalesData["Sub-Category"]=="Tables"]
  TableSegRegionProd = JustTables[['Segment','Region','Profit','Product Name']]
  EastTableSegmentProd = TableSegRegionProd.loc[TableSegRegionProd['Region']=='East']
  EastProfProd = EastTableSegmentProd.groupby(by = 'Segment').sum().sort_values(by = 'Profit')
  print(EastProfProd)

def EastSegProdProf():
  JustTables = SalesData.loc[SalesData["Sub-Category"]=="Tables"]
  TableSegRegionProd = JustTables[['Segment','Region','Profit','Product Name']]
  EastTableSegmentProd = TableSegRegionProd.loc[TableSegRegionProd['Region']=='East']
  EastProfProd = EastTableSegmentProd.groupby(by = 'Segment').sum().sort_values(by = 'Profit')
  EastSegProdProf = EastTableSegmentProd[['Product Name','Profit']].groupby('Product Name').sum()
  NegTables = EastSegProdProf[EastSegProdProf['Profit']< 0.0]
  NegTables = NegTables.sort_values('Profit', ascending = True)
  display(NegTables)

def profitsmenu():
  print('Welcome to the Victor Lins Report for Reducing Poorly Performing and Unprofitable Products')
  print('\n Enter 1 to see the Least Profitable Sub-categories' + 
        '\n Enter 2 to see the Least Profitable Region for the Least Profiable Sub-Category'+
        '\n Enter 3 to see the Least Profitable Segment withtin the Least Profitable Region'+
        '\n Enter 4 to see all Non-Profitable Tables within the Eastern Region'
        '\n Enter 5 to quit\n')
  choice = input('Please enter you selection here:')
  print('\n')
  if choice == '1':
    SubCatsProfits()
    profitsmenu()
  elif choice == '2':
    TableRegion()
    profitsmenu()
  elif choice == '3': 
    TableSegRegionProd()
    profitsmenu()
  elif choice =='4':
    EastSegProdProf()
    profitsmenu()
  elif choice == '5':
    print('Thank you for using the Office Solution Data Analystics System')
  else:
    print('You have entered an invalid option, please select from one of the options provided: ')
    profitsmenu()
    
profitsmenu()

"""# **Main Menu**"""

#main menu
def menu():
  print('Welcome to the Office Solutions Data Analytics System')
  print('\n Enter 1 to see Sales from Chloe' + 
        '\n Enter 2 to see Discount analytics from Steven'+
        '\n Enter 3 to see analytics from Victor'+
        '\n Enter 4 to quit\n')
  choice = input('Please enter you selection here:')
  print('\n')
  if choice == '1':
    salesmenu()
    menu()
  elif choice == '2':
    discountmenu()
    menu()
  elif choice == '3': 
    profitsmenu()
    menu()
  elif choice == '4':
    print('Thank you for using the Office Solution Data Analystics System')
  else:
    print('You have entered an invalid option, please select from one of the options provided: ')
    menu()
    
menu()