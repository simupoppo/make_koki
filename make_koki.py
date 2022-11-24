#----------------read me----------------------------------------------
# container_list is the list of container_list
# container_image_list is the list of container image file list
# input parameter: koki_name,koki_image,koki_length,container_number
# koki_name is the name of kokiXXX
# copyrite is your name
# koki_image is the name of imagefile "kokiXXX" (.png)
# koki_length is the length of kokiXXX (default = 12)
# container_number is the number of loading containers (default = 5)
# topspeed is the maximum speed of the containers[km/s]
# intro_year is the intro year
# retire_year is the retire year
# if not set retire year, input 0 or no input 
# if you input parameters from txtfile, please use below templete.
# please input name or integer in XXX
#--------input.txt-----------
#1  kokiXXX      # koki_name
#2  myname       # copyright
#3  kokiXXX      # koki_image
#4  12           # koki_length
#5  5            # container_number
#6  100          # topspeed
#7  5200000      # freight car cost
#8  100          # freight car runningcost    
#9  20           # freight car weight       
#10 1989         # intro_year
#11 0            # retire_year
#12 0            # the first of container loading length. default=0
#13 12.0         # the end of container loading length. default=koki_length. Don't put the number greater than koki_length!
#----------------------------
#--------container info------ 
# vehlist=container list
# vehlist[i]=[container_name_or_vehicle_name,container_image_path,freightcat,payload,the_top_length_of_container,the_end_length_of_container,kokiflag]
# container_name is vehicle name.
# image_path is the path of image.
# top_length and end length set where the container loaded.
# kokiflag is integer. If vehicle is the container car front, kokiflag = 1.If vehicle is the container car back, kokiflag=2 . Else, kokiflag=0
# ---------Attention!--------
# input freight car image bust be set as below:
# 
# EmptyImage[S]=kokiXXX.0.0
# EmptyImage[E]=kokiXXX.0.1
# EmptyImage[SE]=kokiXXX.0.2
# EmptyImage[SW]=kokiXXX.0.3
# EmptyImage[N]=kokiXXX.0.4
# EmptyImage[W]=kokiXXX.0.5
# EmptyImage[NW]=kokiXXX.0.6
# EmptyImage[NE]=kokiXXX.0.7
# 
# 
#----------------------------
#---------------------------------------------------------------------


import os

def makekoki():
    for i in range(len(vehlist)):
        temp_veh=vehlist[i]
        if temp_veh[4]>=top_length and temp_veh[5]<=end_length:
            const_prev=[]
            const_next=[]
            for j in range(len(vehlist)):
                if vehlist[j][4]>=top_length and vehlist[j][5]<=temp_veh[4] and temp_veh[6]!=1 and vehlist[j][6]!=2:
                    const_prev.append(vehlist[j][0])
                if vehlist[j][5]<=end_length and vehlist[j][4]>=temp_veh[5] and temp_veh[6]!=2 and vehlist[j][6]!=1:
                    const_next.append(vehlist[j][0])
            temp_cost="8000"
            temp_runcost="0.01"
            temp_weight="0.1"
            if temp_veh[6]==1:
                temp_cost=cost_car
                temp_runcost=r_cost_car
                temp_weight=weight_car
            elif temp_veh[6]==2:
                temp_cost="0"
                temp_runcost="0"
                temp_weight="0"
            writing_dat(temp_veh[0],copy_right,temp_veh[2],temp_veh[3],temp_cost,temp_weight,temp_veh[1],const_prev,const_next,temp_runcost,temp_veh[6])
