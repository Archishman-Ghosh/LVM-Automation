import os
import pyfiglet

#Logical Volume Creation

def lvCreation(diskName, vgName, lvName, size, dirName):
    os.system(f'pvcreate {diskName}')
    os.system(f'vgcreate {vgName} {diskName}')
    os.system(f'vgdisplay {vgName}')
    os.system(f'lvcreate --size {size} --name {lvName} {vgName}')
    os.system(f'mkfs.ext4 /dev/{vgName}/{lvName}')
    os.system(f'mount /dev/{vgName}/{lvName} {dirName}')
    os.system('lvdisplay')
    os.system('sleep 2')

#Extend the LV

def lvExtend( extDiskName, extvgName, exsize, extlvName):
    os.system(f'pvcreate {extDiskName}')
    os.system(f'vgextend {extvgName} {extDiskName}')
    os.system('sleep 1')
    os.system(f'lvextend --size {exsize} /dev/{extvgName}/{extlvName}')
    os.system(f'resize2fs /dev/{extvgName}/{extlvName}')
    os.system('sleep 2')

#Reduce the LV Size

def lvReduce(redDirName, redvgName, redlvName, size):
    os.system(f'umount {redDirName}')
    os.system(f'e2fsck -f /dev/mapper/{redvgName}-{redlvName}')
    os.system(f'resize2fs /dev/mapper/{redvgName}-{redlvName} {size}')
    os.system(f'lvreduce -L {size} /dev/mapper/{redvgName}-{redlvName} -y')
    os.system(f'mount /dev/mapper/{redvgName}-{redlvName} {redDirName}')
    os.system('sleep 2')

#Display Volumes

def display():
    os.system('df -h')
    os.system('sleep 3')

#New Screen

def clear():
    os.system('clear')

#Menu Program

while True:
    clear()
    print()
    result = pyfiglet.figlet_format("                       LVM Automation with Python\n                            -by   Archishman Ghosh", font = "digital"  )
    print(result)
    print()
    print("\n\t\t\t**********welcome to the operation menu**********\n")
    inp = input("\n\t\t\t\tType 1 : Logical Volume Creation \n\t\t\t\tType 2 : Logical Volume Extend \n\t\t\t\tType 3 : Logical Volume Reduce \n\t\t\t\tType 4 : Display Volumes \n\t\t\t\tType 0 : Exit Menu\n\n\n\n\t\t\t\tInput : ")
    if inp.strip() == "1":
        diskName = input("Enter disk name - ")
        vgName = input("Enter Volume Group name - ")
        lvName = input("Enter Logical Volume name - ")
        size = input("Enter the size for the Logical Volume - ")
        dirName = input('Enter the directory to mount the LV on -')
        lvCreation(diskName, vgName, lvName, size,  dirName)
        #clear()

    elif inp.strip() == "2":
        extDiskName = input("Enter the new disk name - ")
        extvgName = input("Enter the vg to extend - ")
        extlvName = input("Enter the lv to extend - ")
        size = input("Enter the size to extend to - ")
        lvExtend(extDiskName, extvgName, size, extlvName)
        #os.system('clear')

    elif inp.strip() == "3":
        redDirName = input("Enter the mounted directory - ")
        redvgName  = input("Enter the Volume Group name for reducing - ")
        redlvName = input("Enter the Logical Volume name for reducing - ")
        size = input("Enter the size to reduce to - ")
        lvReduce(redDirName, redvgName, redlvName, size)
        #os.system('clear')

    elif inp.strip() == "4":
        display()
        #os.system('clear')

    elif inp.strip() == "0":
        print("Thanks for Coming. Bye.\n\n")
        break

    else:
        print("Invalid Input!\n\n")
        os.system('sleep 1')
    print('\n'*15)