def displayText():
    print( "Hello World")





'''
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"
if __name__=="main":
    app.run()



name=['\x1b[18;8Hr\x1b[18;9H\x1b[18;9He\x1b[18;10H\x1b[18;10Hs\x1b[18;11H\x1b[18;11He\x1b[18;12H\x1b[18;12Ht\x1b[18;13H\x1b[18;13H\r\n\x08 \x08\x1b[2J\x1b[1;1H\x1b[1;1H\x1b[25;78H98\x1b[1;1H\x1b[25;78H9D\x1b[1;1H\x1b[25;78H9A\x1b[1;1H\x1b[25;78H9C\x1b[1;1H\x1b[25;78HB4\x1b[1;1H\x1b[25;78H92\x1b[1;1H\x1b[25;78HA0\x1b[1;1H\x1b[25;78HA0\x1b[1;1H\x1b[25;78H99\x1b[1;1H\x1b[25;78H92\x1b[1;1H\x1b[25;78H92\x1b[1;1H\x1b[25;78H92\x1b[1;1H\x1b[25;78H92\x1b[1;1H\x1b[0;37;40m\x1b[2J\x1b[1;1H\x1b[1;1H\x1b[1;1HVersion 2.22.1283. Copyright (C) 2022 AMI \x1b[2;1HBIOS Date: 03/27/2022 01:15:44 Ver: 0ACOY021\x1b[3;1H\x1b[4;1H\x1b[5;1H\x1b[6;1H\x1b[7;1H\x1b[8;1H\x1b[9;1H\x1b[10;1H\x1b[11;1H\x1b[12;1H\x1b[13;1H\x1b[14;1H\x1b[15;1H\x1b[16;1H\x1b[17;1H\x1b[18;1H\x1b[19;1H\x1b[20;1H\x1b[21;1H\x1b[22;1H\x1b[23;1H\x1b[24;1H\x1b[25;1H \x1b[3;1H\x1b[3;1HEVALUATION COPY.\x1b[4;1H\x1b[4;1HPress <DEL> or <ESC> to enter setup.\x1b[5;1H\x1b[5;1HEntering Setup...\x1b[25;78HA9\x1b[5;18H\x1b[2J\x1b[1;1H\x1b[1;37;40m\x1b[2J\x1b[1;1H\x1b[1;37;44m\x1b[2J\x1b[1;1H\x1b[25;78HAB\x1b[1;1H\x1b[1;1H\x1b[1;1H Aptio Setup - AMI\x1b[2;1H\x1b[0;37;44m \x1b[0;34;47m Main \x1b[0;37;44m AdvancedPlatform ConfigurationSocket ConfigurationServer Mgmt\x10\x1b[3;1H\x1b[0;34;47mĿ\x1b[4;1H\x1b[0;30;47mBIOS Information \x1b[0;34;47m\x1e \x1b[5;1H\x1b[1;30;47mBIOS Vendor\x1b[0;34;47m\x1b[1;30;47mAmerican Megatrends\x1b[0;34;47m ', ' \x1b[6;1H\x1b[1;30;47mCore Version\x1b[0;34;47m \x1b[1;30;47m5.25\x1b[0;34;47m', ' \x1b[7;1H\x1b[1;30;47mCompliancy\x1b[0;34;47m \x1b[1;30;47mUEFI 2.8; PI 1.7\x1b[0;34;47m', ' \x1b[8;1H\x1b[1;30;47mProject Version\x1b[0;34;47m\x1b[1;30;47m0ACOY 0.21 x64\x1b[0;34;47m', ' \x1b[9;1H\x1b[1;30;47mBuild Date and Time\x1b[0;34;47m\x1b[1;30;47m03/27/2022 01:15:44\x1b[0;34;47m ', ' \x1b[10;1H\x1b[1;30;47mAccess Level\x1b[0;34;47m \x1b[1;30;47mAdministrator\x1b[0;34;47m ', ' \x1b[11;1H ', ' \x1b[12;1H\x1b[0;30;47mPlatform Information \x1b[0;34;47m', ' \x1b[13;1H\x1b[1;30;47mPlatform\x1b[0;34;47m \x1b[1;30;47mServerSocIdaville\x1b[0;34;47m ', 'ĳ\x1b[14;1H\x1b[1;30;47mProcessor\x1b[0;34;47m\x1b[1;30;47m606C1 - ICX-D B0\x1b[0;34;47m', '><: Select Screen\x1b[15;1H\x1b[1;30;47mPCH\x1b[0;34;47m\x1b[1;30;47mCDF SKU - B1\x1b[0;34;47m', '\x18\x19: Select Item\x1b[16;1H\x1b[1;30;47mRC Revision\x1b[0;34;47m\x1b[1;30;47m21.D09\x1b[0;34;47m', 'Enter: Select\x1b[17;1H\x1b[1;30;47mBIOS ACM \x1b[0;34;47m\x1b[1;30;47m0.9.8\x1b[0;34;47m ', '+/-: Change Opt. \x1b[18;1H\x1b[1;30;47mSINIT ACM \x1b[0;34;47m \x1b[1;30;47m0.9.8\x1b[0;34;47m F1: General Help \x1b[19;1H F2: Previous Values\x1b[20;1H\x1b[0;30;47mMemory Information \x1b[0;34;47mF3: Optimized Defaults \x1b[21;1H\x1b[1;30;47mTotal Memory\x1b[0;34;47m \x1b[1;30;47m32768 MB \x1b[0;34;47m \x1fF4: Save & Exit\x1b[22;1HESC: Exit\x1b[23;1H\x1b[24;1H\x1b[0;37;44mVersion 2.22.1283 Copyright (C) 2022 AMI ']
for line in name:
    name=line.replace('  ','')
    print(name)

    name_list = name
    print("name_list: ", name_list)
    BIOS_Information = name_list.index("BIOS Information")
    print("index of Core Version is: ", BIOS_Information)
    print("Name=", name_list[(BIOS_Information + 70 )])
    '''


