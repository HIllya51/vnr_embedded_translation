# coding: utf8
# winlocale.py
# 11/19/2012 jichi

# MS LCID
# See: http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/%5BMS-LCID%5D.pdf
# See: http://msdn.microsoft.com/en-us/library/aa369771%28v=vs.85%29.aspx
# See: http://msdn.microsoft.com/en-us/goglobal/bb964664.aspx
LCID_NULL = 0x0
LCID_AR_SA = 0x0401 # 1025
LCID_BG_BG = 0x0402 # 1026
LCID_ZH_TW = 0x0404 # 1028
LCID_CS_CS = 0x0405 # 1029
LCID_DA_DA = 0x0406 # 1030
LCID_DE_DE = 0x0407 # 1031
LCID_EL_EL = 0x0408 # 1032
LCID_EN_US = 0x0409 # 1033
LCID_FI_FI = 0x040B # 1035
LCID_FR_FR = 0x040C # 1036
LCID_HE_IL = 0x040D # 1027
LCID_HU_HU = 0x040E # 1038
LCID_IT_IT = 0x0410 # 1040
LCID_JA_JP = 0x0411 # 1041
LCID_KO_KR = 0x0412 # 1042
LCID_NL_NL = 0x0413 # 1043
#LCID_NB_NO = 0x0414 # 1044
LCID_NO_NO = 0x0414 # 1044
LCID_PL_PL = 0x0415 # 1045
LCID_RO_RO = 0x0418 # 1048
LCID_RU_RU = 0x0419 # 1049
LCID_SK_SK = 0x041B # 1051
LCID_SV_SV = 0x041D # 1053
LCID_TR_TR = 0x041F # 1055
LCID_ID_ID = 0x0421 # 1057
LCID_UK_UA = 0x0422 # 1058
LCID_BE_BE = 0x0423 # 1059
LCID_SL_SL = 0x0424 # 1060
LCID_ET_EE = 0x0425 # 1061
LCID_LV_LV = 0x0426 # 1062
LCID_LT_LT = 0x0427 # 1063
LCID_VI_VN = 0x042a # 1066
LCID_TH_TH = 0x041e # 1054
LCID_MS_MY = 0x044c # 1100
LCID_TL_TL = 0x0464 # 1124, Filipino
LCID_ZH_CN = 0x0804 # 2052
LCID_PT_PT = 0x0816 # 2070
LCID_ES_ES = 0x0C0A # 3082

LCID_LOCALE = {
  LCID_ZH_TW: 'zh_TW',
  LCID_ZH_CN: 'zh_CN',
  LCID_EN_US: 'en_US',
  LCID_JA_JP: 'ja_JP',
  LCID_KO_KR: 'ko_KR',
  LCID_TH_TH: 'th_TH',
  LCID_VI_VN: 'vi_VN',
  LCID_TL_TL: 'tl_TL',
  LCID_ID_ID: 'id_ID',
  LCID_MS_MY: 'ms_MY',
  LCID_DE_DE: 'de_DE',
  LCID_IT_IT: 'it_IT',
  LCID_NL_NL: 'nl_NL',
  LCID_PL_PL: 'pl_PL',
  LCID_RO_RO: 'ro_RO',
  LCID_RU_RU: 'ru_RU',
  LCID_BE_BE: 'be_BE',
  LCID_FR_FR: 'fr_FR',
  LCID_PT_PT: 'pt_PT',
  LCID_ES_ES: 'es_ES',
  LCID_AR_SA: 'ar_SA',
  LCID_BG_BG: 'bg_BG',
  LCID_CS_CS: 'cs_CS',
  LCID_DA_DA: 'da_DA',
  LCID_FI_FI: 'fi_FI',
  LCID_HE_IL: 'he_IL',
  LCID_HU_HU: 'hu_HU',
  LCID_NO_NO: 'no_NO',
  LCID_SK_SK: 'sk_SK',
  LCID_SL_SL: 'sl_SL',
  LCID_SV_SV: 'sv_SV',
  LCID_EL_EL: 'el_EL',
  LCID_ET_EE: 'et_EE',
  LCID_LV_LV: 'lv_LV',
  LCID_LT_LT: 'lt_LT',
  LCID_TR_TR: 'tr_TR',
  LCID_UK_UA: 'uk_UA',
}

#LCID_LOCALE2 = {k:v[:2] for k,v in LCID_LOCALE.items()}

