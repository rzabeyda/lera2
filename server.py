import os, sqlite3, time, smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB = os.path.join(os.path.dirname(__file__), "reg.db")
MAIL_TO = os.getenv("MAIL_TO", "valeriaja@icloud.com")
SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "25"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
MAIL_FROM = os.getenv("MAIL_FROM", SMTP_USER or "noreply@kompasskool.ee")

def send_mail(r):
    m = EmailMessage()
    m["Subject"] = f"Новая заявка: {r.course} — {r.name}"
    m["From"] = MAIL_FROM
    m["To"] = MAIL_TO
    m["Reply-To"] = r.email
    m.set_content(f"Имя: {r.name}\nТелефон: {r.phone}\nE-mail: {r.email}\nКурс: {r.course}\nЯзык: {r.lang}\n\n{r.msg}")
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15) as s:
        if SMTP_PORT != 25:
            s.starttls()
        if SMTP_USER:
            s.login(SMTP_USER, SMTP_PASS)
        s.send_message(m)
app = FastAPI()

with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS reg(id INTEGER PRIMARY KEY, ts INT, name TEXT, phone TEXT, email TEXT, course TEXT, msg TEXT, lang TEXT)")

class R(BaseModel):
    name: str
    phone: str
    email: str
    course: str
    msg: str = ""
    lang: str = "ru"
    website: str = ""

@app.post("/api/register")
def reg(r: R):
    if r.website:  # honeypot
        return {"ok": True}
    if not (2 <= len(r.name) <= 100 and 5 <= len(r.phone) <= 30 and "@" in r.email):
        raise HTTPException(400)
    with sqlite3.connect(DB) as c:
        c.execute("INSERT INTO reg(ts,name,phone,email,course,msg,lang) VALUES(?,?,?,?,?,?,?)",
                  (int(time.time()), r.name, r.phone, r.email, r.course, r.msg[:1000], r.lang))
    if SMTP_USER:
      try:
        send_mail(r)
      except Exception as e:
        print("mail error:", e, flush=True)
    return {"ok": True}
