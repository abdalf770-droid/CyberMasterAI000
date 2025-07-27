import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if context.user_data.get("mode") == "choose_encrypt_or_decrypt":
        if "تشفير" in text:
            context.user_data["action"] = "encrypt"
            context.user_data["mode"] = "choose_encryption_type"
        elif "فك التشفير" in text:
            context.user_data["action"] = "decrypt"
            context.user_data["mode"] = "choose_encryption_type"
        else:
            await update.message.reply_text("❗️اختر من الأزرار.")
            return
        
        keyboard = [
            ["🔐 AES", "🔐 Caesar"],
            ["🔐 Base64", "🔐 Vigenère"],
            ["⬅️ رجوع"]
        ]
        await update.message.reply_text(
            "اختر نوع التشفير/فك التشفير:",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    elif context.user_data.get("mode") == "choose_encryption_type":
        algo = text.replace("🔐", "").strip().lower()
        context.user_data["algorithm"] = algo
        
        if context.user_data["action"] == "encrypt":
            context.user_data["mode"] = "encrypt_input"
            await update.message.reply_text(f"✍️ أرسل النص لتشفيره باستخدام {algo.upper()}")
        else:
            context.user_data["mode"] = "decrypt_input"
            await update.message.reply_text(f"✍️ أرسل النص لفك تشفيره باستخدام {algo.upper()}")

    elif "🔐 التشفير وفك التشفير" in text:
        context.user_data.clear()
        context.user_data["mode"] = "choose_encrypt_or_decrypt"
        keyboard = [
            ["🔒 تشفير", "🔓 فك التشفير"],
            ["⬅️ رجوع"]
        ]
        await update.message.reply_text("اختر العملية التي تريد تنفيذها:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif "تحليل الشبكات" in text:
        await update.message.reply_text("✍️ أرسل عنوان IP مع CIDR (مثل: 192.168.1.0/24)")

    elif "الإخفاء داخل الصور" in text:
        await update.message.reply_text("📷 أرسل الصورة لإخفاء أو استخراج النص.")

    elif "تحويل أنظمة العد" in text:
        await update.message.reply_text("📊 أرسل الرقم وسيتم تحويله بين (ثنائي - عشري - سداسي).")

    elif "تحويل الأكواد" in text:
        await update.message.reply_text("💻 أرسل الكود + اللغة التي تريد التحويل منها وإليها.")

    elif "اختبار الأمن السيبراني" in text:
        await update.message.reply_text("🧠 سيتم الآن بدء اختبار الأمن السيبراني...")

    elif "OSINT" in text:
        await update.message.reply_text("🔍 أرسل اسم المستخدم أو الإيميل لفحصه.")

    elif "شروحات الأمن" in text:
        await update.message.reply_text("📚 سيتم عرض الشروحات المتوفرة...")

    else:
        await update.message.reply_text("❗️الأمر غير معروف. اختر من الأزرار.")

def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()
