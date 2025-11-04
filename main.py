import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp , random , asyncio
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
try:
    from cfonts import render, say
except ImportError:
    # Fallback if cfonts is not available
    def render(text, **kwargs):
        return text
    def say(text, **kwargs):
        print(text)

# EMOTE DATABASE
EMOTE_DATABASE = {
    # Sequence 1-30 (Existing)
    1: 909000081,
    2: 909000075,
    3: 909000068,
    4: 909000063,
    5: 909000090,
    6: 909033002,
    7: 909033001,
    8: 909000085,
    9: 909039011,
    10: 909038012,
    11: 909035012,
    12: 909035007,
    13: 909042008,
    14: 909049010,
    15: 909045001,
    16: 909041005,
    17: 909040010,
    18: 909051003,
    19: 909051001,
    20: 909051002,
    21: 909051004,
    22: 909051005,
    23: 909051010,
    24: 909051012,
    25: 909051013,
    26: 909051013, # Note: Duplicate ID with 25
    27: 909051014,
    28: 909051015,
    29: 909051017,
    30: 909042007,
    # Sequence 31-262 (Existing)
    31: 909000001,
    32: 909000002,
    33: 909000003,
    34: 909000004,
    35: 909000005,
    36: 909000006,
    37: 909000007,
    38: 909000008,
    39: 909000009,
    40: 909000010,
    41: 909000011,
    42: 909000012,
    43: 909000013,
    44: 909000014,
    45: 909000015,
    46: 909000016,
    47: 909000017,
    48: 909000018,
    49: 909000019,
    50: 909000020,
    51: 909000021,
    52: 909000022,
    53: 909000023,
    54: 909000024,
    55: 909000025,
    56: 909000026,
    57: 909000027,
    58: 909000028,
    59: 909000029,
    60: 909000030,
    61: 909000031,
    62: 909000032,
    63: 909000033,
    64: 909000034,
    65: 909000035,
    66: 909000036,
    67: 909000037,
    68: 909000038,
    69: 909000039,
    70: 909000040,
    71: 909000041,
    72: 909000042,
    73: 909000043,
    74: 909000044,
    75: 909000045,
    76: 909000046,
    77: 909000047,
    78: 909000048,
    79: 909000049,
    80: 909000050,
    81: 909000051,
    82: 909000052,
    83: 909000053,
    84: 909000054,
    85: 909000055,
    86: 909000056,
    87: 909000057,
    88: 909000058,
    89: 909000059,
    90: 909000060,
    91: 909000061,
    92: 909000062,
    93: 909000063,
    94: 909000064,
    95: 909000065,
    96: 909000066,
    97: 909000067,
    98: 909000068,
    99: 909000069,
    100: 909000070,
    101: 909000071,
    102: 909000072,
    103: 909000073,
    104: 909000074,
    105: 909000075,
    106: 909000076,
    107: 909000077,
    108: 909000078,
    109: 909000079,
    110: 909000080,
    111: 909000081,
    112: 909000082,
    113: 909000083,
    114: 909000084,
    115: 909000085,
    116: 909000086,
    117: 909000087,
    118: 909000088,
    119: 909000089,
    120: 909000090,
    121: 909000091,
    122: 909000092,
    123: 909000093,
    124: 909000094,
    125: 909000095,
    126: 909000096,
    127: 909000097,
    128: 909000098,
    129: 909000099,
    130: 909000100,
    131: 909000101,
    132: 909000102,
    133: 909000103,
    134: 909000104,
    135: 909000105,
    136: 909000106,
    137: 909000107,
    138: 909000108,
    139: 909000109,
    140: 909000110,
    141: 909000111,
    142: 909000112,
    143: 909000113,
    144: 909000114,
    145: 909000115,
    146: 909000116,
    147: 909000117,
    148: 909000118,
    149: 909000119,
    150: 909000120,
    151: 909000121,
    152: 909000122,
    153: 909000123,
    154: 909000124,
    155: 909000125,
    156: 909000126,
    157: 909000127,
    158: 909000128,
    159: 909000129,
    160: 909000130,
    161: 909000131,
    162: 909000132,
    163: 909000133,
    164: 909000134,
    165: 909000135,
    166: 909000136,
    167: 909000137,
    168: 909000138,
    169: 909000139,
    170: 909000140,
    171: 909000141,
    172: 909000142,
    173: 909000143,
    174: 909000144,
    175: 909000145,
    176: 909000146,
    177: 909000147,
    178: 909000148,
    179: 909000149,
    180: 909000150,
    181: 909033001,
    182: 909033002,
    183: 909033003,
    184: 909033004,
    185: 909033005,
    186: 909033006,
    187: 909033007,
    188: 909033008,
    189: 909033009,
    190: 909033010,
    191: 909034001,
    192: 909034002,
    193: 909034003,
    194: 909034004,
    195: 909034005,
    196: 909034006,
    197: 909034007,
    198: 909034008,
    199: 909034009,
    200: 909034010,
    201: 909034011,
    202: 909034012,
    203: 909034013,
    204: 909034014,
    205: 909034015,
    206: 909035001,
    207: 909035002,
    208: 909035003,
    209: 909035004,
    210: 909035005,
    211: 909035006,
    212: 909035007,
    213: 909035008,
    214: 909035009,
    215: 909035010,
    216: 909035011,
    217: 909035012,
    218: 909035013,
    219: 909035014,
    220: 909036001,
    221: 909036002,
    222: 909036003,
    223: 909036004,
    224: 909036005,
    225: 909036006,
    226: 909036007,
    227: 909036008,
    228: 909036009,
    229: 909036010,
    230: 909036011,
    231: 909037001,
    232: 909037002,
    233: 909037003,
    234: 909037004,
    235: 909037005,
    236: 909037006,
    237: 909037007,
    238: 909037008,
    239: 909037009,
    240: 909037010,
    241: 909038001,
    242: 909038002,
    243: 909038003,
    244: 909038004,
    245: 909038005,
    246: 909038006,
    247: 909038007,
    248: 909038008,
    249: 909038009,
    250: 909038010,
    251: 909038011,
    252: 909039001,
    253: 909039002,
    254: 909039003,
    255: 909039004,
    256: 909039005,
    257: 909039006,
    258: 909039007,
    259: 909039008,
    260: 909039009,
    261: 909039010,
    262: 909039011,
    # --- NEW EMOTES (Sequence 263-410) ---
    263: 909040001,
    264: 909040002,
    265: 909040003,
    266: 909040004,
    267: 909040005,
    268: 909040006,
    269: 909040007,
    270: 909040008,
    271: 909040009,
    272: 909040010,
    273: 909040011,
    274: 909040012,
    275: 909041001,
    276: 909041002,
    277: 909041003,
    278: 909041004,
    279: 909041005,
    280: 909041006,
    281: 909041007,
    282: 909041008,
    283: 909041009,
    284: 909041010,
    285: 909041011,
    286: 909041012,
    287: 909042001,
    288: 909042002,
    289: 909042003,
    290: 909042004,
    291: 909042005,
    292: 909042006,
    293: 909042007,
    294: 909042008,
    295: 909042009,
    296: 909042010,
    297: 909042011,
    298: 909042012,
    299: 909043001,
    300: 909043002,
    301: 909043003,
    302: 909043004,
    303: 909043005,
    304: 909043006,
    305: 909043007,
    306: 909043008,
    307: 909043009,
    308: 909043010,
    309: 909043011,
    310: 909043012,
    311: 909044001,
    312: 909044002,
    313: 909044003,
    314: 909044004,
    315: 909044005,
    316: 909044006,
    317: 909044007,
    318: 909044008,
    319: 909044009,
    320: 909044010,
    321: 909044011,
    322: 909044012,
    323: 909045001,
    324: 909045002,
    325: 909045003,
    326: 909045004,
    327: 909045005,
    328: 909045006,
    329: 909045007,
    330: 909045008,
    331: 909045009,
    332: 909045010,
    333: 909045011,
    334: 909045012,
    335: 909046001,
    336: 909046002,
    337: 909046003,
    338: 909046004,
    339: 909046005,
    340: 909046006,
    341: 909046007,
    342: 909046008,
    343: 909046009,
    344: 909046010,
    345: 909046011,
    346: 909046012,
    347: 909047001,
    348: 909047002,
    349: 909047003,
    350: 909047004,
    351: 909047005,
    352: 909047006,
    353: 909047007,
    354: 909047008,
    355: 909047009,
    356: 909047010,
    357: 909047011,
    358: 909047012,
    359: 909048001,
    360: 909048002,
    361: 909048003,
    362: 909048004,
    363: 909048005,
    364: 909048006,
    365: 909048007,
    366: 909048008,
    367: 909048009,
    368: 909048010,
    369: 909048011,
    370: 909048012,
    371: 909049001,
    372: 909049002,
    373: 909049003,
    374: 909049004,
    375: 909049005,
    376: 909049006,
    377: 909049007,
    378: 909049008,
    379: 909049009,
    380: 909049010,
    381: 909049011,
    382: 909049012,
    383: 909050001,
    384: 909050002,
    385: 909050003,
    386: 909050004,
    387: 909050005,
    388: 909050006,
    389: 909050007,
    390: 909050008,
    391: 909050009,
    392: 909050010,
    393: 909050011,
    394: 909050012,
    395: 909050013,
    396: 909050014,
    397: 909050015,
    398: 909050016,
    399: 909050017,
    400: 909050018,
    401: 909050019,
    402: 909050020,
    403: 909050021,
    404: 909050022,
    405: 909050023,
    406: 909050024,
    407: 909050025,
    408: 909050026,
    409: 909050027,
    410: 909050028,
}


