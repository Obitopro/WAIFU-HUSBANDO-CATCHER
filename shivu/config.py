class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5490773419"
    sudo_users = "5490773419", "2029960806", "1856430691", "6014835961"
    GROUP_ID = -1002075695525
    TOKEN = "6586089421:AAECQGc2Ca-GwHkdhjC_yoMaIXR8oBuzQA0"
    mongo_url = "mongodb+srv://itachi:itachi@itachi.hyhnjlq.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/06355103255bdeaf79912.jpg", "https://telegra.ph/file/8d7966de81833aca719f5.jpg"]
    SUPPORT_CHAT = "lootgroup25"
    UPDATE_CHAT = "lootupdatesop"
    BOT_USERNAME = "Lootwaifubot"
    CHARA_CHANNEL_ID = "-1002075695525"
    api_id = "24658337"
    api_hash = "bf99242dbb7f3501f28d39f0a0383cbf"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
