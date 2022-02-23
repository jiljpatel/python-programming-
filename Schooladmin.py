#School Administration Program
import csv

def write_into_csv(info_list):
    with open('stu_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

    if csv_file.tell() == 0:  
       writer.writerow(["Name","Age","Contact_Number","E-mail"])

    writer.writerow(info_list)     


if __name__ == '__main__':
   condition = True

   while(condition):
        stu_info = input("Enter the information of students in following format (Name Age Contact_Number E-mail): ")
     

        stu_info_list = stu_info.split(' ')
        print("Entered split up information is : ",  stu_info_list)

        print("\nThe entered information is -\nName: {}\nAge:{}\nContact_Number:{}\nE-mail:{}".format(stu_info_list[0],stu_info_list[1],stu_info_list[2],stu_info_list[3]))
		

     
        choice = input(print("Is Entered information correct? (yes/no): "))
        if choice == "yes":
           write_into_csv(stu_info_list)

           condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
           if condition_check == "yes":
              condition = True
           elif condition_check == "no":
               condition = False
        elif choice =="no":
             print("\nplease re-enter the values: ")