# Store player IDs for each chat group
GROUP_PLAYER_IDS = {}

#EMOTES BY PARAHEX X CODEX

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
spam_task = None
is_spamming = False
BOT_UID = None # <-- বটের UID এখানে সেভ হবে
CURRENT_SQUAD_SIZE = 4 # <-- স্কোয়াডের আকার ট্র্যাক করুন, ডিফল্ট 4
#------------------------------------------#
# --- OWNER INFO (EDIT THIS) ---
# --- অনুগ্রহ করে এই জায়গাটি এডিট করুন ---
OWNER_NAME = "ATX ABIR"
OWNER_TELEGRAM_USER = "atxabir" # <-- শুধু ইউজারনেম, @ ছাড়া
OWNER_TELEGRAM_CHANNEL = "atxmaximbd1" # <-- শুধু চ্যানেলের নাম/লিংক
OWNER_YOUTUBE_CHANNEL = "ATX MAXIM BD" # <-- চ্যানেলের নাম
#------------------------------------------#

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB51"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

# --- FIXED FUNCTION ---
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=Hr, data=data) as response:
                if response.status != 200: 
                    print(f"Garena login failed. Status: {response.status}, Response: {await response.text()}")
                    return (None, None) # <-- FIX 1: Return tuple on failure
                data = await response.json()
                open_id = data.get("open_id")
                access_token = data.get("access_token")
                return (open_id, access_token) if open_id and access_token else (None, None)
    except Exception as e:
        print(f"Error during GeNeRaTeAccEss request: {e}")
        return (None, None) # <-- FIX 2: Return tuple on network error

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.118.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0OUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'

async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

# --- 🟢 [STABILITY FIX] ---
# এই ফাংশনটি এখন কোনো কানেকশন এরর পেলে তা "থ্রো" করবে,
# যা TcPChaT বা TcPOnLine-কে রিকানেক্ট করতে বাধ্য করবে।
async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    # OnLinE = online_writer
    # ChaT = whisper_writer
    try:
        if TypE == 'ChaT':
            if ChaT: # Check if the chat writer (whisper_writer) is valid
                ChaT.write(PacKeT)
                await ChaT.drain()
            else:
                print("SEndPacKeT Error: Chat writer (ChaT) is None. Cannot send message.")
        elif TypE == 'OnLine':
            if OnLinE: # Check if the online writer (online_writer) is valid
                OnLinE.write(PacKeT)
                await OnLinE.drain()
            else:
                print("SEndPacKeT Error: Online writer (OnLinE) is None. Cannot send packet.")
        else: 
            print(f"SEndPacKeT Error: Unsupported type '{TypE}'")
            return 'UnsoPorTed TypE ! >> ErrrroR (:():)'
    except Exception as e:
        # --- ✅ [FIXED] ---
        # এররটি প্রিন্ট করুন এবং এটিকে আবার "থ্রো" করুন
        # এটি TcPChaT বা TcPOnLine-কে রিকানেক্ট করতে বাধ্য করবে
        print(f"SEndPacKeT Write Error ({TypE} packet) - Forcing Reconnect: {e}")
        raise e # <-- এই লাইনটি সবচেয়ে গুরুত্বপূর্ণ
# --- 🟢 END FIX ---

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break

                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                        await SEndPacKeT(online_writer , whisper_writer , 'ChaT' , JoinCHaT)


                        # --- ⛔️ [REMOVED] স্বয়ংক্রিয় ওয়েলকাম মেসেজ মুছে ফেলা হয়েছে ---
                        # message = f'[B][C]{get_random_color()}\n- WeLComE To ! '
                        # P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        # await SEndPacKeT(online_writer , whisper_writer , 'ChaT' , P)
                        # --- ⛔️ END REMOVAL ---

                    # --- ✅ [STABILITY FIX] 'pass' এর পরিবর্তে এরর প্রিন্ট করা ---
                    except Exception as e1: 
                        print(f"Error in TcPOnLine (Outer Try): {e1}")
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                await SEndPacKeT(online_writer , whisper_writer , 'ChaT' , JoinCHaT)

                                # --- ⛔️ [REMOVED] স্বয়ংক্রিয় ওয়েলকাম মেসেজ মুছে ফেলা হয়েছে ---
                                # message = f'[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! \n\n{get_random_color()}- Commands : @a {xMsGFixinG("123456789")} {xMsGFixinG("909000001")}\n\n[00FF00]Dev : @{xMsGFixinG("redzedking")}'
                                # P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                # await SEndPacKeT(online_writer , whisper_writer , 'ChaT' , P)
                                # --- ⛔️ END REMOVAL ---
                            # --- ✅ [STABILITY FIX] 'pass' এর পরিবর্তে এরর প্রিন্ট করা ---
                            except Exception as e2:
                                print(f"Error in TcPOnLine (Inner Try): {e2}")

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)

