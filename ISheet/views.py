from django.shortcuts import render, redirect
from django.db import models
from .models import contact
from .models import form_IS
from static.lists import *
from .forms import Form
from django.http import HttpResponse
from django.utils.translation import gettext
# Create your views here.


def Project(request):
   form = Form()
   menu = {}
   loop_times = range(1, 41)
   menulist = {1: ['Project Info', 'ProjectSettings', 'Project Level Replacement'],
               2: ['Qdb',"",""],
               3: ['Additional Setting',"",""],
               4: ['Brands',"",""],
               5: ['Comms', 'Comms AMP', 'Comms_BrandFluency'],
               6: ['Adnow', 'Ad Messaging', 'Adnow Ads', 'Adnow FMCG', 'Adnow Long term', 'Adnow other'],
               7: ['CrossMedia', 'CrossMedia A Regions', 'CrossMedia B Campaign Builder', 'CrossMedia C Campaign'],
               8: ['Det', 'Det Apps', 'Det DP'],
               9: ['NeedScope', 'NeedScope Attributes', 'NeedScope Collages', 'NeedScope DP'],
               10: ['Quota', 'Quota A Variables', 'Quota A Variables', 'Quota C Tables', 'Quota D Main'],
               11: ['AgeBands',"",""],
               12: ['IA_TARGET_WORDS',"",""],
               13: ['Imagery',"",""],
               14: ['TBCA',"",""],
               15: ['Connect Filter Variables',"",""],
               16: ['COMPETITOR BRANDS',"",""],
               17: ['Brands SelfCoding',"",""],
               18: ['Market Factors',"",""]}

   if request.method == 'POST':
      for i in range(1,19):
         print(i)
         print(request.POST.get("Val_"+str(i)))
         if request.POST.get("Val_"+str(i)) != "on":
            #del menulist[i]
            menulist[i][0]  = "XX"
            menulist[i][1] = "line-through"
         else:
            menulist[i][0]  = ""
            menulist[i][1] = ""

      print(menulist[1][0])
      print(menulist[1][1])
      print(menulist[1][2])
      print(menulist)
      return render(request, 'InputSheet.html', {'CountryList': CountryList, 'SlList': SlList, 'PlatformVal': PlatformVal,
                                           'Methodology': Methodology,
                                           'CategoryInForm': CategoryInForm, 'CategoryInDB': CategoryInDB,
                                           'brandno': brandno, 'loop_times': loop_times, 'agebands': agebands,
                                           'adfmcg': adfmcg, 'media': media, 'adother': adother, 'Numbers': Numbers,
                                           'adlongterm': adlongterm, 'form': form, 'menulist':menulist,'Val': request.POST})

   return render(request,'PrameterPage.html', {'proj_sel' : proj_sel, 'Val' : request.POST})


def MainPage(request):
   print("Request method ", request.method)
   form = Form()
   loop_times = range(1, 41)
   if request.method == 'POST':
      print('select p ', request.POST.get('pd_country'))
      print('select p ', request.POST.get('pd_Plat_methodology'))
      print(form.is_valid())
      print(form.errors)

      if form.is_valid():
         print('POST Yeah!!')
         form.save(commit=False)
         print("Request cname POST " , request.POST.get('pd_country'))
         print("Form PD country method " , request.POST.get('method'))
         print("Form PD country POST ", request.POST.get('pmethod'))
         print("Clean Ctry :" , form.cleaned_data['pd_country'])
         redirect('MainPage/')
      else:
         print("Request cname POST ", request.POST.get('pd_country'))
         print("Form PD country method " , request.POST.get('method'))
         print("Form PD country POST ", request.POST.get('pmethod'))
         p = [["1","Value undefined","ProjectDetails"],["2","Issues","QDB tabs"]]
         FormEntries = request.POST
         print("clk3 ", FormEntries.get('clk3'))
         print("clk5 ", FormEntries.get('clk5'))

         WriteToExcel(FormEntries)

         return render(request, 'error.html', {'p': p, 'form' : form , 'Val' : FormEntries })

   output = gettext("Welcome to my site.")
   print(output)
   print("Shaji")
   return render(request,'InputSheet.html',{'CountryList': CountryList, 'SlList': SlList, 'PlatformVal': PlatformVal, 'Methodology': Methodology,
                     'CategoryInForm': CategoryInForm, 'CategoryInDB': CategoryInDB,'brandno' : brandno,'loop_times': loop_times, 'agebands' : agebands,'adfmcg' : adfmcg,'media' : media,'adother' : adother,'Numbers' : Numbers, 'adlongterm' : adlongterm,'form' : form, 'Val' : request.POST})

def WriteToExcel(p):
   print('Writing out to Excel')
   from openpyxl import load_workbook
   import subprocess

   filepath = ".\static\Inputsheet_Temp.xlsx"
   wb2 = load_workbook(filepath)
   ws1 = wb2['Project Settings']
   print(p['pd_country'])
   ws1['C12'] = p['pd_country']
   ws1['C16'] = p['pmethod']
   ws1['C17'] = p['pd_Plat_methodology']
   ws1['C18'] = p['start_date']
   ws1['C19'] = p['config']
   ws1['C20'] = p['equity']
   ws1['C21'] = p['abs']
   ws1['C22'] = p['pd_sl1name']
   ws1['C23'] = p['pd_sl2name']
   ws1['C24'] = p['pd_sl3name']
   ws1['C25'] = p['pd_sl4name']
   ws1['C26'] = p['pd_sl5name']
   ws1['C30'] = p['ELL']

   ws1['C31'] = p['sdirweb']
   ws1['C32'] = p['quota']
   ws1 = wb2['Additional Project Settings']
   ws1['B22'] = p['ProjDet_addit_rout1']
   ws1['C22'] = p['ProjDet_sel1']
   ws1['D22'] = p['ProjDet_desc1']
   ws1['E22'] = p['ProjDet_filter1']
   ws1['B23'] = p['ProjDet_addit_rout2']
   ws1['C23'] = p['ProjDet_sel2']
   ws1['D23'] = p['ProjDet_desc2']
   ws1['E23'] = p['ProjDet_filter2']

   ws1 = wb2['QDB']

   for i in range(3,91):
      try:
         if p['clk'+str(i)] != "no":
            ws1['C'+str(i)] = "X"
      except:
             ws1['C' + str(i)] = " "