def writing_dat(vehiclename,copy_r,freightcat,payload,cost,weight,EmptyImage,C_Prev,C_Next,runningcost="0.01",kokiflag=0):
    output_dat.write("-------------------------------------------------------------------------------\n")
    output_dat.write("obj=vehicle\n")
    output_dat.write("copyright="+copy_r+"\n")
    output_dat.write("name="+vehiclename+"\n")
    output_dat.write("waytype=track\n")
    output_dat.write("speed="+topspeed+"\n")
    output_dat.write("freight="+freightcat+"\n")
    output_dat.write("payload="+payload+"\n")
    output_dat.write("cost="+cost+"\n")
    output_dat.write("weight="+weight+"\n")
    output_dat.write("RunningCost="+runningcost+"\n")
    output_dat.write("intro_year="+intro_year+"\n")
    if retire_year!='0':
        output_dat.write("retire_year="+retire_year+"\n")
    for i in range(len(C_Prev)):
        output_dat.write("Constraint[Prev]["+str(i)+"]="+C_Prev[i]+"\n")
    for i in range(len(C_Next)):
        output_dat.write("Constraint[Next]["+str(i)+"]="+C_Next[i]+"\n")
    if kokiflag==0:
        output_dat.write("length=0\n")
        output_dat.write("EmptyImage[S]="+EmptyImage+"0\n")
        output_dat.write("EmptyImage[E]="+EmptyImage+"1\n")
        output_dat.write("EmptyImage[SE]="+EmptyImage+"2\n")
        output_dat.write("EmptyImage[SW]="+EmptyImage+"3\n")
        output_dat.write("EmptyImage[N]="+EmptyImage+"4\n")
        output_dat.write("EmptyImage[W]="+EmptyImage+"5\n")
        output_dat.write("EmptyImage[NW]="+EmptyImage+"6\n")
        output_dat.write("EmptyImage[NE]="+EmptyImage+"7\n")
    elif kokiflag==1:
        output_dat.write("length=0\n")
        output_dat.write("EmptyImage[S]=src/koki_a.0.0\n")
        output_dat.write("EmptyImage[E]=src/koki_a.0.1\n")
        output_dat.write("EmptyImage[SE]=src/koki_a.0.2\n")
        output_dat.write("EmptyImage[SW]="+EmptyImage+".0.3\n")
        output_dat.write("EmptyImage[N]="+EmptyImage+".0.4\n")
        output_dat.write("EmptyImage[W]="+EmptyImage+".0.5\n")
        output_dat.write("EmptyImage[NW]="+EmptyImage+".0.6\n")
        output_dat.write("EmptyImage[NE]="+EmptyImage+".0.7\n")
        output_dat.write("FreightImage[S]="+EmptyImage+".0.0\n")
        output_dat.write("FreightImage[E]="+EmptyImage+".0.1\n")
        output_dat.write("FreightImage[SE]="+EmptyImage+".0.2\n")
        output_dat.write("FreightImage[SW]="+EmptyImage+".0.3\n")
        output_dat.write("FreightImage[N]="+EmptyImage+".0.4\n")
        output_dat.write("FreightImage[W]="+EmptyImage+".0.5\n")
        output_dat.write("FreightImage[NW]="+EmptyImage+".0.6\n")
        output_dat.write("FreightImage[NE]="+EmptyImage+".0.7\n")
    elif kokiflag==2:
        output_dat.write("length="+str(koki_length)+"\n")
        output_dat.write("EmptyImage[S]="+EmptyImage+".0.0\n")
        output_dat.write("EmptyImage[E]="+EmptyImage+".0.1\n")
        output_dat.write("EmptyImage[SE]="+EmptyImage+".0.2\n")
        output_dat.write("EmptyImage[SW]=src/koki_a.0.3\n")
        output_dat.write("EmptyImage[N]=src/koki_a.0.4\n")
        output_dat.write("EmptyImage[W]=src/koki_a.0.5\n")
        output_dat.write("EmptyImage[NW]=src/koki_a.0.6\n")
        output_dat.write("EmptyImage[NE]=src/koki_a.0.7\n")
    return()


print("What is the name of freight car? Please input.")
print("If you use txtfile 'input.txt', please input 'isfile'")
koki_name = input()
if koki_name == "isfile":
    file_data=open("input.txt","r")
    lines = file_data.readlines()
    file_data.close()
    for i in range(len(lines)):
        lines[i]=lines[i].rstrip()
        print(lines)
    print(lines)
    koki_name=lines[0]
    copy_right=lines[1]
    koki_image=lines[2]
    if (os.path.isfile(koki_image+".png")==False):
        print("NO SUCH FILE {0} ! PLEASE CHECK SPELLING!".format(koki_image))
        ispng="0"
    koki_length=int(lines[3])
    container_number=int(lines[4])
    topspeed=lines[5]
    cost_car=lines[6]
    r_cost_car=lines[7]
    weight_car=lines[8]
    intro_year=lines[9]
    retire_year=lines[10]
    top_length=float(lines[11])
    end_length=float(lines[12])
    print("loading file...")
else:
    print("What is your name? Please input the copyright name")
    copy_right=input()
    print("What is the name of imagefile of freight car? Please input.")
    koki_image = input()
    ispng="1"
    if (os.path.isfile(koki_image+".png")==False):
        print("NO SUCH FILE {0} ! PLEASE CHECK SPELLING!".format(koki_image))
        ispng="0"
    print("How long is the vehicle? Please input integer!")
    koki_length = input()
    if int(koki_length)==ValueError:
        koki_length=12
        print("Error. The length will be 12.")
    koki_length=int(koki_length)
    print("How many containers can it carry? Please input number integer 1 to 5!")
    container_number = input()
    if int(container_number)==TypeError:
        container_number=5
        print("Error. The number of containers will be 5.")
    container_number=int(container_number)
    print("What is the maximum speed?")
    topspeed=input()
    print("What is the cost of the car? (about 5,000,000)")
    cost_car=input()
    print("What is the running cost of the car? (about 10)")
    r_cost_car=input()
    print("How much does the vehicle weigh? (about 20)")
    weight_car=input()
    print("What is the intro_year?")
    intro_year=input()
    print("What is the retire_year? if not, please input '0'.")
    retire_year=input()
    print("From which length do you start loading containers? Please input float.")
    top_length=float(input())
    print("From which length do you end loading containers? Pleast input float.")  
    end_length=float(input())
    if end_length<koki_length:
        end_length=end_length
    else:
        end_length=koki_length
