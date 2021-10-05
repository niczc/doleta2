import telebot
from datetime import datetime
import threading
from telebot import types
from telebot import util, types
import time
import teoric


bot = telebot.TeleBot('1595466561:AAFPU9UkZGG-ZC-OOXQld0L2w5A8NPmOpqI')

@bot.message_handler(commands=['start'])
def start_menu(message):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Operacionais", callback_data = "operacionais")
    item2 = types.InlineKeyboardButton("Ferramentas", callback_data = "ferramentas")
    item3 = types.InlineKeyboardButton('Psicologia do Trader', callback_data= 'psicologia')
    item4 = types.InlineKeyboardButton('Informações', callback_data= 'informacoes')
    item5 = types.InlineKeyboardButton('Panorama', callback_data = 'panorama')
    mkup.add(item1, item2, item3, item4, item5)
    text = "Olá, " + message.from_user.first_name +  " ,eu sou o Doleta. Precisa de ajuda? "
    bot.send_message(message.chat.id, text, reply_markup=mkup)
   
@bot.callback_query_handler(func = lambda call: call.data == 'panorama')
def panorama_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width = 1)
    item1 = types.InlineKeyboardButton("Calendário Econômico", callback_data = 'calenda')
    item2 = types.InlineKeyboardButton("Voltar", callback_data = 'back')
    mkup.add(item1, item2)
    text = "Panorama Diário"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)
    
