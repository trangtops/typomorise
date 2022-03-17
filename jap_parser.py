hiragana_list = [
    "あ",
    "い",
    "う",
    "え",
    "お",
    "か",
    "き",
    "く",
    "け",
    "こ",
    "さ",
    "し",
    "す",
    "せ",
    "そ",
    "た",
    "ち",
    "つ",
    "て",
    "と",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ひ",
    "ふ",
    "へ",
    "ほ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "や",
    "ゆ",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "わ",
    "を",
    "っ",
]

romanji_to_hiragana = {
    "a": "あ",
    "i": "い",
    "u": "う",
    "e": "え",
    "o": "お",
    "ka": "か",
    "kka": "っか",
    "ki": "き",
    "kki": "っき",
    "ku": "く",
    "kku": "っく",
    "ke": "け",
    "kke": "っけ",
    "ko": "こ",
    "kko": "っこ",
    "sa": "さ",
    "ssa": "っさ",
    "shi": "し",
    "su": "す",
    "ssu": "っす",
    "se": "せ",
    "sse": "っせ",
    "so": "そ",
    "sso": "っそ",
    "ta": "た",
    "tta": "った",
    "chi": "ち",
    "ti": "ち",
    "tti": "っち",
    "tu": "つ",
    "tsu": "つ",
    "ttu": "っつ",
    "te": "て",
    "tte": "って",
    "to": "と",
    "tto": "っと",
    "na": "な",
    "ni": "に",
    "nu": "ぬ",
    "ne": "ね",
    "no": "の",
    "ha": "は",
    "hha": "っは",
    "hi": "ひ",
    "hhi": "っひ",
    "fu": "ふ",
    "hhu": "っふ",
    "he": "へ",
    "hhe": "っへ",
    "ho": "ほ",
    "hho": "っほ",
    "ma": "ま",
    "mma": "っま",
    "mi": "み",
    "mmi": "っみ",
    "mu": "む",
    "mmu": "っむ",
    "me": "め",
    "mme": "っめ",
    "mo": "も",
    "mmo": "っも",
    "ya": "や",
    "yya": "っや",
    "yu": "ゆ",
    "yyu": "っゆ",
    "yo": "よ",
    "yyo": "っよ",
    "ra": "ら",
    "rra": "っら",
    "ri": "り",
    "rre": "っれ",
    "ru": "る",
    "rru": "っる",
    "re": "れ",
    "rri": "っり",
    "ro": "ろ",
    "rro": "っろ",
    "wa": "わ",
    "wwa": "っわ",
    "wo": "を",
    "wwo": "っを",
    "ga": "が",
    "gga": "っが",
    "gi": "ぎ",
    "ggi": "っぎ",
    "gu": "ぐ",
    "ggu": "っぐ",
    "ge": "げ",
    "gge": "っげ",
    "go": "ご",
    "ggo": "っご",
    "za": "ざ",
    "zza": "っざ",
    "ji": "じ",
    "jji": "っじ",
    "zi": "じ",
    "zzi": "っじ",
    "zu": "ず",
    "zzu": "っず",
    "ze": "ぜ",
    "zze": "っぜ",
    "zo": "ぞ",
    "zzo": "っぞ",
    "da": "だ",
    "dda": "っだ",
    "di": "ぢ",
    "ddi": "っぢ",
    "du": "づ",
    "ddu": "っづ",
    "de": "で",
    "dde": "っで",
    "do": "ど",
    "ddo": "っど",
    "ba": "ば",
    "bba": "っば",
    "bi": "び",
    "bbi": "っび",
    "bu": "ぶ",
    "bbu": "っぶ",
    "be": "べ",
    "bbe": "っべ",
    "bo": "ぼ",
    "bbo": "っぼ",
    "pa": "ぱ",
    "ppa": "っぱ",
    "pi": "ぴ",
    "ppi": "っぴ",
    "pu": "ぷ",
    "ppu": "っぷ",
    "pe": "ぺ",
    "ppe": "っぺ",
    "po": "ぽ",
    "ppo": "っぽ",
    "kya": "きゃ",
    "kkya": "っきゃ",
    "kyu": "きゅ",
    "kkyu": "っきゅ",
    "kyo": "きょ",
    "kkyo": "っきょ",
    "sha": "しゃ",
    "ssha": "っしゃ",
    "shu": "しゅ",
    "sshu": "っしゅ",
    "sho": "しょ",
    "ssho": "っしょ",
    "cha": "ちゃ",
    "ccha": "っちゃ",
    "chu": "ちゅ",
    "cchu": "っちゅ",
    "cho": "ちょ",
    "ccho": "っちょ",
    "nya": "にゃ",
    "nyu": "にゅ",
    "nyo": "にょ",
    "hya": "ひゃ",
    "hyu": "ひゅ",
    "hyo": "ひょ",
    "mya": "みゃ",
    "myu": "みゅ",
    "myo": "みょ",
    "rya": "りゃ",
    "rrya": "っりゃ",
    "ryu": "りゅ",
    "rryu": "っりゅ",
    "ryo": "りょ",
    "rryo": "っりょ",
    "gya": "ぎゃ",
    "ggya": "っぎゃ",
    "gyu": "ぎゅ",
    "ggyu": "っぎゅ",
    "gyo": "ぎょ",
    "ggyo": "っぎょ",
    "ja": "じゃ",
    "jja": "っじゃ",
    "ju": "じゅ",
    "jju": "っじゅ",
    "jo": "じょ",
    "jjo": "っじょ",
    "bya": "びゃ",
    "bbya": "っびゃ",
    "byu": "びゅ",
    "bbyu": "っびゅ",
    "byo": "びょ",
    "bbyo": "っびょ",
    "pya": "ぴゃ",
    "ppya": "っぴゃ",
    "pyu": "ぴゅ",
    "ppyu": "っぴゅ",
    "pyo": "ぴょ",
    "ppyo": "っぴょ",
    "nn": "ん",
}


def to_hiragana_converter(romanji):
    hiragana = ""
    buffer = ""
    for char in romanji:
        if ord(char) not in range(97, 123):
            hiragana += char
            continue
        buffer += char
        _buffer = romanji_to_hiragana.get(buffer, buffer)
        if buffer != _buffer:
            hiragana += _buffer
            buffer = ""
    return hiragana + buffer