filename=koki_name+".dat"
output_dat=open(filename,"w")





vehlist=[]
# setting container_list
# if you make other containers, please add below!
vehlist.append([koki_name,koki_image,"None","1",top_length,top_length,1])
vehlist.append([koki_name+"_back",koki_image,"None","1",end_length,end_length,2])
vehlist.append([koki_name+"_JRF_19D_1","src/koki_a.1.","cat2","100",0,2.4,0])
vehlist.append([koki_name+"_JRF_19D_2","src/koki_a.2.","cat2","100",2.4,4.8,0])
vehlist.append([koki_name+"_JRF_19D_3","src/koki_a.3.","cat2","100",4.8,7.2,0])
vehlist.append([koki_name+"_JRF_19D_4","src/koki_a.4.","cat2","100",7.2,9.6,0])
vehlist.append([koki_name+"_JRF_19D_5","src/koki_a.5.","cat2","100",9.6,12,0])
vehlist.append([koki_name+"_JRF_V19A_1","src/koki_e.1.","cat3","10",0,2.4,0])
vehlist.append([koki_name+"_JRF_V19A_2","src/koki_e.2.","cat3","10",2.4,4.8,0])
vehlist.append([koki_name+"_JRF_V19A_3","src/koki_e.3.","cat3","10",4.8,7.2,0])
vehlist.append([koki_name+"_JRF_V19A_4","src/koki_e.4.","cat3","10",7.2,9.6,0])
vehlist.append([koki_name+"_JRF_V19A_5","src/koki_e.5.","cat3","10",9.6,12,0])
vehlist.append([koki_name+"_JRF_UR19A-1_1","src/koki_d.1.","cat13","10",0,2.4,0])
vehlist.append([koki_name+"_JRF_UR19A-1_2","src/koki_d.2.","cat13","10",2.4,4.8,0])
vehlist.append([koki_name+"_JRF_UR19A-1_3","src/koki_d.3.","cat13","10",4.8,7.2,0])
vehlist.append([koki_name+"_JRF_UR19A-1_4","src/koki_d.4.","cat13","10",7.2,9.6,0])
vehlist.append([koki_name+"_JRF_UR19A-1_5","src/koki_d.5.","cat13","10",9.6,12,0])
vehlist.append([koki_name+"_JRF_UR19A-2_1","src/koki_c.1.","cat12","100",0,2.4,0])
vehlist.append([koki_name+"_JRF_UR19A-2_2","src/koki_c.2.","cat12","100",2.4,4.8,0])
vehlist.append([koki_name+"_JRF_UR19A-2_3","src/koki_c.3.","cat12","100",4.8,7.2,0])
vehlist.append([koki_name+"_JRF_UR19A-2_4","src/koki_c.4.","cat12","100",7.2,9.6,0])
vehlist.append([koki_name+"_JRF_UR19A-2_5","src/koki_c.5.","cat12","100",9.6,12,0])
vehlist.append([koki_name+"_JRF_UT20A_1","src/koki_b.0.","Chemicals0","40",0,4,0])
vehlist.append([koki_name+"_JRF_UT20A_2","src/koki_b.1.","Chemicals0","40",4,8,0])
vehlist.append([koki_name+"_JRF_UT20A_4","src/koki_b.2.","Chemicals0","40",8,12,0])
vehlist.append([koki_name+"_JRF_22T6_1","src/koki_b.3.","cat7","40",0,4,0])
vehlist.append([koki_name+"_JRF_22T6_2","src/koki_b.4.","cat7","40",4,8,0])
vehlist.append([koki_name+"_JRF_22T6_4","src/koki_b.5.","cat7","40",8,12,0])
vehlist.append([koki_name+"_JRF_30D_1","src/koki_e.6.","cat3","30",0,6,0])
vehlist.append([koki_name+"_JRF_30D_3","src/koki_e.8.","cat3","30",6,12,0])
vehlist.append([koki_name+"_JRF_U51A-1_1","src/koki_a.6.","cat8","40",0,6,0])
vehlist.append([koki_name+"_JRF_U51A-1_3","src/koki_a.8.","cat8","40",6,12,0])
vehlist.append([koki_name+"_JRF_U51A-2_1","src/koki_a.6.","cat6","350",0,6,0])
vehlist.append([koki_name+"_JRF_U51A-2_3","src/koki_a.8.","cat6","350",6,12,0])
vehlist.append([koki_name+"_JRF_UF42A_1","src/koki_c.6.","cat6","350",0,6,0])
vehlist.append([koki_name+"_JRF_UF42A_3","src/koki_c.8.","cat6","350",6,12,0])


# writing dat file
#close dat file and complete!
makekoki()
output_dat.close()
output=open("output.txt","w")
output.write("pak="+koki_name+".pak\n")
output.write("dat="+filename)
output.write("ispng="+ispng)
output.close()
print("Complete making dat files!")
