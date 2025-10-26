# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21140176")

API_HASH = os.environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8416344037:AAFbuPcxzUI_MSKw_C8kKNhfoo1TSRjPqlw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/+-dkKSAGoUf4wZGFl") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://gouravbolange_db_user:yos9d73FCsyLpiI6@cluster0.wxnzgc0.mongodb.net/?retryWrites=true&w=majority&renamebot=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/LdT5fdJY/photo-2025-08-13-01-12-38-7537871916074270724.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6222491731').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
