SPAM_WORDS = [
    "sale",
    "discount",
    "offer",
    "free",
    "bitcoin",
    "crypto",
    "usdt",
    "優惠",
    "折扣",
    "免費",
    "投資",
    "貸款",
    "賺錢",
    "限時",
    "中獎"
]

NEWSLETTER_WORDS = [
    "newsletter",
    "weekly",
    "digest",
    "godiva",
    "trust",
    "factory",
    "開發工程師",
    "職缺",
    "招募",
    "課程",
    "研討會",
    "直播",
    "電子報"
]

def classify_email(subject):

    s = subject.lower()

    for word in SPAM_WORDS:
        if word.lower() in s:
            return "spam"

    for word in NEWSLETTER_WORDS:
        if word.lower() in s:
            return "newsletter"

    return "important"
