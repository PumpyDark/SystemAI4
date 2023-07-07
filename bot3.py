import logging,time,requests
from telegram import Update
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
# Global variable untuk menyimpan kunci
kunci = None

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username if user.username else user.first_name
    text = update.message.text
    print("==========================================")
    print(f"Pengguna \033[95m{username}\033[97m mengirim pesan: \033[92m{text}\033[97m")
    user_id = user.id
    print("==========================================")
    print(f"💻Nama Pengguna: \033[95m{user.first_name}\033[97m")
    print(f"👤Username: \033[92m@{username}\033[97m")
    print(f"💬ID Obrolan: \033[93m{user_id}\033[97m")
    now = datetime.now()
    tanggal = now.strftime("%Y-%m-%d")
    jam = now.strftime("%H:%M:%S")
    print(f"⌛Tanggal: \033[96m{tanggal}\033[97m")
    print(f"🕧Jam: \033[96m{jam}\033[97m")
    print("==========================================")
    global kunci
    if kunci is None:
        update.message.reply_text('Halo! Selamat datang di bot Telegram.\nSilakan masukkan kunci untuk mengakses fitur bot.')
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('/data/data/com.termux/files/home/bot-telegram/music/music1.mp3', 'rb'))
    else:
        update.message.reply_text('Halo! Anda sudah memiliki akses ke fitur bot.')
# Fungsi untuk menangani pesan teks
def handle_message(update: Update, context: CallbackContext) -> None:
    global kunci
    user = update.message.from_user
    text = update.message.text
    if kunci is None:
        if text == '200518':
            kunci = text
            update.message.reply_text('Kunci berhasil disimpan. Anda sekarang memiliki akses ke fitur bot.')
            update.message.reply_text(""" 🤖 *Selamat datang di Bot Teks Banding!*

🌟 *Perintah yang Tersedia:*
-------------------------------------
/start - Memulai bot
/owner - Melihat info owner
/banding - (/banding +6284858xxxx)
/banding2 - (/banding2 +6284858xxxx)

📝 Gunakan perintah tersebut untuk berinteraksi dengan bot. Terima kasih! 🙏""")
        else:
            update.message.reply_text('Anda harus memasukkan kunci yang benar. Silakan coba lagi.')
    else:
        update.message.reply_text(f"( {text} ) ⚠️ Belum Tersedia Di Menu !!!")

# Fungsi untuk menampilkan informasi pemilik bot
TOKEN = "6132847045:AAFfUUkE8kEw1UqRzce84TZPFeTZT5h9tvw"
YOUTUBE_URL = 'https://youtube.com/@Kz.tutorial'
INSTAGRAM_URL = 'https://instagram.com/kz.tutorial97'
DONATION_URL = 'https://saweria.co/Kztutorial'
WHATSAPP_NUMBER = '6289502821173'