@bot.callback_query_handler(func = lambda call: call.data == 'operacionais')
def opera_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Absorção", callback_data = 'abs')
    item2 = types.InlineKeyboardButton("Exaustao", callback_data = 'ext')
    item3 = types.InlineKeyboardButton("Lote de Liquidez", callback_data = 'liq')
    item4 = types.InlineKeyboardButton("Lote de Escora", callback_data = 'esc')
    item5 = types.InlineKeyboardButton("Renovação", callback_data = 'ren')
    item6 = types.InlineKeyboardButton("Cancelamento", callback_data = 'can')
    item7 = types.InlineKeyboardButton("Voltar", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Operacionais disponiveis"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)
    
@bot.callback_query_handler(func = lambda call: call.data == 'ferramentas')
def ferra_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Times & Trades", callback_data = 'time')
    item2 = types.InlineKeyboardButton("Book de Ofertas", callback_data = 'book')
    item3 = types.InlineKeyboardButton("Super DOM", callback_data = 'dom')
    item4 = types.InlineKeyboardButton("Volume At Price", callback_data = 'vol')
    item5 = types.InlineKeyboardButton("VWAP", callback_data = 'vwap')
    item6 = types.InlineKeyboardButton("Ajuste", callback_data = 'ajuste')
    item7 = types.InlineKeyboardButton("Voltar", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Ferramentas"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func = lambda call: call.data == 'psicologia')
def psico_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Ansiedade", callback_data = 'ansiedade')
    item2 = types.InlineKeyboardButton("Medo", callback_data = 'medo')
    item3 = types.InlineKeyboardButton("Não aceita os erros", callback_data = 'n_erros')
    item4 = types.InlineKeyboardButton("Auto Sabotagem", callback_data = 'sabotagem')
    item5 = types.InlineKeyboardButton("Não sabe perder", callback_data = 'n_perder')
    item6 = types.InlineKeyboardButton("Não sabe ganhar", callback_data = 'n_ganhar')
    item7 = types.InlineKeyboardButton("Dinheiro Rápido", callback_data = 'p_dinheiro')
    item8 = types.InlineKeyboardButton("Sem estudar", callback_data = 'n_estudar')
    item9 = types.InlineKeyboardButton("Metas e Objetivos", callback_data = 'n_metas')
    item10 = types.InlineKeyboardButton("Insegurança", callback_data = 'p_dinheiro')
    item11 = types.InlineKeyboardButton("Saiba mais ", url = "https://instagram.com/renanreligare?utm_medium=copy_link")
    item12 = types.InlineKeyboardButton("Voltar", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7,item8, item9, item10, item11, item12)
    text = "Psicologia do Trader por @RenanReligare"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func = lambda call: call.data == 'informacoes')
def opera_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Regras do Grupo", callback_data = 'abs')
    item2 = types.InlineKeyboardButton("Canal do Youtube", url = 'https://youtube.com.br/olhonoreplay')
    item3 = types.InlineKeyboardButton("Perfil do Instagram", url = 'https://instagram.com/olhonoreplay')
    item3 = types.InlineKeyboardButton("Replay do Dia", callback_data = 'replay')
    item4 = types.InlineKeyboardButton("Lista dos Replays", callback_data = 'lista')
    item5 = types.InlineKeyboardButton("Quero Vinho", callback_data = 'vinho')
    item6 = types.InlineKeyboardButton("Fale com o Desenvolvedor", url = 'https://t.me/Nicolasleao')
    item7 = types.InlineKeyboardButton("Voltar", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Informações do Grupo"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)


@bot.callback_query_handler(func = lambda call: call.data == 'back')
def bac_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Operacionais", callback_data = "operacionais")
    item2 = types.InlineKeyboardButton("Ferramentas", callback_data = "ferramentas")
    item3 = types.InlineKeyboardButton('Psicologia do Trader', callback_data= 'psicologia')
    item4 = types.InlineKeyboardButton('Informações', callback_data= 'informacoes')
    mkup.add(item1, item2, item3, item4)
    text = "Você novamente por aqui? Surgiu mais alguma dúvida? "
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)   


@bot.callback_query_handler(func = lambda call: True)
def asnwer(call):
    #calendario
    noticias = []
    for info in teoric.resultados:
        pais = info['par']
        eventu = info['evento']
        hora = info['horario']
        data_e_hora = datetime.strptime(hora,'%Y/%m/%d %H:%M:%S')
        hora  = data_e_hora.strftime('%H:%M')
        impacto = info['impacto']
        economic = pais + ": " + eventu + " - " + hora + " " + impacto
        noticias.append(economic)
        one_message = ['\n \n'.join(noticias)]
    if call.data == 'calenda':
        print(one_message)
        msg = bot.send_message(call.message.chat.id, one_message)
        threading.Timer(45, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    #operacionais
    if call.data == 'abs':
        msg = bot.send_message(call.message.chat.id, teoric.absorcao)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'ext':
        msg = bot.send_message(call.message.chat.id, teoric.exaustao)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'liq':
        msg = bot.send_message(call.message.chat.id, teoric.liquidez)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'esc':
        msg = bot.send_message(call.message.chat.id, teoric.escora)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'ren':
        msg = bot.send_message(call.message.chat.id, teoric.renovacao)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'can':
        msg = bot.send_message(call.message.chat.id, teoric.cancelamento)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    
    #ferramentas
    if call.data == 'time':
        msg = bot.send_message(call.message.chat.id, teoric.times)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'book':
        msg = bot.send_message(call.message.chat.id, teoric.book)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'dom':
        msg = bot.send_message(call.message.chat.id, teoric.dom)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'vol':
        msg = bot.send_message(call.message.chat.id, teoric.vol)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'vwap':
        msg = bot.send_message(call.message.chat.id, teoric.vwap)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'ajuste':
        msg = bot.send_message(call.message.chat.id, teoric.ajuste)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
        
        #Psicologia 
    if call.data == 'ansiedade':
        msg = bot.send_message(call.message.chat.id, teoric.ansiedade)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'medo':
        msg = bot.send_message(call.message.chat.id, teoric.medo)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'n_erros':
        bot.send_message(call.message.chat.id, teoric.n_erros)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'sabotagem':
        bot.send_message(call.message.chat.id, teoric.sabotagem)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'n_perder':
        bot.send_message(call.message.chat.id, teoric.n_perder)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'n_ganhar':
        bot.send_message(call.message.chat.id, teoric.n_ganhar)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'p_dinheiro':
        bot.send_message(call.message.chat.id, teoric.p_dinheiro)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'n_estudar':
        bot.send_message(call.message.chat.id, teoric.n_estudar)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'n_metas':
        bot.send_message(call.message.chat.id, teoric.n_metas)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'inseguranca':
        bot.send_message(call.message.chat.id, teoric.inseguranca)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()

        #Informações
    if call.data == 'rules':
        msg = bot.send_message(call.message.chat.id, teoric.rules)
        threading.Timer(40, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'replay':
        msg = bot.send_message(call.message.chat.id, teoric.replay)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'lista':
        msg = bot.send_message(call.message.chat.id, teoric.lista)
        threading.Timer(25, bot.delete_message, (msg.chat.id, msg.message_id)).start()
    if call.data == 'vinho':
        msg = bot.send_message(call.message.chat.id, teoric.vinho)
        threading.Timer(15, bot.delete_message, (msg.chat.id, msg.message_id)).start()


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
    