# --- ⚡️ [BURST SPAM] আপডেটেড স্প্যাম লুপ ---
async def emote_spam_loop(target_uid, emote_id, key, iv, region, delay=0.05): # ডিফল্ট ডিলে 0.05 সেকেন্ড (burst-এর মধ্যে)
    """Continuously sends an emote packet until the task is cancelled."""
    global is_spamming
    is_spamming = True

    # টার্গেট একটি তালিকা (group spam) নাকি একক UID তা পরীক্ষা করুন
    is_group_spam = isinstance(target_uid, list)

    if is_group_spam:
        print(f"Starting GROUP emote spam to {len(target_uid)} users with emote {emote_id}")
    else:
        print(f"Starting emote spam to {target_uid} with emote {emote_id}")

    try:
        while True:
            if is_group_spam:
                # --- গ্রুপ স্প্যাম: প্রতিটি প্লেয়ারকে ১০টি করে প্যাকেট পাঠান ---
                for _ in range(10): # প্রতি burst-এ ১০টি প্যাকেট
                    success_count = 0
                    for player_id in target_uid:
                        H = await Emote_k(player_id, emote_id, key, iv, region)
                        if H and online_writer:
                            # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', H)
                            success_count += 1
                            # প্রতিটি প্যাকেটের পর নেটওয়ার্ককে সামান্য সময় দিন
                            await asyncio.sleep(0.0) 
                # print(f"Group spam cycle sent to {success_count}/{len(target_uid)} users.") # (খুব বেশি লগ এড়াতে এটি মন্তব্য করা যেতে পারে)

            else:
                # --- একক টার্গেট স্প্যাম (Burst) ---
                for _ in range(10): # প্রতি burst-এ ১০টি প্যাকেট
                    H = await Emote_k(target_uid, emote_id, key, iv, region)
                    if H and online_writer: 
                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                        await SEndPacKeT(online_writer, whisper_writer, 'OnLine', H)
                         # প্রতিটি প্যাকেটের পর নেটওয়ার্ককে সামান্য সময় দিন
                        await asyncio.sleep(0.0)

            # --- ১০টি প্যাকেটের burst পাঠানোর পর প্রধান ডিলে ---
            await asyncio.sleep(delay)

    except asyncio.CancelledError:
        if is_group_spam:
            print(f"Group emote spam stopped.")
        else:
            print(f"Emote spam to {target_uid} stopped.")

    except Exception as e:
        print(f"Error in spam loop: {e}")

    finally:
        is_spamming = False
        print(f"Emote spam loop cleaned up.")
# --- ⚡️ END [BURST SPAM] ---

# --- 🔼 [NEW] মেসেজ স্প্যাম লুপ ---
async def message_spam_loop(message, XX, uid, chat_id, key, iv, delay=0.01):
    """Continuously sends a CHAT MESSAGE packet until the task is cancelled."""
    global is_spamming, online_writer, whisper_writer
    is_spamming = True
    print(f"Starting MESSAGE spam to chat {chat_id}")

    try:
        while True:
            # 1. মেসেজ প্যাকেট জেনারেট করুন
            P = await SEndMsG(XX, message, uid, chat_id, key, iv)

            # 2. প্যাকেট পাঠান (CHAT writer-এ)
            if P and whisper_writer: # গুরুত্বপূর্ণ: whisper_writer (ChaT) ব্যবহার করুন
                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

            # 3. ডিলে (100 packets/sec এর জন্য 0.01s)
            await asyncio.sleep(delay)

    except asyncio.CancelledError:
        print(f"Message spam to chat {chat_id} stopped.")
    except Exception as e:
        print(f"Error in message spam loop: {e}")
    finally:
        is_spamming = False
        print(f"Message spam loop for chat {chat_id} cleaned up.")
# --- 🔼 END [NEW] ---


# --- 🔼 [NEW] ল্যাগ স্কোয়াড স্প্যাম লুপ ---
async def lag_squad_loop(key, iv, region, delay=0.1):
    """Continuously sends a LagSquad packet until the task is cancelled."""
    global is_spamming, online_writer, whisper_writer
    is_spamming = True
    print(f"Starting Lag Squad Spam Loop")

    try:
        while True:
            # 1. LagSquad প্যাকেট জেনারেট করুন (xC4.py থেকে)
            lag_packet = await LagSquad(key, iv, region)

            # Debug information
            if lag_packet:
                # print(f"Lag packet generated, length: {len(lag_packet)} bytes") # খুব বেশি লগ এড়াতে এটি মন্তব্য করা হলো
                pass
            else:
                print("Failed to generate Lag packet")

            # 2. প্যাকেটটি 'OnLine' স্ট্রিমে পাঠান
            if lag_packet and online_writer:
                # print("Sending Lag packet...") # খুব বেশি লগ এড়াতে এটি মন্তব্য করা হলো
                await SEndPacKeT(online_writer, whisper_writer, 'OnLine', lag_packet)
                # print("Lag packet sent successfully") # খুব বেশি লগ এড়াতে এটি মন্তব্য করা হলো
            elif not online_writer:
                print("Error: No online writer available to send Lag packet")
            else:
                print("Error: Lag packet is None or empty")

            # 3. ডিলে
            await asyncio.sleep(delay)

    except asyncio.CancelledError:
        print(f"Lag Squad Spam stopped.")
    except Exception as e:
        print(f"Error in lag_squad_loop: {e}")
        import traceback
        traceback.print_exc()
    finally:
        is_spamming = False
        print(f"Lag Squad Spam loop cleaned up.")
# --- 🔼 END [NEW] ---


