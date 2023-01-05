import requests
from datetime import datetime
from loader import dp
from aiogram.types import CallbackQuery
import json
x = datetime.now()

@dp.callback_query_handler(text='nam')
async def nami(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/namangan/daily/{x.day}-{x.month}-{x.year}/true/7.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"7","location":"namangan"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Namangan\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='and')
async def andi(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/andijon/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"andijon"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Andijon\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='tos')
async def tosi(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/tashkent/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"tashkent"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Toshkent\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='far')
async def fari(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/fargona/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"fargona"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"Viloyat : Farg'ona\n"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)

@dp.callback_query_handler(text='bux')
async def buxi(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/buxoro/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"buxoro"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Toshkent\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='sur')
async def suri(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/surxondaryo/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"surxondaryo"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"Viloyat : Surxondaryo"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)

@dp.callback_query_handler(text='sir')
async def siri(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/sirdaryo/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"sirdaryo"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Sirdaryo\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='jiz')
async def jizi(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/jizzax/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"jizzax"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"Viloyat : Jizzax"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)

@dp.callback_query_handler(text='qas')
async def qasi(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/qashqadaryo/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"qashqadaryo"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"Viloyat : Qashqadaryo"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)
    

@dp.callback_query_handler(text='sam')
async def sami(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/samarqand/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"samarqand"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Samarqand\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='nav')
async def navi(call : CallbackQuery):
    # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    url = f"https://muslimsalat.com/navoiy/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"navoiy"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"📍Viloyat : Navoiy\n"
    txt+= f"»Bomdod : {dates['items'][0]['fajr']}\n"
    txt+= f"🌄Quyosh chiqishi : {dates['items'][0]['shurooq']}\n"
    txt+=f"»Peshin : {dates['items'][0]['dhuhr']}\n"
    txt+=f"»Asr : {dates['items'][0]['asr']}\n"
    txt+=f"»Shom : {dates['items'][0]['maghrib']}\n"
    txt+=f"»Xufton : {dates['items'][0]['isha']}\n"
    txt+=f"\n🕋Qibla : {dates['qibla_direction']}° da"

    await call.message.answer(txt)

@dp.callback_query_handler(text='xor')
async def xori(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/xorazm/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"xorazm"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"Viloyat : Xorazm"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)

@dp.callback_query_handler(text='qor')
async def qori(call : CallbackQuery):
    # # url = "https://muslimsalat.p.rapidapi.com/tashkent/(times)/(date)/(daylight)/(method).json"
    # url = f"https://muslimsalat.com/qoraqalpogiston/daily/{x.day}-{x.month}-{x.year}/true/5.json"
    # querystring = {"times":"daily","date":f"{x.day}-{x.month}-{x.year}","method":"5","location":"qoraqalpogiston"}

    # headers = {
    #     "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
    #     "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # dates=json.loads(response.text)
    txt = "Bugungi namoz vaqtlari\n"
    txt+= f"\n📅Kun : {x.day}-{x.month}-{x.year}\n"
    txt+= f"Viloyat : Qoraqalpog'iston"
    txt+= f"Afsuski bu viloyat bo'yicha so'rovnoma topilmadi."

    await call.message.answer(txt)