LOCALE_LCID = {v:k for k,v in LCID_LOCALE.items()}

def lcid2locale(k): return LCID_LOCALE.get(k) or '' # long -> str
def locale2lcid(k): return LOCALE_LCID.get(k) or 0  # str ->long

# MS code page
# See: http://msdn.microsoft.com/en-us/library/windows/desktop/dd317756%28v=vs.85%29.aspx
# See: https://docs.moodle.org/dev/Table_of_locales
CODEPAGE_NULL = 0
CODEPAGE_UTF8 = 65001
CODEPAGE_UTF16 = 1200
CODEPAGE_SHIFT_JIS = 932 # ja_JP
CODEPAGE_GBK = 936       # zh_CN
CODEPAGE_EUC_KR = 949    # ko_KR
CODEPAGE_BIG5 = 950      # zh_CN
CODEPAGE_TIS620 = 874    # th_TH
CODEPAGE_CE = 1250       # Central/Eastern Europe
CODEPAGE_CYRILLIC = 1251 # ru_RU
CODEPAGE_LATIN1 = 1252   # en_US
CODEPAGE_EL = 1253       # el_EL
CODEPAGE_TR = 1254       # tr_TR
CODEPAGE_HE = 1255       # he_IL
CODEPAGE_AR = 1256       # ar_SA
CODEPAGE_BALTIC = 1257   # North Europe
CODEPAGE_VI = 1258       # vi_VN

CODEPAGE_ENCODING = {
  CODEPAGE_UTF8: 'utf-8',
  CODEPAGE_UTF16: 'utf-16',
  CODEPAGE_SHIFT_JIS: 'shift-jis',

  CODEPAGE_BIG5: 'big5',
  CODEPAGE_GBK: 'gbk',
  CODEPAGE_EUC_KR: 'euc-kr',
  CODEPAGE_TIS620: 'tis-620',

  CODEPAGE_LATIN1: 'latin1',

  CODEPAGE_CE: 'windows-1250',
  CODEPAGE_BALTIC: 'windows-1257',
  CODEPAGE_EL: 'windows-1253',
  CODEPAGE_TR: 'windows-1254',
  CODEPAGE_AR: 'windows-1256',
  CODEPAGE_CYRILLIC: 'windows-1251',
  CODEPAGE_VI: 'windows-1258',
}

ENCODING_CODEPAGE = {v:k for k,v in CODEPAGE_ENCODING.items()}

CODEPAGE_ENCODING = {
  CODEPAGE_UTF8: 'utf-8',
  CODEPAGE_UTF16: 'utf-16',
  CODEPAGE_BIG5: 'big5',
  CODEPAGE_GBK: 'gbk',
  CODEPAGE_SHIFT_JIS: 'shift-jis',
  CODEPAGE_EUC_KR: 'euc-kr',
  CODEPAGE_TIS620: 'tis-620',
}

CODEPAGE_ENCODING_PY = {k:
  v if v.startswith('utf') else "cp%s" % k
  for k,v in CODEPAGE_ENCODING.items()}

CODEPAGE_ENCODING_QT = {
  CODEPAGE_UTF8: 'utf-8',
  CODEPAGE_UTF16: 'utf-16',
  CODEPAGE_SHIFT_JIS: 'shift-jis',

  CODEPAGE_GBK: 'cp936',
  CODEPAGE_BIG5: 'cp950',
  CODEPAGE_EUC_KR: 'cp949',
  CODEPAGE_TIS620: 'cp874',

  CODEPAGE_LATIN1: 'windows-1252',

  CODEPAGE_CE: 'windows-1250',
  CODEPAGE_CYRILLIC: 'windows-1251',
  CODEPAGE_AR: 'windows-1256',
  CODEPAGE_VI: 'windows-1258',
}

ENCODING_PY = {v:CODEPAGE_ENCODING_PY[k] for k,v in CODEPAGE_ENCODING.items()}
ENCODING_QT = {v:CODEPAGE_ENCODING_PY[k] for k,v in CODEPAGE_ENCODING.items()}

def codepage2encoding(k): return CODEPAGE_ENCODING.get(k) or '' # long -> str
def encoding2codepage(k): return ENCODING_CODEPAGE.get(k) or ''  # str ->long

def encoding2py(k): return ENCODING_PY.get(k) or '' # str -> str
def encoding2qt(k): return ENCODING_PY.get(k) or '' # str -> str