def owner(update, context):
    """Handler for /owner command"""
    keyboard = [[InlineKeyboardButton("Youtube \U0001F4F9", url=YOUTUBE_URL)],
                [InlineKeyboardButton("Instagram \U0001F4F8", url=INSTAGRAM_URL)],
                [InlineKeyboardButton("WhatsApp \U0001F4DE", url=f'https://api.whatsapp.com/send?phone={WHATSAPP_NUMBER}&text=Hello')],
                [InlineKeyboardButton("Donasi \U0001F4B0", url=DONATION_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("👋Hi! My name is 👤SyatemAI, I am the owner of this bot. You can find me on the following platforms:", reply_markup=reply_markup)
    update.message.reply_text(message)
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('/data/data/com.termux/files/home/bot-telegram/music/music.mp3', 'rb'))

def done(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.effective_chat.id

    # Mendapatkan nomor dari input pengguna
    number = update.message.text.split('/done ')[1]

    # Memeriksa keberadaan nomor dalam file "done.txt"
    if check_existing_number(number):
        update.message.reply_text("⚠️ Maaf, nomor tersebut sudah tersimpan sebelumnya.")
    else:
        # Menyimpan nomor dan informasi waktu ke file "done.txt"
        with open("done.txt", "a") as file:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            time_period = "malam" if int(now.strftime("%H")) >= 18 else "pagi"
            emoji = "🌙" if time_period == "malam" else "🌞"
            file.write(f"========[ BERHASIL ]==========\n📱 {number}\n⌛ {timestamp}\n{emoji} ({time_period})\n=============================\n")
        update.message.reply_text("✅ Nomor berhasil disimpan.")

# Fungsi untuk menyimpan nomor ke dalam file
def save_number(number: str) -> None:
    with open("done.txt", "a") as file:
        file.write(number + "\n")

# Fungsi untuk memeriksa keberadaan nomor dalam file
def check_existing_number(number: str) -> bool:
    with open("done.txt", "r") as file:
        for line in file:
            if line.strip() == number:
                return True
    return False

def banding(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.effective_chat.id

    # Menampilkan notifikasi sedang membuat
    time.sleep(1)  # Menunggu selama 2 detik sebagai simulasi pembuatan teks banding
    user_number = update.message.text.split('/banding ')[1]
    update.message.reply_text("Subjek: Permohonan Pemulihan Akun WhatsApp Yang Di Blokir")
    banding_text = f"""Kepada Tim Dukungan WhatsApp,

Saya menulis ini dengan harapan dapat mengajukan banding terkait pemblokiran tiba-tiba pada akun WhatsApp saya. Nomor WhatsApp saya adalah {user_number}. Saya sangat menghargai waktu dan perhatian Anda dalam membaca permohonan saya.

Saya ingin menjelaskan bahwa saya telah menggunakan akun WhatsApp dengan sepenuhnya sesuai dengan kebijakan dan pedoman yang ditetapkan. Saya tidak melanggar aturan apa pun yang berlaku. Namun, sayangnya, akun saya tiba-tiba diblokir tanpa pemberitahuan atau penjelasan yang jelas.

Saya sangat bergantung pada akun WhatsApp saya untuk berkomunikasi dengan keluarga, teman, dan rekan bisnis. Kehilangan akses ke akun WhatsApp saya memberikan dampak yang signifikan pada kehidupan pribadi dan profesional saya.

Nomor WhatsApp: {user_number}"""

    # Mengirim teks banding ke pengguna
    context.bot.send_message(chat_id=chat_id, text=banding_text)

    # Mengirim hasil banding ke alamat email support@whatsapp.com

    # Mengirim konfirmasi ke pengguna
    update.message.reply_text("Terima kasih! Permohonan banding Anda telah dikirim.")

def banding2(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.effective_chat.id

    # Menampilkan notifikasi sedang membuat
#    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    time.sleep(1)  # Menunggu selama 2 detik sebagai simulasi pembuatan teks banding

    # Membuat contoh teks banding yang lebih panjang dan lebih profesional
    user_number = update.message.text.split('/banding2 ')[1]
    update.message.reply_text("Subjek: Permohonan Pemulihan Akun WhatsApp Yang Di Blokir")
    banding_text = f"""Kepada Tim Dukungan WhatsApp,

Saya menulis ini dengan tujuan mengajukan banding terkait pemblokiran akun WhatsApp saya. Saya sangat menghargai waktu dan perhatian Anda dalam meninjau permohonan saya.

Saya ingin menjelaskan bahwa saya telah menggunakan akun WhatsApp saya dengan mematuhi semua kebijakan dan pedoman yang ditetapkan. Saya memahami bahwa penggunaan WhatsApp yang melanggar aturan dapat menyebabkan pemblokiran, tetapi saya meyakinkan Anda bahwa saya tidak terlibat dalam pelanggaran apa pun.

Akun WhatsApp saya sangat penting bagi saya karena saya menggunakannya untuk berkomunikasi dengan keluarga, teman, dan rekan kerja. Saya telah membangun jaringan kontak yang luas melalui platform ini dan kehilangan akses ke akun saya akan memiliki dampak yang signifikan pada kehidupan pribadi dan profesional saya.

Saya mengharapkan agar tim dukungan WhatsApp dapat mengkaji kembali pemblokiran akun saya dan memberikan kesempatan kepada saya untuk membuktikan bahwa saya adalah pengguna yang mematuhi aturan. Saya siap untuk memberikan informasi tambahan atau bukti yang diperlukan untuk mendukung permohonan saya.

Terlampir di bawah ini adalah rincian akun WhatsApp saya:
- Nomor WhatsApp: {user_number}

Saya berharap agar keputusan pemblokiran akun saya dapat ditinjau ulang dengan saksama. Saya mengucapkan terima kasih atas perhatian dan kerjasama Anda dalam menyelesaikan masalah ini."""

    # Mengirim teks banding ke pengguna
    context.bot.send_message(chat_id=chat_id, text=banding_text)
    update.message.reply_text("Terima kasih! Permohonan banding2 Anda telah dikirim.")
# Fungsi untuk menangani pesan teks selain dari perintah /banding
def handle_text(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Perintah tidak valid. Silakan gunakan perintah /banding [nomor WhatsApp].")

def main() -> None:
    # Inisialisasi objek Updater
    updater = Updater("6132847045:AAFfUUkE8kEw1UqRzce84TZPFeTZT5h9tvw", use_context=True)
    updater = Updater(token=TOKEN, use_context=True)
    # Dapatkan objek Dispatcher dari updater
    dispatcher = updater.dispatcher
    dp = updater.dispatcher
    # Daftarkan handler untuk perintah /start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("done", done))
    dp.add_handler(CommandHandler("owner", owner))
    dispatcher.add_handler(CommandHandler("banding", banding))
    dispatcher.add_handler(CommandHandler("banding2", banding2))
    # Daftarkan handler untuk pesan teks
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Jalankan bot
    updater.start_polling()

    # Tetap jalankan bot sampai Ctrl-C ditekan
    updater.idle()

if __name__ == '__main__':
    main()