# -----------------------------------------------------------------
# ------------------ [START] UPDATED TcPChaT ----------------------
# -----------------------------------------------------------------

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(f"TCP CHAT starting for region: {region}")

    # --- 🔼 [FIXED] CURRENT_SQUAD_SIZE গ্লোবাল ভেরিয়েবল যোগ করা হলো ---
    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, spam_task, is_spamming, BOT_UID, CURRENT_SQUAD_SIZE
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break

                # print(f"Received data: {data.hex()[:100]}...")  # Debug line

                # Process team messages to collect player IDs
                # `len(data.hex()) > 100` শর্তটি সরিয়ে ফেলা হয়েছে
                if data.hex().startswith("0500"):
                    try:
                        # Try to decode team message to collect player IDs
                        team_packet = await decode_team_packet(data.hex()[10:])
                        if hasattr(team_packet, 'details') and hasattr(team_packet.details, 'player_uid'):
                            player_uid = team_packet.details.player_uid
                            team_session = team_packet.details.team_session

                            # Store player ID in the group
                            if team_session not in GROUP_PLAYER_IDS:
                                GROUP_PLAYER_IDS[team_session] = set()

                            if player_uid not in GROUP_PLAYER_IDS[team_session]:
                                GROUP_PLAYER_IDS[team_session].add(player_uid)
                                print(f"[CHAT-0500] Auto-collected player {player_uid} for group {team_session}. Group: {GROUP_PLAYER_IDS[team_session]}")

                    except Exception as e:
                        # print(f"Failed to parse 0500 packet in TcPChaT (this is often normal): {e}")
                        pass # এটা স্বাভাবিক, মানে এই 0500 প্যাকেটটি টিম মেসেজ ছিল না

                if data.hex().startswith("120000"):
                    try:
                        msg = await DeCode_PackEt(data.hex()[10:])
                        chatdata = json.loads(msg)
                        # print(f"Chat data: {chatdata}")  # Debug line

                        # Try multiple ways to parse the message
                        inPuTMsG = None
                        XX = None
                        uid = None
                        chat_id = None

                        try:
                            response = await DecodeWhisperMessage(data.hex()[10:])
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            XX = response.Data.chat_type
                            inPuTMsG = response.Data.msg.lower()
                            # print(f"Whisper message: {inPuTMsG} from {uid}, chat type: {XX}, chat_id: {chat_id}") # Debug
                        except Exception as e:
                            # print(f"Whisper parsing failed: {e}")
                            response = None
                            # Alternative parsing for squad messages (JSON fallback)
                            try:
                                if '5' in chatdata and 'data' in chatdata['5']:
                                    if '16' in chatdata['5']['data']: # Sender UID
                                        uid = chatdata['5']['data']['16']
                                    if '4' in chatdata['5']['data']: # Message
                                        inPuTMsG = chatdata['5']['data']['4'].lower()

                                    # --- FIX: Assume '2' is the group_id/chat_id for squad/clan ---
                                    if '2' in chatdata['5']['data']: 
                                        chat_id = chatdata['5']['data']['2']
                                        # Guess chat type (0=squad, 1=clan). Default to squad (0).
                                        XX = 0 
                                        # print(f"Squad/Clan (JSON) message: {inPuTMsG} from {uid}, chat_id: {chat_id}")
                                    else:
                                        # --- 🔼 [FIX] ক্ল্যান চ্যাটের জন্য chat_id খুঁজে বের করা ---
                                        if '1' in chatdata['5']['data']: # Fallback for Clan ID
                                            chat_id = chatdata['5']['data']['1']
                                            XX = 1 # Assume Clan
                                            # print(f"Clan (JSON) message: {inPuTMsG} from {uid}, chat_id: {chat_id}")
                                        else:
                                            print("JSON parsing failed to find chat_id in field '2' or '1'.")

                            except Exception as e:
                                # print(f"Squad parsing failed: {e}")
                                pass

                        # --- NEW LOGIC: Manually populate GROUP_PLAYER_IDS from chat messages ---
                        # This ensures that anyone who chats gets added to the group list
                        if (XX == 0 or XX == 1) and chat_id and uid: # If it's Squad or Clan chat
                            if chat_id not in GROUP_PLAYER_IDS:
                                GROUP_PLAYER_IDS[chat_id] = set()

                            if uid not in GROUP_PLAYER_IDS[chat_id]:
                                GROUP_PLAYER_IDS[chat_id].add(uid)
                                print(f"Updated group {chat_id} with chatting user {uid}. Group members seen: {GROUP_PLAYER_IDS[chat_id]}")
                        # --- END NEW LOGIC ---


                        if inPuTMsG and XX is not None and uid is not None and chat_id is not None:

                            # --- [⭐️ নতুন হেল্প মেনু ⭐️] ---
                            # --- এই অংশটি আপনার অনুরোধ অনুযায়ী সম্পূর্ণ নতুন করে ডিজাইন করা হয়েছে ---
                            if inPuTMsG.strip().startswith("help") or inPuTMsG.strip().startswith("/help"):
                                print("🆘 Help command triggered (New Design)")
                                parts = inPuTMsG.strip().split()
                                arg = parts[1].lower() if len(parts) > 1 else None
                                help_message = ""

                                if arg in ("1", "emote", "emotes"):
                                    # --- Part 1: Emote Commands (New Design) ---
                                    help_message = (
                                        f'[B][C][00FFFF]╔═════  Emote Commands ═════╗\n'
                                        f'[C][FFFFFF]  [Seq/ID] [FFFF00]= 1-410 or full Emote ID\n'
                                        f'[C][00FFFF]╟────────────────────────────╢\n\n'

                                        f'[C][FFFF00]@[a] [Seq/ID]\n'
                                        f'[C][FFFFFF]  Desc: Sends emote to [F08080]yourself.\n'
                                        f'[C][ADD8E6]  Example: @a 10\n\n'

                                        f'[C][FFFF00]@[a] [PlayerID] [Seq/ID]\n'
                                        f'[C][FFFFFF]  Desc: Sends to a [F08080]specific player.\n'
                                        f'[C][ADD8E6]  Example: @a 123456789 10\n\n'

                                        f'[C][FFFF00]@[a] all [Seq/ID]\n'
                                        f'[C][FFFFFF]  Desc: Sends to [F08080]everyone in squad.\n'
                                        f'[C][ADD8E6]  Example: @a all 10\n'

                                        f'[C][00FFFF]╚════════════════════════════╝'
                                    )

                                elif arg in ("2", "spam"):
                                    # --- Part 2: Spam Commands (New Design) ---
                                    help_message = (
                                        f'[B][C][FF0000]╔═════  Spam Commands ═════╗\n'
                                        f'[C][FFFFFF]  [Seq/ID] [FFFF00]= 1-410 or full Emote ID\n'
                                        f'[C][FF0000]╟───────────────────────────╢\n\n'

                                        f'[C][FFFF00]@[spam] [Seq/ID]\n'
                                        f'[C][FFFFFF]  Desc: Spams emote to [F08080]yourself.\n'
                                        f'[C][ADD8E6]  Example: @spam 1\n\n'

                                        f'[C][FFFF00]@[spam] all [Seq/ID]\n'
                                        f'[C][FFFFFF]  Desc: Spams emote to [F08080]everyone.\n'
                                        f'[C][ADD8E6]  Example: @spam all 1\n\n'

                                        f'[C][FFFF00]/sm [FFFFFF]- Spams a welcome message.\n\n'
                                        f'[C][FFFF00]/lag [FFFFFF]- Spams lag packets to squad.\n\n'

                                        f'[C][FF0000]╟───────────────────────────╢\n'
                                        f'[C][FFFF00]@[stop] [FFFFFF]- [00FF00]Stops all active spam.\n'
                                        f'[C][FF0000]╚═══════════════════════════╝'
                                    )

                                elif arg in ("3", "squad", "other"):
                                    # --- Part 3: Squad Commands (New Design) ---
                                    help_message = (
                                        f'[B][C][90EE90]╔═════  Squad Commands ═════╗\n'
                                        f'[C][FFFFFF]  (Commands for the [F08080]Squad Leader)\n'
                                        f'[C][90EE90]╟────────────────────────────╢\n'
                                        f'[C][FFFF00]/4 [FFFFFF]- Set squad size to 4.\n'
                                        f'[C][FFFF00]/5 [FFFFFF]- Set squad size to 5.\n'
                                        f'[C][FFFF00]/leader [FFFFFF]- Give leader to yourself.\n'
                                        f'[C][FFFF00]/invme [FFFFFF]- Invites you to squad.\n'
                                        f'[C][FFFF00]/s [FFFFFF]- Force start match.\n'
                                        f'[C][90EE90]╟────────────────────────────╢\n'
                                        f'[C][FFFFFF]  (Commands for [F08080]Everyone)\n'
                                        f'[C][90EE90]╟────────────────────────────╢\n'
                                        f'[C][FFFF00]/x/[SquadCode]\n'
                                        f'[C][FFFFFF]  Join a squad using its code.\n'
                                        f'[C][ADD8E6]  Example: /x/123456\n\n'

                                        f'[C][FFFF00]leave [FFFFFF]- Leave current squad.\n'
                                        f'[C][FFFF00]owner [FFFFFF]- Show bot owner info.\n'
                                        f'[C][90EE90]╚════════════════════════════╝'
                                    )

                                else:
                                    # --- DEFAULT: Main Menu (New Design) ---
                                    help_message = (
                                        f'[B][C][00FFFF]╔═════ {xMsGFixinG(OWNER_NAME)} ═════╗\n'
                                        f'[C][FFFFFF]     Bot by [FFFF00]@{xMsGFixinG(OWNER_TELEGRAM_USER)}\n'
                                        f'[C][00FFFF]╟───────────────────────╢\n'
                                        f'[C][FFFFFF]  Type [FFFF00]help [number] [FFFFFF]for details\n'
                                        f'[C][00FFFF]╟───────────────────────╢\n'
                                        f'[C][FFFF00]  1. [FFFFFF]✨ Emote Commands\n'
                                        f'[C][FFFF00]  2. [FFFFFF]💥 Spam Commands\n'
                                        f'[C][FFFF00]  3. [FFFFFF]🔰 Squad Commands\n'
                                        f'[C][00FFFF]╚═══════════════════════╝'
                                    )

                                # Send the generated help message
                                P_help = await SEndMsG(XX, help_message, uid, chat_id, key, iv)
                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P_help)
                            # --- [⭐️ নতুন হেল্প মেনুর শেষ ⭐️] ---


                            # --- NEW OWNER COMMAND ---
                            elif inPuTMsG.strip() in ("owner", "/owner", "!owner", "admin"):
                                print("👑 Owner command triggered")

                                owner_message = f'[B][C]{get_random_color()}╔══════ 👑 BOT OWNER 👑 ══════╗\n\n'

                                owner_message += f'[FFFFFF]• [FFFF00]Owner : [00FFFF]{xMsGFixinG(OWNER_NAME)}\n'
                                owner_message += f'[FFFFFF]• [FFFF00]Telegram : [00FFFF]@{xMsGFixinG(OWNER_TELEGRAM_USER)}\n'
                                owner_message += f'[FFFFFF]• [FFFF00]Channel : [00FFFF]{xMsGFixinG(OWNER_TELEGRAM_CHANNEL)}\n'
                                owner_message += f'[FFFFFF]• [FFFF00]YouTube : [00FFFF]{xMsGFixinG(OWNER_YOUTUBE_CHANNEL)}\n\n'

                                owner_message += f'[C]{get_random_color()}╚══════════════════════════════╝\n'
                                owner_message += f'[C][90EE90]Developer: @atx abir'

                                P = await SEndMsG(XX, owner_message, uid, chat_id, key, iv)
                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                            # --- End Owner Command ---

                            # --- 🔼 [NEW] SPAM ALL LOGIC ---
                            elif inPuTMsG.strip().startswith('@spam'):
                                if is_spamming:
                                    message = f'[B][C]{get_random_color()}\nError: Spam is already running. Use @stop first.'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    continue # পরবর্তী কমান্ডের জন্য অপেক্ষা করুন

                                print(f"Processing spam command: {inPuTMsG}")
                                try:
                                    parts = inPuTMsG.strip().split()
                                    target_uid = None
                                    emote_id = None
                                    is_group_spam = False # মেসেজিং এর জন্য ফ্ল্যাগ

                                    if len(parts) == 2:
                                        # @spam [EMOTE_ID/SEQ] (Auto Target)
                                        target_uid = uid
                                        try:
                                            identifier = int(parts[1])
                                            if identifier in EMOTE_DATABASE:
                                                emote_id = EMOTE_DATABASE[identifier]
                                            else:
                                                emote_id = identifier # Assume direct emote ID
                                        except ValueError:
                                            message = f'[B][C]{get_random_color()}\nUsage: @spam [EMOTE_ID/SEQ]. ID must be a number.'
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                            continue

                                    elif len(parts) >= 3:
                                        # --- নতুন "@spam all [ID]" চেক ---
                                        if parts[1].lower() == 'all':
                                            is_group_spam = True
                                            if XX == 0 or XX == 1: # Group (Squad/Clan) Chat
                                                # "@a all" এর মতো একই লজিক ব্যবহার করে প্লেয়ার তালিকা নিন
                                                player_ids_set = set()
                                                if chat_id in GROUP_PLAYER_IDS:
                                                    player_ids_set.update(GROUP_PLAYER_IDS[chat_id])
                                                if BOT_UID:
                                                    player_ids_set.add(BOT_UID)
                                                player_ids_set.add(uid) # কমান্ড ব্যবহারকারীকে যোগ করুন

                                                if len(player_ids_set) > 0:
                                                    target_uid = list(player_ids_set) # এটি এখন একটি তালিকা
                                                    print(f"Group spam target list: {target_uid}")
                                                else:
                                                    message = f'[B][C]{get_random_color()}\nError: No players found for group spam.'
                                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                    continue
                                            else:
                                                message = f'[B][C]{get_random_color()}\nError: "spam all" only works in Squad or Clan chat.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue

                                            # এখন ইমোট আইডি নিন (parts[2] থেকে)
                                            try:
                                                identifier = int(parts[2])
                                                if identifier in EMOTE_DATABASE:
                                                    emote_id = EMOTE_DATABASE[identifier]
                                                else:
                                                    emote_id = identifier # Assume direct emote ID
                                            except ValueError:
                                                message = f'[B][C]{get_random_color()}\nUsage: @spam all [EMOTE_ID/SEQ]. ID must be a number.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue

                                        else:
                                            # বিদ্যমান: @spam [UID] [EMOTE_ID/SEQ]
                                            try:
                                                target_uid = int(parts[1])
                                                identifier = int(parts[2])
                                                if identifier in EMOTE_DATABASE:
                                                    emote_id = EMOTE_DATABASE[identifier]
                                                else:
                                                    emote_id = identifier # Assume direct emote ID
                                            except ValueError:
                                                message = f'[B][C]{get_random_color()}\nUsage: @spam [UID] [EMOTE_ID/SEQ]. IDs must be numbers.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue

                                    if target_uid and emote_id:
                                        # is_spamming = True (এটি লুপ ফাংশনের ভেতরে সেট হবে)
                                        # ব্যাকগ্রাউন্ডে স্প্যাম টাস্কটি শুরু করুন
                                        spam_task = asyncio.create_task(
                                            # --- ⚡️ [BURST SPAM] ডিলে 0.05 সেকেন্ড করা হলো ---
                                            emote_spam_loop(target_uid, emote_id, key, iv, region, delay=0.05) 
                                        )

                                        # কনফার্মেশন মেসেজ আপডেট করুন
                                        if is_group_spam:
                                            msg_target = f'ALL IN GROUP ({len(target_uid)} players)'
                                        else:
                                            msg_target = xMsGFixinG(target_uid)

                                        message = f'[B][C]{get_random_color()}\nStarting Burst Spam (ID: {xMsGFixinG(emote_id)}) to {msg_target}.\nUse @stop to stop.'
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                    else:
                                        # ব্যবহারবিধি মেসেজ আপডেট করুন
                                        message = f'[B][C]{get_random_color()}\nUsage: @spam [UID] [ID], @spam [ID], or @spam all [ID]'
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                except Exception as e:
                                    print(f"Error processing spam command: {e}")
                                    message = f'[B][C]{get_random_color()}\nError: {str(e)}'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                            # --- 🔼 END SPAM COMMAND LOGIC ---

                            # --- 🔼 [NEW] /sm কমান্ড ---
                            elif inPuTMsG.strip() == '/sm':
                                if is_spamming:
                                    message = f'[B][C]{get_random_color()}\nError: Spam is already running. Use @stop first.'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    continue

                                print(f"Starting Welcome Message Spam in chat {chat_id}")

                                # এখানে ওয়েলকাম মেসেজটি লিখুন
                                spam_message = f'[B][C]{get_random_color()}ওয়েলকাম! [FFFF00]বট বাই {OWNER_NAME}'

                                # মেসেজ স্প্যাম লুপটি শুরু করুন
                                spam_task = asyncio.create_task(
                                    message_spam_loop(spam_message, XX, uid, chat_id, key, iv, delay=0.01) # 100 times/sec
                                )

                                # কনফার্মেশন মেসেজ পাঠান
                                message = f'[B][C]{get_random_color()}\nStarting Welcome Message Spam.\nUse @stop to stop.'
                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                            # --- 🔼 END /sm কমান্ড ---


                            # --- NEW STOP COMMAND ---
                            elif inPuTMsG.strip() == '@stop':
                                if not is_spamming or spam_task is None:
                                    message = f'[B][C]{get_random_color()}\nNo spam is currently running.' # <-- CHANGED
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    continue

                                try:
                                    spam_task.cancel() # স্প্যাম লুপ টাস্কটিকে বন্ধ করার সিগন্যাল পাঠান

                                    message = f'[B][C]{get_random_color()}\nSpam stopped successfully.' # <-- CHANGED
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                except Exception as e:
                                    print(f"Error stopping spam task: {e}")
                                    message = f'[B][C]{get_random_color()}\nError stopping spam: {str(e)}'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                finally:
                                    spam_task = None
                                    is_spamming = False # নিশ্চিত হওয়ার জন্য এখানেও রিসেট করুন

                            # --- End Spam Commands ---

                            # Handle emote commands
                            elif inPuTMsG.strip().startswith('@a'):
                                # print(f"Processing emote command: {inPuTMsG}")  # Debug line

                                try:
                                    parts = inPuTMsG.strip().split()
                                    target_uid = None
                                    emote_id = None

                                    if len(parts) == 2:
                                        # @a [EMOTE_ID] (Auto Target) OR @a [1-410] (Auto Target Sequence)
                                        target_uid = uid

                                        try:
                                            identifier = int(parts[1])
                                            if identifier in EMOTE_DATABASE:
                                                # Emote by Sequence ID (Auto Target)
                                                emote_id = EMOTE_DATABASE[identifier]
                                            else:
                                                # Emote by direct ID (Auto Target)
                                                emote_id = identifier
                                        except ValueError:
                                            message = f'[B][C]{get_random_color()}\nUsage: @a [EMOTE_ID] or @a [1-410]. Identifier must be a number.'
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                            continue  

                                    elif len(parts) >= 3:

                                        # --- MODIFIED: @a all [1-410] (Group Target - Bot সহ সবাই) ---
                                        if parts[1] == 'all':
                                            if XX == 0 or XX == 1: # Group (Squad/Clan) Chat

                                                # ডুপ্লিকেট এড়ানোর জন্য set ব্যবহার করুন
                                                player_ids_set = set()

                                                # গ্রুপে দেখা অন্যান্য প্লেয়ারদের যোগ করুন (যারা চ্যাট করেছে বা 0500 প্যাকেটে এসেছে)
                                                if chat_id in GROUP_PLAYER_IDS:
                                                    player_ids_set.update(GROUP_PLAYER_IDS[chat_id])

                                                # --- প্রধান পরিবর্তন: বটের নিজের UID যোগ করুন ---
                                                if BOT_UID:
                                                    player_ids_set.add(BOT_UID)
                                                else:
                                                    print("Warning: BOT_UID is missing!")

                                                # --- প্রধান পরিবর্তন ২: যে কমান্ড দিয়েছে তার UID যোগ করুন ---
                                                player_ids_set.add(uid) 

                                                if len(player_ids_set) > 0:
                                                    target_uid = list(player_ids_set) # সবাইকে টার্গেট করুন
                                                    print(f"Group emote for {len(target_uid)} players: {target_uid}")
                                                else:
                                                    message = f'[B][C]{get_random_color()}\nError: No players found for group emote. (Tip: Ask them to chat once)'
                                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                    continue
                                            else:
                                                message = f'[B][C]{get_random_color()}\nError: "all" command only works in Squad or Clan chat.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue

                                            # --- Emote ID প্রসেসিং (আগের মতোই) ---
                                            try:
                                                sequence_id = int(parts[2])
                                                if sequence_id in EMOTE_DATABASE:
                                                    emote_id = EMOTE_DATABASE[sequence_id]
                                                else:
                                                    # --- 🔼 [FIXED] @a all এখন সরাসরি ইমোট আইডি গ্রহণ করে ---
                                                    emote_id = sequence_id
                                                    # message = f'[B][C]{get_random_color()}\nError: Invalid sequence ID. Use 1-410.'
                                                    # P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                    # await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                    # continue
                                            except ValueError:
                                                message = f'[B][C]{get_random_color()}\nUsage: @a all [ID/SEQ]. ID must be a number.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue
                                        # --- END MODIFIED "all" LOGIC ---

                                        else:
                                            # Existing: @a [UID] [EMOTE_ID] or @a [UID] [SEQUENCE_ID]
                                            try:
                                                target_uid = int(parts[1])
                                                identifier = int(parts[2])

                                                if identifier in EMOTE_DATABASE:
                                                    # Emote by Sequence ID (Specific UID)
                                                    emote_id = EMOTE_DATABASE[identifier]
                                                else:
                                                    # Emote by direct ID (Specific UID)
                                                    emote_id = identifier
                                            except ValueError:
                                                # Handle case where UID or EMOTE_ID/SEQUENCE_ID is not an integer
                                                message = f'[B][C]{get_random_color()}\nUsage: @a [UID] [EMOTE_ID] or @a [UID] [1-410]. UID and Emote/Sequence ID must be numbers.'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                                continue # Stop processing this command

                                    if target_uid and emote_id:
                                        # Send confirmation message
                                        if isinstance(target_uid, list):  # Sending to multiple players
                                            msg_target = f'ALL IN GROUP ({len(target_uid)} players)'
                                        else:
                                            msg_target = xMsGFixinG(target_uid)

                                        message = f'[B][C]{get_random_color()}\nSending emote {xMsGFixinG(emote_id)} to {msg_target}'
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                        # Send the emote packet(s)
                                        if isinstance(target_uid, list):  # Sending to multiple players
                                            success_count = 0
                                            for player_id in target_uid:
                                                H = await Emote_k(player_id, emote_id, key, iv, region)
                                                if H:
                                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                    await SEndPacKeT(online_writer, whisper_writer, 'OnLine', H)
                                                    success_count += 1
                                                    # Add a small delay to avoid flooding
                                                    await asyncio.sleep(0.1) # 0.1 সেকেন্ড ডিলে প্রতিটি ইমোটের মাঝে

                                            # print(f"Emote packets sent successfully to {success_count}/{len(target_uid)} players") # খুব বেশি মেসেজ এড়াতে এটি বন্ধ করা হলো

                                            # Send success message
                                            message = f'[B][C]{get_random_color()}\nEmote {xMsGFixinG(emote_id)} sent successfully to {success_count}/{len(target_uid)} players!'
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            H = await Emote_k(target_uid, emote_id, key, iv, region)
                                            if H:
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'OnLine', H)
                                                # print("Emote packet sent successfully")  # Debug line
                                                # Send success message
                                                message = f'[B][C]{get_random_color()}\nEmote {xMsGFixinG(emote_id)} sent successfully to {msg_target}!'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                            else:
                                                message = f'[B][C]{get_random_color()}\nFailed to generate emote packet!'
                                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        message = f'[B][C]{get_random_color()}\nUsage: @a [UID] [ID], @a [ID], @a [1-410], or @a all [ID/SEQ]'
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                except Exception as e:
                                    print(f"Error processing emote command: {e}")
                                    message = f'[B][C]{get_random_color()}\nError: {str(e)}'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                            # Handle other commands

                            # --- 🔼 [FIXED] SQUAD SIZE COMMANDS ---
                            elif inPuTMsG.strip() == '/4':
                                try:
                                    if XX == 0: # Only in Squad chat
                                        if BOT_UID:
                                            print(f"Changing squad size to 4 (Leader: {BOT_UID})")
                                            # Nu=4, Uid=BOT_UID (leader)
                                            C = await cHSq(4, BOT_UID, key, iv, region) 
                                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', C)

                                            CURRENT_SQUAD_SIZE = 4 # স্কোয়াডের আকার সেভ করুন

                                            message = f"[B][C]{get_random_color()}Squad size changed to 4. (Leader only)"
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            print("Error: BOT_UID not set, cannot change squad size.")
                                            message = f"[B][C]{get_random_color()}Error: Bot UID not found."
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        print("Command /4 ignored (not in squad chat)")
                                        message = f"[B][C]{get_random_color()}Command /4 only works in a squad."
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /4 command: {e}")

                            elif inPuTMsG.strip() == '/5':
                                try:
                                    if XX == 0: # Only in Squad chat
                                        if BOT_UID:
                                            print(f"Changing squad size to 5 (Leader: {BOT_UID})")
                                            # Nu=5, Uid=BOT_UID (leader)
                                            C = await cHSq(5, BOT_UID, key, iv, region)
                                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', C)

                                            CURRENT_SQUAD_SIZE = 5 # স্কোয়াডের আকার সেভ করুন

                                            message = f"[B][C]{get_random_color()}Squad size changed to 5. (Leader only)"
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            print("Error: BOT_UID not set, cannot change squad size.")
                                            message = f"[B][C]{get_random_color()}Error: Bot UID not found."
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        print("Command /5 ignored (not in squad chat)")
                                        message = f"[B][C]{get_random_color()}Command /5 only works in a squad."
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /5 command: {e}")

                            # --- 🔼 [CHANGED] HIDDEN INVITE COMMAND ---
                            elif inPuTMsG.strip() == '/invme': # (Hidden command)
                                try:
                                    # --- 🔰 CHANGE: Allow Squad (0) or Private (2) ---
                                    if XX == 0 or XX == 2: # Squad or Private chat
                                        if BOT_UID:
                                            # --- [FIXED] সঠিক স্কোয়াডের আকার (Nu) ব্যবহার করুন ---
                                            print(f"Sending invite to {uid} (Squad Size: {CURRENT_SQUAD_SIZE})")
                                            # Nu=CURRENT_SQUAD_SIZE, Uid=uid (target)
                                            V = await SEnd_InV(CURRENT_SQUAD_SIZE, uid, key, iv, region) 
                                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', V)

                                            message = f"[B][C]{get_random_color()}Sending invite to {xMsGFixinG(uid)}... (Leader only)"
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            print("Error: BOT_UID not set, cannot send invite.")
                                            message = f"[B][C]{get_random_color()}Error: Bot UID not found."
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        # --- 🔰 CHANGE: Updated error message ---
                                        print("Command /invme ignored (not in squad/private chat)")
                                        message = f"[B][C]{get_random_color()}Command /invme only works in Squad or Private chat."
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /invme command: {e}")

                            # --- 🔼 [CHANGED] /5s (Invite) Command ---
                            elif inPuTMsG.strip() == '/5s':
                                try:
                                    # --- 🔰 CHANGE: Allow Squad (0) or Private (2) ---
                                    if XX == 0 or XX == 2: # Squad or Private chat
                                        if BOT_UID:
                                            # SEnd_InV uses the *current* squad size (tracked by CURRENT_SQUAD_SIZE)
                                            print(f"Sending invite to {uid} via /5s (Squad Size: {CURRENT_SQUAD_SIZE})")

                                            # Nu = CURRENT_SQUAD_SIZE (4 or 5)
                                            # Uid = uid (the user who typed the command)
                                            V = await SEnd_InV(CURRENT_SQUAD_SIZE, uid, key, iv, region) 

                                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', V)

                                            message = f"[B][C]{get_random_color()}Sending invite to {xMsGFixinG(uid)}... (Leader only)"
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            print("Error: BOT_UID not set, cannot send invite.")
                                            message = f"[B][C]{get_random_color()}Error: Bot UID not found."
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        # --- 🔰 CHANGE: Updated error message ---
                                        print("Command /5s ignored (not in squad/private chat)")
                                        message = f"[B][C]{get_random_color()}Command /5s only works in Squad or Private chat."
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /5s command: {e}")
                            # --- 🔼 END /5s Command ---

                            # --- 🔼 [NEW] Transfer Leadership Command ---
                            elif inPuTMsG.strip() == '/leader':
                                try:
                                    if XX == 0: # Only in Squad chat
                                        if BOT_UID:
                                            print(f"Transferring leadership to {uid}...")

                                            # 1. Generate the packet to make 'uid' the new leader
                                            L = await xChLeaDer(uid, key, iv, region) 

                                            # 2. Send the packet
                                            await SEndPacKeT(online_writer, whisper_writer, 'OnLine', L)

                                            # 3. Send confirmation message
                                            message = f"[B][C]{get_random_color()}Transferring leadership to {xMsGFixinG(uid)}... (Leader only)"
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                        else:
                                            print("Error: BOT_UID not set, cannot transfer leadership.")
                                            message = f"[B][C]{get_random_color()}Error: Bot UID not found."
                                            P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                            await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    else:
                                        print("Command /leader ignored (not in squad chat)")
                                        message = f"[B][C]{get_random_color()}Command /leader only works in a squad."
                                        P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /leader command: {e}")
                            # --- 🔼 END Transfer Leadership ---

                            elif inPuTMsG.startswith('/x/'):
                                CodE = inPuTMsG.split('/x/')[1]
                                try:
                                    # --- 🔼 [FIXED] প্রাইভেট এবং গ্রুপ উভয় চ্যাটে কাজ করবে ---
                                    # dd = chatdata['5']['data']['16'] # এই চেকটি অপ্রয়োজনীয়
                                    print(f'Joining squad with code: {CodE}')
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'OnLine', EM)

                                    message = f"[B][C]{get_random_color()}Joining squad {CodE}..."
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /x/ command: {e}")

                            elif inPuTMsG.startswith('leave'):
                                try:
                                    print(f'Bot leaving squad...')
                                    leave = await ExiT(BOT_UID, key, iv) # <-- 🔼 [FIXED] বটের নিজের UID ব্যবহার করুন
                                    await SEndPacKeT(online_writer, whisper_writer, 'OnLine', leave)

                                    message = f"[B][C]{get_random_color()}Leaving squad..."
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing leave command: {e}")


                            elif inPuTMsG.strip().startswith('/s'):
                                try:
                                    print(f'Force starting game...')
                                    EM = await FS(key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'OnLine', EM)

                                    message = f"[B][C]{get_random_color()}Force starting game... (Leader only)"
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                except Exception as e:
                                    print(f"Error processing /s command: {e}")


                            # --- 🔼 [MODIFIED] LAG SQUAD SPAM COMMAND ---
                            elif inPuTMsG.strip() == '/lag':
                                if is_spamming:
                                    message = f'[B][C]{get_random_color()}\nError: Spam is already running. Use @stop first.'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                                    continue

                                print(f"⚡ LagSquad Spam command triggered by {uid}")

                                try:
                                    # 1. ল্যাগ স্প্যাম লুপটি শুরু করুন (ডিলে 0.1 সেকেন্ড)
                                    spam_task = asyncio.create_task(
                                        lag_squad_loop(key, iv, region, delay=0.1) 
                                    )

                                    # 2. চ্যাটে কনফার্মেশন মেসেজ পাঠান
                                    message = f'[B][C]{get_random_color()}\nStarting Lag Squad Spam.\nUse @stop to stop.'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                                except Exception as e:
                                    print(f"Error processing /lag command: {e}")
                                    message = f'[B][C]{get_random_color()}\nError: {str(e)}'
                                    P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)
                            # --- 🔼 END LAG SQUAD SPAM COMMAND ---

                            elif inPuTMsG in ("hi", "hello", "fen", "salam"):
                                message = f'Hello Im {OWNER_NAME}\nType help for commands.'
                                P = await SEndMsG(XX, message, uid, chat_id, key, iv)
                                # --- 🟢 [FIXED] STABILITY FIX (Argument order) ---
                                await SEndPacKeT(online_writer, whisper_writer, 'ChaT', P)

                    except Exception as e:
                        print(f"Error processing packet: {e}")

            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None

        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

