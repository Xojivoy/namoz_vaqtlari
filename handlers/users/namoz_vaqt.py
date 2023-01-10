import requests
from datetime import datetime
from loader import dp
from aiogram.types import CallbackQuery
x = datetime.now()

@dp.callback_query_handler()
async def nami(call:CallbackQuery):
    callll = call.get_current()
    data = callll['data']
    url = f"https://dailyprayer.abdulrcs.repl.co/api/{data}"
    
    response = requests.get(url)
    datas = response.json()
    xufton  = datas['today']['Isha\'a']
    xufton1  = datas['tomorrow']['Isha\'a']
    osha = datas['today']['Asr']
    a,b = osha.split(":")
    a = int(a)
    b = int(b)
    y = a*60 + 40 + b
    d = y // 60
    e = y % 60
    osha1 = datas['tomorrow']['Asr']
    a1,b1 = osha1.split(":")
    a1 = int(a1)
    b1 = int(b1)
    y1 = a1*60 + 40 + b1
    d1 = y1 // 60
    e1 = y1 % 60
    txt = "❗️❕❗️Quyidagilar namoz kirish vaqtlari hisoblanadi❕❗️❕\n" 
    txt+= f"📍Viloyat : {data}\n"
    txt+= "\n⁑Bugungilik Namoz vaqtlari :\n"
    txt+= f"\n📅Kun : {x.day}.{x.month}.{x.year}\n"
    txt+= f"\n🌄Quyosh chiqishi : {datas['today']['Sunrise']}\n"
    txt+= f"\n»Bomdod : {datas['today']['Fajr']}\n"
    txt+= f"»Peshin : {datas['today']['Dhuhr']}\n"
    txt+= f"»Asr : {d}:{e}\n"
    txt+= f"»Shom : {datas['today']['Maghrib']}\n"
    txt+= f"»Xufton : {xufton}"
    txt1 = "❗️❕❗️Quyidagilar namoz kirish vaqtlari hisoblanadi❕❗️❕\n" 
    txt1+= "\n⁑Ertangilik Namoz vaqtlari :\n"
    txt1+= f"\n📅Kun : {x.day}.{x.month}.{x.year}\n"
    txt1+= f"\n🌄Quyosh chiqishi : {datas['tomorrow']['Sunrise']}\n"
    txt1+= f"\n»Bomdod : {datas['tomorrow']['Fajr']}\n"
    txt1+= f"»Peshin : {datas['tomorrow']['Dhuhr']}\n"
    txt1+= f"»Asr : {d1}:{e1}\n"
    txt1+= f"»Shom : {datas['tomorrow']['Maghrib']}\n"
    txt1+= f"»Xufton : {xufton1}"
    await call.message.answer(txt)
    await call.message.answer(txt1)
    # print(datas)
