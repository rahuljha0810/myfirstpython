import pandas as pd
import numpy as np
Name=["Deep","Akash","Neha","Sumit","Rahul"]   
A={"Userid":[114477,112255,116688,224411,665544],
   "Password":[12345,45678,787878,454545,969696],
   "Balance":[40000,25000,12000,47000,100000]}
MyData=pd.DataFrame(A,index=Name)
print(MyData) 
while True:
  print("Type Login To Access You Account")
  print("Type Exit To Exit Our Application")
  Inp=input("Enter Your Option: ").lower()
  if Inp=="login" or Inp=="exit":
    break

if Inp=="login":
  print("Welcome To Our Portal")
  print("prosseing...............")
  print("prosseing...............")
  print("prosseing...............")
  print("prosseing...............")
  Nam=input("Enter your Name: ")
  if Nam in MyData.index:
    Uid=int(input("Enter Your User Id: "))
    if Uid==MyData["Userid"][Nam]:
      Pass=int(input("Enter Your Password: "))
      if Pass==MyData["Password"][Nam]:
        print("You Are Login Now")
        print("Enter 1 for diposit amount")
        print("Enter 2 for deleting account")
        print("Enter 3 for renaming account")
        print("Enter 4 for exit")
        opt=input("Enter your Choice: ")
        if opt=="1":
          namt=int(input("Enter Amount YOu want to deposit"))
          MyData["Balance"][Nam]+=namt
          print("Your New Balance ",MyData["Balance"][Nam])
        elif opt=="2":
          MyData.drop(Nam,axis=0,inplace=True)
          print(MyData)
        elif opt=="3":
          nwnm=input("Enter New Name: ")
          MyData.rename(index={Nam:nwnm},inplace=True)
          print(MyData)
        else:
          print("You are Exit Now Run Me Again")

      else:
        print("Entered Password Is wrong")  
    else:
      print("Wrong uSer iD")  
  else:
    print("User Does Not Exist Try Again")
print(MyData)
MyData.rename(index={"Neha":"Sachin"},inplace=True)
MyData.rename(columns={"Userid":"UID"},inplace=True)
print(MyData)