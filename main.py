# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:13:13 2021

@author: go951
"""
import twstock
#導入 Discord.py
import discord
# import asyncio
import nest_asyncio
import asyncio
import keep_alive
import os
from dotenv import load_dotenv



nest_asyncio.apply()
client = discord.Client()

@client.event
async def on_message(message): 
    
    if message.content == '開始記錄':
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        for i in range(24,0,-1):
            await message.channel.send('大家好，我是垃圾機器人，目前距離測試結束還有{}小時'.format(i))
            
            await asyncio.sleep(3600)
            #await tmpmsg.delete()
         #停頓3秒
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('-s'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])   
       #刪除使用者訊息並覆誦
    if message.content.startswith('-d'):
        await message.delete()
        tmp = message.content.split(" ",2)
        
      #如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:        
            
            await message.channel.send(tmp[1])    




    
    if message.content.startswith == '-t':
          await message.channel.send("請問要查詢哪支股票? -t空一格+上公司代碼即可查詢!")    
    elif message.content == '-t 2330': 
          realdata2330 =twstock.realtime.get('2330')   #台GG
          if realdata2330['success']:  
              realprice2330 = realdata2330['realtime']['latest_trade_price']  #目前股價    #台GG的即時資料
              await message.channel.send('台GG目前股價：' + realprice2330)
    
    elif message.content == '-t 2409':     
          realdata2409 =twstock.realtime.get('2409')  #友達 
          if realdata2409['success']:  
              realprice2409 = realdata2409['realtime']['latest_trade_price']
              await message.channel.send('友達目前股價：' + realprice2409)
    
    elif message.content == '-t 2603':      
          realdata2603 =twstock.realtime.get('2603')  #長榮
          if realdata2603['success']:  
              realprice2603 = realdata2603['realtime']['latest_trade_price']#目前股價
              await message.channel.send('長榮目前股價：' + realprice2603)
         
    elif message.content == '-t 2303':          
          realdata2303 =twstock.realtime.get('2303')  #聯電
          if realdata2303['success']:  
              realprice2303 = realdata2303['realtime']['latest_trade_price']  
              await message.channel.send('聯電目前股價：' + realprice2303)
    
    elif message.content == '-t 2609':        
         realdata2609 =twstock.realtime.get('2609')  #陽明
         if realdata2609['success']:     
              realprice2609 = realdata2609['realtime']['latest_trade_price'] 
              await message.channel.send('陽明目前股價：' + realprice2609)
    
    elif message.content == '-t 1101':    
         realdata1101 =twstock.realtime.get('1101')  
         if realdata1101['success']:     
              realprice1101 = realdata1101['realtime']['latest_trade_price'] 
              await message.channel.send('台泥目前股價：' + realprice1101)      
    
    elif message.content == '-t 1102':   
         realdata1102 =twstock.realtime.get('1102')  
         if realdata1102['success']:     
              realprice1102 = realdata1102['realtime']['latest_trade_price'] 
              await message.channel.send('亞泥目前股價：' + realprice1102)
    
    elif message.content == '-t 1103':        
         realdata1103 =twstock.realtime.get('1103')  
         if realdata1103['success']:     
              realprice1103 = realdata1103['realtime']['latest_trade_price'] 
              await message.channel.send('嘉泥目前股價：' + realprice1103)
   
    elif message.content == '-t 1104':        
         realdata1104 =twstock.realtime.get('1104')  
         if realdata1104['success']:     
              realprice1104 = realdata1104['realtime']['latest_trade_price'] 
              await message.channel.send('環泥目前股價：' + realprice1104)   
    
    elif message.content == '-t 1108':   
         realdata1108 =twstock.realtime.get('1108')  
         if realdata1108['success']:     
              realprice1108 = realdata1108['realtime']['latest_trade_price'] 
              await message.channel.send('幸福目前股價：' + realprice1108)                           

    elif message.content == '-t 1109': 
         realdata1109 =twstock.realtime.get('1109')  
         if realdata1109['success']:     
              realprice1109 = realdata1109['realtime']['latest_trade_price'] 
              await message.channel.send('信大目前股價：' + realprice1109)           

    elif message.content == '-t 1110': 
         realdata1110 =twstock.realtime.get('1110')  
         if realdata1110['success']:     
              realprice1110 = realdata1110['realtime']['latest_trade_price'] 
              await message.channel.send('東泥目前股價：' + realprice1110)          
             
    elif message.content == '-t 1201': 
         realdata1201 =twstock.realtime.get('1201')  
         if realdata1201['success']:     
              realprice1201 = realdata1201['realtime']['latest_trade_price'] 
              await message.channel.send('味全目前股價：' + realprice1201)               
              
    elif message.content == '-t 1203': 
         realdata1203 =twstock.realtime.get('1203')  
         if realdata1203['success']:     
              realprice1203 = realdata1203['realtime']['latest_trade_price'] 
              await message.channel.send('味王目前股價：' + realprice1203)                    
              
    elif message.content == '-t 1210': 
         realdata1210 =twstock.realtime.get('1210')  
         if realdata1210['success']:     
              realprice1210 = realdata1210['realtime']['latest_trade_price'] 
              await message.channel.send('大成目前股價：' + realprice1210)                
                           
    elif message.content == '-t 1213': 
         realdata1213 =twstock.realtime.get('1213')  
         if realdata1213['success']:     
              realprice1213 = realdata1213['realtime']['latest_trade_price'] 
              await message.channel.send('大飲目前股價：' + realprice1213)               
       
    elif message.content == '-t 1215': 
         realdata1215 =twstock.realtime.get('1215')  
         if realdata1215['success']:     
              realprice1215 = realdata1215['realtime']['latest_trade_price'] 
              await message.channel.send('卜蜂目前股價：' + realprice1215)    
    
    elif message.content == '-t 1216': 
         realdata1216 =twstock.realtime.get('1216')  
         if realdata1216['success']:     
              realprice1216 = realdata1216['realtime']['latest_trade_price'] 
              await message.channel.send('統一目前股價：' + realprice1216)        
    
    elif message.content == '-t 1217': 
         realdata1217 =twstock.realtime.get('1217')  
         if realdata1217['success']:     
              realprice1217 = realdata1217['realtime']['latest_trade_price'] 
              await message.channel.send('愛之味目前股價：' + realprice1217)      
    
    elif message.content == '-t 1218': 
         realdata1218 =twstock.realtime.get('1218')  
         if realdata1218['success']:     
              realprice1218 = realdata1218['realtime']['latest_trade_price'] 
              await message.channel.send('泰山目前股價：' + realprice1218)       #第15個
              
    elif message.content == '-t 1219': 
         realdata1219 =twstock.realtime.get('1219')  
         if realdata1219['success']:     
              realprice1219 = realdata1219['realtime']['latest_trade_price'] 
              await message.channel.send('福壽目前股價：' + realprice1219)             
    
    
    elif message.content == '-t 1220': 
         realdata1220 =twstock.realtime.get('1220')  
         if realdata1220['success']:     
              realprice1220 = realdata1220['realtime']['latest_trade_price'] 
              await message.channel.send('台榮目前股價：' + realprice1220)            
    
    elif message.content == '-t 1225': 
         realdata1225 =twstock.realtime.get('1225')  
         if realdata1225['success']:     
              realprice1225 = realdata1225['realtime']['latest_trade_price'] 
              await message.channel.send('福懋油目前股價：' + realprice1225)           

    elif message.content == '-t 1227': 
         realdata1227 =twstock.realtime.get('1227')  
         if realdata1227['success']:     
              realprice1227 = realdata1227['realtime']['latest_trade_price'] 
              await message.channel.send('佳格目前股價：' + realprice1227)           

    elif message.content == '-t 1229': 
         realdata1229 =twstock.realtime.get('1229')  
         if realdata1229['success']:     
              realprice1229 = realdata1229['realtime']['latest_trade_price'] 
              await message.channel.send('聯華目前股價：' + realprice1229)           

    elif message.content == '-t 1231': 
         realdata1231 =twstock.realtime.get('1231')  
         if realdata1231['success']:     
              realprice1231 = realdata1231['realtime']['latest_trade_price'] 
              await message.channel.send('聯華食目前股價：' + realprice1231)       #21    

    elif message.content == '-t 1232': 
         realdata1232 =twstock.realtime.get('1232')  
         if realdata1232['success']:     
              realprice1232 = realdata1232['realtime']['latest_trade_price'] 
              await message.channel.send('大統益目前股價：' + realprice1232)    

    elif message.content == '-t 1233': 
         realdata1233 =twstock.realtime.get('1233')  
         if realdata1233['success']:     
              realprice1233 = realdata1233['realtime']['latest_trade_price'] 
              await message.channel.send('天仁目前股價：' + realprice1233)    

    elif message.content == '-t 1234': 
         realdata1234 =twstock.realtime.get('1234')  
         if realdata1234['success']:     
              realprice1234 = realdata1234['realtime']['latest_trade_price'] 
              await message.channel.send('黑松目前股價：' + realprice1234)    

    elif message.content == '-t 1235': 
         realdata1235 =twstock.realtime.get('1235')  
         if realdata1235['success']:     
              realprice1235 = realdata1235['realtime']['latest_trade_price'] 
              await message.channel.send('興泰目前股價：' + realprice1235)  

    elif message.content == '-t 1236': 
         realdata1236 =twstock.realtime.get('1236')  
         if realdata1236['success']:     
              realprice1236 = realdata1236['realtime']['latest_trade_price'] 
              await message.channel.send('宏亞目前股價：' + realprice1236)  
             
    elif message.content == '-t 1256': 
         realdata1256 =twstock.realtime.get('1256')  
         if realdata1256['success']:     
              realprice1256 = realdata1256['realtime']['latest_trade_price'] 
              await message.channel.send('鮮活果汁-KY目前股價：' + realprice1256)  

    elif message.content == '-t 1301': 
         realdata1301 =twstock.realtime.get('1301')  
         if realdata1301['success']:     
              realprice1301 = realdata1301['realtime']['latest_trade_price']    
              await message.channel.send('台塑目前股價：' + realprice1301)  

    elif message.content == '-t 1303': 
         realdata1303 =twstock.realtime.get('1303')  
         if realdata1303['success']:     
              realprice1303 = realdata1303['realtime']['latest_trade_price']    
              await message.channel.send('南亞目前股價：' + realprice1303)  

    elif message.content == '-t 1304': 
         realdata1304 =twstock.realtime.get('1304')  
         if realdata1304['success']:     
              realprice1304 = realdata1304['realtime']['latest_trade_price']    
              await message.channel.send('台聚目前股價：' + realprice1304)       #30

    elif message.content == '-t 1305': 
         realdata1305 =twstock.realtime.get('1305')  
         if realdata1305['success']:     
              realprice1305 = realdata1305['realtime']['latest_trade_price']    
              await message.channel.send('華夏目前股價：' + realprice1305)       

    elif message.content == '-t 1307': 
         realdata1307 =twstock.realtime.get('1307')  
         if realdata1307['success']:     
              realprice1307 = realdata1307['realtime']['latest_trade_price']    
              await message.channel.send('三芳目前股價：' + realprice1307)   
              
    elif message.content == '-t 1308': 
         realdata1308 =twstock.realtime.get('1308')  
         if realdata1308['success']:     
              realprice1308 = realdata1308['realtime']['latest_trade_price']    
              await message.channel.send('亞聚目前股價：' + realprice1308)  
              
    elif message.content == '-t 1309': 
         realdata1309 =twstock.realtime.get('1309')  
         if realdata1309['success']:     
              realprice1309 = realdata1309['realtime']['latest_trade_price']    
              await message.channel.send('台達化目前股價：' + realprice1309)       

    elif message.content == '-t 1310': 
         realdata1310 =twstock.realtime.get('1310')  
         if realdata1310['success']:     
              realprice1310 = realdata1310['realtime']['latest_trade_price']    
              await message.channel.send('台苯目前股價：' + realprice1310)       #35

    elif message.content == '-t 1312': 
         realdata1312 =twstock.realtime.get('1312')  
         if realdata1312['success']:     
              realprice1312 = realdata1312['realtime']['latest_trade_price']    
              await message.channel.send('國喬目前股價：' + realprice1312)    

    elif message.content == '-t 1313': 
         realdata1313 =twstock.realtime.get('1313')  
         if realdata1313['success']:     
              realprice1313 = realdata1313['realtime']['latest_trade_price']    
              await message.channel.send('聯成目前股價：' + realprice1313)

    elif message.content == '-t 1314': 
         realdata1314 =twstock.realtime.get('1314')  
         if realdata1314['success']:     
              realprice1314 = realdata1314['realtime']['latest_trade_price']    
              await message.channel.send('中石化目前股價：' + realprice1314)

    elif message.content == '-t 1315': 
         realdata1315 =twstock.realtime.get('1315')  
         if realdata1315['success']:     
              realprice1315 = realdata1315['realtime']['latest_trade_price']    
              await message.channel.send('達新目前股價：' + realprice1315)                

    elif message.content == '-t 1316': 
         realdata1316 =twstock.realtime.get('1316')  
         if realdata1316['success']:     
              realprice1316 = realdata1316['realtime']['latest_trade_price']    
              await message.channel.send('上曜目前股價：' + realprice1316) 

    elif message.content == '-t 1319': 
         realdata1319 =twstock.realtime.get('1316')  
         if realdata1319['success']:     
              realprice1319 = realdata1319['realtime']['latest_trade_price']    
              await message.channel.send('東陽目前股價：' + realprice1319) 

    elif message.content == '-t 1321': 
         realdata1321 =twstock.realtime.get('1321')  
         if realdata1321['success']:     
              realprice1321 = realdata1321['realtime']['latest_trade_price']    
              await message.channel.send('大洋目前股價：' + realprice1321) 

    elif message.content == '-t 1323': 
         realdata1323 =twstock.realtime.get('1323')  
         if realdata1323['success']:     
              realprice1323 = realdata1323['realtime']['latest_trade_price']    
              await message.channel.send('永裕目前股價：' + realprice1323) 

    elif message.content == '-t 1324': 
         realdata1324 =twstock.realtime.get('1324')  
         if realdata1324['success']:     
              realprice1324 = realdata1324['realtime']['latest_trade_price']    
              await message.channel.send('地球目前股價：' + realprice1324) 

    elif message.content == '-t 1325': 
         realdata1325 =twstock.realtime.get('1324')  
         if realdata1325['success']:     
              realprice1325 = realdata1325['realtime']['latest_trade_price']    
              await message.channel.send('恆大目前股價：' + realprice1325)

    elif message.content == '-t 1326': 
         realdata1326 =twstock.realtime.get('1326')  
         if realdata1326['success']:     
              realprice1326 = realdata1326['realtime']['latest_trade_price']    
              await message.channel.send('台化目前股價：' + realprice1326)

    elif message.content == '-t 1337': 
         realdata1337 =twstock.realtime.get('1337')  
         if realdata1337['success']:     
              realprice1337 = realdata1337['realtime']['latest_trade_price']    
              await message.channel.send('再生-KY目前股價：' + realprice1337)

    elif message.content == '-t 1338': 
         realdata1338 =twstock.realtime.get('1338')  
         if realdata1338['success']:     
              realprice1338 = realdata1338['realtime']['latest_trade_price']    
              await message.channel.send('廣華-KY目前股價：' + realprice1338)
    elif message.content == '-t 1339': 
         realdata1339 =twstock.realtime.get('1339')  
         if realdata1339['success']:     
              realprice1339 = realdata1339['realtime']['latest_trade_price']    
              await message.channel.send('昭輝目前股價：' + realprice1339)            

    elif message.content == '-t 1340': 
         realdata1340 =twstock.realtime.get('1340')  
         if realdata1340['success']:     
              realprice1340 = realdata1340['realtime']['latest_trade_price']    
              await message.channel.send('勝悅-KY目前股價：' + realprice1340)    #50

    elif message.content == '-t 1341': 
         realdata1341 =twstock.realtime.get('1341')  
         if realdata1341['success']:     
              realprice1341 = realdata1341['realtime']['latest_trade_price']    
              await message.channel.send('富林-KY目前股價：' + realprice1341) 

    elif message.content == '-t 1402': 
         realdata1402 =twstock.realtime.get('1402')  
         if realdata1402['success']:     
              realprice1402 = realdata1402['realtime']['latest_trade_price']    
              await message.channel.send('遠東新目前股價：' + realprice1402)
              
    elif message.content == '-t 1409': 
         realdata1409 =twstock.realtime.get('1409')  
         if realdata1409['success']:     
              realprice1409 = realdata1409['realtime']['latest_trade_price']    
              await message.channel.send('新纖目前股價：' + realprice1409)

    elif message.content == '-t 1410': 
         realdata1410 =twstock.realtime.get('1410')  
         if realdata1410['success']:     
              realprice1410 = realdata1410['realtime']['latest_trade_price']    
              await message.channel.send('南染目前股價：' + realprice1410)
              
    elif message.content == '-t 1413': 
         realdata1413 =twstock.realtime.get('1413')  
         if realdata1413['success']:     
              realprice1413 = realdata1413['realtime']['latest_trade_price']    
              await message.channel.send('宏洲目前股價：' + realprice1413)
              
    elif message.content == '-t 1414': 
         realdata1414 =twstock.realtime.get('1414')  
         if realdata1414['success']:     
              realprice1414 = realdata1414['realtime']['latest_trade_price']    
              await message.channel.send('東和目前股價：' + realprice1414)
              
    elif message.content == '-t 1416': 
         realdata1416 =twstock.realtime.get('1416')  
         if realdata1416['success']:     
              realprice1416 = realdata1416['realtime']['latest_trade_price']    
              await message.channel.send('廣豐目前股價：' + realprice1416)
              
    elif message.content == '-t 1417': 
         realdata1417 =twstock.realtime.get('1417')  
         if realdata1417['success']:     
              realprice1417 = realdata1417['realtime']['latest_trade_price']    
              await message.channel.send('嘉裕目前股價：' + realprice1417)

    elif message.content == '-t 1418': 
         realdata1418 =twstock.realtime.get('1418')  
         if realdata1418['success']:     
              realprice1418 = realdata1418['realtime']['latest_trade_price']    
              await message.channel.send('東華目前股價：' + realprice1418)       #60

    elif message.content == '-t 1419': 
         realdata1419 =twstock.realtime.get('1419')  
         if realdata1419['success']:     
              realprice1419 = realdata1419['realtime']['latest_trade_price']    
              await message.channel.send('新紡目前股價：' + realprice1419) 

    elif message.content == '-t 1423': 
         realdata1423 =twstock.realtime.get('1423')  
         if realdata1423['success']:     
              realprice1423 = realdata1423['realtime']['latest_trade_price']    
              await message.channel.send('利華目前股價：' + realprice1423)
              
    elif message.content == '-t 1432': 
         realdata1432 =twstock.realtime.get('1432')  
         if realdata1432['success']:     
              realprice1432 = realdata1432['realtime']['latest_trade_price']    
              await message.channel.send('大魯閣目前股價：' + realprice1432)

    elif message.content == '-t 1434': 
         realdata1434 =twstock.realtime.get('1434')  
         if realdata1434['success']:     
              realprice1434 = realdata1434['realtime']['latest_trade_price']    
              await message.channel.send('福懋目前股價：' + realprice1434)

    elif message.content == '-t 1435': 
         realdata1435 =twstock.realtime.get('1435')  
         if realdata1435['success']:     
              realprice1435 = realdata1435['realtime']['latest_trade_price']    
              await message.channel.send('中福目前股價：' + realprice1435)

    elif message.content == '-t 1436': 
         realdata1436 =twstock.realtime.get('1436')  
         if realdata1436['success']:     
              realprice1436 = realdata1436['realtime']['latest_trade_price']    
              await message.channel.send('華友聯目前股價：' + realprice1436)

    elif message.content == '-t 1437': 
         realdata1437 =twstock.realtime.get('1437')  
         if realdata1437['success']:     
              realprice1437 = realdata1437['realtime']['latest_trade_price']    
              await message.channel.send('勤益控目前股價：' + realprice1437)

    elif message.content == '-t 1438': 
         realdata1438 =twstock.realtime.get('1438')  
         if realdata1438['success']:     
              realprice1438 = realdata1438['realtime']['latest_trade_price']    
              await message.channel.send('三地開發目前股價：' + realprice1438)

    elif message.content == '-t 1439': 
         realdata1439 =twstock.realtime.get('1439')  
         if realdata1439['success']:     
              realprice1439 = realdata1439['realtime']['latest_trade_price']    
              await message.channel.send('中和目前股價：' + realprice1439)

    elif message.content == '-t 1440': 
         realdata1440 =twstock.realtime.get('1440')  
         if realdata1440['success']:     
              realprice1440 = realdata1440['realtime']['latest_trade_price']    
              await message.channel.send('南紡目前股價：' + realprice1440)

    elif message.content == '-t 1441': 
         realdata1441 =twstock.realtime.get('1441')  
         if realdata1441['success']:     
              realprice1441 = realdata1441['realtime']['latest_trade_price']    
              await message.channel.send('大東目前股價：' + realprice1441)

    elif message.content == '-t 1442': 
         realdata1442 =twstock.realtime.get('1442')  
         if realdata1442['success']:     
              realprice1442 = realdata1442['realtime']['latest_trade_price']    
              await message.channel.send('名軒目前股價：' + realprice1442)

    elif message.content == '-t 1443': 
         realdata1443 =twstock.realtime.get('1443')  
         if realdata1443['success']:     
              realprice1443 = realdata1443['realtime']['latest_trade_price']    
              await message.channel.send('立益目前股價：' + realprice1443)

    elif message.content == '-t 1444': 
         realdata1444 =twstock.realtime.get('1444')  
         if realdata1444['success']:     
              realprice1444 = realdata1444['realtime']['latest_trade_price']    
              await message.channel.send('力麗目前股價：' + realprice1444)

    elif message.content == '-t 1445': 
         realdata1445=twstock.realtime.get('1445')  
         if realdata1445['success']:     
              realprice1445 = realdata1445['realtime']['latest_trade_price']    
              await message.channel.send('大宇目前股價：' + realprice1445)

    elif message.content == '-t 1446': 
         realdata1446=twstock.realtime.get('1446')  
         if realdata1446['success']:     
              realprice1446 = realdata1446['realtime']['latest_trade_price']    
              await message.channel.send('宏和目前股價：' + realprice1446)

    elif message.content == '-t 1447': 
         realdata1447=twstock.realtime.get('1447')  
         if realdata1447['success']:     
              realprice1447 = realdata1447['realtime']['latest_trade_price']    
              await message.channel.send('力鵬目前股價：' + realprice1447)

    elif message.content == '-t 1449': 
         realdata1449=twstock.realtime.get('1449')  
         if realdata1449['success']:     
              realprice1449 = realdata1449['realtime']['latest_trade_price']    
              await message.channel.send('佳和目前股價：' + realprice1449)

    elif message.content == '-t 1451': 
         realdata1451=twstock.realtime.get('1451')  
         if realdata1451['success']:     
              realprice1451 = realdata1451['realtime']['latest_trade_price']    
              await message.channel.send('年興目前股價：' + realprice1451)

    elif message.content == '-t 1452': 
         realdata1452=twstock.realtime.get('1452')  
         if realdata1452['success']:     
              realprice1452 = realdata1452['realtime']['latest_trade_price']    
              await message.channel.send('宏益目前股價：' + realprice1452)       #80

    elif message.content == '-t 1453': 
         realdata1453=twstock.realtime.get('1453')  
         if realdata1453['success']:     
              realprice1453 = realdata1453['realtime']['latest_trade_price']    
              await message.channel.send('大將目前股價：' + realprice1453)    

    elif message.content == '-t 1454': 
         realdata1454=twstock.realtime.get('1454')  
         if realdata1454['success']:     
              realprice1454 = realdata1454['realtime']['latest_trade_price']    
              await message.channel.send('台富目前股價：' + realprice1454)

    elif message.content == '-t 1455': 
         realdata1455=twstock.realtime.get('1455')  
         if realdata1455['success']:     
              realprice1455 = realdata1455['realtime']['latest_trade_price']    
              await message.channel.send('集盛目前股價：' + realprice1455)

    elif message.content == '-t 1456': 
         realdata1456=twstock.realtime.get('1456')  
         if realdata1456['success']:     
              realprice1456 = realdata1456['realtime']['latest_trade_price']    #84
              await message.channel.send('怡華目前股價：' + realprice1456)
              
    elif message.content == '-t 1457': 
         realdata1457=twstock.realtime.get('1457')  
         if realdata1457['success']:     
              realprice1457 = realdata1457['realtime']['latest_trade_price']    #85
              await message.channel.send('宜進目前股價：' + realprice1457)    
              
    elif message.content == '-t 1459': 
         realdata1459=twstock.realtime.get('1459')  
         if realdata1459['success']:     
              realprice1459 = realdata1459['realtime']['latest_trade_price']    
              await message.channel.send('聯發目前股價：' + realprice1459)     
              
    elif message.content == '-t 1460': 
         realdata1460=twstock.realtime.get('1460')  
         if realdata1460['success']:     
              realprice1460 = realdata1460['realtime']['latest_trade_price']    
              await message.channel.send('宏遠目前股價：' + realprice1460)  
              
    elif message.content == '-t 1463': 
         realdata1463=twstock.realtime.get('1463')  
         if realdata1463['success']:     
              realprice1463 = realdata1463['realtime']['latest_trade_price']    
              await message.channel.send('強盛目前股價：' + realprice1463)  
              
    elif message.content == '-t 1464': 
         realdata1464=twstock.realtime.get('1464')  
         if realdata1464['success']:     
              realprice1464 = realdata1464['realtime']['latest_trade_price']    
              await message.channel.send('得力目前股價：' + realprice1464) 
              
    elif message.content == '-t 1465': 
         realdata1465=twstock.realtime.get('1465')  
         if realdata1465['success']:     
              realprice1465 = realdata1465['realtime']['latest_trade_price']    
              await message.channel.send('偉全目前股價：' + realprice1465) 
              
    elif message.content == '-t 1466': 
         realdata1466=twstock.realtime.get('1466')  
         if realdata1466['success']:     
              realprice1466= realdata1466['realtime']['latest_trade_price']              
              await message.channel.send('聚隆目前股價：' + realprice1466) 
              
    elif message.content == '-t 1467': 
         realdata1467=twstock.realtime.get('1467')  
         if realdata1467['success']:     
              realprice1467 = realdata1467['realtime']['latest_trade_price']              
              await message.channel.send('南緯目前股價：' + realprice1467) 
              
    elif message.content == '-t 1468': 
         realdata1468=twstock.realtime.get('1468')  
         if realdata1468['success']:     
              realprice1468 = realdata1468['realtime']['latest_trade_price']             
              await message.channel.send('昶和目前股價：' + realprice1468) 
              
    elif message.content == '-t 1470': 
         realdata1470=twstock.realtime.get('1470')  
         if realdata1470['success']:     
              realprice1470 = realdata1470['realtime']['latest_trade_price']             
              await message.channel.send('大統新創目前股價：' + realprice1470) 
            
    elif message.content == '-t 1471': 
         realdata1471=twstock.realtime.get('1471')  
         if realdata1471['success']:     
              realprice1471 = realdata1471['realtime']['latest_trade_price']             
              await message.channel.send('首利目前股價：' + realprice1471) 

    elif message.content == '-t 1472': 
         realdata1472=twstock.realtime.get('1472')  
         if realdata1472['success']:     
              realprice1472 = realdata1472['realtime']['latest_trade_price']              
              await message.channel.send('三洋實業目前股價：' + realprice1472) 
            
    elif message.content == '-t 1473': 
         realdata1473=twstock.realtime.get('1473')  
         if realdata1473['success']:     
              realprice1473 = realdata1473['realtime']['latest_trade_price']             
              await message.channel.send('台南目前股價：' + realprice1473)  
              
    elif message.content == '-t 1474': 
         realdata1474=twstock.realtime.get('1474')  
         if realdata1474['success']:     
              realprice1474 = realdata1474['realtime']['latest_trade_price']                     
              await message.channel.send('弘裕目前股價：' + realprice1474)   
              
    elif message.content == '-t 1475': 
         realdata1475=twstock.realtime.get('1475')  
         if realdata1475['success']:     
              realprice1475 = realdata1475['realtime']['latest_trade_price']                     
              await message.channel.send('業旺目前股價：' + realprice1475) 

    elif message.content == '-t 1476': 
         realdata1476=twstock.realtime.get('1476')  
         if realdata1476['success']:     
              realprice1476 = realdata1476['realtime']['latest_trade_price']        #100            
              await message.channel.send('儒鴻目前股價：' + realprice1476)           

    elif message.content == '-t 1477': 
         realdata1477=twstock.realtime.get('1477')  
         if realdata1477['success']:     
              realprice1477 = realdata1477['realtime']['latest_trade_price']                    
              await message.channel.send('聚陽目前股價：' + realprice1477) 

    elif message.content == '-t 1503': 
         realdata1503=twstock.realtime.get('1503')  
         if realdata1503['success']:     
              realprice1503 = realdata1503['realtime']['latest_trade_price']                    
              await message.channel.send('士電目前股價：' + realprice1503) 

    elif message.content == '-t 1504': 
         realdata1504=twstock.realtime.get('1504')  
         if realdata1504['success']:     
              realprice1504 = realdata1504['realtime']['latest_trade_price']                
              await message.channel.send('東元目前股價：' + realprice1504) 

    elif message.content == '-t 1506': 
         realdata1506=twstock.realtime.get('1506')  
         if realdata1506['success']:     
              realprice1506 = realdata1506['realtime']['latest_trade_price']                     
              await message.channel.send('正道目前股價：' + realprice1506) 

    elif message.content == '-t 1507': 
         realdata1507=twstock.realtime.get('1507')  
         if realdata1507['success']:     
              realprice1507 = realdata1507['realtime']['latest_trade_price']                      
              await message.channel.send('永大目前股價：' + realprice1507) 

    elif message.content == '-t 1512': 
         realdata1512=twstock.realtime.get('1512')  
         if realdata1512['success']:     
              realprice1512 = realdata1512['realtime']['latest_trade_price']                    
              await message.channel.send('瑞利目前股價：' + realprice1512) 

    elif message.content == '-t 1513': 
         realdata1513=twstock.realtime.get('1513')  
         if realdata1513['success']:     
              realprice1513 = realdata1513['realtime']['latest_trade_price']                    
              await message.channel.send('中興電目前股價：' + realprice1513) 

    elif message.content == '-t 1514': 
         realdata1514=twstock.realtime.get('1514')  
         if realdata1514['success']:     
              realprice1514 = realdata1514['realtime']['latest_trade_price']                   
              await message.channel.send('亞力目前股價：' + realprice1514) 

    elif message.content == '-t 1515': 
         realdata1515=twstock.realtime.get('1515')  
         if realdata1515['success']:     
              realprice1515 = realdata1515['realtime']['latest_trade_price']                     
              await message.channel.send('力山目前股價：' + realprice1515) 

    elif message.content == '-t 1516': 
         realdata1516=twstock.realtime.get('1516')  
         if realdata1516['success']:     
              realprice1516 = realdata1516['realtime']['latest_trade_price']                   
              await message.channel.send('川飛目前股價：' + realprice1516) 

    elif message.content == '-t 1517': 
         realdata1517=twstock.realtime.get('1517')  
         if realdata1517['success']:     
              realprice1517 = realdata1517['realtime']['latest_trade_price']                      
              await message.channel.send('利奇目前股價：' + realprice1517) 

    elif message.content == '-t 1519': 
         realdata1519=twstock.realtime.get('1519')  
         if realdata1519['success']:     
              realprice1519 = realdata1519['realtime']['latest_trade_price']                    
              await message.channel.send('華城目前股價：' + realprice1519) 

    elif message.content == '-t 1521': 
         realdata1521=twstock.realtime.get('1521')  
         if realdata1521['success']:     
              realprice1521 = realdata1521['realtime']['latest_trade_price']                      
              await message.channel.send('大億目前股價：' + realprice1521) 

    elif message.content == '-t 1522': 
         realdata1522=twstock.realtime.get('1522')  
         if realdata1522['success']:     
              realprice1522 = realdata1522['realtime']['latest_trade_price']                    
              await message.channel.send('堤維西目前股價：' + realprice1522) 

    elif message.content == '-t 1524': 
         realdata1524=twstock.realtime.get('1524')  
         if realdata1524['success']:     
              realprice1524 = realdata1524['realtime']['latest_trade_price']                      
              await message.channel.send('耿鼎目前股價：' + realprice1524) 

    elif message.content == '-t 1525': 
         realdata1525=twstock.realtime.get('1525')  
         if realdata1525['success']:     
              realprice1525 = realdata1525['realtime']['latest_trade_price']                     
              await message.channel.send('江申目前股價：' + realprice1525) 

    elif message.content == '-t 1526': 
         realdata1526=twstock.realtime.get('1526')  
         if realdata1526['success']:     
              realprice1526 = realdata1526['realtime']['latest_trade_price']                    
              await message.channel.send('日馳目前股價：' + realprice1526) 

    elif message.content == '-t 1527': 
         realdata1527=twstock.realtime.get('1527')  
         if realdata1527['success']:     
              realprice1527 = realdata1527['realtime']['latest_trade_price']                    
              await message.channel.send('鑽全目前股價：' + realprice1527) 

    elif message.content == '-t 1528': 
         realdata1528=twstock.realtime.get('1528')  
         if realdata1528['success']:     
              realprice1528 = realdata1528['realtime']['latest_trade_price']                    
              await message.channel.send('恩德目前股價：' + realprice1528) 

    elif message.content == '-t 1529': 
         realdata1529=twstock.realtime.get('1529')  
         if realdata1529['success']:     
              realprice1529 = realdata1529['realtime']['latest_trade_price']     #120            
              await message.channel.send('樂士目前股價：' + realprice1529) 

    elif message.content == '-t 1530': 
         realdata1530=twstock.realtime.get('1530')  
         if realdata1530['success']:     
              realprice1530 = realdata1530['realtime']['latest_trade_price']                      
              await message.channel.send('亞崴目前股價：' + realprice1530) 

    elif message.content == '-t 1532': 
         realdata1532=twstock.realtime.get('1532')  
         if realdata1532['success']:     
              realprice1532 = realdata1532['realtime']['latest_trade_price']                     
              await message.channel.send('勤美目前股價：' + realprice1532)

    elif message.content == '-t 1533': 
         realdata1533=twstock.realtime.get('1533')  
         if realdata1533['success']:     
              realprice1533 = realdata1533['realtime']['latest_trade_price']                    
              await message.channel.send('車王電目前股價：' + realprice1533)   

    elif message.content == '-t 1535': 
         realdata1535=twstock.realtime.get('1535')  
         if realdata1535['success']:     
              realprice1535 = realdata1535['realtime']['latest_trade_price']                     
              await message.channel.send('中宇目前股價：' + realprice1535)   

    elif message.content == '-t 1536': 
         realdata1536=twstock.realtime.get('1536')  
         if realdata1536['success']:     
              realprice1536 = realdata1536['realtime']['latest_trade_price']                    
              await message.channel.send('和大目前股價：' + realprice1536)   

    elif message.content == '-t 1537': 
         realdata1537=twstock.realtime.get('1537')  
         if realdata1537['success']:     
              realprice1537 = realdata1537['realtime']['latest_trade_price']                    
              await message.channel.send('廣隆目前股價：' + realprice1537)   

    elif message.content == '-t 1538': 
         realdata1538=twstock.realtime.get('1538')  
         if realdata1538['success']:     
              realprice1538 = realdata1538['realtime']['latest_trade_price']                     
              await message.channel.send('正峰目前股價：' + realprice1538)   

    elif message.content == '-t 1539': 
         realdata1539=twstock.realtime.get('1539')  
         if realdata1539['success']:     
              realprice1539 = realdata1539['realtime']['latest_trade_price']                    
              await message.channel.send('巨庭目前股價：' + realprice1539)   

    elif message.content == '-t 1540': 
         realdata1540=twstock.realtime.get('1540')  
         if realdata1540['success']:     
              realprice1540 = realdata1540['realtime']['latest_trade_price']                    
              await message.channel.send('喬福目前股價：' + realprice1540)   

    elif message.content == '-t 1541': 
         realdata1541=twstock.realtime.get('1541')  
         if realdata1541['success']:     
              realprice1541 = realdata1541['realtime']['latest_trade_price']                   
              await message.channel.send('錩泰目前股價：' + realprice1541)   

    elif message.content == '-t 1558': 
         realdata1558=twstock.realtime.get('1558')  
         if realdata1558['success']:     
              realprice1558 = realdata1558['realtime']['latest_trade_price']                    
              await message.channel.send('伸興目前股價：' + realprice1558)   

    elif message.content == '-t 1560': 
         realdata1560=twstock.realtime.get('1560')  
         if realdata1560['success']:     
              realprice1560 = realdata1560['realtime']['latest_trade_price']                      
              await message.channel.send('中砂目前股價：' + realprice1560)   

    elif message.content == '-t 1568': 
         realdata1568=twstock.realtime.get('1568')  
         if realdata1568['success']:     
              realprice1568 = realdata1568['realtime']['latest_trade_price']                      
              await message.channel.send('倉佑目前股價：' + realprice1568)   

    elif message.content == '-t 1582': 
         realdata1582=twstock.realtime.get('1582')  
         if realdata1582['success']:     
              realprice1582 = realdata1582['realtime']['latest_trade_price']                     
              await message.channel.send('信錦目前股價：' + realprice1582)   

    elif message.content == '-t 1583': 
         realdata1583=twstock.realtime.get('1583')  
         if realdata1583['success']:     
              realprice1583 = realdata1583['realtime']['latest_trade_price']                    
              await message.channel.send('程泰目前股價：' + realprice1583)   

    elif message.content == '-t 1587': 
         realdata1587=twstock.realtime.get('1587')  
         if realdata1587['success']:     
              realprice1587 = realdata1587['realtime']['latest_trade_price']                    
              await message.channel.send('吉茂目前股價：' + realprice1587)   

    elif message.content == '-t 1589': 
         realdata1589=twstock.realtime.get('1589')  
         if realdata1589['success']:     
              realprice1589 = realdata1589['realtime']['latest_trade_price']                    
              await message.channel.send('永冠-KY目前股價：' + realprice1589)   

    elif message.content == '-t 1590': 
         realdata1590=twstock.realtime.get('1590')  
         if realdata1590['success']:     
              realprice1590 = realdata1590['realtime']['latest_trade_price']            
              await message.channel.send('亞德客-KY目前股價：' + realprice1590)   

    elif message.content == '-t 1592': 
         realdata1592=twstock.realtime.get('1592')  
         if realdata1592['success']:     
              realprice1592 = realdata1592['realtime']['latest_trade_price']                     
              await message.channel.send('英瑞-KY	目前股價：' + realprice1592)   

    elif message.content == '-t 1597': 
         realdata1597=twstock.realtime.get('1597')  
         if realdata1597['success']:     
              realprice1597 = realdata1597['realtime']['latest_trade_price']                      
              await message.channel.send('直得目前股價：' + realprice1597)   

    elif message.content == '-t 1598': 
         realdata1598=twstock.realtime.get('1598')  
         if realdata1598['success']:     
              realprice1598 = realdata1598['realtime']['latest_trade_price']                      
              await message.channel.send('岱宇目前股價：' + realprice1598)   

    elif message.content == '-t 1603': 
         realdata1603=twstock.realtime.get('1603')  
         if realdata1603['success']:     
              realprice1603 = realdata1603['realtime']['latest_trade_price']                      
              await message.channel.send('華電目前股價：' + realprice1603)   

    elif message.content == '-t 1604': 
         realdata1604=twstock.realtime.get('1604')  
         if realdata1604['success']:     
              realprice1604 = realdata1604['realtime']['latest_trade_price']                      
              await message.channel.send('聲寶目前股價：' + realprice1604)   

    elif message.content == '-t 1605': 
         realdata1605=twstock.realtime.get('1605')  
         if realdata1605['success']:     
              realprice1605 = realdata1605['realtime']['latest_trade_price']                     
              await message.channel.send('華新目前股價：' + realprice1605)   
 
    elif message.content == '-t 1608': 
         realdata1608=twstock.realtime.get('1608')  
         if realdata1608['success']:     
              realprice1608 = realdata1608['realtime']['latest_trade_price']                      
              await message.channel.send('華榮目前股價：' + realprice1608)  

    elif message.content == '-t 1609': 
         realdata1609=twstock.realtime.get('1609')  
         if realdata1609['success']:     
              realprice1609 = realdata1609['realtime']['latest_trade_price']                    
              await message.channel.send('大亞目前股價：' + realprice1609)   

    elif message.content == '-t 1611': 
         realdata1611=twstock.realtime.get('1611')  
         if realdata1611['success']:     
              realprice1611 = realdata1611['realtime']['latest_trade_price']                      
              await message.channel.send('中電目前股價：' + realprice1611)   

    elif message.content == '-t 1612': 
         realdata1612=twstock.realtime.get('1612')  
         if realdata1612['success']:     
              realprice1612 = realdata1612['realtime']['latest_trade_price']                     
              await message.channel.send('宏泰目前股價：' + realprice1612)   

    elif message.content == '-t 1614': 
         realdata1614=twstock.realtime.get('1614')  
         if realdata1614['success']:     
              realprice1614 = realdata1614['realtime']['latest_trade_price']         #150            
              await message.channel.send('三洋電	目前股價：' + realprice1614)   

    elif message.content == '-t 1615': 
         realdata1615=twstock.realtime.get('1615')  
         if realdata1615['success']:     
              realprice1615 = realdata1615['realtime']['latest_trade_price']                     
              await message.channel.send('大山目前股價：' + realprice1615)   

    elif message.content == '-t 1616': 
         realdata1616=twstock.realtime.get('1616')  
         if realdata1616['success']:     
              realprice1616 = realdata1616['realtime']['latest_trade_price']                     
              await message.channel.send('億泰目前股價：' + realprice1616)   

    elif message.content == '-t 1617': 
         realdata1617=twstock.realtime.get('1617')  
         if realdata1617['success']:     
              realprice1617 = realdata1617['realtime']['latest_trade_price']                     
              await message.channel.send('榮星目前股價：' + realprice1617)   

    elif message.content == '-t 1618': 
         realdata1618=twstock.realtime.get('1618')  
         if realdata1618['success']:     
              realprice1618 = realdata1618['realtime']['latest_trade_price']                     
              await message.channel.send('合機目前股價：' + realprice1618)   

    elif message.content == '-t 1626': 
         realdata1626=twstock.realtime.get('1626')  
         if realdata1626['success']:     
              realprice1626= realdata1626['realtime']['latest_trade_price']                      
              await message.channel.send('艾美特-KY目前股價：' + realprice1626)   

    elif message.content == '-t 1701': 
         realdata1701=twstock.realtime.get('1701')  
         if realdata1701['success']:     
              realprice1701 = realdata1701['realtime']['latest_trade_price']                      
              await message.channel.send('中化目前股價：' + realprice1701)   

    elif message.content == '-t 1702': 
         realdata1702=twstock.realtime.get('1702')  
         if realdata1702['success']:     
              realprice1702 = realdata1702['realtime']['latest_trade_price']                      
              await message.channel.send('南僑目前股價：' + realprice1702)   

    elif message.content == '-t 1707': 
         realdata1707=twstock.realtime.get('1707')  
         if realdata1707['success']:     
              realprice1707 = realdata1707['realtime']['latest_trade_price']                    
              await message.channel.send('葡萄王目前股價：' + realprice1707)   

    elif message.content == '-t 1708': 
         realdata1708=twstock.realtime.get('1708')  
         if realdata1708['success']:     
              realprice1708 = realdata1708['realtime']['latest_trade_price']                      
              await message.channel.send('東鹼目前股價：' + realprice1708)   

    elif message.content == '-t 1709': 
         realdata1709=twstock.realtime.get('1709')  
         if realdata1709['success']:     
              realprice1709 = realdata1709['realtime']['latest_trade_price']                   
              await message.channel.send('和益目前股價：' + realprice1709)   

    elif message.content == '-t 1710': 
         realdata1710=twstock.realtime.get('1710')  
         if realdata1710['success']:     
              realprice1710 = realdata1710['realtime']['latest_trade_price']                    
              await message.channel.send('東聯目前股價：' + realprice1710)   

    elif message.content == '-t 1711': 
         realdata1711=twstock.realtime.get('1711')  
         if realdata1711['success']:     
              realprice1711 = realdata1711['realtime']['latest_trade_price']                     
              await message.channel.send('永光目前股價：' + realprice1711)   

    elif message.content == '-t 1712': 
         realdata1712=twstock.realtime.get('1712')  
         if realdata1712['success']:     
              realprice1712 = realdata1712['realtime']['latest_trade_price']                     
              await message.channel.send('興農目前股價：' + realprice1712)   

    elif message.content == '-t 1713': 
         realdata1713=twstock.realtime.get('1713')  
         if realdata1713['success']:     
              realprice1713 = realdata1713['realtime']['latest_trade_price']                     
              await message.channel.send('國化目前股價：' + realprice1713)   

    elif message.content == '-t 1714': 
         realdata1714=twstock.realtime.get('1714')  
         if realdata1714['success']:     
              realprice1714 = realdata1714['realtime']['latest_trade_price']                    
              await message.channel.send('和桐目前股價：' + realprice1714)   

    elif message.content == '-t 1717': 
         realdata1717=twstock.realtime.get('1717')  
         if realdata1717['success']:     
              realprice1717 = realdata1717['realtime']['latest_trade_price']                      
              await message.channel.send('長興目前股價：' + realprice1717)
              
    elif message.content == '-t 1718': 
         realdata1718=twstock.realtime.get('1718')  
         if realdata1718['success']:     
              realprice1718 = realdata1718['realtime']['latest_trade_price']                    
              await message.channel.send('中纖目前股價：' + realprice1718)
             
    elif message.content == '-t 1720': 
         realdata1720=twstock.realtime.get('1720')  
         if realdata1720['success']:     
              realprice1720 = realdata1720['realtime']['latest_trade_price']                     
              await message.channel.send('生達目前股價：' + realprice1720)
              
    elif message.content == '-t 1721': 
         realdata1721=twstock.realtime.get('1721')  
         if realdata1721['success']:     
              realprice1721 = realdata1721['realtime']['latest_trade_price']                     
              await message.channel.send('三晃目前股價：' + realprice1721)
              
    elif message.content == '-t 1722': 
         realdata1722=twstock.realtime.get('1722')  
         if realdata1722['success']:     
              realprice1722 = realdata1722['realtime']['latest_trade_price']                    
              await message.channel.send('台肥目前股價：' + realprice1722)
             
    elif message.content == '-t 1723': 
         realdata1723=twstock.realtime.get('1723')  
         if realdata1723['success']:     
              realprice1723 = realdata1723['realtime']['latest_trade_price']                      
              await message.channel.send('中碳目前股價：' + realprice1723)
              
    elif message.content == '-t 1725': 
         realdata1725=twstock.realtime.get('1725')  
         if realdata1725['success']:     
              realprice1725 = realdata1725['realtime']['latest_trade_price']                      
              await message.channel.send('元禎目前股價：' + realprice1725)
              
    elif message.content == '-t 1726': 
         realdata1726=twstock.realtime.get('1726')  
         if realdata1726['success']:     
              realprice1726 = realdata1726['realtime']['latest_trade_price']                      
              await message.channel.send('永記目前股價：' + realprice1726)
        
    elif message.content == '-t 1727': 
         realdata1727=twstock.realtime.get('1727')  
         if realdata1727['success']:     
              realprice1727 = realdata1727['realtime']['latest_trade_price']                     
              await message.channel.send('中華化目前股價：' + realprice1727)
              
    elif message.content == '-t 1730': 
         realdata1730=twstock.realtime.get('1730')  
         if realdata1730['success']:     
              realprice1730 = realdata1730['realtime']['latest_trade_price']                      
              await message.channel.send('花仙子目前股價：' + realprice1730)
              
    elif message.content == '-t 1731': 
         realdata1731=twstock.realtime.get('1731')  
         if realdata1731['success']:     
              realprice1731 = realdata1731['realtime']['latest_trade_price']                     
              await message.channel.send('美吾華目前股價：' + realprice1731)

    elif message.content == '-t 1732': 
         realdata1732=twstock.realtime.get('1732')  
         if realdata1732['success']:     
              realprice1732 = realdata1732['realtime']['latest_trade_price']                     
              await message.channel.send('毛寶目前股價：' + realprice1732)
              
    elif message.content == '-t 1733': 
         realdata1733=twstock.realtime.get('1733')  
         if realdata1733['success']:     
              realprice1733 = realdata1733['realtime']['latest_trade_price']                      
              await message.channel.send('五鼎目前股價：' + realprice1733)
               
    elif message.content == '-t 1734': 
         realdata1734=twstock.realtime.get('1734')  
         if realdata1734['success']:     
              realprice1734 = realdata1734['realtime']['latest_trade_price']                     
              await message.channel.send('杏輝目前股價：' + realprice1734)
             
    elif message.content == '-t 1735': 
         realdata1735=twstock.realtime.get('1735')  
         if realdata1735['success']:     
              realprice1735 = realdata1735['realtime']['latest_trade_price']                    
              await message.channel.send('日勝化目前股價：' + realprice1735)
              
    elif message.content == '-t 1736': 
         realdata1736=twstock.realtime.get('1736')  
         if realdata1736['success']:     
              realprice1736 = realdata1736['realtime']['latest_trade_price']                    
              await message.channel.send('喬山目前股價：' + realprice1736)
              
    elif message.content == '-t 1737': 
         realdata1737=twstock.realtime.get('1737')  
         if realdata1737['success']:     
              realprice1737 = realdata1737['realtime']['latest_trade_price']                     
              await message.channel.send('臺鹽目前股價：' + realprice1737)
              
    elif message.content == '-t 1760': 
         realdata1760=twstock.realtime.get('1760')  
         if realdata1760['success']:     
              realprice1760 = realdata1760['realtime']['latest_trade_price']                    
              await message.channel.send('寶齡富錦目前股價：' + realprice1760)
              
    elif message.content == '-t 1762': 
         realdata1762=twstock.realtime.get('1762')  
         if realdata1762['success']:     
              realprice1762 = realdata1762['realtime']['latest_trade_price']                     
              await message.channel.send('中化生目前股價：' + realprice1762)
              
    elif message.content == '-t 1773': 
         realdata1773=twstock.realtime.get('1773')  
         if realdata1773['success']:     
              realprice1773 = realdata1773['realtime']['latest_trade_price']                      
              await message.channel.send('勝一目前股價：' + realprice1773)
              
    elif message.content == '-t 1776': 
         realdata1776=twstock.realtime.get('1776')  
         if realdata1776['success']:     
              realprice1776 = realdata1776['realtime']['latest_trade_price']                    
              await message.channel.send('展宇目前股價：' + realprice1776)
              
    elif message.content == '-t 1783': 
         realdata1783=twstock.realtime.get('1783')  
         if realdata1783['success']:     
              realprice1783 = realdata1783['realtime']['latest_trade_price']                   
              await message.channel.send('和康生目前股價：' + realprice1783)
              
    elif message.content == '-t 1786': 
         realdata1786=twstock.realtime.get('1786')  
         if realdata1786['success']:     
              realprice1786 = realdata1786['realtime']['latest_trade_price']                      
              await message.channel.send('科妍目前股價：' + realprice1786)
              
    elif message.content == '-t 1789': 
         realdata1789=twstock.realtime.get('1789')  
         if realdata1789['success']:     
              realprice1789 = realdata1789['realtime']['latest_trade_price']                    
              await message.channel.send('神隆目前股價：' + realprice1789)
              
    elif message.content == '-t 1795': 
         realdata1795=twstock.realtime.get('1795')  
         if realdata1795['success']:     
              realprice1795 = realdata1795['realtime']['latest_trade_price']                      
              await message.channel.send('美時目前股價：' + realprice1795)
              
    elif message.content == '-t 1802': 
         realdata1802=twstock.realtime.get('1802')  
         if realdata1802['success']:     
              realprice1802 = realdata1802['realtime']['latest_trade_price']                     
              await message.channel.send('台玻目前股價：' + realprice1802)
              
    elif message.content == '-t 1805': 
         realdata1805=twstock.realtime.get('1805')  
         if realdata1805['success']:     
              realprice1805 = realdata1805['realtime']['latest_trade_price']                     
              await message.channel.send('寶徠目前股價：' + realprice1805)
              
    elif message.content == '-t 1806': 
         realdata1806=twstock.realtime.get('1806')  
         if realdata1806['success']:     
              realprice1806 = realdata1806['realtime']['latest_trade_price']                     
              await message.channel.send('冠軍目前股價：' + realprice1806)
              
    elif message.content == '-t 1808': 
         realdata1808=twstock.realtime.get('1808')  
         if realdata1808['success']:     
              realprice1808 = realdata1808['realtime']['latest_trade_price']                    
              await message.channel.send('潤隆目前股價：' + realprice1808)
              
    elif message.content == '-t 1809': 
         realdata1809=twstock.realtime.get('1809')  
         if realdata1809['success']:     
              realprice1809 = realdata1809['realtime']['latest_trade_price']                      
              await message.channel.send('中釉目前股價：' + realprice1809)
              
    elif message.content == '-t 1810': 
         realdata1810=twstock.realtime.get('1810')  
         if realdata1810['success']:     
              realprice1810 = realdata1810['realtime']['latest_trade_price']                      
              await message.channel.send('和成目前股價：' + realprice1810)
              
    elif message.content == '-t 1817': 
         realdata1817=twstock.realtime.get('1817')  
         if realdata1817['success']:     
              realprice1817 = realdata1817['realtime']['latest_trade_price']                      
              await message.channel.send('凱撒衛目前股價：' + realprice1817)
              
    elif message.content == '-t 1903': 
         realdata1903=twstock.realtime.get('1903')  
         if realdata1903['success']:     
              realprice1903 = realdata1903['realtime']['latest_trade_price']                      
              await message.channel.send('士紙目前股價：' + realprice1903)
              
    elif message.content == '-t 1904': 
         realdata1904=twstock.realtime.get('1904')  
         if realdata1904['success']:     
              realprice1904 = realdata1904['realtime']['latest_trade_price']                     
              await message.channel.send('正隆目前股價：' + realprice1904)
              
    elif message.content == '-t 1905': 
         realdata1905=twstock.realtime.get('1905')  
         if realdata1905['success']:     
              realprice1905 = realdata1905['realtime']['latest_trade_price']            #200          
              await message.channel.send('華紙目前股價：' + realprice1905)              
              
    elif message.content == '-t 1906': 
         realdata1906=twstock.realtime.get('1906')  
         if realdata1906['success']:     
              realprice1906 = realdata1906['realtime']['latest_trade_price']                      
              await message.channel.send('寶隆目前股價：' + realprice1906)              
              
    elif message.content == '-t 1907': 
         realdata1907=twstock.realtime.get('1907')  
         if realdata1907['success']:     
              realprice1907 = realdata1907['realtime']['latest_trade_price']                      
              await message.channel.send('永豐餘目前股價：' + realprice1907)              
              
    elif message.content == '-t 1909': 
         realdata1909=twstock.realtime.get('1909')  
         if realdata1909['success']:     
              realprice1909 = realdata1909['realtime']['latest_trade_price']                     
              await message.channel.send('榮成目前股價：' + realprice1909)              
              
    elif message.content == '-t 2002': 
         realdata2002=twstock.realtime.get('2002')  
         if realdata2002['success']:     
              realprice2002 = realdata2002['realtime']['latest_trade_price']                    
              await message.channel.send('中鋼目前股價：' + realprice2002)              
              
    elif message.content == '-t 2006': 
         realdata2006=twstock.realtime.get('2006')  
         if realdata2006['success']:     
              realprice2006 = realdata2006['realtime']['latest_trade_price']                      
              await message.channel.send('東和鋼鐵目前股價：' + realprice2006)              
              
    elif message.content == '-t 2007': 
         realdata2007=twstock.realtime.get('2007')  
         if realdata2007['success']:     
              realprice2007 = realdata2007['realtime']['latest_trade_price']                     
              await message.channel.send('燁興目前股價：' + realprice2007)              
              
    elif message.content == '-t 2008': 
         realdata2008=twstock.realtime.get('2008')  
         if realdata2008['success']:     
              realprice2008 = realdata2008['realtime']['latest_trade_price']                    
              await message.channel.send('高興昌目前股價：' + realprice2008)              
              
    elif message.content == '-t 2009': 
         realdata2009=twstock.realtime.get('2009')  
         if realdata2009['success']:     
              realprice2009 = realdata2009['realtime']['latest_trade_price']                     
              await message.channel.send('第一銅目前股價：' + realprice2009)              
              
    elif message.content == '-t 2010': 
         realdata2010=twstock.realtime.get('2010')  
         if realdata2010['success']:     
              realprice2010 = realdata2010['realtime']['latest_trade_price']                    
              await message.channel.send('春源目前股價：' + realprice2010)              
            
    elif message.content == '-t 2012': 
         realdata2012=twstock.realtime.get('2012')  
         if realdata2012['success']:     
              realprice2012 = realdata2012['realtime']['latest_trade_price']                     
              await message.channel.send('春雨目前股價：' + realprice2012)

    elif message.content == '-t 2013': 
         realdata2013=twstock.realtime.get('2013')  
         if realdata2013['success']:     
              realprice2013 = realdata2013['realtime']['latest_trade_price']                      
              await message.channel.send('中鋼構目前股價：' + realprice2013)
              
    elif message.content == '-t 2014': 
         realdata2014=twstock.realtime.get('2014')  
         if realdata2014['success']:     
              realprice2014 = realdata2014['realtime']['latest_trade_price']                     
              await message.channel.send('中鴻目前股價：' + realprice2014) 
              
    elif message.content == '-t 2015': 
         realdata2015=twstock.realtime.get('2015')  
         if realdata2015['success']:     
              realprice2015 = realdata2015['realtime']['latest_trade_price']                     
              await message.channel.send('豐興目前股價：' + realprice2015)  
             
    elif message.content == '-t 2017': 
         realdata2017=twstock.realtime.get('2017')  
         if realdata2017['success']:     
              realprice2017 = realdata2017['realtime']['latest_trade_price']                      
              await message.channel.send('官田鋼目前股價：' + realprice2017)  
              
    elif message.content == '-t 2020': 
         realdata2020=twstock.realtime.get('2020')  
         if realdata2020['success']:     
              realprice2020 = realdata2020['realtime']['latest_trade_price']                     
              await message.channel.send('美亞目前股價：' + realprice2020)  
             
    elif message.content == '-t 2022': 
         realdata2022=twstock.realtime.get('2022')  
         if realdata2022['success']:     
              realprice2022 = realdata2022['realtime']['latest_trade_price']                    
              await message.channel.send('聚亨目前股價：' + realprice2022)  
              
    elif message.content == '-t 2023': 
         realdata2023=twstock.realtime.get('2023')  
         if realdata2023['success']:     
              realprice2023 = realdata2023['realtime']['latest_trade_price']                     
              await message.channel.send('燁輝目前股價：' + realprice2023)  
              
    elif message.content == '-t 2024': 
         realdata2024=twstock.realtime.get('2024')  
         if realdata2024['success']:     
              realprice2024 = realdata2024['realtime']['latest_trade_price']                      
              await message.channel.send('志聯目前股價：' + realprice2024)  
              
    elif message.content == '-t 2025': 
         realdata2025=twstock.realtime.get('2025')  
         if realdata2025['success']:     
              realprice2025 = realdata2025['realtime']['latest_trade_price']                    
              await message.channel.send('千興目前股價：' + realprice2025)  
              
    elif message.content == '-t 2027': 
         realdata2027=twstock.realtime.get('2027')  
         if realdata2027['success']:     
              realprice2027 = realdata2027['realtime']['latest_trade_price']         #220            
              await message.channel.send('大成鋼目前股價：' + realprice2027)  
              
    elif message.content == '-t 2028': 
         realdata2028=twstock.realtime.get('2028')  
         if realdata2028['success']:     
              realprice2028 = realdata2028['realtime']['latest_trade_price']                    
              await message.channel.send('威致目前股價：' + realprice2028)  
              
    elif message.content == '-t 2029': 
         realdata2029=twstock.realtime.get('2029')  
         if realdata2029['success']:     
              realprice2029 = realdata2029['realtime']['latest_trade_price']                      
              await message.channel.send('盛餘目前股價：' + realprice2029)  
             
    elif message.content == '-t 2030': 
         realdata2030=twstock.realtime.get('2030')  
         if realdata2030['success']:     
              realprice2030 = realdata2030['realtime']['latest_trade_price']                    
              await message.channel.send('彰源目前股價：' + realprice2030)  
              
    elif message.content == '-t 2031': 
         realdata2031=twstock.realtime.get('2031')  
         if realdata2031['success']:     
              realprice2031 = realdata2031['realtime']['latest_trade_price']                     
              await message.channel.send('新光鋼目前股價：' + realprice2031)  
            
    elif message.content == '-t 2032': 
         realdata2032=twstock.realtime.get('2032')  
         if realdata2032['success']:     
              realprice2032 = realdata2032['realtime']['latest_trade_price']                     
              await message.channel.send('新鋼目前股價：' + realprice2032)  
              
    elif message.content == '-t 2033': 
         realdata2033=twstock.realtime.get('2033')  
         if realdata2033['success']:     
              realprice2033 = realdata2033['realtime']['latest_trade_price']                     
              await message.channel.send('佳大目前股價：' + realprice2033)  
              
    elif message.content == '-t 2034': 
         realdata2034=twstock.realtime.get('2034')  
         if realdata2034['success']:     
              realprice2034 = realdata2034['realtime']['latest_trade_price']                      
              await message.channel.send('允強目前股價：' + realprice2034)  
              
    elif message.content == '-t 2038': 
         realdata2038=twstock.realtime.get('2038')  
         if realdata2038['success']:     
              realprice2038 = realdata2038['realtime']['latest_trade_price']                      
              await message.channel.send('海光目前股價：' + realprice2038)  
              
    elif message.content == '-t 2049': 
         realdata2049=twstock.realtime.get('2049')  
         if realdata2049['success']:     
              realprice2049 = realdata2049['realtime']['latest_trade_price']                     
              await message.channel.send('上銀目前股價：' + realprice2049)  
              
    elif message.content == '-t 2059': 
         realdata2059=twstock.realtime.get('2059')  
         if realdata2059['success']:     
              realprice2059 = realdata2059['realtime']['latest_trade_price']                     
              await message.channel.send('川湖目前股價：' + realprice2059)  
              
    elif message.content == '-t 2062': 
         realdata2062=twstock.realtime.get('2062')  
         if realdata2062['success']:     
              realprice2062 = realdata2062['realtime']['latest_trade_price']                      
              await message.channel.send('橋椿目前股價：' + realprice2062)  
              
    elif message.content == '-t 2069': 
         realdata2069=twstock.realtime.get('2069')  
         if realdata2069['success']:     
              realprice2069 = realdata2069['realtime']['latest_trade_price']                     
              await message.channel.send('運錩目前股價：' + realprice2069)
              
    elif message.content == '-t 2101': 
         realdata2101=twstock.realtime.get('2101')  
         if realdata2101['success']:     
              realprice2101 = realdata2101['realtime']['latest_trade_price']                      
              await message.channel.send('南港目前股價：' + realprice2101)
              
    elif message.content == '-t 2102': 
         realdata2102=twstock.realtime.get('2102')  
         if realdata2102['success']:     
              realprice2102 = realdata2102['realtime']['latest_trade_price']                      
              await message.channel.send('泰豐目前股價：' + realprice2102)
              
    elif message.content == '-t 2103': 
         realdata2103=twstock.realtime.get('2103')  
         if realdata2103['success']:     
              realprice2103 = realdata2103['realtime']['latest_trade_price']                      
              await message.channel.send('台橡目前股價：' + realprice2103)
              
    elif message.content == '-t 2104': 
         realdata2104=twstock.realtime.get('2104')  
         if realdata2104['success']:     
              realprice2104 = realdata2104['realtime']['latest_trade_price']                     
              await message.channel.send('國際中橡目前股價：' + realprice2104)
              
    elif message.content == '-t 2105': 
         realdata2105=twstock.realtime.get('2105')  
         if realdata2105['success']:     
              realprice2105 = realdata2105['realtime']['latest_trade_price']                     
              await message.channel.send('正新目前股價：' + realprice2105)
              
    elif message.content == '-t 2106': 
         realdata2106=twstock.realtime.get('2106')  
         if realdata2106['success']:     
              realprice2106 = realdata2106['realtime']['latest_trade_price']                     
              await message.channel.send('建大目前股價：' + realprice2106)
              
    elif message.content == '-t 2107': 
         realdata2107=twstock.realtime.get('2107')  
         if realdata2107['success']:     
              realprice2107 = realdata2107['realtime']['latest_trade_price']                      
              await message.channel.send('厚生目前股價：' + realprice2107)
              
    elif message.content == '-t 2108': 
         realdata2108=twstock.realtime.get('2108')  
         if realdata2108['success']:     
              realprice2108 = realdata2108['realtime']['latest_trade_price']                     
              await message.channel.send('南帝目前股價：' + realprice2108)
              
    elif message.content == '-t 2109': 
         realdata2109=twstock.realtime.get('2109')  
         if realdata2109['success']:     
              realprice2109 = realdata2109['realtime']['latest_trade_price']                      
              await message.channel.send('華豐目前股價：' + realprice2109)
              
    elif message.content == '-t 2114': 
         realdata2114=twstock.realtime.get('2114')  
         if realdata2114['success']:     
              realprice2114 = realdata2114['realtime']['latest_trade_price']                      
              await message.channel.send('鑫永銓	目前股價：' + realprice2114)
              
    elif message.content == '-t 2115': 
         realdata2115=twstock.realtime.get('2115')  
         if realdata2115['success']:     
              realprice2115 = realdata2115['realtime']['latest_trade_price']                      
              await message.channel.send('六暉-KY目前股價：' + realprice2115)
              
    elif message.content == '-t 2201': 
         realdata2201=twstock.realtime.get('2201')  
         if realdata2201['success']:     
              realprice2201 = realdata2201['realtime']['latest_trade_price']                      
              await message.channel.send('裕隆目前股價：' + realprice2201)
              
    elif message.content == '-t 2204': 
         realdata2204=twstock.realtime.get('2204')  
         if realdata2204['success']:     
              realprice2204 = realdata2204['realtime']['latest_trade_price']                      
              await message.channel.send('中華目前股價：' + realprice2204)
              
    elif message.content == '-t 2206': 
         realdata2206=twstock.realtime.get('2206')  
         if realdata2206['success']:     
              realprice2206 = realdata2206['realtime']['latest_trade_price']                      
              await message.channel.send('三陽工業目前股價：' + realprice2206)
              
    elif message.content == '-t 2207': 
         realdata2207=twstock.realtime.get('2207')  
         if realdata2207['success']:     
              realprice2207 = realdata2207['realtime']['latest_trade_price']                      
              await message.channel.send('和泰車目前股價：' + realprice2207)
              
    elif message.content == '-t 2208': 
         realdata2208=twstock.realtime.get('2208')  
         if realdata2208['success']:     
              realprice2208 = realdata2208['realtime']['latest_trade_price']                     
              await message.channel.send('台船目前股價：' + realprice2208)
              
    elif message.content == '-t 2211': 
         realdata2211=twstock.realtime.get('2211')  
         if realdata2211['success']:     
              realprice2211 = realdata2211['realtime']['latest_trade_price']                      
              await message.channel.send('長榮鋼目前股價：' + realprice2211)
              
    elif message.content == '-t 2227': 
         realdata2227=twstock.realtime.get('2227')  
         if realdata2227['success']:     
              realprice2227 = realdata2227['realtime']['latest_trade_price']          #250            
              await message.channel.send('裕日車目前股價：' + realprice2227)
              
    elif message.content == '-t 2228': 
         realdata2228=twstock.realtime.get('2228')  
         if realdata2228['success']:     
              realprice2228 = realdata2228['realtime']['latest_trade_price']                     
              await message.channel.send('劍麟目前股價：' + realprice2228)
              
    elif message.content == '-t 2231': 
         realdata2231=twstock.realtime.get('2231')  
         if realdata2231['success']:     
              realprice2231 = realdata2231['realtime']['latest_trade_price']                      
              await message.channel.send('為升目前股價：' + realprice2231)
              
    elif message.content == '-t 2233': 
         realdata2233=twstock.realtime.get('2233')  
         if realdata2233['success']:     
              realprice2233 = realdata2233['realtime']['latest_trade_price']                      
              await message.channel.send('宇隆目前股價：' + realprice2233)
              
    elif message.content == '-t 2236': 
         realdata2236=twstock.realtime.get('2236')  
         if realdata2236['success']:     
              realprice2236 = realdata2236['realtime']['latest_trade_price']                    
              await message.channel.send('百達-KY目前股價：' + realprice2236)
              
    elif message.content == '-t 2239': 
         realdata2239=twstock.realtime.get('2239')  
         if realdata2239['success']:     
              realprice2239 = realdata2239['realtime']['latest_trade_price']                      
              await message.channel.send('英利-KY目前股價：' + realprice2239)
              
    elif message.content == '-t 2241': 
         realdata2241=twstock.realtime.get('2241')  
         if realdata2241['success']:     
              realprice2241 = realdata2241['realtime']['latest_trade_price']                      
              await message.channel.send('艾姆勒目前股價：' + realprice2241)
              
    elif message.content == '-t 2243': 
         realdata2243=twstock.realtime.get('2243')  
         if realdata2243['success']:     
              realprice2243 = realdata2243['realtime']['latest_trade_price']                      
              await message.channel.send('宏旭-KY目前股價：' + realprice2243)
              
    elif message.content == '-t 2247': 
         realdata2247=twstock.realtime.get('2247')  
         if realdata2247['success']:     
              realprice2247 = realdata2247['realtime']['latest_trade_price']                      
              await message.channel.send('汎德永業目前股價：' + realprice2247)
              
    elif message.content == '-t 2250': 
         realdata2250=twstock.realtime.get('2250')  
         if realdata2250['success']:     
              realprice2250 = realdata2250['realtime']['latest_trade_price']                     
              await message.channel.send('IKKA-KY目前股價：' + realprice2250)
              
    elif message.content == '-t 2301': 
         realdata2301=twstock.realtime.get('2301')  
         if realdata2301['success']:     
              realprice2301 = realdata2301['realtime']['latest_trade_price']                     
              await message.channel.send('光寶科目前股價：' + realprice2301)
            
    elif message.content == '-t 2302': 
         realdata2302=twstock.realtime.get('2302')  
         if realdata2302['success']:     
              realprice2302 = realdata2302['realtime']['latest_trade_price']             
              await message.channel.send('麗正目前股價：' + realprice2302)
              
    elif message.content == '-t 2303': 
         realdata2303=twstock.realtime.get('2303')  
         if realdata2303['success']:     
              realprice2303 = realdata2303['realtime']['latest_trade_price']                      
              await message.channel.send('聯電目前股價：' + realprice2303)
              
    elif message.content == '-t 2305': 
         realdata2305=twstock.realtime.get('2305')  
         if realdata2305['success']:     
              realprice2305 = realdata2305['realtime']['latest_trade_price']                      
              await message.channel.send('全友目前股價：' + realprice2305)
              
    elif message.content == '-t 2308': 
         realdata2308=twstock.realtime.get('2308')  
         if realdata2308['success']:     
              realprice2308 = realdata2308['realtime']['latest_trade_price']                      
              await message.channel.send('台達電目前股價：' + realprice2308)
              
    elif message.content == '-t 2312': 
         realdata2312=twstock.realtime.get('2312')  
         if realdata2312['success']:     
              realprice2312 = realdata2312['realtime']['latest_trade_price']                     
              await message.channel.send('金寶目前股價：' + realprice2312)
              
    elif message.content == '-t 2313': 
         realdata2313=twstock.realtime.get('2313')  
         if realdata2313['success']:     
              realprice2313 = realdata2313['realtime']['latest_trade_price']                      
              await message.channel.send('華通目前股價：' + realprice2313)
            
    elif message.content == '-t 2314': 
         realdata2314=twstock.realtime.get('2314')  
         if realdata2314['success']:     
              realprice2314 = realdata2314['realtime']['latest_trade_price']                      
              await message.channel.send('台揚目前股價：' + realprice2314)
              
    elif message.content == '-t 2316': 
         realdata2316=twstock.realtime.get('2316')  
         if realdata2316['success']:     
              realprice2316 = realdata2316['realtime']['latest_trade_price']                      
              await message.channel.send('楠梓電目前股價：' + realprice2316)
              
    elif message.content == '-t 2317': 
         realdata2317=twstock.realtime.get('2317')  
         if realdata2317['success']:     
              realprice2317 = realdata2317['realtime']['latest_trade_price']                      
              await message.channel.send('鴻海目前股價：' + realprice2317)
              
    elif message.content == '-t 2321': 
         realdata2321=twstock.realtime.get('2321')  
         if realdata2321['success']:     
              realprice2321 = realdata2321['realtime']['latest_trade_price']                      
              await message.channel.send('東訊目前股價：' + realprice2321)
              
    elif message.content == '-t 2323': 
         realdata2323=twstock.realtime.get('2323')  
         if realdata2323['success']:     
              realprice2323 = realdata2323['realtime']['latest_trade_price']                      
              await message.channel.send('中環目前股價：' + realprice2323)
            
    elif message.content == '-t 2324': 
         realdata2324=twstock.realtime.get('2324')  
         if realdata2324['success']:     
              realprice2324 = realdata2324['realtime']['latest_trade_price']                      
              await message.channel.send('仁寶目前股價：' + realprice2324)
              
    elif message.content == '-t 2327': 
         realdata2327=twstock.realtime.get('2327')  
         if realdata2327['success']:     
              realprice2327 = realdata2327['realtime']['latest_trade_price']                     
              await message.channel.send('國巨目前股價：' + realprice2327)
              
    elif message.content == '-t 2328': 
         realdata2328=twstock.realtime.get('2328')  
         if realdata2328['success']:     
              realprice2328 = realdata2328['realtime']['latest_trade_price']                     
              await message.channel.send('廣宇目前股價：' + realprice2328)
              
    elif message.content == '-t 2329': 
         realdata2329=twstock.realtime.get('2329')  
         if realdata2329['success']:     
              realprice2329 = realdata2329['realtime']['latest_trade_price']                     
              await message.channel.send('華泰目前股價：' + realprice2329)
              
    elif message.content == '-t 2331': 
         realdata2331=twstock.realtime.get('2331')  
         if realdata2331['success']:     
              realprice2331 = realdata2331['realtime']['latest_trade_price']                     
              await message.channel.send('精英目前股價：' + realprice2331)
              
    elif message.content == '-t 2332': 
         realdata2332=twstock.realtime.get('2332')  
         if realdata2332['success']:     
              realprice2332 = realdata2332['realtime']['latest_trade_price']                      
              await message.channel.send('友訊目前股價：' + realprice2332)
              
    elif message.content == '-t 2337': 
         realdata2337=twstock.realtime.get('2337')  
         if realdata2337['success']:     
              realprice2337 = realdata2337['realtime']['latest_trade_price']                     
              await message.channel.send('旺宏目前股價：' + realprice2337)
              
    elif message.content == '-t 2338': 
         realdata2338=twstock.realtime.get('2338')  
         if realdata2338['success']:     
              realprice2338 = realdata2338['realtime']['latest_trade_price']                      
              await message.channel.send('光罩目前股價：' + realprice2338)
              
    elif message.content == '-t 2340': 
         realdata2340=twstock.realtime.get('2340')  
         if realdata2340['success']:     
              realprice2340 = realdata2340['realtime']['latest_trade_price']                      
              await message.channel.send('光磊目前股價：' + realprice2340)
              
    elif message.content == '-t 2342': 
         realdata2342=twstock.realtime.get('2342')  
         if realdata2342['success']:     
              realprice2342 = realdata2342['realtime']['latest_trade_price']                    
              await message.channel.send('茂矽目前股價：' + realprice2342)
              
    elif message.content == '-t 2344': 
         realdata2344=twstock.realtime.get('2344')  
         if realdata2344['success']:     
              realprice2344 = realdata2344['realtime']['latest_trade_price']                    
              await message.channel.send('華邦電目前股價：' + realprice2344)
              
    elif message.content == '-t 2345': 
         realdata2345=twstock.realtime.get('2345')  
         if realdata2345['success']:     
              realprice2345 = realdata2345['realtime']['latest_trade_price']                     
              await message.channel.send('智邦目前股價：' + realprice2345)
              
    elif message.content == '-t 2347': 
         realdata2347=twstock.realtime.get('2347')  
         if realdata2347['success']:     
              realprice2347 = realdata2347['realtime']['latest_trade_price']                      
              await message.channel.send('聯強目前股價：' + realprice2347)
              
    elif message.content == '-t 2348': 
         realdata2348=twstock.realtime.get('2348')  
         if realdata2348['success']:     
              realprice2348 = realdata2348['realtime']['latest_trade_price']                     
              await message.channel.send('海悅目前股價：' + realprice2348)
              
    elif message.content == '-t 2349': 
         realdata2349=twstock.realtime.get('2349')  
         if realdata2349['success']:     
              realprice2349 = realdata2349['realtime']['latest_trade_price']             
              await message.channel.send('錸德目前股價：' + realprice2349)
              
    elif message.content == '-t 2351': 
         realdata2351=twstock.realtime.get('2351')  
         if realdata2351['success']:     
              realprice2351 = realdata2351['realtime']['latest_trade_price']                      
              await message.channel.send('順德目前股價：' + realprice2351)
              
    elif message.content == '-t 2352': 
         realdata2352=twstock.realtime.get('2352')  
         if realdata2352['success']:     
              realprice2352 = realdata2352['realtime']['latest_trade_price']                      
              await message.channel.send('佳世達目前股價：' + realprice2352)
              
    elif message.content == '-t 2353': 
         realdata2353=twstock.realtime.get('2353')  
         if realdata2353['success']:     
              realprice2353 = realdata2353['realtime']['latest_trade_price']             
              await message.channel.send('宏碁目前股價：' + realprice2353)
              
    elif message.content == '-t 2354': 
         realdata2354=twstock.realtime.get('2354')  
         if realdata2354['success']:     
              realprice2354 = realdata2354['realtime']['latest_trade_price']                      
              await message.channel.send('鴻準目前股價：' + realprice2354)
              
    elif message.content == '-t 2355': 
         realdata2355=twstock.realtime.get('2355')  
         if realdata2355['success']:     
              realprice2355 = realdata2355['realtime']['latest_trade_price']                      
              await message.channel.send('敬鵬目前股價：' + realprice2355)
              
    elif message.content == '-t 2356': 
         realdata2356=twstock.realtime.get('2356')  
         if realdata2356['success']:     
              realprice2356 = realdata2356['realtime']['latest_trade_price']                      
              await message.channel.send('英業達目前股價：' + realprice2356)
              
    elif message.content == '-t 2357': 
         realdata2357=twstock.realtime.get('2357')  
         if realdata2357['success']:     
              realprice2357 = realdata2357['realtime']['latest_trade_price']                      
              await message.channel.send('華碩目前股價：' + realprice2357)
             
    elif message.content == '-t 2358': 
         realdata2358=twstock.realtime.get('2358')  
         if realdata2358['success']:     
              realprice2358 = realdata2358['realtime']['latest_trade_price']                     
              await message.channel.send('廷鑫目前股價：' + realprice2358)
              
    elif message.content == '-t 2359': 
         realdata2359=twstock.realtime.get('2359')  
         if realdata2359['success']:     
              realprice2359 = realdata2359['realtime']['latest_trade_price']                      
              await message.channel.send('所羅門目前股價：' + realprice2359)
             
    elif message.content == '-t 2360': 
         realdata2360=twstock.realtime.get('2360')  
         if realdata2360['success']:     
              realprice2360 = realdata2360['realtime']['latest_trade_price']                      
              await message.channel.send('致茂目前股價：' + realprice2360)
              
    elif message.content == '-t 2362': 
         realdata=twstock.realtime.get('2362')  
         if realdata['success']:     
              realprice = realdata['realtime']['latest_trade_price']                      
              await message.channel.send('藍天目前股價：' + realprice)
              
    elif message.content == '-t 2363': 
         realdata2363=twstock.realtime.get('2363')  
         if realdata2363['success']:     
              realprice2363 = realdata2363['realtime']['latest_trade_price']                     
              await message.channel.send('矽統目前股價：' + realprice2363)
              
    elif message.content == '-t 2364': 
         realdata2364=twstock.realtime.get('2364')  
         if realdata2364['success']:     
              realprice2364 = realdata2364['realtime']['latest_trade_price']          #300              
              await message.channel.send('倫飛目前股價：' + realprice2364)
              
    elif message.content == '-t 2365': 
         realdata2365=twstock.realtime.get('2365')  
         if realdata2365['success']:     
              realprice2365 = realdata2365['realtime']['latest_trade_price']                      
              await message.channel.send('昆盈目前股價：' + realprice2365) 
              
    elif message.content == '-t 2367': 
         realdata2367=twstock.realtime.get('2367')  
         if realdata2367['success']:     
              realprice2367 = realdata2367['realtime']['latest_trade_price']                     
              await message.channel.send('燿華目前股價：' + realprice2367) 
              
    elif message.content == '-t 2368': 
         realdata2368=twstock.realtime.get('2368')  
         if realdata2368['success']:     
              realprice2368 = realdata2368['realtime']['latest_trade_price']                      
              await message.channel.send('金像電目前股價：' + realprice2368) 
              
    elif message.content == '-t 2369': 
         realdata2369=twstock.realtime.get('2369')  
         if realdata2369['success']:     
              realprice2369 = realdata2369['realtime']['latest_trade_price']                      
              await message.channel.send('菱生目前股價：' + realprice2369) 
              
    elif message.content == '-t 2371': 
         realdata2371=twstock.realtime.get('2371')  
         if realdata2371['success']:     
              realprice2371 = realdata2371['realtime']['latest_trade_price']                      
              await message.channel.send('大同目前股價：' + realprice2371) 
              
    elif message.content == '-t 2373': 
         realdata2373=twstock.realtime.get('2373')  
         if realdata2373['success']:     
              realprice2373 = realdata2373['realtime']['latest_trade_price']                      
              await message.channel.send('目前股價：' + realprice2373) 
              
    elif message.content == '-t 2374': 
         realdata2374=twstock.realtime.get('2374')  
         if realdata2374['success']:     
              realprice2374 = realdata2374['realtime']['latest_trade_price']                     
              await message.channel.send('佳能目前股價：' + realprice2374) 
              
    elif message.content == '-t 2375': 
         realdata2375=twstock.realtime.get('2375')  
         if realdata2375['success']:     
              realprice2375 = realdata2375['realtime']['latest_trade_price']                     
              await message.channel.send('凱美目前股價：' + realprice2375) 
              
    elif message.content == '-t 2376': 
         realdata2376=twstock.realtime.get('2376')  
         if realdata2376['success']:     
              realprice2376 = realdata2376['realtime']['latest_trade_price']                      
              await message.channel.send('技嘉目前股價：' + realprice2376) 
              
    elif message.content == '-t 2377': 
         realdata2377=twstock.realtime.get('2377')  
         if realdata2377['success']:     
              realprice2377 = realdata2377['realtime']['latest_trade_price']                    
              await message.channel.send('微星目前股價：' + realprice2377) 
              
    elif message.content == '-t 2379': 
         realdata2379=twstock.realtime.get('2379')  
         if realdata2379['success']:     
              realprice2379 = realdata2379['realtime']['latest_trade_price']                     
              await message.channel.send('瑞昱目前股價：' + realprice2379) 
              
    elif message.content == '-t 2380': 
         realdata2380=twstock.realtime.get('2380')  
         if realdata2380['success']:     
              realprice2380 = realdata2380['realtime']['latest_trade_price']                     
              await message.channel.send('虹光目前股價：' + realprice2380) 
              
    elif message.content == '-t 2382': 
         realdata2382=twstock.realtime.get('2382')  
         if realdata2382['success']:     
              realprice2382 = realdata2382['realtime']['latest_trade_price']                     
              await message.channel.send('廣達目前股價：' + realprice2382) 
              
    elif message.content == '-t 2383': 
         realdata2383=twstock.realtime.get('2383')  
         if realdata2383['success']:     
              realprice2383 = realdata2383['realtime']['latest_trade_price']                     
              await message.channel.send('台光電目前股價：' + realprice2383) 
              
    elif message.content == '-t 2385': 
         realdata2385=twstock.realtime.get('2385')  
         if realdata2385['success']:     
              realprice2385 = realdata2385['realtime']['latest_trade_price']                     
              await message.channel.send('群光目前股價：' + realprice2385) 
            
    elif message.content == '-t 2387': 
         realdata2387=twstock.realtime.get('2387')  
         if realdata2387['success']:     
              realprice2387 = realdata2387['realtime']['latest_trade_price']                      
              await message.channel.send('精元目前股價：' + realprice2387) 
              
    elif message.content == '-t 2388': 
         realdata2388=twstock.realtime.get('2388')  
         if realdata2388['success']:     
              realprice2388 = realdata2388['realtime']['latest_trade_price']                      
              await message.channel.send('威盛目前股價：' + realprice2388) 
              
    elif message.content == '-t 2390': 
         realdata2390=twstock.realtime.get('2390')  
         if realdata2390['success']:     
              realprice2390 = realdata2390['realtime']['latest_trade_price']                     
              await message.channel.send('云辰目前股價：' + realprice2390) 
              
    elif message.content == '-t 2392': 
         realdata2392=twstock.realtime.get('2392')  
         if realdata2392['success']:     
              realprice2392 = realdata2392['realtime']['latest_trade_price']                      
              await message.channel.send('正崴目前股價：' + realprice2392) 
              
    elif message.content == '-t 2393': 
         realdata2393=twstock.realtime.get('2393')  
         if realdata2393['success']:     
              realprice2393 = realdata2393['realtime']['latest_trade_price']            #320         
              await message.channel.send('億光目前股價：' + realprice2393) 
              
    elif message.content == '-t 2395': 
         realdata2395=twstock.realtime.get('2395')  
         if realdata2395['success']:     
              realprice2395 = realdata2395['realtime']['latest_trade_price']         #0             
              await message.channel.send('研華目前股價：' + realprice2395)    

    elif message.content == '-t 2397': 
          realdata2397=twstock.realtime.get('2397')  
          if realdata2397['success']:     
              realprice2397 = realdata2397['realtime']['latest_trade_price']                     
              await message.channel.send('友通目前股價：' + realprice2397) 
              
    elif message.content == '-t 2399': 
          realdata2399=twstock.realtime.get('2399')  
          if realdata2399['success']:     
              realprice2399 = realdata2399['realtime']['latest_trade_price']                     
              await message.channel.send('映泰目前股價：' + realprice2399) 
        
    elif message.content == '-t 2401': 
          realdata2401=twstock.realtime.get('2401')  
          if realdata2401['success']:     
              realprice2401 = realdata2401['realtime']['latest_trade_price']                     
              await message.channel.send('凌陽目前股價：' + realprice2401) 
              
    elif message.content == '-t 2402': 
          realdata2402=twstock.realtime.get('2402')  
          if realdata2402['success']:     
              realprice2402 = realdata2402['realtime']['latest_trade_price']                     
              await message.channel.send('毅嘉目前股價：' + realprice2402) 
              
    elif message.content == '-t 2404': 
          realdata2404=twstock.realtime.get('2404')  
          if realdata2404['success']:     
              realprice2404 = realdata2404['realtime']['latest_trade_price']                   
              await message.channel.send('漢唐目前股價：' + realprice2404) 
             
    elif message.content == '-t 2405': 
          realdata2405=twstock.realtime.get('2405')  
          if realdata2405['success']:     
              realprice2405 = realdata2405['realtime']['latest_trade_price']                      
              await message.channel.send('浩鑫目前股價：' + realprice2405) 
              
    elif message.content == '-t 2406': 
          realdata=twstock.realtime.get('2406')  
          if realdata['success']:     
              realprice = realdata['realtime']['latest_trade_price']                      
              await message.channel.send('國碩目前股價：' + realprice) 
              
    elif message.content == '-t 2408': 
          realdata2408=twstock.realtime.get('2408')  
          if realdata2408['success']:     
              realprice2408 = realdata2408['realtime']['latest_trade_price']                      
              await message.channel.send('南亞科目前股價：' + realprice2408) 
             
    elif message.content == '-t 2412': 
          realdata2412=twstock.realtime.get('2412')  
          if realdata2412['success']:     
              realprice2412 = realdata2412['realtime']['latest_trade_price']                      
              await message.channel.send('中華電目前股價：' + realprice2412) 
              
    elif message.content == '-t 2413': 
          realdata2413=twstock.realtime.get('2413')  
          if realdata2413['success']:     
              realprice2413 = realdata2413['realtime']['latest_trade_price']                      
              await message.channel.send('環科目前股價：' + realprice2413) 
              
    elif message.content == '-t 2414': 
          realdata2414=twstock.realtime.get('2414')  
          if realdata2414['success']:     
              realprice2414 = realdata2414['realtime']['latest_trade_price']                     
              await message.channel.send('精技目前股價：' + realprice2414) 
              
    elif message.content == '-t 2415': 
          realdata2415=twstock.realtime.get('2415')  
          if realdata2415['success']:     
              realprice2415 = realdata2415['realtime']['latest_trade_price']                      
              await message.channel.send('錩新目前股價：' + realprice2415) 
              
    elif message.content == '-t 2417': 
          realdata2417=twstock.realtime.get('2417')  
          if realdata2417['success']:     
              realprice2417 = realdata2417['realtime']['latest_trade_price']                     
              await message.channel.send('圓剛目前股價：' + realprice2417) 
              
    elif message.content == '-t 2419': 
          realdata2419=twstock.realtime.get('2419')  
          if realdata2419['success']:     
              realprice2419 = realdata2419['realtime']['latest_trade_price']                    
              await message.channel.send('仲琦目前股價：' + realprice2419) 
              
    elif message.content == '-t 2420': 
          realdata2420=twstock.realtime.get('2420')  
          if realdata2420['success']:     
              realprice2420 = realdata2420['realtime']['latest_trade_price']                     
              await message.channel.send('新巨目前股價：' + realprice2420) 
              
    elif message.content == '-t 2421': 
          realdata2421=twstock.realtime.get('2421')  
          if realdata2421['success']:     
              realprice2421 = realdata2421['realtime']['latest_trade_price']                      
              await message.channel.send('建準目前股價：' + realprice2421) 
              
    elif message.content == '-t 2423': 
          realdata2423=twstock.realtime.get('2423')  
          if realdata2423['success']:     
              realprice2423 = realdata2423['realtime']['latest_trade_price']                      
              await message.channel.send('固緯目前股價：' + realprice2423) 
              
    elif message.content == '-t 2424': 
          realdata2424=twstock.realtime.get('2424')  
          if realdata2424['success']:     
              realprice2424 = realdata2424['realtime']['latest_trade_price']         #340             
              await message.channel.send('隴華目前股價：' + realprice2424) 
              
    elif message.content == '-t 2425': 
          realdata2425=twstock.realtime.get('2425')  
          if realdata2425['success']:     
              realprice2425 = realdata2425['realtime']['latest_trade_price']                     
              await message.channel.send('承啟目前股價：' + realprice2425) 
              
    elif message.content == '-t 2426': 
          realdata2426=twstock.realtime.get('2426')  
          if realdata2426['success']:     
              realprice2426 = realdata2426['realtime']['latest_trade_price']                    
              await message.channel.send('鼎元目前股價：' + realprice2426) 
              
    elif message.content == '-t 2427': 
          realdata2427=twstock.realtime.get('2427')  
          if realdata2427['success']:     
              realprice2427 = realdata2427['realtime']['latest_trade_price']                     
              await message.channel.send('三商電目前股價：' + realprice2427) 
              
    elif message.content == '-t 2428': 
          realdata2428=twstock.realtime.get('2428')  
          if realdata2428['success']:     
              realprice2428 = realdata2428['realtime']['latest_trade_price']                     
              await message.channel.send('興勤目前股價：' + realprice2428) 
              
    elif message.content == '-t 2429': 
          realdata2429=twstock.realtime.get('2429')  
          if realdata2429['success']:     
              realprice2429 = realdata2429['realtime']['latest_trade_price']                     
              await message.channel.send('銘旺科目前股價：' + realprice2429) 
              
    elif message.content == '-t 2430': 
          realdata2430=twstock.realtime.get('2430')  
          if realdata2430['success']:     
              realprice2430 = realdata2430['realtime']['latest_trade_price']                      
              await message.channel.send('燦坤目前股價：' + realprice2430) 
              
    elif message.content == '-t 2431': 
          realdata2431=twstock.realtime.get('2431')  
          if realdata2431['success']:     
              realprice2431 = realdata2431['realtime']['latest_trade_price']                      
              await message.channel.send('聯昌目前股價：' + realprice2431) 
              
    elif message.content == '-t 2433': 
          realdata2433=twstock.realtime.get('2433')  
          if realdata2433['success']:     
              realprice2433 = realdata2433['realtime']['latest_trade_price']                     
              await message.channel.send('互盛電目前股價：' + realprice2433) 
              
    elif message.content == '-t 2434': 
          realdata2434=twstock.realtime.get('2434')  
          if realdata2434['success']:     
              realprice2434 = realdata2434['realtime']['latest_trade_price']                      
              await message.channel.send('統懋目前股價：' + realprice2434) 
              
    elif message.content == '-t 2436': 
          realdata2436=twstock.realtime.get('2436')  
          if realdata2436['success']:     
              realprice2436 = realdata2436['realtime']['latest_trade_price']                    
              await message.channel.send('偉詮電目前股價：' + realprice2436) 
              
    elif message.content == '-t 2438': 
          realdata2438=twstock.realtime.get('2438')  
          if realdata2438['success']:     
              realprice2438 = realdata2438['realtime']['latest_trade_price']                   
              await message.channel.send('翔耀目前股價：' + realprice2438) 
              
    elif message.content == '-t 2439': 
          realdata2439=twstock.realtime.get('2439')  
          if realdata2439['success']:     
              realprice2439 = realdata2439['realtime']['latest_trade_price']                     
              await message.channel.send('美律目前股價：' + realprice2439) 
              
    elif message.content == '-t 2440': 
          realdata2440=twstock.realtime.get('2440')  
          if realdata2440['success']:     
              realprice2440 = realdata2440['realtime']['latest_trade_price']                      
              await message.channel.send('太空梭目前股價：' + realprice2440) 
              
    elif message.content == '-t 2441': 
          realdata2441=twstock.realtime.get('2441')  
          if realdata2441['success']:     
              realprice2441 = realdata2441['realtime']['latest_trade_price']                     
              await message.channel.send('超豐目前股價：' + realprice2441) 
              
    elif message.content == '-t 2442': 
          realdata2442=twstock.realtime.get('2442')  
          if realdata2442['success']:     
              realprice2442 = realdata2442['realtime']['latest_trade_price']                      
              await message.channel.send('新美齊目前股價：' + realprice2442) 
              
    elif message.content == '-t 2443': 
          realdata2443=twstock.realtime.get('2443')  
          if realdata2443['success']:     
              realprice2443 = realdata2443['realtime']['latest_trade_price']                      
              await message.channel.send('億麗目前股價：' + realprice2443) 
              
    elif message.content == '-t 2444': 
          realdata2444=twstock.realtime.get('2444')  
          if realdata2444['success']:     
              realprice2444 = realdata2444['realtime']['latest_trade_price']                      
              await message.channel.send('兆勁目前股價：' + realprice2444) 
              
    elif message.content == '-t 2449': 
          realdata2449=twstock.realtime.get('2449')  
          if realdata2449['success']:     
              realprice2449 = realdata2449['realtime']['latest_trade_price']                      
              await message.channel.send('京元電子目前股價：' + realprice2449) 
              
    elif message.content == '-t 2450': 
          realdata2450=twstock.realtime.get('2450')  
          if realdata2450['success']:     
              realprice2450 = realdata2450['realtime']['latest_trade_price']                     
              await message.channel.send('神腦目前股價：' + realprice2450) 
              
    elif message.content == '-t 2451': 
          realdata2451=twstock.realtime.get('2451')  
          if realdata2451['success']:     
              realprice2451 = realdata2451['realtime']['latest_trade_price']                     
              await message.channel.send('創見目前股價：' + realprice2451)
              
    elif message.content == '-t 2453': 
          realdata2453=twstock.realtime.get('2453')  
          if realdata2453['success']:     
              realprice2453 = realdata2453['realtime']['latest_trade_price']                      
              await message.channel.send('凌群目前股價：' + realprice2453)
              
    elif message.content == '-t 2454': 
          realdata2454=twstock.realtime.get('2454')  
          if realdata2454['success']:     
              realprice2454 = realdata2454['realtime']['latest_trade_price']                     
              await message.channel.send('聯發科目前股價：' + realprice2454)
              
    elif message.content == '-t 2455': 
          realdata2455=twstock.realtime.get('2455')  
          if realdata2455['success']:     
              realprice2455 = realdata2455['realtime']['latest_trade_price']                      
              await message.channel.send('全新目前股價：' + realprice2455)
              
    elif message.content == '-t 2456': 
          realdata2456=twstock.realtime.get('2456')  
          if realdata2456['success']:     
              realprice2456 = realdata2456['realtime']['latest_trade_price']                     
              await message.channel.send('奇力新目前股價：' + realprice2456)
              
    elif message.content == '-t 2457': 
          realdata2457=twstock.realtime.get('2457')  
          if realdata2457['success']:     
              realprice2457 = realdata2457['realtime']['latest_trade_price']                     
              await message.channel.send('飛宏目前股價：' + realprice2457)
              
    elif message.content == '-t 2458': 
          realdata2458=twstock.realtime.get('2458')  
          if realdata2458['success']:     
              realprice2458 = realdata2458['realtime']['latest_trade_price']                    
              await message.channel.send('義隆目前股價：' + realprice2458)
             
    elif message.content == '-t 2459': 
          realdata2459=twstock.realtime.get('2459')  
          if realdata2459['success']:     
              realprice2459 = realdata2459['realtime']['latest_trade_price']                     
              await message.channel.send('敦吉目前股價：' + realprice2459)
              
    elif message.content == '-t 2460': 
          realdata2460=twstock.realtime.get('2460')  
          if realdata2460['success']:     
              realprice2460 = realdata2460['realtime']['latest_trade_price']                      
              await message.channel.send('建通目前股價：' + realprice2460)
              
    elif message.content == '-t 2461': 
          realdata2461=twstock.realtime.get('2461')  
          if realdata2461['success']:     
              realprice2461 = realdata2461['realtime']['latest_trade_price']                      
              await message.channel.send('光群雷目前股價：' + realprice2461)
              
    elif message.content == '-t 2462': 
          realdata2462=twstock.realtime.get('2462')  
          if realdata2462['success']:     
              realprice2462 = realdata2462['realtime']['latest_trade_price']                      
              await message.channel.send('良得電目前股價：' + realprice2462)
              
    elif message.content == '-t 2464': 
          realdata2464=twstock.realtime.get('2464')  
          if realdata2464['success']:     
              realprice2464 = realdata2464['realtime']['latest_trade_price']                     
              await message.channel.send('盟立目前股價：' + realprice2464)
                            
    elif message.content == '-t 2465': 
          realdata2465=twstock.realtime.get('2465')  
          if realdata2465['success']:     
              realprice2465 = realdata2465['realtime']['latest_trade_price']                     
              await message.channel.send('麗臺目前股價：' + realprice2465)
              
    elif message.content == '-t 2466': 
          realdata2466=twstock.realtime.get('2466')  
          if realdata2466['success']:     
              realprice2466 = realdata2466['realtime']['latest_trade_price']                      
              await message.channel.send('冠西電目前股價：' + realprice2466)
              
    elif message.content == '-t 2467': 
          realdata2467=twstock.realtime.get('2467')  
          if realdata2467['success']:     
              realprice2467 = realdata2467['realtime']['latest_trade_price']                    
              await message.channel.send('志聖目前股價：' + realprice2467)
              
    elif message.content == '-t 2468': 
          realdata2468=twstock.realtime.get('2468')  
          if realdata2468['success']:     
              realprice2468 = realdata2468['realtime']['latest_trade_price']                      
              await message.channel.send('華經目前股價：' + realprice2468)
              
    elif message.content == '-t 2471': 
          realdata2471=twstock.realtime.get('2471')  
          if realdata2471['success']:     
              realprice2471 = realdata2471['realtime']['latest_trade_price']                      
              await message.channel.send('資通目前股價：' + realprice2471)
              
    elif message.content == '-t 2472': 
          realdata2472=twstock.realtime.get('2472')  
          if realdata2472['success']:     
              realprice2472 = realdata2472['realtime']['latest_trade_price']                      
              await message.channel.send('立隆電目前股價：' + realprice2472)
                  
    elif message.content == '-t 2474': 
          realdata2474=twstock.realtime.get('2474')  
          if realdata2474['success']:     
              realprice2474 = realdata2474['realtime']['latest_trade_price']                      
              await message.channel.send('可成目前股價：' + realprice2474)
              
    elif message.content == '-t 2476': 
          realdata2476=twstock.realtime.get('2476')  
          if realdata2476['success']:     
              realprice2476 = realdata2476['realtime']['latest_trade_price']                      
              await message.channel.send('鉅祥目前股價：' + realprice2476)
              
    elif message.content == '-t 2477': 
          realdata2477=twstock.realtime.get('2477')  
          if realdata2477['success']:     
              realprice2477 = realdata2477['realtime']['latest_trade_price']                     
              await message.channel.send('美隆電目前股價：' + realprice2477)
              
    elif message.content == '-t 2478': 
          realdata2478=twstock.realtime.get('2478')  
          if realdata2478['success']:     
              realprice2478 = realdata2478['realtime']['latest_trade_price']                     
              await message.channel.send('大毅目前股價：' + realprice2478)
              
    elif message.content == '-t 2480': 
          realdata2480=twstock.realtime.get('2480')  
          if realdata2480['success']:     
              realprice2480 = realdata2480['realtime']['latest_trade_price']                      
              await message.channel.send('敦陽科目前股價：' + realprice2480)
              
    elif message.content == '-t 2481': 
          realdata2481=twstock.realtime.get('2481')  
          if realdata2481['success']:     
              realprice2481 = realdata2481['realtime']['latest_trade_price']                     
              await message.channel.send('強茂目前股價：' + realprice2481)
              
    elif message.content == '-t 2482': 
          realdata2482=twstock.realtime.get('2482')  
          if realdata2482['success']:     
              realprice2482 = realdata2482['realtime']['latest_trade_price']                    
              await message.channel.send('連宇目前股價：' + realprice2482)
              
    elif message.content == '-t 2483': 
          realdata2483=twstock.realtime.get('2483')  
          if realdata2483['success']:     
              realprice2483 = realdata2483['realtime']['latest_trade_price']                     
              await message.channel.send('百容目前股價：' + realprice2483)
              
    elif message.content == '-t 2484': 
          realdata2484=twstock.realtime.get('2484')  
          if realdata2484['success']:     
              realprice2484 = realdata2484['realtime']['latest_trade_price']                     
              await message.channel.send('希華目前股價：' + realprice2484)
              
    elif message.content == '-t 2485': 
          realdata2485=twstock.realtime.get('2485')  
          if realdata2485['success']:     
              realprice2485 = realdata2485['realtime']['latest_trade_price']                     
              await message.channel.send('兆赫目前股價：' + realprice2485)
              
    elif message.content == '-t 2486': 
          realdata2486=twstock.realtime.get('2486')  
          if realdata2486['success']:     
              realprice2486 = realdata2486['realtime']['latest_trade_price']                    
              await message.channel.send('一詮目前股價：' + realprice2486)
              
    elif message.content == '-t 2488': 
          realdata2488=twstock.realtime.get('2488')  
          if realdata2488['success']:     
              realprice2488 = realdata2488['realtime']['latest_trade_price']                      
              await message.channel.send('漢平目前股價：' + realprice2488)
              
    elif message.content == '-t 2489': 
          realdata2489=twstock.realtime.get('2489')  
          if realdata2489['success']:     
              realprice2489 = realdata2489['realtime']['latest_trade_price']                     
              await message.channel.send('瑞軒目前股價：' + realprice2489)
              
    elif message.content == '-t 2491': 
          realdata2491=twstock.realtime.get('2491')  
          if realdata2491['success']:     
              realprice2491 = realdata2491['realtime']['latest_trade_price']                     
              await message.channel.send('吉祥全目前股價：' + realprice2491)
              
    elif message.content == '-t 2492': 
          realdata2492=twstock.realtime.get('2492')  
          if realdata2492['success']:     
              realprice2492 = realdata2492['realtime']['latest_trade_price']                      
              await message.channel.send('華新科目前股價：' + realprice2492)
              
    elif message.content == '-t 2493': 
          realdata2493=twstock.realtime.get('2493')  
          if realdata2493['success']:     
              realprice2493 = realdata2493['realtime']['latest_trade_price']                      
              await message.channel.send('揚博目前股價：' + realprice2493)
              
    elif message.content == '-t 2495': 
          realdata2495=twstock.realtime.get('2495')  
          if realdata2495['success']:     
              realprice2495 = realdata2495['realtime']['latest_trade_price']                     
              await message.channel.send('普安目前股價：' + realprice2495)
              
    elif message.content == '-t 2496': 
          realdata2496=twstock.realtime.get('2496')  
          if realdata2496['success']:     
              realprice2496 = realdata2496['realtime']['latest_trade_price']                      
              await message.channel.send('卓越目前股價：' + realprice2496)
              
    elif message.content == '-t 2497': 
          realdata2497=twstock.realtime.get('2497')  
          if realdata2497['success']:     
              realprice2497 = realdata2497['realtime']['latest_trade_price']                    
              await message.channel.send('怡利電目前股價：' + realprice2497)
              
    elif message.content == '-t 2498': 
          realdata2498=twstock.realtime.get('2498')  
          if realdata2498['success']:     
              realprice2498 = realdata2498['realtime']['latest_trade_price']                   
              await message.channel.send('宏達電目前股價：' + realprice2498)
              
    elif message.content == '-t 2501': 
          realdata2501=twstock.realtime.get('2501')  
          if realdata2501['success']:     
              realprice2501 = realdata2501['realtime']['latest_trade_price']                      
              await message.channel.send('國建目前股價：' + realprice2501)
              
    elif message.content == '-t 2504': 
          realdata2504=twstock.realtime.get('2504')  
          if realdata2504['success']:     
              realprice2504 = realdata2504['realtime']['latest_trade_price']                      
              await message.channel.send('國產目前股價：' + realprice2504)
              
    elif message.content == '-t 2505': 
          realdata2505=twstock.realtime.get('2505')  
          if realdata2505['success']:     
              realprice2505 = realdata2505['realtime']['latest_trade_price']          #400            
              await message.channel.send('國揚目前股價：' + realprice2505)

    elif message.content == '-t 2506': 
          realdata2506=twstock.realtime.get('2506')  
          if realdata2506['success']:     
              realprice2506 = realdata2506['realtime']['latest_trade_price']                     
              await message.channel.send('太設目前股價：' + realprice2506)
              
    elif message.content == '-t 2509': 
          realdata2509=twstock.realtime.get('2509')  
          if realdata2509['success']:     
              realprice2509 = realdata2509['realtime']['latest_trade_price']                      
              await message.channel.send('全坤建目前股價：' + realprice2509)
              
    elif message.content == '-t 2511': 
          realdata2511=twstock.realtime.get('2511')  
          if realdata2511['success']:     
              realprice2511 = realdata2511['realtime']['latest_trade_price']                     
              await message.channel.send('太子目前股價：' + realprice2511)
              
    elif message.content == '-t 2514': 
          realdata2514=twstock.realtime.get('2514')  
          if realdata2514['success']:     
              realprice2514 = realdata2514['realtime']['latest_trade_price']                      
              await message.channel.send('龍邦目前股價：' + realprice2514)
              
    elif message.content == '-t 2515': 
          realdata2515=twstock.realtime.get('2515')  
          if realdata2515['success']:     
              realprice2515 = realdata2515['realtime']['latest_trade_price']                     
              await message.channel.send('中工目前股價：' + realprice2515)
              
    elif message.content == '-t 2516': 
          realdata2516=twstock.realtime.get('2516')  
          if realdata2516['success']:     
              realprice2516 = realdata2516['realtime']['latest_trade_price']                     
              await message.channel.send('新建目前股價：' + realprice2516)
              
    elif message.content == '-t 2520': 
          realdata2520=twstock.realtime.get('2520')  
          if realdata2520['success']:     
              realprice2520 = realdata2520['realtime']['latest_trade_price']                      
              await message.channel.send('冠德目前股價：' + realprice2520)
              
    elif message.content == '-t 2524': 
          realdata2524=twstock.realtime.get('2524')  
          if realdata2524['success']:     
              realprice2524 = realdata2524['realtime']['latest_trade_price']                      
              await message.channel.send('京城目前股價：' + realprice2524)
              
    elif message.content == '-t 2527': 
          realdata2527=twstock.realtime.get('2527')  
          if realdata2527['success']:     
              realprice2527 = realdata2527['realtime']['latest_trade_price']                     
              await message.channel.send('宏璟目前股價：' + realprice2527)
              
    elif message.content == '-t 2528': 
          realdata2528=twstock.realtime.get('2528')  
          if realdata2528['success']:     
              realprice2528 = realdata2528['realtime']['latest_trade_price']                      
              await message.channel.send('皇普目前股價：' + realprice2528)
              
    elif message.content == '-t 2530': 
          realdata2530=twstock.realtime.get('2530')  
          if realdata2530['success']:     
              realprice2530 = realdata2530['realtime']['latest_trade_price']                      
              await message.channel.send('華建目前股價：' + realprice2530)
              
    elif message.content == '-t 2534': 
          realdata2534=twstock.realtime.get('2534')  
          if realdata2534['success']:     
              realprice2534 = realdata2534['realtime']['latest_trade_price']                      
              await message.channel.send('宏盛目前股價：' + realprice2534)
             
              
    elif message.content == '-t 2535': 
          realdata2535=twstock.realtime.get('2535')  
          if realdata2535['success']:     
              realprice2535 = realdata2535['realtime']['latest_trade_price']                    
              await message.channel.send('達欣工目前股價：' + realprice2535)
              
    elif message.content == '-t 2536': 
          realdata2536=twstock.realtime.get('2536')  
          if realdata2536['success']:     
              realprice2536 = realdata2536['realtime']['latest_trade_price']                    
              await message.channel.send('宏普目前股價：' + realprice2536)
              
    elif message.content == '-t 2537': 
          realdata2537=twstock.realtime.get('2537')  
          if realdata2537['success']:     
              realprice2537 = realdata2537['realtime']['latest_trade_price']                      
              await message.channel.send('聯上發目前股價：' + realprice2537)
              
    elif message.content == '-t 2538': 
          realdata2538=twstock.realtime.get('2538')  
          if realdata2538['success']:     
              realprice2538 = realdata2538['realtime']['latest_trade_price']                     
              await message.channel.send('基泰目前股價：' + realprice2538)
              
    elif message.content == '-t 2539': 
          realdata2539=twstock.realtime.get('2539')  
          if realdata2539['success']:     
              realprice2539 = realdata2539['realtime']['latest_trade_price']                      
              await message.channel.send('櫻花建目前股價：' + realprice2539)
              
    elif message.content == '-t 2540': 
          realdata2540=twstock.realtime.get('2540')  
          if realdata2540['success']:     
              realprice2540 = realdata2540['realtime']['latest_trade_price']                     
              await message.channel.send('愛山林目前股價：' + realprice2540)              
              
              
    elif message.content == '-t 2542': 
          realdata2542=twstock.realtime.get('2542')  
          if realdata2542['success']:     
              realprice2542 = realdata2542['realtime']['latest_trade_price']                      
              await message.channel.send('興富發目前股價：' + realprice2542)
              
    elif message.content == '-t 2543': 
          realdata2543=twstock.realtime.get('2543')  
          if realdata2543['success']:     
              realprice2543 = realdata2543['realtime']['latest_trade_price']                      
              await message.channel.send('皇昌目前股價：' + realprice2543)
              
    elif message.content == '-t 2545': 
          realdata2545=twstock.realtime.get('2545')  
          if realdata2545['success']:     
              realprice2545 = realdata2545['realtime']['latest_trade_price']                    
              await message.channel.send('皇翔目前股價：' + realprice2545)
              
    elif message.content == '-t 2546': 
          realdata2546=twstock.realtime.get('2546')  
          if realdata2546['success']:     
              realprice2546 = realdata2546['realtime']['latest_trade_price']                     
              await message.channel.send('根基目前股價：' + realprice2546)
              
    elif message.content == '-t 2547': 
          realdata2547=twstock.realtime.get('2547')  
          if realdata2547['success']:     
              realprice2547 = realdata2547['realtime']['latest_trade_price']                     
              await message.channel.send('日勝生目前股價：' + realprice2547)
              
    elif message.content == '-t 2548': 
          realdata2548=twstock.realtime.get('2548')  
          if realdata2548['success']:     
              realprice2548 = realdata2548['realtime']['latest_trade_price']                     
              await message.channel.send('華固目前股價：' + realprice2548)             
              
              
    elif message.content == '-t 2597': 
          realdata2597=twstock.realtime.get('2597')  
          if realdata2597['success']:     
              realprice2597 = realdata2597['realtime']['latest_trade_price']                      
              await message.channel.send('潤弘目前股價：' + realprice2597)
              
    elif message.content == '-t 2601': 
          realdata2601=twstock.realtime.get('2601')  
          if realdata2601['success']:     
              realprice2601 = realdata2601['realtime']['latest_trade_price']                     
              await message.channel.send('益航目前股價：' + realprice2601)
              
    elif message.content == '-t 2605': 
          realdata2605=twstock.realtime.get('2605')  
          if realdata2605['success']:     
              realprice2605 = realdata2605['realtime']['latest_trade_price']                      
              await message.channel.send('新興目前股價：' + realprice2605)
              
    elif message.content == '-t 2606': 
          realdata2606=twstock.realtime.get('2606')  
          if realdata2606['success']:     
              realprice2606 = realdata2606['realtime']['latest_trade_price']                      
              await message.channel.send('裕民目前股價：' + realprice2606)
              
    elif message.content == '-t 2607': 
          realdata2607=twstock.realtime.get('2607')  
          if realdata2607['success']:     
              realprice2607 = realdata2607['realtime']['latest_trade_price']                     
              await message.channel.send('榮運目前股價：' + realprice2607)
              
    elif message.content == '-t 2608': 
          realdata2608=twstock.realtime.get('2608')  
          if realdata2608['success']:     
              realprice2608 = realdata2608['realtime']['latest_trade_price']                     
              await message.channel.send('嘉里大榮目前股價：' + realprice2608)              

    elif message.content == '-t 2610': 
          realdata2610=twstock.realtime.get('2610')  
          if realdata2610['success']:     
              realprice2610 = realdata2610['realtime']['latest_trade_price']                      
              await message.channel.send('華航目前股價：' + realprice2610)
              
    elif message.content == '-t 2611': 
          realdata2611=twstock.realtime.get('2611')  
          if realdata2611['success']:     
              realprice2611 = realdata2611['realtime']['latest_trade_price']                      
              await message.channel.send('志信目前股價：' + realprice2611)
              
    elif message.content == '-t 2612': 
          realdata2612=twstock.realtime.get('2612')  
          if realdata2612['success']:     
              realprice2612 = realdata2612['realtime']['latest_trade_price']                    
              await message.channel.send('中航目前股價：' + realprice2612)
              
    elif message.content == '-t 2613': 
          realdata2613=twstock.realtime.get('2613')  
          if realdata2613['success']:     
              realprice2613 = realdata2613['realtime']['latest_trade_price']                   
              await message.channel.send('中櫃目前股價：' + realprice2613)

    elif message.content == '-t 2614': 
          realdata2614=twstock.realtime.get('2614')  
          if realdata2614['success']:     
              realprice2614 = realdata2614['realtime']['latest_trade_price']                    
              await message.channel.send('東森目前股價：' + realprice2614)
              
    elif message.content == '-t 2615': 
          realdata2615=twstock.realtime.get('2615')  
          if realdata2615['success']:     
              realprice2615 = realdata2615['realtime']['latest_trade_price']                   
              await message.channel.send('萬海目前股價：' + realprice2615)
              
    elif message.content == '-t 2616': 
          realdata2616=twstock.realtime.get('2616')  
          if realdata2616['success']:     
              realprice2616 = realdata2616['realtime']['latest_trade_price']                     
              await message.channel.send('山隆目前股價：' + realprice2616)
              
    elif message.content == '-t 2617': 
          realdata2617=twstock.realtime.get('2617')  
          if realdata2617['success']:     
              realprice2617 = realdata2617['realtime']['latest_trade_price']                    
              await message.channel.send('台航目前股價：' + realprice2617)              

    elif message.content == '-t 2618': 
          realdata2618=twstock.realtime.get('2618')  
          if realdata2618['success']:     
              realprice2618 = realdata2618['realtime']['latest_trade_price']                   
              await message.channel.send('長榮航目前股價：' + realprice2618)
              
    elif message.content == '-t 2630': 
          realdata2630=twstock.realtime.get('2630')  
          if realdata2630['success']:     
              realprice2630 = realdata2630['realtime']['latest_trade_price']                    
              await message.channel.send('亞航目前股價：' + realprice2630)
              
    elif message.content == '-t 2633': 
          realdata2633=twstock.realtime.get('2633')  
          if realdata2633['success']:     
              realprice2633 = realdata2633['realtime']['latest_trade_price']                   
              await message.channel.send('台灣高鐵目前股價：' + realprice2633)
              
    elif message.content == '-t 2634': 
          realdata2634=twstock.realtime.get('2634')  
          if realdata2634['success']:     
              realprice2634 = realdata2634['realtime']['latest_trade_price']                      
              await message.channel.send('漢翔目前股價：' + realprice2634)              

    elif message.content == '-t 2636': 
          realdata2636=twstock.realtime.get('2636')  
          if realdata2636['success']:     
              realprice2636 = realdata2636['realtime']['latest_trade_price']                      
              await message.channel.send('台驊投控目前股價：' + realprice2636)
              
    elif message.content == '-t 2637': 
          realdata2637=twstock.realtime.get('2637')  
          if realdata2637['success']:     
              realprice2637 = realdata2637['realtime']['latest_trade_price']                      
              await message.channel.send('慧洋-KY目前股價：' + realprice2637)
              
    elif message.content == '-t 2642': 
          realdata2642=twstock.realtime.get('2642')  
          if realdata2642['success']:     
              realprice2642 = realdata2642['realtime']['latest_trade_price']                    
              await message.channel.send('宅配通目前股價：' + realprice2642)
              
    elif message.content == '-t 2701': 
          realdata2701=twstock.realtime.get('2701')  
          if realdata2701['success']:     
              realprice2701 = realdata2701['realtime']['latest_trade_price']                  
              await message.channel.send('萬企目前股價：' + realprice2701)              

    elif message.content == '-t 2702': 
          realdata2702=twstock.realtime.get('2702')  
          if realdata2702['success']:     
              realprice2702 = realdata2702['realtime']['latest_trade_price']                   
              await message.channel.send('華園目前股價：' + realprice2702)
              
    elif message.content == '-t 2704': 
          realdata2704=twstock.realtime.get('2704')  
          if realdata2704['success']:     
              realprice2704 = realdata2704['realtime']['latest_trade_price']                    
              await message.channel.send('國賓目前股價：' + realprice2704)    #450
              
    elif message.content == '-t 2705': 
          realdata2705=twstock.realtime.get('2705')  
          if realdata2705['success']:     
              realprice2705 = realdata2705['realtime']['latest_trade_price']                     
              await message.channel.send('六福目前股價：' + realprice2705)
              
    elif message.content == '-t 2706': 
          realdata2706=twstock.realtime.get('2706')  
          if realdata2706['success']:     
              realprice2706 = realdata2706['realtime']['latest_trade_price']                    
              await message.channel.send('第一店目前股價：' + realprice2706)              

    elif message.content == '-t 2707': 
          realdata2707=twstock.realtime.get('2707')  
          if realdata2707['success']:     
              realprice2707 = realdata2707['realtime']['latest_trade_price']                    
              await message.channel.send('晶華目前股價：' + realprice2707)
              
    elif message.content == '-t 2712': 
          realdata2712=twstock.realtime.get('2712')  
          if realdata2712['success']:     
              realprice2712 = realdata2712['realtime']['latest_trade_price']                   
              await message.channel.send('遠雄來目前股價：' + realprice2712)
              
    elif message.content == '-t 2722': 
          realdata2722=twstock.realtime.get('2722')  
          if realdata2722['success']:     
              realprice2722 = realdata2722['realtime']['latest_trade_price']                  
              await message.channel.send('夏都目前股價：' + realprice2722)
              
    elif message.content == '-t 2723': 
          realdata2723=twstock.realtime.get('2723')  
          if realdata2723['success']:     
              realprice2723 = realdata2723['realtime']['latest_trade_price']                     
              await message.channel.send('美食-KY目前股價：' + realprice2723)              

    elif message.content == '-t 2727': 
          realdata2727=twstock.realtime.get('2727')  
          if realdata2727['success']:     
              realprice2727 = realdata2727['realtime']['latest_trade_price']                     
              await message.channel.send('王品目前股價：' + realprice2727)
              
    elif message.content == '-t 2731': 
          realdata2731=twstock.realtime.get('2731')  
          if realdata2731['success']:     
              realprice2731 = realdata2731['realtime']['latest_trade_price']                    
              await message.channel.send('雄獅目前股價：' + realprice2731)
              
    elif message.content == '-t 2739': 
          realdata2739=twstock.realtime.get('2739')  
          if realdata2739['success']:     
              realprice2739 = realdata2739['realtime']['latest_trade_price']                     
              await message.channel.send('寒舍目前股價：' + realprice2739)
              
    elif message.content == '-t 2748': 
          realdata2748=twstock.realtime.get('2748')  
          if realdata2748['success']:     
              realprice2748 = realdata2748['realtime']['latest_trade_price']                     
              await message.channel.send('雲品目前股價：' + realprice2748)              

    elif message.content == '-t 2753': 
          realdata2753=twstock.realtime.get('2753')  
          if realdata2753['success']:     
              realprice2753 = realdata2753['realtime']['latest_trade_price']                      
              await message.channel.send('八方雲集目前股價：' + realprice2753)
              
    elif message.content == '-t 2801': 
          realdata2801=twstock.realtime.get('2801')  
          if realdata2801['success']:     
              realprice2801 = realdata2801['realtime']['latest_trade_price']                      
              await message.channel.send('彰銀目前股價：' + realprice2801)
              
    elif message.content == '-t 2809': 
          realdata2809=twstock.realtime.get('2809')  
          if realdata2809['success']:     
              realprice2809 = realdata2809['realtime']['latest_trade_price']                      
              await message.channel.send('京城銀目前股價：' + realprice2809)
              
    elif message.content == '-t 2812': 
          realdata2812=twstock.realtime.get('2812')  
          if realdata2812['success']:     
              realprice2812 = realdata2812['realtime']['latest_trade_price']                      
              await message.channel.send('台中銀目前股價：' + realprice2812)              

    elif message.content == '-t 2816': 
          realdata2816=twstock.realtime.get('2816')  
          if realdata2816['success']:     
              realprice2816 = realdata2816['realtime']['latest_trade_price']                    
              await message.channel.send('旺旺保目前股價：' + realprice2816)
              
    elif message.content == '-t 2820': 
          realdata2820=twstock.realtime.get('2820')  
          if realdata2820['success']:     
              realprice2820 = realdata2820['realtime']['latest_trade_price']                      
              await message.channel.send('華票目前股價：' + realprice2820)
              
    elif message.content == '-t 2823': 
          realdata2823=twstock.realtime.get('2823')  
          if realdata2823['success']:     
              realprice2823 = realdata2823['realtime']['latest_trade_price']                      
              await message.channel.send('中壽目前股價：' + realprice2823)
              
    elif message.content == '-t 2832': 
          realdata2832=twstock.realtime.get('2832')  
          if realdata2832['success']:     
              realprice2832 = realdata2832['realtime']['latest_trade_price']                      
              await message.channel.send('台產目前股價：' + realprice2832)                
              
    elif message.content == '-t 2834': 
          realdata2834=twstock.realtime.get('2834')  
          if realdata2834['success']:     
              realprice2834 = realdata2834['realtime']['latest_trade_price']                      
              await message.channel.send('臺企銀目前股價：' + realprice2834)
              
    elif message.content == '-t 2836': 
          realdata2836=twstock.realtime.get('2836')  
          if realdata2836['success']:     
              realprice2836 = realdata2836['realtime']['latest_trade_price']                      
              await message.channel.send('高雄銀目前股價：' + realprice2836)
              
    elif message.content == '-t 2838': 
          realdata2838=twstock.realtime.get('2838')  
          if realdata2838['success']:     
              realprice2838 = realdata2838['realtime']['latest_trade_price']                      
              await message.channel.send('聯邦銀目前股價：' + realprice2838)
              
    elif message.content == '-t 2841': 
          realdata2841=twstock.realtime.get('2841')  
          if realdata2841['success']:     
              realprice2841 = realdata2841['realtime']['latest_trade_price']                     
              await message.channel.send('台開目前股價：' + realprice2841)              

    elif message.content == '-t 2845': 
          realdata2845=twstock.realtime.get('2845')  
          if realdata2845['success']:     
              realprice2845 = realdata2845['realtime']['latest_trade_price']                      
              await message.channel.send('遠東銀目前股價：' + realprice2845)
              
    elif message.content == '-t 2849': 
          realdata2849=twstock.realtime.get('2849')  
          if realdata2849['success']:     
              realprice2849 = realdata2849['realtime']['latest_trade_price']                      
              await message.channel.send('安泰銀目前股價：' + realprice2849)
              
    elif message.content == '-t 2850': 
          realdata2850=twstock.realtime.get('2850')  
          if realdata2850['success']:     
              realprice2850 = realdata2850['realtime']['latest_trade_price']                     
              await message.channel.send('新產目前股價：' + realprice2850)
              
    elif message.content == '-t 2851': 
          realdata2851=twstock.realtime.get('2851')  
          if realdata2851['success']:     
              realprice2851 = realdata2851['realtime']['latest_trade_price']                      
              await message.channel.send('中再保目前股價：' + realprice2851)              
              
    elif message.content == '-t 2852': 
          realdata2852=twstock.realtime.get('2852')  
          if realdata2852['success']:     
              realprice2852 = realdata2852['realtime']['latest_trade_price']                      
              await message.channel.send('第一保目前股價：' + realprice2852)
              
    elif message.content == '-t 2855': 
          realdata2855=twstock.realtime.get('2855')  
          if realdata2855['success']:     
              realprice2855 = realdata2855['realtime']['latest_trade_price']                      
              await message.channel.send('統一證目前股價：' + realprice2855)
              
    elif message.content == '-t 2867': 
          realdata2867=twstock.realtime.get('2867')  
          if realdata2867['success']:     
              realprice2867 = realdata2867['realtime']['latest_trade_price']                      
              await message.channel.send('三商壽目前股價：' + realprice2867)
              
    elif message.content == '-t 2880': 
          realdata2880=twstock.realtime.get('2880')  
          if realdata2880['success']:     
              realprice2880 = realdata2880['realtime']['latest_trade_price']                      
              await message.channel.send('華南金目前股價：' + realprice2880)              

    elif message.content == '-t 2881': 
          realdata2881=twstock.realtime.get('2881')  
          if realdata2881['success']:     
              realprice2881 = realdata2881['realtime']['latest_trade_price']                     
              await message.channel.send('富邦金目前股價：' + realprice2881)
              
    elif message.content == '-t 2882': 
          realdata2882=twstock.realtime.get('2882')  
          if realdata2882['success']:     
              realprice2882 = realdata2882['realtime']['latest_trade_price']             
              await message.channel.send('國泰金目前股價：' + realprice2882)
              
    elif message.content == '-t 2883': 
          realdata2883=twstock.realtime.get('2883')  
          if realdata2883['success']:     
              realprice2883 = realdata2883['realtime']['latest_trade_price']                     
              await message.channel.send('開發金目前股價：' + realprice2883)
              
    elif message.content == '-t 2884': 
          realdata2884=twstock.realtime.get('2884')  
          if realdata2884['success']:     
              realprice2884 = realdata2884['realtime']['latest_trade_price']                     
              await message.channel.send('玉山金目前股價：' + realprice2884) 
              
    elif message.content == '-t 2885': 
          realdata2885=twstock.realtime.get('2885')  
          if realdata2885['success']:     
              realprice2885 = realdata2885['realtime']['latest_trade_price']                      
              await message.channel.send('元大金目前股價：' + realprice2885)
              
    elif message.content == '-t 2886': 
          realdata2886=twstock.realtime.get('2886')  
          if realdata2886['success']:     
              realprice2886 = realdata2886['realtime']['latest_trade_price']                     
              await message.channel.send('兆豐金目前股價：' + realprice2886) 
              
    elif message.content == '-t 2887': 
          realdata2887=twstock.realtime.get('2887')  
          if realdata2887['success']:     
              realprice2887 = realdata2887['realtime']['latest_trade_price']                     
              await message.channel.send('台新金目前股價：' + realprice2887)             

    elif message.content == '-t 2888': 
          realdata2888=twstock.realtime.get('2888')  
          if realdata2888['success']:     
              realprice2888 = realdata2888['realtime']['latest_trade_price']                      
              await message.channel.send('新光金目前股價：' + realprice2888) 
              
    elif message.content == '-t 2889': 
          realdata2889=twstock.realtime.get('2889')  
          if realdata2889['success']:     
              realprice2889 = realdata2889['realtime']['latest_trade_price']                      
              await message.channel.send('國票金目前股價：' + realprice2889)
              
    elif message.content == '-t 2890': 
          realdata2890=twstock.realtime.get('2890')  
          if realdata2890['success']:     
              realprice2890 = realdata2890['realtime']['latest_trade_price']                      
              await message.channel.send('永豐金目前股價：' + realprice2890) 
              
    elif message.content == '-t 2891': 
          realdata2891=twstock.realtime.get('2891')  
          if realdata2891['success']:     
              realprice2891 = realdata2891['realtime']['latest_trade_price']                      
              await message.channel.send('中信金目前股價：' + realprice2891)            
 
    elif message.content == '-t 2892': 
          realdata2892=twstock.realtime.get('2892')  
          if realdata2892['success']:     
              realprice2892 = realdata2892['realtime']['latest_trade_price']                      
              await message.channel.send('第一金目前股價：' + realprice2892) 
              
    elif message.content == '-t 2897': 
          realdata2897=twstock.realtime.get('2897')  
          if realdata2897['success']:     
              realprice2897 = realdata2897['realtime']['latest_trade_price']                      
              await message.channel.send('王道銀行目前股價：' + realprice2897)             

    elif message.content == '-t 2901': 
          realdata2901=twstock.realtime.get('2901')  
          if realdata2901['success']:     
              realprice2901 = realdata2901['realtime']['latest_trade_price']                      
              await message.channel.send('欣欣目前股價：' + realprice2901) 
              
    elif message.content == '-t 2903': 
          realdata2903=twstock.realtime.get('2903')  
          if realdata2903['success']:     
              realprice2903 = realdata2903['realtime']['latest_trade_price']                      
              await message.channel.send('遠百目前股價：' + realprice2903)
              
    elif message.content == '-t 2904': 
          realdata2904=twstock.realtime.get('2904')  
          if realdata2904['success']:     
              realprice2904 = realdata2904['realtime']['latest_trade_price']                      
              await message.channel.send('匯僑目前股價：' + realprice2904) 
              
    elif message.content == '-t 2905': 
          realdata2905=twstock.realtime.get('2905')  
          if realdata2905['success']:     
              realprice2905 = realdata2905['realtime']['latest_trade_price']                      
              await message.channel.send('三商目前股價：' + realprice2905)

    elif message.content == '-t 2906': 
          realdata2906=twstock.realtime.get('2906')  
          if realdata2906['success']:     
              realprice2906 = realdata2906['realtime']['latest_trade_price']                      
              await message.channel.send('高林目前股價：' + realprice2906) 
              
    elif message.content == '-t 2908': 
          realdata2908=twstock.realtime.get('2908')  
          if realdata2908['success']:     
              realprice2908 = realdata2908['realtime']['latest_trade_price']                      
              await message.channel.send('特力目前股價：' + realprice2908)
              
    elif message.content == '-t 2910': 
          realdata2910=twstock.realtime.get('2910')  
          if realdata2910['success']:     
              realprice2910 = realdata2910['realtime']['latest_trade_price']                     
              await message.channel.send('統領目前股價：' + realprice2910)            #500    
    elif message.content == '-t 2911': 
          realdata2911=twstock.realtime.get('2911')  
          if realdata2911['success']:     
              realprice2911 = realdata2911['realtime']['latest_trade_price']                      
              await message.channel.send('麗嬰房目前股價：' + realprice2911)             

    elif message.content == '-t 2912': 
          realdata2912=twstock.realtime.get('2912')  
          if realdata2912['success']:     
              realprice2912 = realdata2912['realtime']['latest_trade_price']                      
              await message.channel.send('統一超目前股價：' + realprice2912) 
              
    elif message.content == '-t 2913': 
          realdata2913=twstock.realtime.get('2913')  
          if realdata2913['success']:     
              realprice2913 = realdata2913['realtime']['latest_trade_price']                      
              await message.channel.send('農林目前股價：' + realprice2913)
              
    elif message.content == '-t 2915': 
          realdata2915=twstock.realtime.get('2915')  
          if realdata2915['success']:     
              realprice2915 = realdata2915['realtime']['latest_trade_price']                     
              await message.channel.send('潤泰全目前股價：' + realprice2915) 
              
    elif message.content == '-t 2923': 
          realdata2923=twstock.realtime.get('2923')  
          if realdata2923['success']:     
              realprice2923 = realdata2923['realtime']['latest_trade_price']                      
              await message.channel.send('鼎固-KY目前股價：' + realprice2923)            
 
    elif message.content == '-t 2929': 
          realdata2929=twstock.realtime.get('2929')  
          if realdata2929['success']:     
              realprice2929 = realdata2929['realtime']['latest_trade_price']                      
              await message.channel.send('淘帝-KY目前股價：' + realprice2929) 
              
    elif message.content == '-t 2936': 
          realdata2936=twstock.realtime.get('2936')  
          if realdata2936['success']:     
              realprice2936 = realdata2936['realtime']['latest_trade_price']                    
              await message.channel.send('客思達-KY目前股價：' + realprice2936)             

    elif message.content == '-t 2939': 
          realdata2939=twstock.realtime.get('2939')  
          if realdata2939['success']:     
              realprice2939 = realdata2939['realtime']['latest_trade_price']                     
              await message.channel.send('凱羿-KY目前股價：' + realprice2939) 
              
    elif message.content == '-t 2945': 
          realdata2945=twstock.realtime.get('2945')  
          if realdata2945['success']:     
              realprice2945 = realdata2945['realtime']['latest_trade_price']                      
              await message.channel.send('三商家購目前股價：' + realprice2945)
              
    elif message.content == '-t 3002': 
          realdata3002=twstock.realtime.get('3002')  
          if realdata3002['success']:     
              realprice3002 = realdata3002['realtime']['latest_trade_price']                      
              await message.channel.send('歐格目前股價：' + realprice3002) 
              
    elif message.content == '-t 3003': 
          realdata3003=twstock.realtime.get('3003')  
          if realdata3003['success']:     
              realprice3003 = realdata3003['realtime']['latest_trade_price']                      
              await message.channel.send('健和興目前股價：' + realprice3003)              
              
    elif message.content == '-t 3004': 
          realdata3004=twstock.realtime.get('3004')  
          if realdata3004['success']:     
              realprice3004 = realdata3004['realtime']['latest_trade_price']                     
              await message.channel.send('豐達科目前股價：' + realprice3004)             

    elif message.content == '-t 3005': 
          realdata3005=twstock.realtime.get('3005')  
          if realdata3005['success']:     
              realprice3005 = realdata3005['realtime']['latest_trade_price']                      
              await message.channel.send('神基目前股價：' + realprice3005) 
              
    elif message.content == '-t 3006': 
          realdata3006=twstock.realtime.get('3006')  
          if realdata3006['success']:     
              realprice3006 = realdata3006['realtime']['latest_trade_price']                      
              await message.channel.send('晶豪科目前股價：' + realprice3006)
              
    elif message.content == '-t 3008': 
          realdata3008=twstock.realtime.get('3008')  
          if realdata3008['success']:     
              realprice3008 = realdata3008['realtime']['latest_trade_price']                      
              await message.channel.send('大立光目前股價：' + realprice3008) 
              
    elif message.content == '-t 3010': 
          realdata3010=twstock.realtime.get('3010')  
          if realdata3010['success']:     
              realprice3010 = realdata3010['realtime']['latest_trade_price']                      
              await message.channel.send('華立目前股價：' + realprice3010)            
 
    elif message.content == '-t 3011': 
          realdata3011=twstock.realtime.get('3011')  
          if realdata3011['success']:     
              realprice3011 = realdata3011['realtime']['latest_trade_price']                      
              await message.channel.send('今皓目前股價：' + realprice3011) 
              
    elif message.content == '-t 3013': 
          realdata3013=twstock.realtime.get('3013')  
          if realdata3013['success']:     
              realprice3013 = realdata3013['realtime']['latest_trade_price']                      
              await message.channel.send('晟銘電目前股價：' + realprice3013)             

    elif message.content == '-t 3014': 
          realdata3014=twstock.realtime.get('3014')  
          if realdata3014['success']:     
              realprice3014 = realdata3014['realtime']['latest_trade_price']                      
              await message.channel.send('聯陽目前股價：' + realprice3014) 
              
    elif message.content == '-t 3015': 
          realdata3015=twstock.realtime.get('3015')  
          if realdata3015['success']:     
              realprice3015 = realdata3015['realtime']['latest_trade_price']                      
              await message.channel.send('全漢目前股價：' + realprice3015)
              
    elif message.content == '-t 3016': 
          realdata3016=twstock.realtime.get('3016')  
          if realdata3016['success']:     
              realprice3016 = realdata3016['realtime']['latest_trade_price']                      
              await message.channel.send('嘉晶目前股價：' + realprice3016) 
              
    elif message.content == '-t 3017': 
          realdata3017=twstock.realtime.get('3017')  
          if realdata3017['success']:     
              realprice3017 = realdata3017['realtime']['latest_trade_price']                      
              await message.channel.send('奇鋐目前股價：' + realprice3017)              
              
    elif message.content == '-t 3018': 
          realdata3018=twstock.realtime.get('3018')  
          if realdata3018['success']:     
              realprice3018 = realdata3018['realtime']['latest_trade_price']                      
              await message.channel.send('同開目前股價：' + realprice3018)             

    elif message.content == '-t 3019': 
          realdata3019=twstock.realtime.get('3019')  
          if realdata3019['success']:     
              realprice3019 = realdata3019['realtime']['latest_trade_price']                      
              await message.channel.send('亞光目前股價：' + realprice3019) 
              
    elif message.content == '-t 3021': 
          realdata3021=twstock.realtime.get('3021')  
          if realdata3021['success']:     
              realprice3021 = realdata3021['realtime']['latest_trade_price']                      
              await message.channel.send('鴻名目前股價：' + realprice3021)
              
    elif message.content == '-t 3022': 
          realdata3022=twstock.realtime.get('3022')  
          if realdata3022['success']:     
              realprice3022 = realdata3022['realtime']['latest_trade_price']                      
              await message.channel.send('威強電目前股價：' + realprice3022) 
              
    elif message.content == '-t 3023': 
          realdata3023=twstock.realtime.get('3023')  
          if realdata3023['success']:     
              realprice3023 = realdata3023['realtime']['latest_trade_price']                      
              await message.channel.send('信邦目前股價：' + realprice3023)            
 
    elif message.content == '-t 3024': 
          realdata3024=twstock.realtime.get('3024')  
          if realdata3024['success']:     
              realprice3024 = realdata3024['realtime']['latest_trade_price']                      
              await message.channel.send('憶聲目前股價：' + realprice3024) 
              
    elif message.content == '-t 3025': 
          realdata3025=twstock.realtime.get('3025')  
          if realdata3025['success']:     
              realprice3025 = realdata3025['realtime']['latest_trade_price']                      
              await message.channel.send('星通目前股價：' + realprice3025)             

    elif message.content == '-t 3026': 
          realdata3026=twstock.realtime.get('3026')  
          if realdata3026['success']:     
              realprice3026 = realdata3026['realtime']['latest_trade_price']                     
              await message.channel.send('禾伸堂目前股價：' + realprice3026) 
              
    elif message.content == '-t 3027': 
          realdata3027=twstock.realtime.get('3027')  
          if realdata3027['success']:     
              realprice3027 = realdata3027['realtime']['latest_trade_price']                      
              await message.channel.send('盛達目前股價：' + realprice3027)
              
    elif message.content == '-t 3028': 
          realdata3028=twstock.realtime.get('3028')  
          if realdata3028['success']:     
              realprice3028 = realdata3028['realtime']['latest_trade_price']                     
              await message.channel.send('增你強目前股價：' + realprice3028) 
              
    elif message.content == '-t 3029': 
          realdata3029=twstock.realtime.get('3029')  
          if realdata3029['success']:     
              realprice3029 = realdata3029['realtime']['latest_trade_price']                      
              await message.channel.send('零壹目前股價：' + realprice3029)              
              
    elif message.content == '-t 3030': 
          realdata3030=twstock.realtime.get('3030')  
          if realdata3030['success']:     
              realprice3030 = realdata3030['realtime']['latest_trade_price']                      
              await message.channel.send('德律目前股價：' + realprice3030)             

    elif message.content == '-t 3031': 
          realdata3031=twstock.realtime.get('3031')  
          if realdata3031['success']:     
              realprice3031 = realdata3031['realtime']['latest_trade_price']                     
              await message.channel.send('佰鴻目前股價：' + realprice3031) 
              
    elif message.content == '-t 3032': 
          realdata3032=twstock.realtime.get('3032')  
          if realdata3032['success']:     
              realprice3032 = realdata3032['realtime']['latest_trade_price']                      
              await message.channel.send('偉訓目前股價：' + realprice3032)
              
    elif message.content == '-t 3033': 
          realdata3033=twstock.realtime.get('3033')  
          if realdata3033['success']:     
              realprice3033 = realdata3033['realtime']['latest_trade_price']                      
              await message.channel.send('威健目前股價：' + realprice3033) 
              
    elif message.content == '-t 3034': 
          realdata3034=twstock.realtime.get('3034')  
          if realdata3034['success']:     
              realprice3034 = realdata3034['realtime']['latest_trade_price']                      
              await message.channel.send('聯詠目前股價：' + realprice3034)            
 
    elif message.content == '-t 3035': 
          realdata3035=twstock.realtime.get('3035')  
          if realdata3035['success']:     
              realprice3035 = realdata3035['realtime']['latest_trade_price']                     
              await message.channel.send('智原目前股價：' + realprice3035) 
              
    elif message.content == '-t 3036': 
          realdata3036=twstock.realtime.get('3036')  
          if realdata3036['success']:     
              realprice3036 = realdata3036['realtime']['latest_trade_price']                      
              await message.channel.send('文曄目前股價：' + realprice3036)             

    elif message.content == '-t 3037': 
          realdata3037=twstock.realtime.get('3037')  
          if realdata3037['success']:     
              realprice3037 = realdata3037['realtime']['latest_trade_price']                      
              await message.channel.send('欣興目前股價：' + realprice3037) 
              
    elif message.content == '-t 3038': 
          realdata3038=twstock.realtime.get('3038')  
          if realdata3038['success']:     
              realprice3038 = realdata3038['realtime']['latest_trade_price']                      
              await message.channel.send('全台目前股價：' + realprice3038)
              
    elif message.content == '-t 3040': 
          realdata3040=twstock.realtime.get('3040')  
          if realdata3040['success']:     
              realprice3040 = realdata3040['realtime']['latest_trade_price']                      
              await message.channel.send('遠見目前股價：' + realprice3040) 
              
    elif message.content == '-t 3041': 
          realdata3041=twstock.realtime.get('3041')  
          if realdata3041['success']:     
              realprice3041 = realdata3041['realtime']['latest_trade_price']                      
              await message.channel.send('揚智目前股價：' + realprice3041)              
              
    elif message.content == '-t 3042': 
          realdata3042=twstock.realtime.get('3042')  
          if realdata3042['success']:     
              realprice3042 = realdata3042['realtime']['latest_trade_price']                      
              await message.channel.send('晶技目前股價：' + realprice3042)              
              
    elif message.content == '-t 3043': 
          realdata3043=twstock.realtime.get('3043')  
          if realdata3043['success']:     
              realprice3043 = realdata3043['realtime']['latest_trade_price']                      
              await message.channel.send('科風目前股價：' + realprice3043)             

    elif message.content == '-t 3044': 
          realdata3044=twstock.realtime.get('3044')  
          if realdata3044['success']:     
              realprice3044 = realdata3044['realtime']['latest_trade_price']                     
              await message.channel.send('健鼎目前股價：' + realprice3044) 
              
    elif message.content == '-t 3045': 
          realdata3045=twstock.realtime.get('3045')  
          if realdata3045['success']:     
              realprice3045 = realdata3045['realtime']['latest_trade_price']                      
              await message.channel.send('台灣大目前股價：' + realprice3045)
              
    elif message.content == '-t 3046': 
          realdata3046=twstock.realtime.get('3046')  
          if realdata3046['success']:     
              realprice3046 = realdata3046['realtime']['latest_trade_price']                     
              await message.channel.send('建碁目前股價：' + realprice3046) 
              
    elif message.content == '-t 3047': 
          realdata3047=twstock.realtime.get('3047')  
          if realdata3047['success']:     
              realprice3047 = realdata3047['realtime']['latest_trade_price']         #550             
              await message.channel.send('訊舟目前股價：' + realprice3047)            
 
    elif message.content == '-t 3048': 
          realdata3048=twstock.realtime.get('3048')  
          if realdata3048['success']:     
              realprice3048 = realdata3048['realtime']['latest_trade_price']                      
              await message.channel.send('益登目前股價：' + realprice3048) 
              
    elif message.content == '-t 3049': 
          realdata3049=twstock.realtime.get('3049')  
          if realdata3049['success']:     
              realprice3049 = realdata3049['realtime']['latest_trade_price']                     
              await message.channel.send('和鑫目前股價：' + realprice3049)             

    elif message.content == '-t 3050': 
          realdata3050=twstock.realtime.get('3050')  
          if realdata3050['success']:     
              realprice3050 = realdata3050['realtime']['latest_trade_price']                     
              await message.channel.send('鈺德目前股價：' + realprice3050) 
              
    elif message.content == '-t 3051': 
          realdata3051=twstock.realtime.get('3051')  
          if realdata3051['success']:     
              realprice3051 = realdata3051['realtime']['latest_trade_price']                    
              await message.channel.send('力特目前股價：' + realprice3051)
              
    elif message.content == '-t 3052': 
          realdata3052=twstock.realtime.get('3052')  
          if realdata3052['success']:     
              realprice3052 = realdata3052['realtime']['latest_trade_price']                      
              await message.channel.send('夆典目前股價：' + realprice3052) 
              
    elif message.content == '-t 3054': 
          realdata3054=twstock.realtime.get('3054')  
          if realdata3054['success']:     
              realprice3054 = realdata3054['realtime']['latest_trade_price']                      
              await message.channel.send('立萬利目前股價：' + realprice3054)              
              
    elif message.content == '-t 3055': 
          realdata3055=twstock.realtime.get('3055')  
          if realdata3055['success']:     
              realprice3055 = realdata3055['realtime']['latest_trade_price']                     
              await message.channel.send('蔚華科目前股價：' + realprice3055)             

    elif message.content == '-t 3056': 
          realdata3056=twstock.realtime.get('3056')  
          if realdata3056['success']:     
              realprice3056 = realdata3056['realtime']['latest_trade_price']                      
              await message.channel.send('總太目前股價：' + realprice3056) 
              
    elif message.content == '-t 3057': 
          realdata3057=twstock.realtime.get('3057')  
          if realdata3057['success']:     
              realprice3057 = realdata3057['realtime']['latest_trade_price']                      
              await message.channel.send('喬鼎目前股價：' + realprice3057)
              
    elif message.content == '-t 3058': 
          realdata3058=twstock.realtime.get('3058')  
          if realdata3058['success']:     
              realprice3058 = realdata3058['realtime']['latest_trade_price']                      
              await message.channel.send('立德目前股價：' + realprice3058) 
              
    elif message.content == '-t 3059': 
          realdata3059=twstock.realtime.get('3059')  
          if realdata3059['success']:     
              realprice3059 = realdata3059['realtime']['latest_trade_price']                      
              await message.channel.send('華晶科目前股價：' + realprice3059)            
 
    elif message.content == '-t 3060': 
          realdata3060=twstock.realtime.get('3060')  
          if realdata3060['success']:     
              realprice3060 = realdata3060['realtime']['latest_trade_price']                      
              await message.channel.send('銘異目前股價：' + realprice3060) 
              
    elif message.content == '-t 3062': 
          realdata3062=twstock.realtime.get('3062')  
          if realdata3062['success']:     
              realprice3062 = realdata3062['realtime']['latest_trade_price']                      
              await message.channel.send('建漢目前股價：' + realprice3062)             

    elif message.content == '-t 3090': 
          realdata3090=twstock.realtime.get('3090')  
          if realdata3090['success']:     
              realprice3090 = realdata3090['realtime']['latest_trade_price']                     
              await message.channel.send('日電貿目前股價：' + realprice3090) 
              
    elif message.content == '-t 3092': 
          realdata3092=twstock.realtime.get('3092')  
          if realdata3092['success']:     
              realprice3092 = realdata3092['realtime']['latest_trade_price']                      
              await message.channel.send('鴻碩目前股價：' + realprice3092)
              
    elif message.content == '-t 3094': 
          realdata3094=twstock.realtime.get('3094')  
          if realdata3094['success']:     
              realprice3094 = realdata3094['realtime']['latest_trade_price']                     
              await message.channel.send('聯傑目前股價：' + realprice3094) 
              
    elif message.content == '-t 3130': 
          realdata3130=twstock.realtime.get('3130')  
          if realdata3130['success']:     
              realprice3130 = realdata3130['realtime']['latest_trade_price']                      
              await message.channel.send('一零四目前股價：' + realprice3130)              
              
    elif message.content == '-t 3138': 
          realdata3138=twstock.realtime.get('3138')  
          if realdata3138['success']:     
              realprice3138 = realdata3138['realtime']['latest_trade_price']                      
              await message.channel.send('耀登目前股價：' + realprice3138)             

    elif message.content == '-t 3149': 
          realdata3149=twstock.realtime.get('3149')  
          if realdata3149['success']:     
              realprice3149 = realdata3149['realtime']['latest_trade_price']                      
              await message.channel.send('正達目前股價：' + realprice3149) 
              
    elif message.content == '-t 3164': 
          realdata3164=twstock.realtime.get('3164')  
          if realdata3164['success']:     
              realprice3164 = realdata3164['realtime']['latest_trade_price']                      
              await message.channel.send('景岳目前股價：' + realprice3164)
              
    elif message.content == '-t 3167': 
          realdata3167=twstock.realtime.get('3167')  
          if realdata3167['success']:     
              realprice3167 = realdata3167['realtime']['latest_trade_price']                      
              await message.channel.send('大量目前股價：' + realprice3167) 
              
    elif message.content == '-t 3189': 
          realdata3189=twstock.realtime.get('3189')  
          if realdata3189['success']:     
              realprice3189 = realdata3189['realtime']['latest_trade_price']                     
              await message.channel.send('景碩目前股價：' + realprice3189)            
 
    elif message.content == '-t 3209': 
          realdata3209=twstock.realtime.get('3209')  
          if realdata3209['success']:     
              realprice3209 = realdata3209['realtime']['latest_trade_price']                      
              await message.channel.send('全科目前股價：' + realprice3209) 
              
    elif message.content == '-t 3229': 
          realdata3229=twstock.realtime.get('3229')  
          if realdata3229['success']:     
              realprice3229 = realdata3229['realtime']['latest_trade_price']                     
              await message.channel.send('晟鈦目前股價：' + realprice3229)             

    elif message.content == '-t 3231': 
          realdata3231=twstock.realtime.get('3231')  
          if realdata3231['success']:     
              realprice3231 = realdata3231['realtime']['latest_trade_price']                     
              await message.channel.send('緯創目前股價：' + realprice3231) 
              
    elif message.content == '-t 3257': 
          realdata3257=twstock.realtime.get('3257')  
          if realdata3257['success']:     
              realprice3257 = realdata3257['realtime']['latest_trade_price']                     
              await message.channel.send('虹冠電目前股價：' + realprice3257)
              
    elif message.content == '-t 3266': 
          realdata3266=twstock.realtime.get('3266')  
          if realdata3266['success']:     
              realprice3266 = realdata3266['realtime']['latest_trade_price']                      
              await message.channel.send('昇陽目前股價：' + realprice3266) 
              
    elif message.content == '-t 3296': 
          realdata3296=twstock.realtime.get('3296')  
          if realdata3296['success']:     
              realprice3296 = realdata3296['realtime']['latest_trade_price']                      
              await message.channel.send('勝德目前股價：' + realprice3296)                
              
    elif message.content == '-t 3305': 
          realdata3305=twstock.realtime.get('3305')  
          if realdata3305['success']:     
              realprice3305 = realdata3305['realtime']['latest_trade_price']                      
              await message.channel.send('昇貿目前股價：' + realprice3305)              
              
    elif message.content == '-t 3308': 
          realdata3308=twstock.realtime.get('3308')  
          if realdata3308['success']:     
              realprice3308 = realdata3308['realtime']['latest_trade_price']                      
              await message.channel.send('聯德目前股價：' + realprice3308)             

    elif message.content == '-t 3311': 
          realdata3311=twstock.realtime.get('3311')  
          if realdata3311['success']:     
              realprice3311 = realdata3311['realtime']['latest_trade_price']                      
              await message.channel.send('閎暉目前股價：' + realprice3311) 
              
    elif message.content == '-t 3312': 
          realdata3312=twstock.realtime.get('3312')  
          if realdata3312['success']:     
              realprice3312 = realdata3312['realtime']['latest_trade_price']                      
              await message.channel.send('弘憶股目前股價：' + realprice3312)
              
    elif message.content == '-t 3321': 
          realdata3321=twstock.realtime.get('3321')  
          if realdata3321['success']:     
              realprice3321 = realdata3321['realtime']['latest_trade_price']                     
              await message.channel.send('同泰目前股價：' + realprice3321) 
              
    elif message.content == '-t 3338': 
          realdata3338=twstock.realtime.get('3338')  
          if realdata3338['success']:     
              realprice3338 = realdata3338['realtime']['latest_trade_price']                      
              await message.channel.send('泰碩目前股價：' + realprice3338)            
 
    elif message.content == '-t 3346': 
          realdata3346=twstock.realtime.get('3346')  
          if realdata3346['success']:     
              realprice3346 = realdata3346['realtime']['latest_trade_price']                      
              await message.channel.send('麗清目前股價：' + realprice3346) 
              
    elif message.content == '-t 3356': 
          realdata3356=twstock.realtime.get('3356')  
          if realdata3356['success']:     
              realprice3356 = realdata3356['realtime']['latest_trade_price']                      
              await message.channel.send('奇偶目前股價：' + realprice3356)             

    elif message.content == '-t 3376': 
          realdata3376=twstock.realtime.get('3376')  
          if realdata3376['success']:     
              realprice3376 = realdata3376['realtime']['latest_trade_price']                      
              await message.channel.send('新日興目前股價：' + realprice3376) 
              
    elif message.content == '-t 3380': 
          realdata3380=twstock.realtime.get('3380')  
          if realdata3380['success']:     
              realprice3380 = realdata3380['realtime']['latest_trade_price']                      
              await message.channel.send('明泰目前股價：' + realprice3380)
              
    elif message.content == '-t 3383': 
          realdata3383=twstock.realtime.get('3383')  
          if realdata3383['success']:     
              realprice3383 = realdata3383['realtime']['latest_trade_price']                      
              await message.channel.send('新世紀目前股價：' + realprice3383) 
              
    elif message.content == '-t 3406': 
          realdata3406=twstock.realtime.get('3406')  
          if realdata3406['success']:     
              realprice3406 = realdata3406['realtime']['latest_trade_price']                      
              await message.channel.send('玉晶光目前股價：' + realprice3406)              
              
    elif message.content == '-t 3413': 
          realdata3413=twstock.realtime.get('3413')  
          if realdata3413['success']:     
              realprice3413 = realdata3413['realtime']['latest_trade_price']                     
              await message.channel.send('京鼎目前股價：' + realprice3413)             

    elif message.content == '-t 3416': 
          realdata3416=twstock.realtime.get('3416')  
          if realdata3416['success']:     
              realprice3416 = realdata3416['realtime']['latest_trade_price']                      
              await message.channel.send('融程電目前股價：' + realprice3416) 
              
    elif message.content == '-t 3419': 
          realdata3419=twstock.realtime.get('3419')  
          if realdata3419['success']:     
              realprice3419 = realdata3419['realtime']['latest_trade_price']                      
              await message.channel.send('譁裕目前股價：' + realprice3419)
              
    elif message.content == '-t 3432': 
          realdata3432=twstock.realtime.get('3432')  
          if realdata3432['success']:     
              realprice3432 = realdata3432['realtime']['latest_trade_price']                      
              await message.channel.send('台端目前股價：' + realprice3432) 
              
    elif message.content == '-t 3437': 
          realdata3437=twstock.realtime.get('3437')  
          if realdata3437['success']:     
              realprice3437 = realdata3437['realtime']['latest_trade_price']                      
              await message.channel.send('榮創目前股價：' + realprice3437)            
 
    elif message.content == '-t 3443': 
          realdata3443=twstock.realtime.get('3443')  
          if realdata3443['success']:     
              realprice3443 = realdata3443['realtime']['latest_trade_price']                      
              await message.channel.send('創意目前股價：' + realprice3443) 
              
    elif message.content == '-t 3450': 
          realdata3450=twstock.realtime.get('3450')  
          if realdata3450['success']:     
              realprice3450 = realdata3450['realtime']['latest_trade_price']                      
              await message.channel.send('聯鈞目前股價：' + realprice3450)             

    elif message.content == '-t 3454': 
          realdata3454=twstock.realtime.get('3454')  
          if realdata3454['success']:     
              realprice3454 = realdata3454['realtime']['latest_trade_price']                      
              await message.channel.send('晶睿目前股價：' + realprice3454) 
              
    elif message.content == '-t 3481': 
          realdata3481=twstock.realtime.get('3481')  
          if realdata3481['success']:     
              realprice3481 = realdata3481['realtime']['latest_trade_price']                      
              await message.channel.send('群創目前股價：' + realprice3481)
              
    elif message.content == '-t 3494': 
          realdata3494=twstock.realtime.get('3494')  
          if realdata3494['success']:     
              realprice3494 = realdata3494['realtime']['latest_trade_price']      #  600              
              await message.channel.send('誠研目前股價：' + realprice3494) 
              
    elif message.content == '-t 3501': 
          realdata3501=twstock.realtime.get('3501')  
          if realdata3501['success']:     
              realprice3501 = realdata3501['realtime']['latest_trade_price']                      
              await message.channel.send('維熹目前股價：' + realprice3501)              
              
    elif message.content == '-t 3504': 
          realdata3504=twstock.realtime.get('3504')  
          if realdata3504['success']:     
              realprice3504 = realdata3504['realtime']['latest_trade_price']                      
              await message.channel.send('揚明光目前股價：' + realprice3504)             

    elif message.content == '-t 3515': 
          realdata3515=twstock.realtime.get('3515')  
          if realdata3515['success']:     
              realprice3515 = realdata3515['realtime']['latest_trade_price']                      
              await message.channel.send('華擎目前股價：' + realprice3515) 
              
    elif message.content == '-t 3518': 
          realdata3518=twstock.realtime.get('3518')  
          if realdata3518['success']:     
              realprice3518 = realdata3518['realtime']['latest_trade_price']                      
              await message.channel.send('柏騰目前股價：' + realprice3518)
              
    elif message.content == '-t 3528': 
          realdata3528=twstock.realtime.get('3528')  
          if realdata3528['success']:     
              realprice3528 = realdata3528['realtime']['latest_trade_price']                      
              await message.channel.send('安馳目前股價：' + realprice3528) 
              
    elif message.content == '-t 3530': 
          realdata3530=twstock.realtime.get('3530')  
          if realdata3530['success']:     
              realprice3530 = realdata3530['realtime']['latest_trade_price']                     
              await message.channel.send('晶相光目前股價：' + realprice3530)            
 
    elif message.content == '-t 3532': 
          realdata3532=twstock.realtime.get('3532')  
          if realdata3532['success']:     
              realprice3532 = realdata3532['realtime']['latest_trade_price']                     
              await message.channel.send('台勝科目前股價：' + realprice3532) 
              
    elif message.content == '-t 3533': 
          realdata3533=twstock.realtime.get('3533')  
          if realdata3533['success']:     
              realprice3533 = realdata3533['realtime']['latest_trade_price']                     
              await message.channel.send('嘉澤目前股價：' + realprice3533)             

    elif message.content == '-t 3535': 
          realdata3535=twstock.realtime.get('3535')  
          if realdata3535['success']:     
              realprice3535 = realdata3535['realtime']['latest_trade_price']             
              await message.channel.send('晶彩科目前股價：' + realprice3535) 
              
    elif message.content == '-t 3536': 
          realdata3536=twstock.realtime.get('3536')  
          if realdata3536['success']:     
              realprice3536 = realdata3536['realtime']['latest_trade_price']                      
              await message.channel.send('誠創目前股價：' + realprice3536)
              
    elif message.content == '-t 3543': 
          realdata3543=twstock.realtime.get('3543')  
          if realdata3543['success']:     
              realprice3543 = realdata3543['realtime']['latest_trade_price']                     
              await message.channel.send('州巧目前股價：' + realprice3543) 
              
    elif message.content == '-t 3545': 
          realdata3545=twstock.realtime.get('3545')  
          if realdata3545['success']:     
              realprice3545 = realdata3545['realtime']['latest_trade_price']                      
              await message.channel.send('敦泰目前股價：' + realprice3545)                
              
    elif message.content == '-t 3550': 
          realdata3550=twstock.realtime.get('3550')  
          if realdata3550['success']:     
              realprice3550 = realdata3550['realtime']['latest_trade_price']                    
              await message.channel.send('聯穎目前股價：' + realprice3550)              
              
    elif message.content == '-t 3557': 
          realdata3557=twstock.realtime.get('3557')  
          if realdata3557['success']:     
              realprice3557 = realdata3557['realtime']['latest_trade_price']                  
              await message.channel.send('嘉威目前股價：' + realprice3557)             

    elif message.content == '-t 3563': 
          realdata3563=twstock.realtime.get('3563')  
          if realdata3563['success']:     
              realprice3563 = realdata3563['realtime']['latest_trade_price']                  
              await message.channel.send('牧德目前股價：' + realprice3563) 
              
    elif message.content == '-t 3576': 
          realdata3576=twstock.realtime.get('3576')  
          if realdata3576['success']:     
              realprice3576 = realdata3576['realtime']['latest_trade_price']                   
              await message.channel.send('聯合再生目前股價：' + realprice3576)
              
    elif message.content == '-t 3583': 
          realdata3583=twstock.realtime.get('3583')  
          if realdata3583['success']:     
              realprice3583 = realdata3583['realtime']['latest_trade_price']                   
              await message.channel.send('辛耘目前股價：' + realprice3583) 
              
    elif message.content == '-t 3588': 
          realdata3588=twstock.realtime.get('3588')  
          if realdata3588['success']:     
              realprice3588 = realdata3588['realtime']['latest_trade_price']                   
              await message.channel.send('通嘉目前股價：' + realprice3588)            
 
    elif message.content == '-t 3591': 
          realdata3591=twstock.realtime.get('3591')  
          if realdata3591['success']:     
              realprice3591 = realdata3591['realtime']['latest_trade_price']                  
              await message.channel.send('艾笛森目前股價：' + realprice3591) 
              
    elif message.content == '-t 3593': 
          realdata3593=twstock.realtime.get('3593')  
          if realdata3593['success']:     
              realprice3593 = realdata3593['realtime']['latest_trade_price']                     
              await message.channel.send('力銘目前股價：' + realprice3593)             

    elif message.content == '-t 3596': 
          realdata3596=twstock.realtime.get('3596')  
          if realdata3596['success']:     
              realprice3596 = realdata3596['realtime']['latest_trade_price']                      
              await message.channel.send('智易目前股價：' + realprice3596) 
              
    elif message.content == '-t 3605': 
          realdata3605=twstock.realtime.get('3605')  
          if realdata3605['success']:     
              realprice3605 = realdata3605['realtime']['latest_trade_price']                    
              await message.channel.send('宏致目前股價：' + realprice3605)
              
    elif message.content == '-t 3607': 
          realdata3607=twstock.realtime.get('3607')  
          if realdata3607['success']:     
              realprice3607 = realdata3607['realtime']['latest_trade_price']                      
              await message.channel.send('谷崧目前股價：' + realprice3607) 
              
    elif message.content == '-t 3617': 
          realdata3617=twstock.realtime.get('3617')  
          if realdata3617['success']:     
              realprice3617 = realdata3617['realtime']['latest_trade_price']                      
              await message.channel.send('碩天目前股價：' + realprice3617)              
              
    elif message.content == '-t 3622': 
          realdata3622=twstock.realtime.get('3622')  
          if realdata3622['success']:     
              realprice3622 = realdata3622['realtime']['latest_trade_price']                     
              await message.channel.send('洋華目前股價：' + realprice3622)             

    elif message.content == '-t 3645': 
          realdata3645=twstock.realtime.get('3645')  
          if realdata3645['success']:     
              realprice3645 = realdata3645['realtime']['latest_trade_price']                      
              await message.channel.send('達邁目前股價：' + realprice3645) 
              
    elif message.content == '-t 3653': 
          realdata3653=twstock.realtime.get('3653')  
          if realdata3653['success']:     
              realprice3653 = realdata3653['realtime']['latest_trade_price']                      
              await message.channel.send('健策目前股價：' + realprice3653)
              
    elif message.content == '-t 3661': 
          realdata3661=twstock.realtime.get('3661')  
          if realdata3661['success']:     
              realprice3661 = realdata3661['realtime']['latest_trade_price']                      
              await message.channel.send('世芯-KY目前股價：' + realprice3661) 
              
    elif message.content == '-t 3665': 
          realdata3665=twstock.realtime.get('3665')  
          if realdata3665['success']:     
              realprice3665 = realdata3665['realtime']['latest_trade_price']                     
              await message.channel.send('貿聯-KY目前股價：' + realprice3665)            
 
    elif message.content == '-t 3669': 
          realdata3669=twstock.realtime.get('3669')  
          if realdata3669['success']:     
              realprice3669 = realdata3669['realtime']['latest_trade_price']                     
              await message.channel.send('圓展目前股價：' + realprice3669) 
              
    elif message.content == '-t 3673': 
          realdata3673=twstock.realtime.get('3673')  
          if realdata3673['success']:     
              realprice3673 = realdata3673['realtime']['latest_trade_price']                     
              await message.channel.send('TPK-KY目前股價：' + realprice3673)             

    elif message.content == '-t 3679': 
          realdata3679=twstock.realtime.get('3679')  
          if realdata3679['success']:     
              realprice3679 = realdata3679['realtime']['latest_trade_price']                      
              await message.channel.send('新至陞目前股價：' + realprice3679) 
              
    elif message.content == '-t 3682': 
          realdata3682=twstock.realtime.get('3682')  
          if realdata3682['success']:     
              realprice3682 = realdata3682['realtime']['latest_trade_price']                      
              await message.channel.send('亞太電目前股價：' + realprice3682)
              
    elif message.content == '-t 3686': 
          realdata3686=twstock.realtime.get('3686')  
          if realdata3686['success']:     
              realprice3686 = realdata3686['realtime']['latest_trade_price']                     
              await message.channel.send('達能目前股價：' + realprice3686) 
              
    elif message.content == '-t 3694': 
          realdata3694=twstock.realtime.get('3694')  
          if realdata3694['success']:     
              realprice3694 = realdata3694['realtime']['latest_trade_price']                      
              await message.channel.send('海華目前股價：' + realprice3694)              
              
    elif message.content == '-t 3701': 
          realdata3701=twstock.realtime.get('3701')  
          if realdata3701['success']:     
              realprice3701 = realdata3701['realtime']['latest_trade_price']                     
              await message.channel.send('大眾控目前股價：' + realprice3701)             

    elif message.content == '-t 3702': 
          realdata3702=twstock.realtime.get('3702')  
          if realdata3702['success']:     
              realprice3702 = realdata3702['realtime']['latest_trade_price']                      
              await message.channel.send('大聯大目前股價：' + realprice3702) 
              
    elif message.content == '-t 3703': 
          realdata3703=twstock.realtime.get('3703')  
          if realdata3703['success']:     
              realprice3703 = realdata3703['realtime']['latest_trade_price']                      
              await message.channel.send('欣陸目前股價：' + realprice3703)
              
    elif message.content == '-t 3704': 
          realdata3704=twstock.realtime.get('3704')  
          if realdata3704['success']:     
              realprice3704 = realdata3704['realtime']['latest_trade_price']                    
              await message.channel.send('合勤控目前股價：' + realprice3704) 
              
    elif message.content == '-t 3705': 
          realdata3705=twstock.realtime.get('3705')  
          if realdata3705['success']:     
              realprice3705 = realdata3705['realtime']['latest_trade_price']                      
              await message.channel.send('永信目前股價：' + realprice3705)            
 
    elif message.content == '-t 3706': 
          realdata3706=twstock.realtime.get('3706')  
          if realdata3706['success']:     
              realprice3706 = realdata3706['realtime']['latest_trade_price']                      
              await message.channel.send('神達目前股價：' + realprice3706) 
              
    elif message.content == '-t 3708': 
          realdata3708=twstock.realtime.get('3708')  
          if realdata3708['success']:     
              realprice3708 = realdata3708['realtime']['latest_trade_price']                      
              await message.channel.send('上緯投控目前股價：' + realprice3708)             

    elif message.content == '-t 3711': 
          realdata3711=twstock.realtime.get('3711')  
          if realdata3711['success']:     
              realprice3711 = realdata3711['realtime']['latest_trade_price']                     
              await message.channel.send('日月光投控目前股價：' + realprice3711) 
              
    elif message.content == '-t 3712': 
          realdata3712=twstock.realtime.get('3712')  
          if realdata3712['success']:     
              realprice3712 = realdata3712['realtime']['latest_trade_price']                    
              await message.channel.send('永崴投控目前股價：' + realprice3712)
              
    elif message.content == '-t 3714': 
          realdata3714=twstock.realtime.get('3714')  
          if realdata3714['success']:     
              realprice3714 = realdata3714['realtime']['latest_trade_price']                   
              await message.channel.send('富采目前股價：' + realprice3714) 
              
    elif message.content == '-t 4104': 
          realdata4104=twstock.realtime.get('4104')  
          if realdata4104['success']:     
              realprice4104 = realdata4104['realtime']['latest_trade_price']                     
              await message.channel.send('佳醫目前股價：' + realprice4104)                

    elif message.content == '-t 4108': 
          realdata4108=twstock.realtime.get('4108')  
          if realdata4108['success']:     
              realprice4108 = realdata4108['realtime']['latest_trade_price']                      
              await message.channel.send('懷特目前股價：' + realprice4108)             

    elif message.content == '-t 4119': 
          realdata4119=twstock.realtime.get('4119')  
          if realdata4119['success']:     
              realprice4119 = realdata4119['realtime']['latest_trade_price']                      
              await message.channel.send('旭富目前股價：' + realprice4119) 
              
    elif message.content == '-t 4133': 
          realdata4133=twstock.realtime.get('4133')  
          if realdata4133['success']:     
              realprice4133 = realdata4133['realtime']['latest_trade_price']         #650            
              await message.channel.send('亞諾法目前股價：' + realprice4133)
              
    elif message.content == '-t 4137': 
          realdata4137=twstock.realtime.get('4137')  
          if realdata4137['success']:     
              realprice4137 = realdata4137['realtime']['latest_trade_price']                     
              await message.channel.send('麗豐-KY目前股價：' + realprice4137) 
              
    elif message.content == '-t 4141': 
          realdata4141=twstock.realtime.get('4141')  
          if realdata4141['success']:     
              realprice4141 = realdata4141['realtime']['latest_trade_price']                      
              await message.channel.send('龍燈-KY目前股價：' + realprice4141)            
 
    elif message.content == '-t 4142': 
          realdata4142=twstock.realtime.get('4142')  
          if realdata4142['success']:     
              realprice4142 = realdata4142['realtime']['latest_trade_price']                    
              await message.channel.send('國光生目前股價：' + realprice4142) 
              
    elif message.content == '-t 4148': 
          realdata4148=twstock.realtime.get('4148')
          if realdata4148['success']:     
              realprice4148 = realdata4148['realtime']['latest_trade_price']                      
              await message.channel.send('全宇生技-KY目前股價：' + realprice4148)             

    elif message.content == '-t 4155': 
          realdata4155=twstock.realtime.get('4155')  
          if realdata4155['success']:     
              realprice4155 = realdata4155['realtime']['latest_trade_price']                     
              await message.channel.send('訊映目前股價：' + realprice4155) 
              
    elif message.content == '-t 4164': 
          realdata4164=twstock.realtime.get('4164')  
          if realdata4164['success']:     
              realprice4164 = realdata4164['realtime']['latest_trade_price']                    
              await message.channel.send('承業醫目前股價：' + realprice4164)
              
    elif message.content == '-t 4190': 
          realdata4190=twstock.realtime.get('4190')  
          if realdata4190['success']:     
              realprice4190 = realdata4190['realtime']['latest_trade_price']                 
              await message.channel.send('佐登-KY目前股價：' + realprice4190) 
              
    elif message.content == '-t 4306': 
          realdata4306=twstock.realtime.get('4306')  
          if realdata4306['success']:     
              realprice4306 = realdata4306['realtime']['latest_trade_price']                     
              await message.channel.send('炎洲目前股價：' + realprice4306)                
              
    elif message.content == '-t 4414': 
          realdata4414=twstock.realtime.get('4414')  
          if realdata4414['success']:     
              realprice4414 = realdata4414['realtime']['latest_trade_price']                   
              await message.channel.send('如興目前股價：' + realprice4414)              
              
    elif message.content == '-t 4426': 
          realdata4426=twstock.realtime.get('4426')  
          if realdata4426['success']:     
              realprice4426 = realdata4426['realtime']['latest_trade_price']                  
              await message.channel.send('利勤目前股價：' + realprice4426)             

    elif message.content == '-t 4438': 
          realdata4438=twstock.realtime.get('4438')  
          if realdata4438['success']:     
              realprice4438 = realdata4438['realtime']['latest_trade_price']                    
              await message.channel.send('廣越目前股價：' + realprice4438) 
              
    elif message.content == '-t 4439': 
          realdata4439=twstock.realtime.get('4439')  
          if realdata4439['success']:     
              realprice4439 = realdata4439['realtime']['latest_trade_price']                 
              await message.channel.send('冠星-KY目前股價：' + realprice4439)
              
    elif message.content == '-t 4440': 
          realdata4440=twstock.realtime.get('4440')  
          if realdata4440['success']:     
              realprice4440 = realdata4440['realtime']['latest_trade_price']                    
              await message.channel.send('宜新實業目前股價：' + realprice4440) 
              
    elif message.content == '-t 4526': 
          realdata4526=twstock.realtime.get('4526')  
          if realdata4526['success']:     
              realprice4526 = realdata4526['realtime']['latest_trade_price']                      
              await message.channel.send('東台目前股價：' + realprice4526)            
 
    elif message.content == '-t 4532': 
          realdata4532=twstock.realtime.get('4532')  
          if realdata4532['success']:     
              realprice4532 = realdata4532['realtime']['latest_trade_price']                    
              await message.channel.send('瑞智目前股價：' + realprice4532) 
              
    elif message.content == '-t 4536': 
          realdata4536=twstock.realtime.get('4536')  
          if realdata4536['success']:     
              realprice4536 = realdata4536['realtime']['latest_trade_price']                    
              await message.channel.send('拓凱目前股價：' + realprice4536)             

    elif message.content == '-t 4540': 
          realdata4540=twstock.realtime.get('4540')  
          if realdata4540['success']:     
              realprice4540 = realdata4540['realtime']['latest_trade_price']                      
              await message.channel.send('全球傳動目前股價：' + realprice4540) 
              
    elif message.content == '-t 4545': 
          realdata4545=twstock.realtime.get('4545')  
          if realdata4545['success']:     
              realprice4545 = realdata4545['realtime']['latest_trade_price']                      
              await message.channel.send('銘鈺目前股價：' + realprice4545)
              
    elif message.content == '-t 4551': 
          realdata4551=twstock.realtime.get('4551')  
          if realdata4551['success']:     
              realprice4551 = realdata4551['realtime']['latest_trade_price']                     
              await message.channel.send('智伸科	目前股價：' + realprice4551) 
              
    elif message.content == '-t 4552': 
          realdata4552=twstock.realtime.get('4552')  
          if realdata4552['success']:     
              realprice4552 = realdata4552['realtime']['latest_trade_price']                     
              await message.channel.send('力達-KY目前股價：' + realprice4552)              
              
    elif message.content == '-t 4555': 
          realdata4555=twstock.realtime.get('4555')  
          if realdata4555['success']:     
              realprice4555 = realdata4555['realtime']['latest_trade_price']                     
              await message.channel.send('氣立目前股價：' + realprice4555)             

    elif message.content == '-t 4557': 
          realdata4557=twstock.realtime.get('4557')  
          if realdata4557['success']:     
              realprice4557 = realdata4557['realtime']['latest_trade_price']                     
              await message.channel.send('永新-KY目前股價：' + realprice4557) 
              
    elif message.content == '-t 4560': 
          realdata4560=twstock.realtime.get('4560')  
          if realdata4560['success']:     
              realprice4560 = realdata4560['realtime']['latest_trade_price']                    
              await message.channel.send('強信-KY目前股價：' + realprice4560)
              
    elif message.content == '-t 4562': 
          realdata4562=twstock.realtime.get('4562')  
          if realdata4562['success']:     
              realprice4562 = realdata4562['realtime']['latest_trade_price']                     
              await message.channel.send('穎漢目前股價：' + realprice4562) 
              
    elif message.content == '-t 4564': 
          realdata4564=twstock.realtime.get('4564')  
          if realdata4564['success']:     
              realprice4564 = realdata4564['realtime']['latest_trade_price']                     
              await message.channel.send('元翎目前股價：' + realprice4564)            
 
    elif message.content == '-t 4566': 
          realdata4566=twstock.realtime.get('4566')  
          if realdata4566['success']:     
              realprice4566 = realdata4566['realtime']['latest_trade_price']                     
              await message.channel.send('時碩工業目前股價：' + realprice4566) 
              
    elif message.content == '-t 4571': 
          realdata4571=twstock.realtime.get('4571')  
          if realdata4571['success']:     
              realprice4571 = realdata4571['realtime']['latest_trade_price']                     
              await message.channel.send('鈞興-KY目前股價：' + realprice4571)             

    elif message.content == '-t 4572': 
          realdata4572=twstock.realtime.get('4572')  
          if realdata4572['success']:     
              realprice4572 = realdata4572['realtime']['latest_trade_price']                      
              await message.channel.send('駐龍目前股價：' + realprice4572) 
              
    elif message.content == '-t 4576': 
          realdata4576=twstock.realtime.get('4576')  
          if realdata4576['success']:     
              realprice4576 = realdata4576['realtime']['latest_trade_price']                  
              await message.channel.send('大銀微系統目前股價：' + realprice4576)
              
    elif message.content == '-t 4581': 
          realdata4581=twstock.realtime.get('4581')  
          if realdata4581['success']:     
              realprice4581 = realdata4581['realtime']['latest_trade_price']                   
              await message.channel.send('光隆精密-KY目前股價：' + realprice4581) 
              
    elif message.content == '-t 4720': 
          realdata4720=twstock.realtime.get('4720')  
          if realdata4720['success']:     
              realprice4720 = realdata4720['realtime']['latest_trade_price']                     
              await message.channel.send('德淵目前股價：' + realprice4720)              
              
    elif message.content == '-t 4722': 
          realdata4722=twstock.realtime.get('4722')  
          if realdata4722['success']:     
              realprice4722 = realdata4722['realtime']['latest_trade_price']                    
              await message.channel.send('國精化目前股價：' + realprice4722)             

    elif message.content == '-t 4737': 
          realdata4737=twstock.realtime.get('4737')  
          if realdata4737['success']:     
              realprice4737 = realdata4737['realtime']['latest_trade_price']                    
              await message.channel.send('華廣目前股價：' + realprice4737) 
              
    elif message.content == '-t 4739': 
          realdata4739=twstock.realtime.get('4739')  
          if realdata4739['success']:     
              realprice4739 = realdata4739['realtime']['latest_trade_price']                      
              await message.channel.send('康普目前股價：' + realprice4739)
              
    elif message.content == '-t 4746': 
          realdata4746=twstock.realtime.get('4746')  
          if realdata4746['success']:     
              realprice4746 = realdata4746['realtime']['latest_trade_price']                      
              await message.channel.send('台耀目前股價：' + realprice4746) 
              
    elif message.content == '-t 4755': 
          realdata4755=twstock.realtime.get('4755')  
          if realdata4755['success']:     
              realprice4755 = realdata4755['realtime']['latest_trade_price']                   
              await message.channel.send('三福化目前股價：' + realprice4755)            
 
    elif message.content == '-t 4763': 
          realdata4763=twstock.realtime.get('4763')  
          if realdata4763['success']:     
              realprice4763 = realdata4763['realtime']['latest_trade_price']                      
              await message.channel.send('材料-KY目前股價：' + realprice4763) 
              
    elif message.content == '-t 4764': 
          realdata4764=twstock.realtime.get('4764')  
          if realdata4764['success']:     
              realprice4764 = realdata4764['realtime']['latest_trade_price']                    
              await message.channel.send('雙鍵目前股價：' + realprice4764)             

    elif message.content == '-t 4766': 
          realdata4766=twstock.realtime.get('4766')  
          if realdata4766['success']:     
              realprice4766 = realdata4766['realtime']['latest_trade_price']                    
              await message.channel.send('南寶目前股價：' + realprice4766) 
              
    elif message.content == '-t 4807': 
          realdata4807=twstock.realtime.get('4807')  
          if realdata4807['success']:     
              realprice4807 = realdata4807['realtime']['latest_trade_price']                    
              await message.channel.send('日成-KY目前股價：' + realprice4807)
              
    elif message.content == '-t 4904': 
          realdata4904=twstock.realtime.get('4904')  
          if realdata4904['success']:     
              realprice4904 = realdata4904['realtime']['latest_trade_price']                
              await message.channel.send('遠傳目前股價：' + realprice4904) 
              
    elif message.content == '-t 4906': 
          realdata4906=twstock.realtime.get('4906')  
          if realdata4906['success']:     
              realprice4906 = realdata4906['realtime']['latest_trade_price']                    
              await message.channel.send('正文目前股價：' + realprice4906)                
              
    elif message.content == '-t 4912': 
          realdata4912=twstock.realtime.get('4912')  
          if realdata4912['success']:     
              realprice4912 = realdata4912['realtime']['latest_trade_price']                    
              await message.channel.send('聯德控股-KY目前股價：' + realprice4912)              
              
    elif message.content == '-t 4915': 
          realdata4915=twstock.realtime.get('4915')  
          if realdata4915['success']:     
              realprice4915 = realdata4915['realtime']['latest_trade_price']                      
              await message.channel.send('致伸目前股價：' + realprice4915)             

    elif message.content == '-t 4916': 
          realdata4916=twstock.realtime.get('4916')  
          if realdata4916['success']:     
              realprice4916 = realdata4916['realtime']['latest_trade_price']                   
              await message.channel.send('事欣科目前股價：' + realprice4916) 
              
    elif message.content == '-t 4919': 
          realdata4919=twstock.realtime.get('4919')  
          if realdata4919['success']:     
              realprice4919 = realdata4919['realtime']['latest_trade_price']                    
              await message.channel.send('新唐目前股價：' + realprice4919)
              
    elif message.content == '-t 4927': 
          realdata4927=twstock.realtime.get('4927')  
          if realdata4927['success']:     
              realprice4927 = realdata4927['realtime']['latest_trade_price']                     
              await message.channel.send('泰鼎-KY目前股價：' + realprice4927) 
              
    elif message.content == '-t 4930': 
          realdata4930=twstock.realtime.get('4930')  
          if realdata4930['success']:     
              realprice4930 = realdata4930['realtime']['latest_trade_price']                      
              await message.channel.send('燦星網目前股價：' + realprice4930)            
 
    elif message.content == '-t 4934': 
          realdata4934=twstock.realtime.get('4934')  
          if realdata4934['success']:     
              realprice4934 = realdata4934['realtime']['latest_trade_price']                      
              await message.channel.send('太極目前股價：' + realprice4934) 
              
    elif message.content == '-t 4935': 
          realdata4935=twstock.realtime.get('4935')  
          if realdata4935['success']:     
              realprice4935 = realdata4935['realtime']['latest_trade_price']                    
              await message.channel.send('茂林-KY目前股價：' + realprice4935)     
    #700
    elif message.content == '-t 4938': 
          realdata4938=twstock.realtime.get('4938')  
          if realdata4938['success']:     
              realprice4938 = realdata4938['realtime']['latest_trade_price']                    
              await message.channel.send('和碩目前股價：' + realprice4938) 
              
    elif message.content == '-t 4942': 
          realdata4942=twstock.realtime.get('4942')  
          if realdata4942['success']:     
              realprice4942 = realdata4942['realtime']['latest_trade_price']                    
              await message.channel.send('嘉彰目前股價：' + realprice4942)
              
    elif message.content == '-t 4943': 
          realdata4943=twstock.realtime.get('4943')  
          if realdata4943['success']:     
              realprice4943 = realdata4943['realtime']['latest_trade_price']                
              await message.channel.send('康控-KY目前股價：' + realprice4943) 
              
    elif message.content == '-t 4952': 
          realdata4952=twstock.realtime.get('4952')  
          if realdata4952['success']:     
              realprice4952 = realdata4952['realtime']['latest_trade_price']                 
              await message.channel.send('凌通目前股價：' + realprice4952)              
              
    elif message.content == '-t 4956': 
          realdata4956=twstock.realtime.get('4956')  
          if realdata4956['success']:     
              realprice4956 = realdata4956['realtime']['latest_trade_price']               
              await message.channel.send('光鋐目前股價：' + realprice4956)             

    elif message.content == '-t 4958': 
          realdata4958=twstock.realtime.get('4958')  
          if realdata4958['success']:     
              realprice4958 = realdata4958['realtime']['latest_trade_price']                    
              await message.channel.send('臻鼎-KY目前股價：' + realprice4958) 
              
    elif message.content == '-t 4960': 
          realdata4960=twstock.realtime.get('4960')  
          if realdata4960['success']:     
              realprice4960 = realdata4960['realtime']['latest_trade_price']                  
              await message.channel.send('誠美材目前股價：' + realprice4960)
              
    elif message.content == '-t 4961': 
          realdata4961=twstock.realtime.get('4961')  
          if realdata4961['success']:     
              realprice4961 = realdata4961['realtime']['latest_trade_price']                      
              await message.channel.send('天鈺目前股價：' + realprice4961) 
              
    elif message.content == '-t 4967': 
          realdata4967=twstock.realtime.get('4967')  
          if realdata4967['success']:     
              realprice4967 = realdata4967['realtime']['latest_trade_price']                     
              await message.channel.send('十銓目前股價：' + realprice4967)            
 
    elif message.content == '-t 4968': 
          realdata4968=twstock.realtime.get('4968')  
          if realdata4968['success']:     
              realprice4968 = realdata4968['realtime']['latest_trade_price']                     
              await message.channel.send('立積目前股價：' + realprice4968) 
              
    elif message.content == '-t 4976': 
          realdata4976=twstock.realtime.get('4976')  
          if realdata4976['success']:     
              realprice4976 = realdata4976['realtime']['latest_trade_price']                      
              await message.channel.send('佳凌目前股價：' + realprice4976)             

    elif message.content == '-t 4977': 
          realdata4977=twstock.realtime.get('4977')  
          if realdata4977['success']:     
              realprice4977 = realdata4977['realtime']['latest_trade_price']                      
              await message.channel.send('眾達-KY目前股價：' + realprice4977) 
              
    elif message.content == '-t 4989': 
          realdata4989=twstock.realtime.get('4989')  
          if realdata4989['success']:     
              realprice4989 = realdata4989['realtime']['latest_trade_price']                    
              await message.channel.send('榮科目前股價：' + realprice4989)
              
    elif message.content == '-t 4994': 
          realdata4994=twstock.realtime.get('4994')  
          if realdata4994['success']:     
              realprice4994 = realdata4994['realtime']['latest_trade_price']                     
              await message.channel.send('傳奇目前股價：' + realprice4994) 
              
    elif message.content == '-t 4999': 
          realdata4999=twstock.realtime.get('4999')  
          if realdata4999['success']:     
              realprice4999 = realdata4999['realtime']['latest_trade_price']                   
              await message.channel.send('鑫禾目前股價：' + realprice4999)              
              
    elif message.content == '-t 5007': 
          realdata5007=twstock.realtime.get('5007')  
          if realdata5007['success']:     
              realprice5007 = realdata5007['realtime']['latest_trade_price']                  
              await message.channel.send('三星目前股價：' + realprice5007)             

    elif message.content == '-t 5203': 
          realdata5203=twstock.realtime.get('5203')  
          if realdata5203['success']:     
              realprice5203 = realdata5203['realtime']['latest_trade_price']                    
              await message.channel.send('訊連目前股價：' + realprice5203) 
              
    elif message.content == '-t 5215': 
          realdata5215=twstock.realtime.get('5215')  
          if realdata5215['success']:     
              realprice5215 = realdata5215['realtime']['latest_trade_price']                     
              await message.channel.send('科嘉-KY目前股價：' + realprice5215)
              
    elif message.content == '-t 5222': 
          realdata5222=twstock.realtime.get('5222')  
          if realdata5222['success']:     
              realprice5222 = realdata5222['realtime']['latest_trade_price']                     
              await message.channel.send('全訊目前股價：' + realprice5222) 
              
    elif message.content == '-t 5225': 
          realdata5225=twstock.realtime.get('5225')  
          if realdata5225['success']:     
              realprice5225 = realdata5225['realtime']['latest_trade_price']                     
              await message.channel.send('東科-KY目前股價：' + realprice5225)            
 
    elif message.content == '-t 5234': 
          realdata5234=twstock.realtime.get('5234')  
          if realdata5234['success']:     
              realprice5234 = realdata5234['realtime']['latest_trade_price']                      
              await message.channel.send('達興材料目前股價：' + realprice5234) 
              
    elif message.content == '-t 5243': 
          realdata5243=twstock.realtime.get('5243')  
          if realdata5243['success']:     
              realprice5243 = realdata5243['realtime']['latest_trade_price']                      
              await message.channel.send('乙盛-KY目前股價：' + realprice5243)             

    elif message.content == '-t 5258': 
          realdata5258=twstock.realtime.get('5258')  
          if realdata5258['success']:     
              realprice5258 = realdata5258['realtime']['latest_trade_price']                     
              await message.channel.send('虹堡目前股價：' + realprice5258) 
              
    elif message.content == '-t 5269': 
          realdata5269=twstock.realtime.get('5269')  
          if realdata5269['success']:     
              realprice5269 = realdata5269['realtime']['latest_trade_price']                    
              await message.channel.send('祥碩目前股價：' + realprice5269)
              
    elif message.content == '-t 5283': 
          realdata5283=twstock.realtime.get('5283')  
          if realdata5283['success']:     
              realprice5283 = realdata5283['realtime']['latest_trade_price']                  
              await message.channel.send('禾聯碩目前股價：' + realprice5283) 
              
    elif message.content == '-t 5284': 
          realdata5284=twstock.realtime.get('5284')  
          if realdata5284['success']:     
              realprice5284 = realdata5284['realtime']['latest_trade_price']                   
              await message.channel.send('jpp-KY目前股價：' + realprice5284)               

    elif message.content == '-t 5285': 
         realdata5285=twstock.realtime.get('5285')  
         if realdata5285['success']:     
              realprice5285 = realdata5285['realtime']['latest_trade_price']                
              await message.channel.send('界霖目前股價：' + realprice5285)                
              
    elif message.content == '-t 5288': 
          realdata5288=twstock.realtime.get('5288')  
          if realdata5288['success']:     
              realprice5288 = realdata5288['realtime']['latest_trade_price']                 
              await message.channel.send('豐祥-KY目前股價：' + realprice5288) 
              
    elif message.content == '-t 5388': 
          realdata5388=twstock.realtime.get('5388')  
          if realdata5388['success']:     
              realprice5388 = realdata5388['realtime']['latest_trade_price']                 
              await message.channel.send('中磊目前股價：' + realprice5388)               

    elif message.content == '-t 5434': 
         realdata5434=twstock.realtime.get('5434')  
         if realdata5434['success']:     
              realprice5434 = realdata5434['realtime']['latest_trade_price']                  
              await message.channel.send('崇越目前股價：' + realprice5434)                  
              
    elif message.content == '-t 5469': 
          realdata5469=twstock.realtime.get('5469')  
          if realdata5469['success']:     
              realprice5469 = realdata5469['realtime']['latest_trade_price']                     
              await message.channel.send('瀚宇博目前股價：' + realprice5469) 
              
    elif message.content == '-t 5471': 
          realdata5471=twstock.realtime.get('5471')  
          if realdata5471['success']:     
              realprice5471 = realdata5471['realtime']['latest_trade_price']                 
              await message.channel.send('松翰目前股價：' + realprice5471)               

    elif message.content == '-t 5484': 
         realdata5484=twstock.realtime.get('5484')  
         if realdata5484['success']:     
              realprice5484 = realdata5484['realtime']['latest_trade_price']                  
              await message.channel.send('慧友目前股價：' + realprice5484)                
              
    elif message.content == '-t 5515': 
          realdata5515=twstock.realtime.get('5515')  
          if realdata5515['success']:     
              realprice5515 = realdata5515['realtime']['latest_trade_price']                   
              await message.channel.send('建國目前股價：' + realprice5515) 
              
    elif message.content == '-t 5519': 
          realdata5519=twstock.realtime.get('5519')  
          if realdata5519['success']:     
              realprice5519 = realdata5519['realtime']['latest_trade_price']                      
              await message.channel.send('隆大目前股價：' + realprice5519)               

    elif message.content == '-t 5521': 
         realdata5521=twstock.realtime.get('5521')  
         if realdata5521['success']:     
              realprice5521 = realdata5521['realtime']['latest_trade_price']                      
              await message.channel.send('工信目前股價：' + realprice5521)                      
              
    elif message.content == '-t 5522': 
          realdata5522=twstock.realtime.get('5522')  
          if realdata5522['success']:     
              realprice5522 = realdata5522['realtime']['latest_trade_price']                     
              await message.channel.send('遠雄目前股價：' + realprice5522) 
              
    elif message.content == '-t 5525': 
          realdata5525=twstock.realtime.get('5525')  
          if realdata5525['success']:     
              realprice5525 = realdata5525['realtime']['latest_trade_price']                    
              await message.channel.send('順天目前股價：' + realprice5525)               

    elif message.content == '-t 5531': 
         realdata5531=twstock.realtime.get('5531')  
         if realdata5531['success']:     
              realprice5531 = realdata5531['realtime']['latest_trade_price']                     
              await message.channel.send('鄉林目前股價：' + realprice5531)                
              
    elif message.content == '-t 5533': 
          realdata5533=twstock.realtime.get('5533')  
          if realdata5533['success']:     
              realprice5533 = realdata5533['realtime']['latest_trade_price']                    
              await message.channel.send('皇鼎目前股價：' + realprice5533) 
              
    elif message.content == '-t 5534': 
          realdata5534=twstock.realtime.get('5534')  
          if realdata5534['success']:     
              realprice5534 = realdata5534['realtime']['latest_trade_price']                     
              await message.channel.send('長虹目前股價：' + realprice5534)               

    elif message.content == '-t 5538': 
         realdata5538=twstock.realtime.get('5538')  
         if realdata5538['success']:     
              realprice5538 = realdata5538['realtime']['latest_trade_price']                    
              await message.channel.send('東明-KY目前股價：' + realprice5538)                  
              
    elif message.content == '-t 5546': 
          realdata5546=twstock.realtime.get('5546')  
          if realdata5546['success']:     
              realprice5546 = realdata5546['realtime']['latest_trade_price']                   
              await message.channel.send('永固-KY目前股價：' + realprice5546) 
              
    elif message.content == '-t 5607': 
          realdata5607=twstock.realtime.get('5607')  
          if realdata5607['success']:     
              realprice5607 = realdata5607['realtime']['latest_trade_price']                
              await message.channel.send('遠雄港目前股價：' + realprice5607)               

    elif message.content == '-t 5608': 
         realdata5608=twstock.realtime.get('5608')  
         if realdata5608['success']:     
              realprice5608 = realdata5608['realtime']['latest_trade_price']                      
              await message.channel.send('四維航目前股價：' + realprice5608)                
              
    elif message.content == '-t 5706': 
          realdata5706=twstock.realtime.get('5706')  
          if realdata5706['success']:     
              realprice5706 = realdata5706['realtime']['latest_trade_price']                     
              await message.channel.send('鳳凰目前股價：' + realprice5706) 
              
    elif message.content == '-t 5871': 
          realdata5871=twstock.realtime.get('5871')  
          if realdata5871['success']:     
              realprice5871 = realdata5871['realtime']['latest_trade_price']                      
              await message.channel.send('中租-KY目前股價：' + realprice5871)               

    elif message.content == '-t 5876': 
         realdata5876=twstock.realtime.get('5876')  
         if realdata5876['success']:     
              realprice5876 = realdata5876['realtime']['latest_trade_price']                   
              await message.channel.send('上海商銀目前股價：' + realprice5876)               
              
    elif message.content == '-t 5880': 
          realdata5880=twstock.realtime.get('5880')  
          if realdata5880['success']:     
              realprice5880 = realdata5880['realtime']['latest_trade_price']                    
              await message.channel.send('合庫金目前股價：' + realprice5880) 
              
    elif message.content == '-t 5906': 
          realdata5906=twstock.realtime.get('5906')  
          if realdata5906['success']:                                                                   #750
              realprice5906 = realdata5906['realtime']['latest_trade_price']                 
              await message.channel.send('台南-KY目前股價：' + realprice5906) 

    elif message.content == '-t 5907': 
         realdata5907=twstock.realtime.get('5907')  
         if realdata5907['success']:     
              realprice5907 = realdata5907['realtime']['latest_trade_price']                  
              await message.channel.send('大洋-KY目前股價：' + realprice5907)                
              
    elif message.content == '-t 6005': 
          realdata6005=twstock.realtime.get('6005')  
          if realdata6005['success']:     
              realprice6005 = realdata6005['realtime']['latest_trade_price']                  
              await message.channel.send('群益證目前股價：' + realprice6005) 
              
    elif message.content == '-t 6024': 
          realdata6024=twstock.realtime.get('6024')  
          if realdata6024['success']:     
              realprice6024 = realdata6024['realtime']['latest_trade_price']                
              await message.channel.send('群益期目前股價：' + realprice6024)               

    elif message.content == '-t 6108': 
         realdata6108=twstock.realtime.get('6108')  
         if realdata6108['success']:     
              realprice6108 = realdata6108['realtime']['latest_trade_price']                 
              await message.channel.send('競國目前股價：' + realprice6108)                  
              
    elif message.content == '-t 6112': 
          realdata6112=twstock.realtime.get('6112')  
          if realdata6112['success']:     
              realprice6112 = realdata6112['realtime']['latest_trade_price']                 
              await message.channel.send('聚碩目前股價：' + realprice6112) 
              
    elif message.content == '-t 6115': 
          realdata6115=twstock.realtime.get('6115')  
          if realdata6115['success']:     
              realprice6115 = realdata6115['realtime']['latest_trade_price']                  
              await message.channel.send('鎰勝目前股價：' + realprice6115)               

    elif message.content == '-t 6116': 
         realdata6116=twstock.realtime.get('6116')  
         if realdata6116['success']:     
              realprice6116 = realdata6116['realtime']['latest_trade_price']               
              await message.channel.send('彩晶目前股價：' + realprice6116)                
              
    elif message.content == '-t 6117': 
          realdata6117=twstock.realtime.get('6117')  
          if realdata6117['success']:     
              realprice6117 = realdata6117['realtime']['latest_trade_price']                      
              await message.channel.send('迎廣目前股價：' + realprice6117) 
              
    elif message.content == '-t 6120': 
          realdata6120=twstock.realtime.get('6120')  
          if realdata6120['success']:     
              realprice6120 = realdata6120['realtime']['latest_trade_price']                   
              await message.channel.send('達運目前股價：' + realprice6120)               

    elif message.content == '-t 6128': 
         realdata6128=twstock.realtime.get('6128')  
         if realdata6128['success']:     
              realprice6128 = realdata6128['realtime']['latest_trade_price']              
              await message.channel.send('上福目前股價：' + realprice6128)                      
              
    elif message.content == '-t 6133': 
          realdata6133=twstock.realtime.get('6133')  
          if realdata6133['success']:     
              realprice6133 = realdata6133['realtime']['latest_trade_price']                
              await message.channel.send('金橋目前股價：' + realprice6133) 
              
    elif message.content == '-t 6136': 
          realdata6136=twstock.realtime.get('6136')  
          if realdata6136['success']:     
              realprice6136 = realdata6136['realtime']['latest_trade_price']                   
              await message.channel.send('富爾特目前股價：' + realprice6136)               

    elif message.content == '-t 6139': 
         realdata6139=twstock.realtime.get('6139')  
         if realdata6139['success']:     
              realprice6139 = realdata6139['realtime']['latest_trade_price']                      
              await message.channel.send('亞翔目前股價：' + realprice6139)                
              
    elif message.content == '-t 6141': 
          realdata6141=twstock.realtime.get('6141')  
          if realdata6141['success']:     
              realprice6141 = realdata6141['realtime']['latest_trade_price']                   
              await message.channel.send('柏承目前股價：' + realprice6141) 
              
    elif message.content == '-t 6142': 
          realdata6142=twstock.realtime.get('6142')  
          if realdata6142['success']:     
              realprice6142 = realdata6142['realtime']['latest_trade_price']                    
              await message.channel.send('友勁目前股價：' + realprice6142)               

    elif message.content == '-t 6152': 
         realdata6152=twstock.realtime.get('6152')  
         if realdata6152['success']:     
              realprice6152 = realdata6152['realtime']['latest_trade_price']                     
              await message.channel.send('百一目前股價：' + realprice6152)                  
              
    elif message.content == '-t 6153': 
          realdata6153=twstock.realtime.get('6153')  
          if realdata6153['success']:     
              realprice6153 = realdata6153['realtime']['latest_trade_price']                      
              await message.channel.send('嘉聯益目前股價：' + realprice6153) 
              
    elif message.content == '-t 6155': 
          realdata6155=twstock.realtime.get('6155')  
          if realdata6155['success']:     
              realprice6155 = realdata6155['realtime']['latest_trade_price']                     
              await message.channel.send('鈞寶目前股價：' + realprice6155)               

    elif message.content == '-t 6164': 
         realdata6164=twstock.realtime.get('6164')  
         if realdata6164['success']:     
              realprice6164 = realdata6164['realtime']['latest_trade_price']                    
              await message.channel.send('華興目前股價：' + realprice6164)                
              
    elif message.content == '-t 6165': 
          realdata6165=twstock.realtime.get('6165')  
          if realdata6165['success']:     
              realprice6165 = realdata6165['realtime']['latest_trade_price']                    
              await message.channel.send('浪凡目前股價：' + realprice6165) 
              
    elif message.content == '-t 6166': 
          realdata6166=twstock.realtime.get('6166')  
          if realdata6166['success']:     
              realprice6166 = realdata6166['realtime']['latest_trade_price']                    
              await message.channel.send('凌華目前股價：' + realprice6166)               

    elif message.content == '-t 6172': 
         realdata6172=twstock.realtime.get('6172')  
         if realdata6172['success']:     
              realprice6172 = realdata6172['realtime']['latest_trade_price']                    
              await message.channel.send('互億目前股價：' + realprice6172)               
              
    elif message.content == '-t 6176': 
          realdata6176=twstock.realtime.get('6176')  
          if realdata6176['success']:     
              realprice6176 = realdata6176['realtime']['latest_trade_price']                   
              await message.channel.send('瑞儀目前股價：' + realprice6176) 
              
    elif message.content == '-t 6177': 
          realdata6177=twstock.realtime.get('6177')  
          if realdata6177['success']:     
              realprice6177 = realdata6177['realtime']['latest_trade_price']                   
              await message.channel.send('達麗目前股價：' + realprice6177)               

    elif message.content == '-t 6183': 
         realdata6183=twstock.realtime.get('6183')  
         if realdata6183['success']:     
              realprice6183 = realdata6183['realtime']['latest_trade_price']                
              await message.channel.send('關貿目前股價：' + realprice6183)                
              
    elif message.content == '-t 6184': 
          realdata6184=twstock.realtime.get('6184')  
          if realdata6184['success']:     
              realprice6184 = realdata6184['realtime']['latest_trade_price']                    
              await message.channel.send('大豐電目前股價：' + realprice6184) 
              
    elif message.content == '-t 6189': 
          realdata6189=twstock.realtime.get('6189')  
          if realdata6189['success']:     
              realprice6189 = realdata6189['realtime']['latest_trade_price']               
              await message.channel.send('豐藝目前股價：' + realprice6189)               

    elif message.content == '-t 6191': 
         realdata6191=twstock.realtime.get('6191')  
         if realdata6191['success']:     
              realprice6191 = realdata6191['realtime']['latest_trade_price']                
              await message.channel.send('精成科目前股價：' + realprice6191)                  
              
    elif message.content == '-t 6192': 
          realdata6192=twstock.realtime.get('6192')  
          if realdata6192['success']:     
              realprice6192 = realdata6192['realtime']['latest_trade_price']                  
              await message.channel.send('巨路目前股價：' + realprice6192) 
              
    elif message.content == '-t 6196': 
          realdata6196=twstock.realtime.get('6196')  
          if realdata6196['success']:     
              realprice6196 = realdata6196['realtime']['latest_trade_price']                   
              await message.channel.send('帆宣目前股價：' + realprice6196)               

    elif message.content == '-t 6197': 
         realdata6197=twstock.realtime.get('6197')  
         if realdata6197['success']:     
              realprice6197 = realdata6197['realtime']['latest_trade_price']                     
              await message.channel.send('佳必琪目前股價：' + realprice6197)                
              
    elif message.content == '-t 6201': 
          realdata6201=twstock.realtime.get('6201')  
          if realdata6201['success']:     
              realprice6201 = realdata6201['realtime']['latest_trade_price']                 
              await message.channel.send('亞弘電目前股價：' + realprice6201) 
              
    elif message.content == '-t 6202': 
          realdata6202=twstock.realtime.get('6202')  
          if realdata6202['success']:     
              realprice6202 = realdata6202['realtime']['latest_trade_price']                   
              await message.channel.send('盛群目前股價：' + realprice6202)               

    elif message.content == '-t 6205': 
         realdata6205=twstock.realtime.get('6205')  
         if realdata6205['success']:     
              realprice6205 = realdata6205['realtime']['latest_trade_price']                    
              await message.channel.send('詮欣目前股價：' + realprice6205)                      
              
    elif message.content == '-t 6206': 
          realdata6206=twstock.realtime.get('6206')  
          if realdata6206['success']:     
              realprice6206 = realdata6206['realtime']['latest_trade_price']                
              await message.channel.send('飛捷目前股價：' + realprice6206) 
              
    elif message.content == '-t 6209': 
          realdata6209=twstock.realtime.get('6209')  
          if realdata6209['success']:     
              realprice6209 = realdata6209['realtime']['latest_trade_price']                  
              await message.channel.send('今國光	目前股價：' + realprice6209)               

    elif message.content == '-t 6213': 
         realdata6213=twstock.realtime.get('6213')  
         if realdata6213['success']:     
              realprice6213 = realdata6213['realtime']['latest_trade_price']               
              await message.channel.send('聯茂目前股價：' + realprice6213)                
              
    elif message.content == '-t 6214': 
          realdata6214=twstock.realtime.get('6214')  
          if realdata6214['success']:     
              realprice6214 = realdata6214['realtime']['latest_trade_price']                   
              await message.channel.send('精誠目前股價：' + realprice6214) 
              
    elif message.content == '-t 6215': 
          realdata=twstock.realtime.get('6215')  
          if realdata6215['success']:     
              realprice6215 = realdata6215['realtime']['latest_trade_price']                   
              await message.channel.send('和椿目前股價：' + realprice6215)               

    elif message.content == '-t 6216': 
         realdata6216=twstock.realtime.get('6216')  
         if realdata6216['success']:     
              realprice6216 = realdata6216['realtime']['latest_trade_price']                
              await message.channel.send('居易目前股價：' + realprice6216)                  
              
    elif message.content == '-t 6224': 
          realdata6224=twstock.realtime.get('6224')  
          if realdata6224['success']:     
              realprice6224 = realdata6224['realtime']['latest_trade_price']                   
              await message.channel.send('聚鼎目前股價：' + realprice6224) 
              
    elif message.content == '-t 6225': 
          realdata6225=twstock.realtime.get('6225')  
          if realdata6225['success']:     
              realprice6225 = realdata6225['realtime']['latest_trade_price']                  
              await message.channel.send('天瀚目前股價：' + realprice6225)               

    elif message.content == '-t 6226': 
         realdata6226=twstock.realtime.get('6226')  
         if realdata6226['success']:     
              realprice6226 = realdata6226['realtime']['latest_trade_price']           
              await message.channel.send('光鼎目前股價：' + realprice6226)                
              
    elif message.content == '-t 6230': 
          realdata6230=twstock.realtime.get('6230')  
          if realdata6230['success']:     
              realprice6230 = realdata6230['realtime']['latest_trade_price']                 
              await message.channel.send('尼得科超眾目前股價：' + realprice6230) 
              
    elif message.content == '-t 6235': 
          realdata6235=twstock.realtime.get('6235')  
          if realdata6235['success']:     
              realprice6235 = realdata6235['realtime']['latest_trade_price']                
              await message.channel.send('華孚目前股價：' + realprice6235)               

    elif message.content == '-t 6239': 
         realdata6239=twstock.realtime.get('6239')  
         if realdata6239['success']:     
              realprice6239 = realdata6239['realtime']['latest_trade_price']                      
              await message.channel.send('力成目前股價：' + realprice6239)               
              
    elif message.content == '-t 6243': 
          realdata6243=twstock.realtime.get('6243')  
          if realdata6243['success']:     
              realprice6243 = realdata6243['realtime']['latest_trade_price']                
              await message.channel.send('迅杰目前股價：' + realprice6243) 
              
    elif message.content == '-t 6251': 
          realdata6251=twstock.realtime.get('6251')  
          if realdata6251['success']:     
              realprice6251 = realdata6251['realtime']['latest_trade_price']                 
              await message.channel.send('定穎目前股價：' + realprice6251)               

    elif message.content == '-t 6257': 
         realdata6257=twstock.realtime.get('6257')  
         if realdata6257['success']:     
              realprice6257 = realdata6257['realtime']['latest_trade_price']         #800             
              await message.channel.send('矽格目前股價：' + realprice6257)  

    elif message.content == '-t 6269': 
          realdata6269=twstock.realtime.get('6269')  
          if realdata6269['success']:     
              realprice6269 = realdata6269['realtime']['latest_trade_price']                   
              await message.channel.send('台郡目前股價：' + realprice6269) 
              
    elif message.content == '-t 6271': 
          realdata6271=twstock.realtime.get('6271')  
          if realdata6271['success']:     
              realprice6271 = realdata6271['realtime']['latest_trade_price']                     
              await message.channel.send('同欣電目前股價：' + realprice6271)               

    elif message.content == '-t 6277': 
         realdata6277=twstock.realtime.get('6277')  
         if realdata6277['success']:     
              realprice6277 = realdata6277['realtime']['latest_trade_price']                 
              await message.channel.send('宏正目前股價：' + realprice6277)                  
              
    elif message.content == '-t 6278': 
          realdata6278=twstock.realtime.get('6278')  
          if realdata6278['success']:     
              realprice6278 = realdata6278['realtime']['latest_trade_price']                     
              await message.channel.send('台表科目前股價：' + realprice6278) 
              
    elif message.content == '-t 6281': 
          realdata6281=twstock.realtime.get('6281')  
          if realdata6281['success']:     
              realprice6281 = realdata6281['realtime']['latest_trade_price']                   
              await message.channel.send('全國電目前股價：' + realprice6281)               

    elif message.content == '-t 6282': 
         realdata6282=twstock.realtime.get('6282')  
         if realdata6282['success']:     
              realprice6282 = realdata6282['realtime']['latest_trade_price']                    
              await message.channel.send('康舒目前股價：' + realprice6282)                
              
    elif message.content == '-t 6283': 
          realdata6283=twstock.realtime.get('6283')  
          if realdata6283['success']:     
              realprice6283 = realdata6283['realtime']['latest_trade_price']                   
              await message.channel.send('淳安目前股價：' + realprice6283) 
              
    elif message.content == '-t 6285': 
          realdata6285=twstock.realtime.get('6285')  
          if realdata6285['success']:     
              realprice6285 = realdata6285['realtime']['latest_trade_price']                     
              await message.channel.send('啟碁目前股價：' + realprice6285)               

    elif message.content == '-t 6288': 
         realdata6288=twstock.realtime.get('6288')  
         if realdata6288['success']:     
              realprice6288 = realdata6288['realtime']['latest_trade_price']                  
              await message.channel.send('聯嘉目前股價：' + realprice6288)                      
              
    elif message.content == '-t 6289': 
          realdata6289=twstock.realtime.get('6289')  
          if realdata6289['success']:     
              realprice6289 = realdata6289['realtime']['latest_trade_price']                   
              await message.channel.send('華上目前股價：' + realprice6289) 
              
    elif message.content == '-t 6405': 
          realdata6405=twstock.realtime.get('6405')  
          if realdata6405['success']:     
              realprice6405 = realdata6405['realtime']['latest_trade_price']                     
              await message.channel.send('悅城目前股價：' + realprice6405)               

    elif message.content == '-t 6409': 
         realdata6409=twstock.realtime.get('6409')  
         if realdata6409['success']:     
              realprice6409 = realdata6409['realtime']['latest_trade_price']             
              await message.channel.send('旭隼目前股價：' + realprice6409)                
              
    elif message.content == '-t 6412': 
          realdata6412=twstock.realtime.get('6412')  
          if realdata6412['success']:     
              realprice6412 = realdata6412['realtime']['latest_trade_price']             
              await message.channel.send('群電目前股價：' + realprice6412) 
              
    elif message.content == '-t 6414': 
          realdata6414=twstock.realtime.get('6414')  
          if realdata6414['success']:     
              realprice6414 = realdata6414['realtime']['latest_trade_price']                     
              await message.channel.send('樺漢目前股價：' + realprice6414)               

    elif message.content == '-t 6415': 
         realdata6415=twstock.realtime.get('6415')  
         if realdata6415['success']:     
              realprice6415 = realdata6415['realtime']['latest_trade_price']                     
              await message.channel.send('矽力-KY目前股價：' + realprice6415)                  
              
    elif message.content == '-t 6416': 
          realdata6416=twstock.realtime.get('6416')  
          if realdata6416['success']:     
              realprice6416 = realdata6416['realtime']['latest_trade_price']                     
              await message.channel.send('瑞祺電通目前股價：' + realprice6416) 
              
    elif message.content == '-t 6426': 
          realdata6426=twstock.realtime.get('6426')  
          if realdata6426['success']:     
              realprice6426 = realdata6426['realtime']['latest_trade_price']                  
              await message.channel.send('統新目前股價：' + realprice6426)               

    elif message.content == '-t 6431': 
         realdata6431=twstock.realtime.get('6431')  
         if realdata6431['success']:     
              realprice6431 = realdata6431['realtime']['latest_trade_price']                    
              await message.channel.send('光麗-KY目前股價：' + realprice6431)                
              
    elif message.content == '-t 6438': 
          realdata6438=twstock.realtime.get('6438')  
          if realdata6438['success']:     
              realprice6438 = realdata6438['realtime']['latest_trade_price']                  
              await message.channel.send('迅得目前股價：' + realprice6438) 
              
    elif message.content == '-t 6442': 
          realdata6442=twstock.realtime.get('6442')  
          if realdata6442['success']:     
              realprice6442 = realdata6442['realtime']['latest_trade_price']                     
              await message.channel.send('光聖目前股價：' + realprice6442)               

    elif message.content == '-t 6443': 
         realdata6443=twstock.realtime.get('6443')  
         if realdata6443['success']:     
              realprice6443 = realdata6443['realtime']['latest_trade_price']                    
              await message.channel.send('元晶目前股價：' + realprice6443)                   
              
    elif message.content == '-t 6449': 
          realdata6449=twstock.realtime.get('6449')  
          if realdata6449['success']:     
              realprice6449 = realdata6449['realtime']['latest_trade_price']                    
              await message.channel.send('鈺邦目前股價：' + realprice6449) 
              
    elif message.content == '-t 6451': 
          realdata6451=twstock.realtime.get('6451')  
          if realdata6451['success']:     
              realprice6451 = realdata6451['realtime']['latest_trade_price']                      
              await message.channel.send('訊芯-KY目前股價：' + realprice6451)               

    elif message.content == '-t 6456': 
         realdata6456=twstock.realtime.get('6456')  
         if realdata6456['success']:     
              realprice6456 = realdata6456['realtime']['latest_trade_price']                   
              await message.channel.send('GIS-KY目前股價：' + realprice6456)                
              
    elif message.content == '-t 6464': 
          realdata6464=twstock.realtime.get('6464')  
          if realdata6464['success']:     
              realprice6464 = realdata6464['realtime']['latest_trade_price']                    
              await message.channel.send('台數科目前股價：' + realprice6464) 
              
    elif message.content == '-t 6477': 
          realdata6477=twstock.realtime.get('6477')  
          if realdata6477['success']:     
              realprice6477 = realdata6477['realtime']['latest_trade_price']                     
              await message.channel.send('安集目前股價：' + realprice6477)               

    elif message.content == '-t 6491': 
         realdata6491=twstock.realtime.get('6491')  
         if realdata6491['success']:     
              realprice6491 = realdata6491['realtime']['latest_trade_price']                   
              await message.channel.send('晶碩目前股價：' + realprice6491)                  
              
    elif message.content == '-t 6504': 
          realdata6504=twstock.realtime.get('6504')  
          if realdata6504['success']:     
              realprice6504 = realdata6504['realtime']['latest_trade_price']                  
              await message.channel.send('南六目前股價：' + realprice6504) 
              
    elif message.content == '-t 6505': 
          realdata6505=twstock.realtime.get('6505')  
          if realdata6505['success']:     
              realprice6505 = realdata6505['realtime']['latest_trade_price']                  
              await message.channel.send('台塑化目前股價：' + realprice6505)               

    elif message.content == '-t 6515': 
         realdata6515=twstock.realtime.get('6515')  
         if realdata6515['success']:     
              realprice6515 = realdata6515['realtime']['latest_trade_price']                  
              await message.channel.send('穎崴目前股價：' + realprice6515)                
              
    elif message.content == '-t 6525': 
          realdata6525=twstock.realtime.get('6525')  
          if realdata6525['success']:     
              realprice6525 = realdata6525['realtime']['latest_trade_price']                     
              await message.channel.send('捷敏-KY目前股價：' + realprice6525) 
              
    elif message.content == '-t 6531': 
          realdata6531=twstock.realtime.get('6531')  
          if realdata6531['success']:     
              realprice6531 = realdata6531['realtime']['latest_trade_price']                    
              await message.channel.send('愛普*目前股價：' + realprice6531)               

    elif message.content == '-t 6533': 
         realdata6533=twstock.realtime.get('6533')  
         if realdata6533['success']:     
              realprice6533 = realdata6533['realtime']['latest_trade_price']                      
              await message.channel.send('晶心科目前股價：' + realprice6533)                      
              
    elif message.content == '-t 6541': 
          realdata6541=twstock.realtime.get('6541')  
          if realdata6541['success']:     
              realprice6541 = realdata6541['realtime']['latest_trade_price']                   
              await message.channel.send('泰福-KY目前股價：' + realprice6541) 
              
    elif message.content == '-t 6552': 
          realdata6552=twstock.realtime.get('6552')  
          if realdata6552['success']:     
              realprice6552 = realdata6552['realtime']['latest_trade_price']                     
              await message.channel.send('易華電目前股價：' + realprice6552)               

    elif message.content == '-t 6558': 
         realdata6558=twstock.realtime.get('6558')  
         if realdata6558['success']:     
              realprice6558 = realdata6558['realtime']['latest_trade_price']                    
              await message.channel.send('興能高目前股價：' + realprice6558)                
              
    elif message.content == '-t 6573': 
          realdata6573=twstock.realtime.get('6573')  
          if realdata6573['success']:     
              realprice6573 = realdata6573['realtime']['latest_trade_price']                      
              await message.channel.send('虹揚-KY目前股價：' + realprice6573) 
              
    elif message.content == '-t 6579': 
          realdata6579=twstock.realtime.get('6579')  
          if realdata6579['success']:     
              realprice6579 = realdata6579['realtime']['latest_trade_price']                      
              await message.channel.send('研揚目前股價：' + realprice6579)               

    elif message.content == '-t 6581': 
         realdata6581=twstock.realtime.get('6581')  
         if realdata6581['success']:     
              realprice6581 = realdata6581['realtime']['latest_trade_price']                     
              await message.channel.send('鋼聯目前股價：' + realprice6581)                  
              
    elif message.content == '-t 6582': 
          realdata6582=twstock.realtime.get('6582')  
          if realdata6582['success']:     
              realprice6582 = realdata6582['realtime']['latest_trade_price']                   
              await message.channel.send('申豐目前股價：' + realprice6582) 
              
    elif message.content == '-t 6591': 
          realdata6591=twstock.realtime.get('6591')  
          if realdata6591['success']:     
              realprice6591 = realdata6591['realtime']['latest_trade_price']                     
              await message.channel.send('動力-KY目前股價：' + realprice6591)               

    elif message.content == '-t 6592': 
         realdata6592=twstock.realtime.get('6592')  
         if realdata6592['success']:     
              realprice6592 = realdata6592['realtime']['latest_trade_price']                     
              await message.channel.send('和潤企業目前股價：' + realprice6592)                
              
    elif message.content == '-t 6598': 
          realdata6598=twstock.realtime.get('6598')  
          if realdata6598['success']:     
              realprice6598 = realdata6598['realtime']['latest_trade_price']                     
              await message.channel.send('ABC-KY目前股價：' + realprice6598) 
              
    elif message.content == '-t 6605': 
          realdata6605=twstock.realtime.get('6605')  
          if realdata6605['success']:     
              realprice6605 = realdata6605['realtime']['latest_trade_price']                     
              await message.channel.send('帝寶目前股價：' + realprice6605)               

    elif message.content == '-t 6625': 
         realdata6625=twstock.realtime.get('6625')  
         if realdata6625['success']:     
              realprice6625 = realdata6625['realtime']['latest_trade_price']                     
              await message.channel.send('必應目前股價：' + realprice6625)               
              
    elif message.content == '-t 6641': 
          realdata6641=twstock.realtime.get('6641')  
          if realdata6641['success']:     
              realprice6641 = realdata6641['realtime']['latest_trade_price']                 
              await message.channel.send('基士德-KY目前股價：' + realprice6641) 
              
    elif message.content == '-t 6655': 
          realdata6655=twstock.realtime.get('6655')  
          if realdata6655['success']:     
              realprice6655 = realdata6655['realtime']['latest_trade_price']                    
              await message.channel.send('科定目前股價：' + realprice6655)               

    elif message.content == '-t 6666': 
         realdata6666=twstock.realtime.get('6666')  
         if realdata6666['success']:     
              realprice6666 = realdata6666['realtime']['latest_trade_price']                  
              await message.channel.send('羅麗芬-KY目前股價：' + realprice6666)                
              
    elif message.content == '-t 6668': 
          realdata6668=twstock.realtime.get('6668')  
          if realdata6668['success']:     
              realprice6668 = realdata6668['realtime']['latest_trade_price']                    
              await message.channel.send('中揚光目前股價：' + realprice6668) 
              
    elif message.content == '-t 6669': 
          realdata6669=twstock.realtime.get('6669')  
          if realdata6669['success']:                                                   #850
              realprice6669 = realdata6669['realtime']['latest_trade_price']                   
              await message.channel.send('緯穎目前股價：' + realprice6669)               

    elif message.content == '-t 6670': 
         realdata6670=twstock.realtime.get('6670')  
         if realdata6670['success']:     
              realprice6670 = realdata6670['realtime']['latest_trade_price']                   
              await message.channel.send('復盛應用目前股價：' + realprice6670)                  
              
    elif message.content == '-t 6671': 
          realdata6671=twstock.realtime.get('6671')  
          if realdata6671['success']:     
              realprice6671 = realdata6671['realtime']['latest_trade_price']                 
              await message.channel.send('三能-KY目前股價：' + realprice6671) 
              
    elif message.content == '-t 6672': 
          realdata6672=twstock.realtime.get('6672')  
          if realdata6672['success']:     
              realprice6672 = realdata6672['realtime']['latest_trade_price']                   
              await message.channel.send('騰輝電子-KY目前股價：' + realprice6672)               

    elif message.content == '-t 6698': 
         realdata6698=twstock.realtime.get('6698')  
         if realdata6698['success']:     
              realprice6698 = realdata6698['realtime']['latest_trade_price']                 
              await message.channel.send('旭暉應材目前股價：' + realprice6698)                
              
    elif message.content == '-t 6706': 
          realdata6706=twstock.realtime.get('6706')  
          if realdata6706['success']:     
              realprice6706 = realdata6706['realtime']['latest_trade_price']                 
              await message.channel.send('惠特目前股價：' + realprice6706) 
              
    elif message.content == '-t 6715': 
          realdata6715=twstock.realtime.get('6715')  
          if realdata6715['success']:     
              realprice6715 = realdata6715['realtime']['latest_trade_price']                  
              await message.channel.send('嘉基目前股價：' + realprice6715)               

    elif message.content == '-t 6743': 
         realdata6743=twstock.realtime.get('6743')  
         if realdata6743['success']:     
              realprice6743 = realdata6743['realtime']['latest_trade_price']                  
              await message.channel.send('安普新目前股價：' + realprice6743)                      
              
    elif message.content == '-t 6754': 
          realdata6754=twstock.realtime.get('6754')  
          if realdata6754['success']:     
              realprice6754 = realdata6754['realtime']['latest_trade_price']                
              await message.channel.send('匯僑設計目前股價：' + realprice6754) 
              
    elif message.content == '-t 6756': 
          realdata6756=twstock.realtime.get('6756')  
          if realdata6756['success']:     
              realprice6756 = realdata6756['realtime']['latest_trade_price']                
              await message.channel.send('威鋒電子目前股價：' + realprice6756)               

    elif message.content == '-t 6768': 
         realdata6768=twstock.realtime.get('6768')  
         if realdata6768['success']:     
              realprice6768 = realdata6768['realtime']['latest_trade_price']               
              await message.channel.send('志強-KY目前股價：' + realprice6768)                
              
    elif message.content == '-t 6770': 
          realdata6770=twstock.realtime.get('6770')  
          if realdata6770['success']:     
              realprice6770 = realdata6770['realtime']['latest_trade_price']                  
              await message.channel.send('力積電目前股價：' + realprice6770) 
              
    elif message.content == '-t 6776': 
          realdata6776=twstock.realtime.get('6776')  
          if realdata6776['success']:     
              realprice6776 = realdata6776['realtime']['latest_trade_price']               
              await message.channel.send('展碁國際目前股價：' + realprice6776)               

    elif message.content == '-t 6781': 
         realdata6781=twstock.realtime.get('6781')  
         if realdata6781['success']:     
              realprice6781 = realdata6781['realtime']['latest_trade_price']                   
              await message.channel.send('AES-KY目前股價：' + realprice6781)                  
              
    elif message.content == '-t 6790': 
          realdata6790=twstock.realtime.get('6790')  
          if realdata6790['success']:     
              realprice6790 = realdata6790['realtime']['latest_trade_price']                    
              await message.channel.send('永豐實目前股價：' + realprice6790) 
              
    elif message.content == '-t 6792': 
          realdata6792=twstock.realtime.get('6792')  
          if realdata6792['success']:     
              realprice6792 = realdata6792['realtime']['latest_trade_price']                  
              await message.channel.send('詠業目前股價：' + realprice6792)               

    elif message.content == '-t 6806': 
         realdata6806=twstock.realtime.get('6806')  
         if realdata6806['success']:     
              realprice6806 = realdata6806['realtime']['latest_trade_price']                   
              await message.channel.send('森崴能源目前股價：' + realprice6806)                
              
    elif message.content == '-t 8011': 
          realdata8011=twstock.realtime.get('8011')  
          if realdata8011['success']:     
              realprice8011 = realdata8011['realtime']['latest_trade_price']             
              await message.channel.send('台通目前股價：' + realprice8011) 
              
    elif message.content == '-t 8016': 
          realdata8016=twstock.realtime.get('8016')  
          if realdata8016['success']:     
              realprice8016 = realdata8016['realtime']['latest_trade_price']                     
              await message.channel.send('矽創目前股價：' + realprice8016)               

    elif message.content == '-t 8021': 
         realdata8021=twstock.realtime.get('8021')  
         if realdata8021['success']:     
              realprice8021 = realdata8021['realtime']['latest_trade_price']             
              await message.channel.send('尖點目前股價：' + realprice8021)                   
              
    elif message.content == '-t 8028': 
          realdata8028=twstock.realtime.get('8028')  
          if realdata8028['success']:     
              realprice8028 = realdata8028['realtime']['latest_trade_price']                    
              await message.channel.send('昇陽半導體目前股價：' + realprice8028) 
              
    elif message.content == '-t 8033': 
          realdata8033=twstock.realtime.get('8033')  
          if realdata8033['success']:     
              realprice8033 = realdata8033['realtime']['latest_trade_price']                   
              await message.channel.send('雷虎目前股價：' + realprice8033)               

    elif message.content == '-t 8039': 
         realdata8039=twstock.realtime.get('8039')  
         if realdata8039['success']:     
              realprice8039 = realdata8039['realtime']['latest_trade_price']                   
              await message.channel.send('台虹目前股價：' + realprice8039)                
              
    elif message.content == '-t 8046': 
          realdata8046=twstock.realtime.get('8046')  
          if realdata8046['success']:     
              realprice8046 = realdata8046['realtime']['latest_trade_price']                   
              await message.channel.send('南電目前股價：' + realprice8046) 
              
    elif message.content == '-t 8070': 
          realdata8070=twstock.realtime.get('8070')  
          if realdata8070['success']:     
              realprice8070 = realdata8070['realtime']['latest_trade_price']                    
              await message.channel.send('長華*目前股價：' + realprice8070)               

    elif message.content == '-t 8072': 
         realdata8072=twstock.realtime.get('8072')  
         if realdata8072['success']:     
              realprice8072 = realdata8072['realtime']['latest_trade_price']                      
              await message.channel.send('陞泰目前股價：' + realprice8072)                  
              
    elif message.content == '-t 8081': 
          realdata8081=twstock.realtime.get('8081')  
          if realdata8081['success']:     
              realprice8081 = realdata8081['realtime']['latest_trade_price']                    
              await message.channel.send('致新目前股價：' + realprice8081) 
              
    elif message.content == '-t 8101': 
          realdata8101=twstock.realtime.get('8101')  
          if realdata8101['success']:     
              realprice8101 = realdata8101['realtime']['latest_trade_price']                     
              await message.channel.send('華冠目前股價：' + realprice8101)               

    elif message.content == '-t 8103': 
         realdata8103=twstock.realtime.get('8103')  
         if realdata8103['success']:     
              realprice8103 = realdata8103['realtime']['latest_trade_price']                      
              await message.channel.send('瀚荃目前股價：' + realprice8103)                
              
    elif message.content == '-t 8104': 
          realdata8104=twstock.realtime.get('8104')  
          if realdata8104['success']:     
              realprice8104 = realdata8104['realtime']['latest_trade_price']                     
              await message.channel.send('錸寶目前股價：' + realprice8104) 
              
    elif message.content == '-t 8105': 
          realdata8105=twstock.realtime.get('8105')  
          if realdata8105['success']:     
              realprice8105 = realdata8105['realtime']['latest_trade_price']                     
              await message.channel.send('凌巨目前股價：' + realprice8105)               

    elif message.content == '-t 8110': 
         realdata8110=twstock.realtime.get('8110')  
         if realdata8110['success']:     
              realprice8110 = realdata8110['realtime']['latest_trade_price']                   
              await message.channel.send('華東目前股價：' + realprice8110)                      
              
    elif message.content == '-t 8112': 
          realdata8112=twstock.realtime.get('8112')  
          if realdata8112['success']:     
              realprice8112 = realdata8112['realtime']['latest_trade_price']                    
              await message.channel.send('至上目前股價：' + realprice8112) 
              
    elif message.content == '-t 8114': 
          realdata8114=twstock.realtime.get('8114')  
          if realdata8114['success']:     
              realprice8114 = realdata8114['realtime']['latest_trade_price']                   
              await message.channel.send('振樺電目前股價：' + realprice8114)               

    elif message.content == '-t 8131': 
         realdata8131=twstock.realtime.get('8131')  
         if realdata8131['success']:     
              realprice8131 = realdata8131['realtime']['latest_trade_price']                      
              await message.channel.send('福懋科目前股價：' + realprice8131)                
              
    elif message.content == '-t 8150': 
          realdata8150=twstock.realtime.get('8150')  
          if realdata8150['success']:     
              realprice8150 = realdata8150['realtime']['latest_trade_price']                      
              await message.channel.send('南茂目前股價：' + realprice8150) 
              
    elif message.content == '-t 8163': 
          realdata8163=twstock.realtime.get('8163')  
          if realdata8163['success']:     
              realprice8163 = realdata8163['realtime']['latest_trade_price']             
              await message.channel.send('達方目前股價：' + realprice8163)               

    elif message.content == '-t 8201': 
         realdata8201=twstock.realtime.get('8201')  
         if realdata8201['success']:     
              realprice8201 = realdata8201['realtime']['latest_trade_price']                    
              await message.channel.send('無敵目前股價：' + realprice8201)                  
              
    elif message.content == '-t 8210': 
          realdata8210=twstock.realtime.get('8210')  
          if realdata8210['success']:     
              realprice8210 = realdata8210['realtime']['latest_trade_price']                
              await message.channel.send('勤誠目前股價：' + realprice8210) 
              
    elif message.content == '-t 8213': 
          realdata8213=twstock.realtime.get('8213')  
          if realdata8213['success']:     
              realprice8213 = realdata8213['realtime']['latest_trade_price']                  
              await message.channel.send('志超目前股價：' + realprice8213)               

    elif message.content == '-t 8215': 
         realdata8215=twstock.realtime.get('8215')  
         if realdata8215['success']:     
              realprice8215 = realdata8215['realtime']['latest_trade_price']                 
              await message.channel.send('明基材目前股價：' + realprice8215)                
              
    elif message.content == '-t 8222': 
          realdata8222=twstock.realtime.get('8222')  
          if realdata8222['success']:     
              realprice8222 = realdata8222['realtime']['latest_trade_price']                     
              await message.channel.send('寶一目前股價：' + realprice8222) 
              
    elif message.content == '-t 8249': 
          realdata8249=twstock.realtime.get('8249')  
          if realdata8249['success']:     
              realprice8249 = realdata8249['realtime']['latest_trade_price']                      
              await message.channel.send('菱光目前股價：' + realprice8249)               

    elif message.content == '-t 8261': 
         realdata8261=twstock.realtime.get('8261')  
         if realdata8261['success']:     
              realprice8261 = realdata8261['realtime']['latest_trade_price']                     
              await message.channel.send('富鼎目前股價：' + realprice8261)               
              
    elif message.content == '-t 8271': 
          realdata8271=twstock.realtime.get('8271')  
          if realdata8271['success']:     
              realprice8271 = realdata8271['realtime']['latest_trade_price']                    
              await message.channel.send('宇瞻目前股價：' + realprice8271) 
              
    elif message.content == '-t 8341': 
          realdata8341=twstock.realtime.get('8341')  
          if realdata8341['success']:     
              realprice8341 = realdata8341['realtime']['latest_trade_price']                    
              await message.channel.send('日友目前股價：' + realprice8341)               

    elif message.content == '-t 8367': 
         realdata8367=twstock.realtime.get('8367')  
         if realdata8367['success']:     
              realprice8367 = realdata8367['realtime']['latest_trade_price']                    
              await message.channel.send('建新國際目前股價：' + realprice8367)                
              
    elif message.content == '-t 8374': 
          realdata8374=twstock.realtime.get('8374')  
          if realdata8374['success']:     
              realprice8374 = realdata8374['realtime']['latest_trade_price']                      
              await message.channel.send('羅昇目前股價：' + realprice8374) 
              
    elif message.content == '-t 8404': 
          realdata8404=twstock.realtime.get('8404')  
          if realdata8404['success']:     
              realprice8404 = realdata8404['realtime']['latest_trade_price']                    
              await message.channel.send('百和興業-KY目前股價：' + realprice8404)               

    elif message.content == '-t 8411': 
         realdata8411=twstock.realtime.get('8411')  
         if realdata8411['success']:     
              realprice8411 = realdata8411['realtime']['latest_trade_price']         #900             
              await message.channel.send('福貞-KY目前股價：' + realprice8411)                  
              
    elif message.content == '-t 8422': 
          realdata8422=twstock.realtime.get('8422')  
          if realdata8422['success']:     
              realprice8422 = realdata8422['realtime']['latest_trade_price']               
              await message.channel.send('可寧衛目前股價：' + realprice8422) 
              
    elif message.content == '-t 8427': 
          realdata8427=twstock.realtime.get('8427')  
          if realdata8427['success']:     
              realprice8427 = realdata8427['realtime']['latest_trade_price']                  
              await message.channel.send('基勝-KY目前股價：' + realprice8427)               

    elif message.content == '-t 8429': 
         realdata8429=twstock.realtime.get('8429')  
         if realdata8429['success']:     
              realprice8429 = realdata8429['realtime']['latest_trade_price']                  
              await message.channel.send('金麗-KY目前股價：' + realprice8429)                
              
    elif message.content == '-t 8442': 
          realdata8442=twstock.realtime.get('8442')  
          if realdata8442['success']:     
              realprice8442 = realdata8442['realtime']['latest_trade_price']                     
              await message.channel.send('威宏-KY目前股價：' + realprice8442) 
              
    elif message.content == '-t 8443': 
          realdata8443=twstock.realtime.get('8443')  
          if realdata8443['success']:     
              realprice8443 = realdata8443['realtime']['latest_trade_price']                   
              await message.channel.send('阿瘦目前股價：' + realprice8443)               

    elif message.content == '-t 8454': 
         realdata8454=twstock.realtime.get('8454')  
         if realdata8454['success']:     
              realprice8454 = realdata8454['realtime']['latest_trade_price']                
              await message.channel.send('富邦媒目前股價：' + realprice8454)                      
              
    elif message.content == '-t 8462': 
          realdata8462=twstock.realtime.get('8462')  
          if realdata8462['success']:     
              realprice8462 = realdata8462['realtime']['latest_trade_price']                  
              await message.channel.send('柏文目前股價：' + realprice8462) 
              
    elif message.content == '-t 8463': 
          realdata8463=twstock.realtime.get('8463')  
          if realdata8463['success']:     
              realprice8463 = realdata8463['realtime']['latest_trade_price']                  
              await message.channel.send('潤泰材目前股價：' + realprice8463)               

    elif message.content == '-t 8464': 
         realdata8464=twstock.realtime.get('8464')  
         if realdata8464['success']:     
              realprice8464 = realdata8464['realtime']['latest_trade_price']                   
              await message.channel.send('億豐目前股價：' + realprice8464)                
              
    elif message.content == '-t 8466': 
          realdata8466=twstock.realtime.get('8466')  
          if realdata8466['success']:     
              realprice8466 = realdata8466['realtime']['latest_trade_price']               
              await message.channel.send('美吉吉-KY目前股價：' + realprice8466) 
              
    elif message.content == '-t 8467': 
          realdata8467=twstock.realtime.get('8467')  
          if realdata8467['success']:     
              realprice8467 = realdata8467['realtime']['latest_trade_price']           
              await message.channel.send('波力-KY目前股價：' + realprice8467)               

    elif message.content == '-t 8473': 
         realdata8473=twstock.realtime.get('8473')  
         if realdata8473['success']:     
              realprice8473 = realdata8473['realtime']['latest_trade_price']                   
              await message.channel.send('山林水目前股價：' + realprice8473)                  
              
    elif message.content == '-t 8478': 
          realdata8478=twstock.realtime.get('8478')  
          if realdata8478['success']:     
              realprice8478 = realdata8478['realtime']['latest_trade_price']                    
              await message.channel.send('東哥遊艇目前股價：' + realprice8478) 
              
    elif message.content == '-t 8480': 
          realdata8480=twstock.realtime.get('8480')  
          if realdata8480['success']:     
              realprice8480 = realdata8480['realtime']['latest_trade_price']                    
              await message.channel.send('泰昇-KY目前股價：' + realprice8480)               

    elif message.content == '-t 8481': 
         realdata8481=twstock.realtime.get('8481')  
         if realdata8481['success']:     
              realprice8481 = realdata8481['realtime']['latest_trade_price']                 
              await message.channel.send('政伸目前股價：' + realprice8481)                
              
    elif message.content == '-t 8482': 
          realdata8482=twstock.realtime.get('8482')  
          if realdata8482['success']:     
              realprice8482 = realdata8482['realtime']['latest_trade_price']                   
              await message.channel.send('商億-KY目前股價：' + realprice8482) 
              
    elif message.content == '-t 8488': 
          realdata8488=twstock.realtime.get('8488')  
          if realdata8488['success']:     
              realprice8488 = realdata8488['realtime']['latest_trade_price']                    
              await message.channel.send('吉源-KY目前股價：' + realprice8488)               

    elif message.content == '-t 8499': 
         realdata8499=twstock.realtime.get('8499')  
         if realdata8499['success']:     
              realprice8499 = realdata8499['realtime']['latest_trade_price']                    
              await message.channel.send('鼎炫-KY目前股價：' + realprice8499)                   
              
    elif message.content == '-t 8926': 
          realdata8926=twstock.realtime.get('8926')  
          if realdata8926['success']:     
              realprice8926 = realdata8926['realtime']['latest_trade_price']                 
              await message.channel.send('台汽電目前股價：' + realprice8926) 
              
    elif message.content == '-t 8940': 
          realdata8940=twstock.realtime.get('8940')  
          if realdata8940['success']:     
              realprice8940 = realdata8940['realtime']['latest_trade_price']                   
              await message.channel.send('新天地目前股價：' + realprice8940)               

    elif message.content == '-t 8996': 
         realdata8996=twstock.realtime.get('8996')  
         if realdata8996['success']:     
              realprice8996 = realdata8996['realtime']['latest_trade_price']                     
              await message.channel.send('高力目前股價：' + realprice8996)                
              
    elif message.content == '-t 9802': 
          realdata9802 =twstock.realtime.get('9802')  
          if realdata9802	['success']:     
              realprice9802	 = realdata9802['realtime']['latest_trade_price']                     
              await message.channel.send('鈺齊-KY目前股價：' + realprice9802) 
              
    elif message.content == '-t 9902': 
          realdata9902=twstock.realtime.get('9902')  
          if realdata9902['success']:     
              realprice9902 = realdata9902['realtime']['latest_trade_price']                    
              await message.channel.send('台火目前股價：' + realprice9902)               

    elif message.content == '-t 9904': 
         realdata9904=twstock.realtime.get('9904')  
         if realdata9904['success']:     
              realprice9904 = realdata9904['realtime']['latest_trade_price']                   
              await message.channel.send('寶成目前股價：' + realprice9904)                  
              
    elif message.content == '-t 9905': 
          realdata9905=twstock.realtime.get('9905')  
          if realdata9905['success']:     
              realprice9905 = realdata9905['realtime']['latest_trade_price']                    
              await message.channel.send('大華目前股價：' + realprice9905) 
              
    elif message.content == '-t 9906': 
          realdata9906=twstock.realtime.get('9906')  
          if realdata9906['success']:     
              realprice9906 = realdata9906['realtime']['latest_trade_price']                    
              await message.channel.send('欣巴巴目前股價：' + realprice9906)               

    elif message.content == '-t 9907': 
         realdata9907=twstock.realtime.get('9907')  
         if realdata9907['success']:     
              realprice9907 = realdata9907['realtime']['latest_trade_price']                    
              await message.channel.send('統一實目前股價：' + realprice9907)                
              
    elif message.content == '-t 9908': 
          realdata9908=twstock.realtime.get('9908')  
          if realdata9908['success']:     
              realprice9908 = realdata9908['realtime']['latest_trade_price']                    
              await message.channel.send('大台北目前股價：' + realprice9908) 
              
    elif message.content == '-t 9910': 
          realdata9910=twstock.realtime.get('9910')  
          if realdata9910['success']:     
              realprice9910 = realdata9910['realtime']['latest_trade_price']                    
              await message.channel.send('豐泰目前股價：' + realprice9910)               

    elif message.content == '-t 9911': 
         realdata9911=twstock.realtime.get('9911')  
         if realdata9911['success']:     
              realprice9911 = realdata9911['realtime']['latest_trade_price']                     
              await message.channel.send('櫻花目前股價：' + realprice9911)                      
              
    elif message.content == '-t 9912': 
          realdata9912=twstock.realtime.get('9912')  
          if realdata9912['success']:     
              realprice9912 = realdata9912['realtime']['latest_trade_price']             
              await message.channel.send('偉聯目前股價：' + realprice9912) 
              
    elif message.content == '-t 9914': 
          realdata9914=twstock.realtime.get('9914')  
          if realdata9914['success']:     
              realprice9914 = realdata9914['realtime']['latest_trade_price']             
              await message.channel.send('美利達目前股價：' + realprice9914)               

    elif message.content == '-t 9917': 
         realdata9917=twstock.realtime.get('9917')  
         if realdata9917['success']:     
              realprice9917 = realdata9917['realtime']['latest_trade_price']             
              await message.channel.send('中保科目前股價：' + realprice9917)                
              
    elif message.content == '-t 9918': 
          realdata9918=twstock.realtime.get('9918')  
          if realdata9918['success']:     
              realprice9918 = realdata9918['realtime']['latest_trade_price']                     
              await message.channel.send('欣天然目前股價：' + realprice9918) 
              
    elif message.content == '-t 9919': 
          realdata9919=twstock.realtime.get('9919')  
          if realdata9919['success']:     
              realprice9919 = realdata9919['realtime']['latest_trade_price']                      
              await message.channel.send('康那香目前股價：' + realprice9919)               

    elif message.content == '-t 9921': 
         realdata9921=twstock.realtime.get('9921')  
         if realdata9921['success']:     
              realprice9921 = realdata9921['realtime']['latest_trade_price']                  
              await message.channel.send('巨大目前股價：' + realprice9921)                  
              
    elif message.content == '-t 9924': 
          realdata9924=twstock.realtime.get('9924')  
          if realdata9924['success']:     
              realprice9924 = realdata9924['realtime']['latest_trade_price']                   
              await message.channel.send('福興目前股價：' + realprice9924) 
              
    elif message.content == '-t 9925': 
          realdata9925=twstock.realtime.get('9925')  
          if realdata9925['success']:     
              realprice9925 = realdata9925['realtime']['latest_trade_price']                      
              await message.channel.send('新保目前股價：' + realprice9925)               

    elif message.content == '-t 9926': 
         realdata9926=twstock.realtime.get('9926')  
         if realdata9926['success']:     
              realprice9926 = realdata9926['realtime']['latest_trade_price']                      
              await message.channel.send('新海目前股價：' + realprice9926)                
              
    elif message.content == '-t 9927': 
          realdata9927=twstock.realtime.get('9927')  
          if realdata9927['success']:     
              realprice9927 = realdata9927['realtime']['latest_trade_price']                      
              await message.channel.send('泰銘目前股價：' + realprice9927) 
              
    elif message.content == '-t 9928': 
          realdata9928=twstock.realtime.get('9928')  
          if realdata9928['success']:     
              realprice9928 = realdata9928['realtime']['latest_trade_price']                     
              await message.channel.send('中視目前股價：' + realprice9928)               

    elif message.content == '-t 9929': 
         realdata9929=twstock.realtime.get('9929')  
         if realdata9929['success']:     
              realprice9929 = realdata9929['realtime']['latest_trade_price']                      
              await message.channel.send('秋雨目前股價：' + realprice9929)               
              
    elif message.content == '-t 9930': 
          realdata9930=twstock.realtime.get('9930')  
          if realdata9930['success']:     
              realprice9930 = realdata9930['realtime']['latest_trade_price']                      
              await message.channel.send('中聯資源目前股價：' + realprice9930) 
              
    elif message.content == '-t 9931': 
          realdata9931=twstock.realtime.get('9931')  
          if realdata9931['success']:     
              realprice9931 = realdata9931['realtime']['latest_trade_price']                      
              await message.channel.send('欣高目前股價：' + realprice9931)               

    elif message.content == '-t 9933': 
         realdata9933=twstock.realtime.get('9933')  
         if realdata9933['success']:     
              realprice9933 = realdata9933['realtime']['latest_trade_price']                     
              await message.channel.send('中鼎目前股價：' + realprice9933)                
              
    elif message.content == '-t 9934': 
          realdata9934=twstock.realtime.get('9934')  
          if realdata9934['success']:     
              realprice9934 = realdata9934['realtime']['latest_trade_price']                     
              await message.channel.send('成霖目前股價：' + realprice9934) 
              
    elif message.content == '-t 9935': 
          realdata9935=twstock.realtime.get('9935')  
          if realdata9935['success']:     
              realprice9935 = realdata9935['realtime']['latest_trade_price']                      
              await message.channel.send('慶豐富目前股價：' + realprice9935)               

    elif message.content == '-t 9937': 
         realdata9937=twstock.realtime.get('9937')  
         if realdata9937['success']:     
              realprice9937 = realdata9937['realtime']['latest_trade_price']                      
              await message.channel.send('全國目前股價：' + realprice9937)                  
              
    elif message.content == '-t 9938': 
          realdata9938=twstock.realtime.get('9938')  
          if realdata9938['success']:     
              realprice9938 = realdata9938['realtime']['latest_trade_price']                      
              await message.channel.send('百和目前股價：' + realprice9938) 
              
    elif message.content == '-t 9939': 
          realdata9939=twstock.realtime.get('9939')  
          if realdata9939['success']:     
              realprice9939 = realdata9939['realtime']['latest_trade_price']                     
              await message.channel.send('宏全目前股價：' + realprice9939)               

    elif message.content == '-t 9940': 
         realdata9940=twstock.realtime.get('9940')  
         if realdata9940['success']:     
              realprice9940 = realdata9940['realtime']['latest_trade_price']                      
              await message.channel.send('信義目前股價：' + realprice9940)                
              
    elif message.content == '-t 9941': 
          realdata9941=twstock.realtime.get('9941')  
          if realdata9941['success']:     
              realprice9941 = realdata9941['realtime']['latest_trade_price']                     
              await message.channel.send('裕融目前股價：' + realprice9941) 
              
    elif message.content == '-t 9942': 
          realdata9942=twstock.realtime.get('9942')  
          if realdata9942['success']:     
              realprice9942 = realdata9942['realtime']['latest_trade_price']                      
              await message.channel.send('茂順目前股價：' + realprice9942)               

    elif message.content == '-t 9943': 
         realdata9943=twstock.realtime.get('9943')  
         if realdata9943['success']:     
              realprice9943 = realdata9943['realtime']['latest_trade_price']                     
              await message.channel.send('好樂迪目前股價：' + realprice9943)                      
              
    elif message.content == '-t 9944': 
          realdata9944=twstock.realtime.get('9944')  
          if realdata9944['success']:     
              realprice9944 = realdata9944['realtime']['latest_trade_price']                     
              await message.channel.send('新麗目前股價：' + realprice9944) 
              
    elif message.content == '-t 9945': 
          realdata9945=twstock.realtime.get('9945')  
          if realdata9945['success']:     
              realprice9945 = realdata9945['realtime']['latest_trade_price']                      
              await message.channel.send('潤泰新目前股價：' + realprice9945)               

    elif message.content == '-t 9946': 
         realdata9946=twstock.realtime.get('9946')  
         if realdata9946['success']:     
              realprice9946 = realdata9946['realtime']['latest_trade_price']                    
              await message.channel.send('三發地產目前股價：' + realprice9946)                
              
    elif message.content == '-t 9955': 
          realdata9955=twstock.realtime.get('9955')  
          if realdata9955['success']:     
              realprice9955 = realdata9955['realtime']['latest_trade_price']                      
              await message.channel.send('佳龍目前股價：' + realprice9955) 
              
    elif message.content == '-t 9958': 
          realdata9958=twstock.realtime.get('9958')  
          if realdata9958['success']:     
              realprice9958 = realdata9958['realtime']['latest_trade_price']                     
              await message.channel.send('世紀鋼目前股價：' + realprice9958)      


    if message.content == '-help':
        await message.channel.send("-s =覆誦\n-d =發完訊息後刪除，然後機器人覆誦一次訊息\n-t空一格公司代碼=查詢股票")
        
        
         
   
load_dotenv()        
keep_alive.keep_alive()        
client.run(os.getenv('TOKEN'))  #TOKEN在Discord Developer那邊「BOT」頁面裡面   
"""           

                        _oo0oo_
                       o8888888o
                       88" . "88
                       (| -_- |)
                       0\  =  /0
                     ___/`---'\___
                   .' \\|     |// '.
                  / \\|||  :  |||// \
                 / _||||| -:- |||||- \
                |   | \\\  -  /// |   |
                | \_|  ''\---/''  |_/ |
                \  .-\__  '-'  ___/-. /
              ___'. .'  /--.--\  `. .'___
           ."" '<  `.___\_<|>_/___.' >' "".
          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
          \  \ `_.   \_ __\ /__ _/   .-` /  /
      =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                佛祖保佑         永無BUG             
              
              
             
"""