#for i in range(3, 91):
   #   print(p['clk']+str(i))


   wb2.save("InputSheet.xls")
   print('File written')
   subprocess.Popen(["InputSheet.xls"], shell=True)


def InputSheet(request):
   form_class = Is_Form
   if request.method == 'POST':
      form = Is_Form(request.POST)
      if form.is_valid():
         form.save(commit=False)
         print('Select P ', request.POST.get('CntryName'))
      else:
         print('nnnn ', request.POST.get('CntryName'))
         print('yyyy ', request.POST.get('form.pd_country'))
   else:
      print('Select G ', request.GET.get('CntryName'))
      print('Select G ', request.GET.get('form.pd_country'))

   return render(request,'index.html',{'CountryList': CountryList, 'SlList': SlList, 'PlatformVal': PlatformVal, 'Methodology': Methodology,
                     'CategoryInForm': CategoryInForm, 'CategoryInDB': CategoryInDB, 'brandno' : 16})


def index(request):
   return render(request,'MainLandingPage.html')


def Contacts(request):
   contact1 = contact()
   contact1.ImgName = "Dnyanesh.png"
   contact1.place = "Pune GDC - India"
   contact1.name = "Dnyaneshwar Salvi"
   contact1.passion = "I am passionate about new technologies, love to explore new places and listen to music"
   contact1.mailid = "Dnyaneshwar.Salvi@kantar.com"
   contact2 = contact()
   contact2.ImgName = "juvy.png"
   contact2.place = "Phillipines"
   contact2.name = "Juvy Sorian"
   contact2.passion = "I am passionate about singing and enjoy beaches, I am currently exploring photography and yes. I am an artist when it comes to painting"
   contact2.mailid = "Juvy.Soriano@kantar.com"

   contact3 = contact()
   contact3.ImgName = "Abhinav.png"
   contact3.place = "Bangalore - India"
   contact3.name = "Abhinav"
   contact3.passion = "I am passionate about automation and new technologies, I love to travel and watch movies"
   contact3.mailid = "Abhinav.Mathur@kantar.com"


   contact4 = contact()
   contact4.ImgName = "prabhakar.png"
   contact4.place = "Hyderabad GDC - India"
   contact4.name = "Prabhakar Murthy"
   contact4.passion = "I am interested in reading books, watching cricket. I am also passionate about working on new platforms and handling new tasks"
   contact4.mailid = "Prabhakar.Murthy@kantar.com"


   contact5 = contact()
   contact5.ImgName = "Santosh.png"
   contact5.place = "Phillipines GDC - India"
   contact5.name = "Santosh Kakade"
   contact5.passion = "I love watching movies, documentaries, writing poetry and knowing new people. Sharing and discussing ideas is also one of my hobby"
   contact5.mailid = "Santosh.Kakade@kantar.com"


   contact6 = contact()
   contact6.ImgName = "Sanjeev.png"
   contact6.place = "Pune GDC - India"
   contact6.name = "Sanjeev Jha"
   contact6.passion = "I am passionate about learning new technolgies and keep myself updated. I spend my free time singing and in social activities, and I feel proud helping needy people in the society"
   contact6.mailid = "Sanjeev.Jha@kantar.com"


   contact7 = contact()
   contact7.ImgName = "praveen.png"
   contact7.place = "Hyderabad GDC - India"
   contact7.name = "Praveen Kumar Sudarsanam"
   contact7.passion = "I like to spend time with family and friends and love watching cricket"
   contact7.mailid = "Praveenkumar.Sudarsanam@kantar.com"


   contactsall = [contact1, contact2, contact3, contact4, contact5, contact6, contact7]
   return render(request, 'contacts.html',{'contact_list':contactsall})


def Newtry(request):
   print('select p ', request.POST.get('cname'))
   if request.method == 'POST':
      form = Form(request.POST)
      print('shaji')
      print('select p ', request.POST.get('pd_country'))
      print('select pForm ',form.cleaned_data['pd_country'])
      if form.is_valid():
         form.save(commit=False)
         #form.cleaned_data['pd_plat_methodology'] = form.cleaned_data['pd_country']
         print('select p ', request.POST.get('cname'))
         print('select cntry ', form.cleaned_data['pd_country'])
         print('select method ', form.cleaned_data['pd_Plat_methodology'])
         return render(request, 'New.html',{'CountryList': CountryList,'form': form})

      else:
         print('invalid form')
         print('yyyy ', request.POST.get('pd_country'))
         print('nnnn ', request.POST.get('cname'))
         return render(request, 'New.html',{'CountryList': CountryList,'form': form})

   else:
      print('select g ', request.GET.get('cname'))
      print('select g ', request.GET.get('form.pd_country'))
      return render(request, 'New.html', {'CountryList': CountryList})
