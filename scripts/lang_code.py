# -*- coding: UTF-8 -*-
# always put en to the first
lang_code_dict = {
    # refer: http://api.fanyi.baidu.com/doc/21
    "baidu": {
        "英语": "en",
        "中文": "zh"
    },
    #refer: https://www.deepl.com/docs-api/translate-text/translate-text/
    "deepl": {
        "English": "EN",
        "Japanese": "JA",
        "Korean": "KO",
        "Russian": "RU",
        "Bulgarian": "BG",
        "Czech": "CS",
        "Danish": "DA",
        "German": "DE",
        "Greek": "EL",
        "Spanish": "ES",
        "Estonian": "ET",
        "Finnish": "FI",
        "French": "FR",
        "Hungarian": "HU",
        "Indonesian": "ID",
        "Italian": "IT",
        "Lithuanian": "LT",
        "Latvian": "LV",
        "Norwegian": "NB",
        "Dutch": "NL",
        "Polish": "PL",
        "Portuguese": "PT",
        "Romanian": "RO",
        "Slovak": "SK",
        "Slovenian": "SL",
        "Swedish": "SV",
        "Turkish": "TR",
        "Ukrainian": "UK",
        "Chinese": "ZH"
    },
    # refer: https://cloud.google.com/translate/docs/languages?hl=en
    "google": {
        "English": "en",
        "Japanese": "ja",
        "Korean": "ko",
        "Afrikaans": "af",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Assamese": "as",
        "Aymara": "ay",
        "Azerbaijani": "az",
        "Bambara": "bm",
        "Basque": "eu",
        "Belarusian": "be",
        "Bengali": "bn",
        "Bhojpuri": "bho",
        "Bosnian": "bs",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Cebuano": "ceb",
        "Chinese(Simplified)": "zh",
        "Chinese(Traditional)": "zh-TW",
        "Corsican": "co",
        "Croatian": "hr",
        "Czech": "cs",
        "Danish": "da",
        "Dhivehi": "dv",
        "Dogri": "doi",
        "Dutch": "nl",
        "Esperanto": "eo",
        "Estonian": "et",
        "Ewe": "ee",
        "Filipino (Tagalog)": "fil",
        "Finnish": "fi",
        "French": "fr",
        "Frisian": "fy",
        "Galician": "gl",
        "Georgian": "ka",
        "German": "de",
        "Greek": "el",
        "Guarani": "gn",
        "Gujarati": "gu",
        "HaitianCreole": "ht",
        "Hausa": "ha",
        "Hawaiian": "haw",
        "Hebrew": "he",
        "Hindi": "hi",
        "Hmong": "hmn",
        "Hungarian": "hu",
        "Icelandic": "is",
        "Igbo": "ig",
        "Ilocano": "ilo",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Javanese": "jv",
        "Kannada": "kn",
        "Kazakh": "kk",
        "Khmer": "km",
        "Kinyarwanda": "rw",
        "Konkani": "gom",
        "Krio": "kri",
        "Kurdish": "ku",
        "Kurdish (Sorani)": "ckb",
        "Kyrgyz": "ky",
        "Lao": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lingala": "ln",
        "Lithuanian": "lt",
        "Luganda": "lg",
        "Luxembourgish": "lb",
        "Macedonian": "mk",
        "Maithili": "mai",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Maori": "mi",
        "Marathi": "mr",
        "Meiteilon": "mni-Mtei",
        "Mizo": "lus",
        "Mongolian": "mn",
        "Myanmar": "my",
        "Nepali": "ne",
        "Norwegian": "no",
        "Nyanja": "ny",
        "Odia (Oriya)": "or",
        "Oromo": "om",
        "Pashto": "ps",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese": "pt",
        "Punjabi": "pa",
        "Quechua": "qu",
        "Romanian": "ro",
        "Russian": "ru",
        "Samoan": "sm",
        "Sanskrit": "sa",
        "Scots Gaelic": "gd",
        "Sepedi": "nso",
        "Serbian": "sr",
        "Sesotho": "st",
        "Shona": "sn",
        "Sindhi": "sd",
        "Sinhala": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Somali": "so",
        "Spanish": "es",
        "Sundanese": "su",
        "Swahili": "sw",
        "Swedish": "sv",
        "Tagalog": "tl",
        "Tajik": "tg",
        "Tamil": "ta",
        "Tatar": "tt",
        "Telugu": "te",
        "Thai": "th",
        "Tigrinya": "ti",
        "Tsonga": "ts",
        "Turkish": "tr",
        "Turkmen": "tk",
        "Twi(Akan)": "ak",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Uyghur": "ug",
        "Uzbek": "uz",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Xhosa": "xh",
        "Yiddish": "yi",
        "Yoruba": "yo",
        "Zulu": "zu"
    },
    # refer: https://cloud.google.com/translate/docs/languages?hl=en
    "yandex": {
        "English": "en",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru",
        "Azerbaijani": "az",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Afrikaans": "af",
        "Basque": "eu",
        "Bashkir": "ba",
        "Belarusian": "be",
        "Bengal": "bn",
        "Burmese": "my",
        "Bulgarian": "bg",
        "Bosnian": "bs",
        "Welsh": "cy",
        "Hungarian": "hu",
        "Vietnamese": "vi",
        "Haitian (Creole)\t": "ht",
        "Galician": "gl",
        "Dutch": "nl",
        "Hill Mari": "mrj",
        "Greek": "el",
        "Georgian": "ka",
        "Gujarati": "gu",
        "Danish": "da",
        "Hebrew": "he",
        "Yiddish": "yi",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Icelandic": "is",
        "Spanish": "es",
        "Kazakh": "kk",
        "Kannada": "kn",
        "Catalan": "ca",
        "Kirghiz": "ky",
        "Chinese": "zh",
        "Xhosa": "xh",
        "Khmer": "km",
        "Laotian": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lithuanian": "lt",
        "Luxembourg": "lb",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Macedonian": "mk",
        "Maori": "mi",
        "Marathi": "mr",
        "Mari": "mhr",
        "Mongolian": "mn",
        "German": "de",
        "Nepalese": "ne",
        "Norwegian": "no",
        "Punjabi": "pa",
        "Papiamento": "pap",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese": "pt",
        "Romanian": "ro",
        "Cebuano": "ceb",
        "Serbian": "sr",
        "Sinhalese": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Swahili": "sw",
        "Sundanese": "su",
        "Tajik": "tg",
        "Thai": "th",
        "Tagalog": "tl",
        "Tamil": "ta",
        "Tartar": "tt",
        "Telugu": "te",
        "Turkish": "tr",
        "Udmurt": "udm",
        "Uzbek": "uz",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Finnish": "fi",
        "French": "fr",
        "Hindi": "hi",
        "Croatian": "hr",
        "Czech": "cs",
        "Swedish": "sv",
        "Scottish": "gd",
        "Estonian": "et",
        "Esperanto": "eo",
        "Javanese": "jv"
    }

}

