from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "8990210984:AAGNLX_k-4RDoB5MNuGZ3rzde9hoDtL8Cho"

participantes = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Olá! Bem-vindo ao MillySorteiosBot!\n\nUse /participar para entrar no sorteio."
    )

async def participar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name

    if nome not in participantes:
        participantes.append(nome)
        await update.message.reply_text(f"✅ {nome} entrou no sorteio!")
    else:
        await update.message.reply_text("Você já está participando.")

async def sortear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not participantes:
        await update.message.reply_text("Nenhum participante cadastrado.")
        return

    vencedor = random.choice(participantes)
    await update.message.reply_text(f"🏆 O vencedor foi: {vencedor}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("participar", participar))
app.add_handler(CommandHandler("sortear", sortear))

print("Bot online...")
app.run_polling()