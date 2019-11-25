menulist = {'115':['Project Info','ProjectSettings','Project Level Replacement'],1:['Project Info','ProjectSettings','Project Level Replacement'],2:['Qdb'],3:['Additional Setting'],4:['Brands'],5:['Comms','Comms AMP','Comms_BrandFluency'],6:['Adnow','Ad Messaging','Adnow Ads','Adnow FMCG','Adnow Long term','Adnow other'],7:['CrossMedia','CrossMedia A Regions','CrossMedia B Campaign Builder','CrossMedia C Campaign'],8:['Det','Det Apps','Det DP'],9:['NeedScope','NeedScope Attributes','NeedScope Collages','NeedScope DP'],10:['Quota','Quota A Variables','Quota A Variables','Quota C Tables','Quota D Main'],11:['AgeBands'],12:['IA_TARGET_WORDS'],13:['Imagery'],14:['TBCA'],15:['Others','Connect Filter Variables','COMPETITOR BRANDS','Brands SelfCoding','Market Factors']}

for i,y in menulist.items():
    print(i ," : ", y)
print(menulist[1][0])
menulist[1][0] = "shaji"
print(menulist[1][0])
print(menulist['115'])