# -----------------------------------------------------------------
# ------------------ [END] UPDATED TcPChaT ------------------------
# -----------------------------------------------------------------


# --- FIXED FUNCTION ---
async def MaiiiinE():
    global BOT_UID # <-- গ্লোবাল ভেরিয়েবল অ্যাক্সেস করুন
    Uid , Pw = '4254052669','6DD23A30100AC32A8B752016598ECE937CD1BD3D3DE361D8EE7811D1A1FE1206' # <-- RESTORED

    open_id , access_token = await GeNeRaTeAccEss(Uid , Pw)
    if not open_id or not access_token: 
        print("ErroR - InvaLid AccounT or Login Failed!") # <-- Improved message
        await asyncio.sleep(10) # Wait before retrying
        return None

    PyL = await EncRypTMajoRLoGin(open_id , access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL) # <-- RESTORED
    if not MajoRLoGinResPonsE: 
        print("TarGeT AccounT => BannEd / NoT ReGisTeReD ! ") 
        await asyncio.sleep(10) # Wait before retrying
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE) # <-- RESTORED
    UrL = MajoRLoGinauTh.url
    print(f"Login URL: {UrL}")
    region = MajoRLoGinauTh.region
    print(f"Region: {region}")

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    BOT_UID = TarGeT # <-- বটের UID এখানে সেভ করুন
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: 
        print("ErroR - GeTinG PorTs From LoGin Da Ta !") 
        return None

    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port

    # --- Proactive check for IP/Port errors ---
    if not OnLinePorTs or ":" not in OnLinePorTs:
        print(f"Error: Invalid Online_IP_Port received: {OnLinePorTs}")
        return None
    if not ChaTPorTs or ":" not in ChaTPorTs:
        print(f"Error: Invalid AccountIP_Port received: {ChaTPorTs}")
        return None

    OnLineiP , OnLineporT = OnLinePorTs.split(":") # <-- RESTORED
    ChaTiP , ChaTporT = ChaTPorTs.split(":") # <-- RESTORED
    acc_name = LoGinDaTaUncRypTinG.AccountName

    print(f"Account Name: {acc_name}")
    print(f"Token: {ToKen}")
    equie_emote(ToKen,UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()

    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))

    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen))
    os.system('clear')
    print(render('REDZED', colors=['white', 'green'], align='center'))
    print('')
    print(f" - Region: {region}")
    print(f" - BoT STarTinG And OnLine on TarGeT : {TarGeT} | BOT NAME : {acc_name}")
    print(f" - BoT sTaTus > GooD | OnLinE !")
    print(f" - Commands: help, owner, /sm") # <-- Updated commands

    await asyncio.gather(task1 , task2)

async def StarTinG():
    while True:
        try: 
            await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except asyncio.TimeoutError: 
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e: 
            print(f"ErroR TcP - {e} => ResTarTinG ...")
            await asyncio.sleep(5) # Add a small delay on error to prevent spamming

async def StarTinG():
    while True:
        try: 
            await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except asyncio.TimeoutError: 
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e: 
            print(f"ErroR TcP - {e} => ResTarTinG ...")
            await asyncio.sleep(5) # Add a small delay on error to prevent spamming

if __name__ == '__main__':
    asyncio.run(StarTinG())