LOCALE_CODEPAGE = {
  'zh_TW': CODEPAGE_BIG5,
  'zh_CN': CODEPAGE_GBK,
  'ja_JP': CODEPAGE_SHIFT_JIS,
  'ko_KR': CODEPAGE_EUC_KR,

  'th_TH': CODEPAGE_TIS620,
  'th_VI': CODEPAGE_VI,
  'el_EL': CODEPAGE_EL,
  'tr_TR': CODEPAGE_TR,
  'ar_SA': CODEPAGE_AR,
  'he_IL': CODEPAGE_HE,

  'ru_RU': CODEPAGE_CYRILLIC,
  'be_BE': CODEPAGE_CYRILLIC,
  'bg_BG': CODEPAGE_CYRILLIC,
  'uk_UA': CODEPAGE_CYRILLIC,

  'fi_FI': CODEPAGE_BALTIC,
  'no_NO': CODEPAGE_BALTIC,
  'sv_SV': CODEPAGE_BALTIC,
  'da_DA': CODEPAGE_BALTIC,
  'et_EE': CODEPAGE_BALTIC,
  'lt_LT': CODEPAGE_BALTIC,
  'lv_LV': CODEPAGE_BALTIC,

  # http://en.wikipedia.org/wiki/Windows-1250
  'pl_PL': CODEPAGE_CE,
  'cs_CS': CODEPAGE_CE,
  'hu_HU': CODEPAGE_CE,
  'ro_RO': CODEPAGE_CE,
  'sk_SK': CODEPAGE_CE,
  'sl_SL': CODEPAGE_CE,

  'de_DE': CODEPAGE_LATIN1,
  'en_US': CODEPAGE_LATIN1,
  'es_ES': CODEPAGE_LATIN1,
  'fr_FR': CODEPAGE_LATIN1,
  'id_ID': CODEPAGE_LATIN1,
  'it_IT': CODEPAGE_LATIN1,
  'pt_PT': CODEPAGE_LATIN1,
  'ms_MY': CODEPAGE_LATIN1,
  'nl_NL': CODEPAGE_LATIN1,

  'tl_TL': CODEPAGE_LATIN1,
}

def locale2codepage(k): return LOCALE_CODEPAGE.get(k) or 0  # str ->long

# Character sets

# https://msdn.microsoft.com/en-us/library/cc250412.aspx
# typedef enum // BYTE
# {
#   ANSI_CHARSET = 0x00000000,
#   DEFAULT_CHARSET = 0x00000001,
#   SYMBOL_CHARSET = 0x00000002,
#   MAC_CHARSET = 0x0000004D,
#   SHIFTJIS_CHARSET = 0x00000080,
#   HANGUL_CHARSET = 0x00000081,
#   JOHAB_CHARSET = 0x00000082,
#   GB2312_CHARSET = 0x00000086,
#   CHINESEBIG5_CHARSET = 0x00000088,
#   GREEK_CHARSET = 0x000000A1,
#   TURKISH_CHARSET = 0x000000A2,
#   VIETNAMESE_CHARSET = 0x000000A3,
#   HEBREW_CHARSET = 0x000000B1,
#   ARABIC_CHARSET = 0x000000B2,
#   BALTIC_CHARSET = 0x000000BA,
#   RUSSIAN_CHARSET = 0x000000CC,
#   THAI_CHARSET = 0x000000DE,
#   EASTEUROPE_CHARSET = 0x000000EE,
#   OEM_CHARSET = 0x000000FF
# } CharacterSet;

ANSI_CHARSET = 0x00000000
DEFAULT_CHARSET = 0x00000001
SYMBOL_CHARSET = 0x00000002
MAC_CHARSET = 0x0000004D
SHIFTJIS_CHARSET = 0x00000080
HANGUL_CHARSET = 0x00000081
JOHAB_CHARSET = 0x00000082
GB2312_CHARSET = 0x00000086
CHINESEBIG5_CHARSET = 0x00000088
GREEK_CHARSET = 0x000000A1
TURKISH_CHARSET = 0x000000A2
VIETNAMESE_CHARSET = 0x000000A3
HEBREW_CHARSET = 0x000000B1
ARABIC_CHARSET = 0x000000B2
BALTIC_CHARSET = 0x000000BA
RUSSIAN_CHARSET = 0x000000CC
THAI_CHARSET = 0x000000DE
EASTEUROPE_CHARSET = 0x000000EE
OEM_CHARSET = 0x000000FF

# EOF
