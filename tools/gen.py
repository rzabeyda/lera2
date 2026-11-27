import os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import C, T, PRACT

OUT = sys.argv[1]
e = html.escape

L = {
 "ru": {"back": "← Все курсы", "reg": "Записаться на курс", "price": "Стоимость", "hours": "Объём", "ah": "ак. часов", "dates": "Даты", "place": "Место", "lang": "Язык обучения", "langv": "русский",
        "group": "Группа учебной программы", "for": "Для кого", "goal": "Цель курса", "out": "Чему вы научитесь", "mod": "Программа курса", "h": "ч", "fin": "Окончание и документы",
        "start": "Для начала обучения нужны заявление и документ, удостоверяющий личность.", "pr": "Практика", "mat": "Учебные материалы", "tea": "Преподаватели",
        "pdf": "Скачать программу (PDF)", "cta": "Остались вопросы? Позвоните или оставьте заявку — мы подтвердим место в группе.", "org1": "Курсы организует MTÜ Nagu Sina", "org2": "Рег. код: 80600369",
        "pl": "Liimi 1, Таллин", "titlesuf": "курс в Таллине"},
 "et": {"back": "← Kõik kursused", "reg": "Registreeru kursusele", "price": "Hind", "hours": "Maht", "ah": "ak tundi", "dates": "Kuupäevad", "place": "Koht", "lang": "Õppekeel", "langv": "vene keel",
        "group": "Õppekavarühm", "for": "Kellele", "goal": "Koolituse eesmärk", "out": "Õpiväljundid", "mod": "Õppekava", "h": "t", "fin": "Lõpetamine ja dokumendid",
        "start": "Õpingute alustamiseks on vaja avaldust ja isikut tõendavat dokumenti.", "pr": "Praktika", "mat": "Õppematerjalid", "tea": "Koolitajad",
        "pdf": "Laadi õppekava alla (PDF)", "cta": "Küsimusi? Helista või jäta avaldus — kinnitame koha grupis.", "org1": "Koolitusi korraldab MTÜ Nagu Sina", "org2": "Registrikood: 80600369",
        "pl": "Liimi 1, Tallinn", "titlesuf": "kursus Tallinnas"},
}

CSS = """:root{--c:#82027d;--c2:#e6007a;--bg:#fbf1f8;--t:#2a1a29;--m:#6b5a69;--b:#f0dcea}
*{box-sizing:border-box}body{margin:0;font:17px/1.65 Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--t);background:#fff;-webkit-font-smoothing:antialiased}
a{color:var(--c)}.wrap{max-width:900px;margin:0 auto;padding:0 20px}
html[data-l=ru] .l-et,html[data-l=et] .l-ru{display:none!important}
header{position:sticky;top:0;background:rgba(255,255,255,.95);backdrop-filter:blur(10px);border-bottom:1px solid var(--b);z-index:10}
.bar{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:68px;padding:8px 0}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:22px;letter-spacing:.06em;text-decoration:none;color:var(--c);line-height:1}.logo img{height:52px;width:auto;display:block}
.logo small{display:block;margin-top:4px;font-size:10.5px;font-weight:700;color:var(--c2);letter-spacing:.18em}
.logo em{display:block;margin-top:4px;font-style:normal;font-size:11px;font-weight:500;color:var(--m);letter-spacing:0;line-height:1.35}.logo em i{display:block;font-style:normal}
.lb{display:flex;gap:6px}.lb button{font:inherit;font-size:15px;font-weight:600;border:1px solid var(--c);color:var(--c);background:none;padding:7px 12px;border-radius:8px;cursor:pointer}.lb button.on{background:var(--c);color:#fff}
.hero{position:relative;color:#fff;background:#2a1a29;overflow:hidden}.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.45}
.hero .wrap{position:relative;padding:42px 20px 56px}.back{color:#fff;opacity:.9;text-decoration:none;font-size:15px}
h1{font-size:clamp(28px,5vw,44px);line-height:1.15;margin:14px 0 6px;letter-spacing:-.02em}.grp{opacity:.9;margin:0 0 20px}
.btn{display:inline-block;background:var(--c2);color:#fff;padding:13px 26px;border-radius:12px;text-decoration:none;font-weight:600;box-shadow:0 6px 18px rgba(230,0,122,.28)}
.facts{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:-28px auto 0;position:relative}
.facts div{background:#fff;border:1px solid var(--b);border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px rgba(130,2,125,.08)}.facts b{display:block;font-size:12.5px;color:var(--m);font-weight:500}.facts span{font-weight:700;font-size:15.5px;line-height:1.35;display:block}
h2{color:var(--c);font-size:clamp(22px,3vw,28px);margin:44px 0 12px;letter-spacing:-.01em}
ul.ck{list-style:none;padding:0;margin:0}ul.ck li{padding:6px 0 6px 30px;position:relative}ul.ck li:before{content:"✓";position:absolute;left:4px;top:6px;color:var(--c2);font-weight:800}
table{width:100%;border-collapse:collapse;border:1px solid var(--b);border-radius:14px;overflow:hidden}td{padding:11px 14px;border-top:1px solid var(--b);vertical-align:top}tr:first-child td{border-top:0}tr:nth-child(even){background:var(--bg)}
td.n{width:42px;color:var(--m);font-weight:600}td.h{width:90px;text-align:right;font-weight:700;color:var(--c);white-space:nowrap}
.note{background:var(--bg);border-left:4px solid var(--c2);border-radius:10px;padding:14px 18px;margin:16px 0}
.tea{display:grid;gap:12px}.tea p{margin:0;padding:14px 16px;border:1px solid var(--b);border-radius:12px}
.cta{background:linear-gradient(135deg,#82027d,#5a0257);color:#fff;margin-top:56px;padding:44px 0}.cta p{font-size:19px;margin:0 0 20px}.cta .btn{background:#fff;color:#82027d;box-shadow:none}.cta a.pdf{color:#fff;margin-left:16px}
footer{background:#3a0638;color:#ecd6e8;padding:28px 0;font-size:15px}footer a{color:#fff}
@media(max-width:760px){.facts{grid-template-columns:repeat(2,1fr)}}@media(max-width:600px){.logo em{font-size:10.5px}.cta a.pdf{display:block;margin:16px 0 0}}"""

def both(fn):
    return "".join(f'<div class="l-{l}">{fn(l)}</div>' for l in ("ru", "et"))

def page(c):
    def head_title(l):
        return e(c[l]["title"])
    def body(l):
        d, t = c[l], L[l]
        place = t["pl"] + (" / Zoom" if c["zoom"] else "")
        mods = "".join(f'<tr><td class="n">{i}</td><td>{e(m)}</td><td class="h">{h} {t["h"]}</td></tr>' for i, (m, h) in enumerate(d["mod"], 1))
        outs = "".join(f"<li>{e(o)}</li>" for o in d["out"])
        fin = "".join(f"<li>{e(f)}</li>" for f in d["fin"])
        tea = "".join(f"<p>{e(T[k][l])}</p>" for k in c["t"])
        return f"""
<section class="hero"><img src="/img/{c['img']}" alt="" style="object-position:{c['pos']}"><div class="wrap">
<a class="back" href="/#kursused">{t['back']}</a>
<h1>{e(d['title'])}</h1><p class="grp">{t['group']}: {e(d['group'])}</p>
<a class="btn" href="/?kursus={c['id']}#reg">{t['reg']}</a></div></section>
<div class="wrap">
<div class="facts"><div><b>{t['price']}</b><span>{c['p']} €</span></div><div><b>{t['hours']}</b><span>{c['h']} {t['ah']}</span></div><div><b>{t['dates']}</b><span>{c['d']}</span></div><div><b>{t['place']}</b><span>{place}</span></div><div><b>{t['lang']}</b><span>{t['langv']}</span></div></div>
<h2>{t['for']}</h2><p>{e(d['target'])}</p>
<h2>{t['goal']}</h2><p>{e(d['goal'])}</p>
<h2>{t['out']}</h2><ul class="ck">{outs}</ul>
<h2>{t['mod']}</h2><p style="color:var(--m)">{e(d['vol'])}</p><table>{mods}</table>
<h2>{t['pr']}</h2><p>{e(PRACT[l])}</p><div class="note">{e(d['extra'])}</div>
<h2>{t['fin']}</h2><p>{t['start']}</p><ul class="ck">{fin}</ul>
<h2>{t['mat']}</h2><p>{e(d['mat'])}</p>
<h2>{t['tea']}</h2><div class="tea">{tea}</div>
</div>
<section class="cta"><div class="wrap"><p>{t['cta']}</p><a class="btn" href="/?kursus={c['id']}#reg">{t['reg']}</a><a class="pdf" href="/docs/{c['pdf']}" target="_blank" rel="noopener">{t['pdf']}</a></div></section>"""
    org = "".join(f'<em class="l-{l}"><i>{L[l]["org1"]}</i><i>{L[l]["org2"]}</i></em>' for l in ("ru", "et"))
    return f"""<!doctype html>
<html lang="ru" data-l="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(c['ru']['title'])} — {L['ru']['titlesuf']} | Kompass</title>
<meta name="description" content="{e(c['ru']['title'])} / {e(c['et']['title'])}: {c['h']} ak. h, {c['p']} €. Liimi 1, Tallinn.">
<link rel="icon" href="/ns-favicon.ico?v=7" sizes="any"><link rel="icon" href="/img/ns-favicon-64.png?v=7" type="image/png"><link rel="apple-touch-icon" href="/img/ns-apple-touch-icon.png?v=7"><meta name="theme-color" content="#82027d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script>(function(){{var l="ru";try{{l=localStorage.getItem("l")||((navigator.language||"").toLowerCase().indexOf("et")===0?"et":"ru")}}catch(e){{}}document.documentElement.setAttribute("data-l",l);document.documentElement.lang=l}})()</script>
</head><body>
<header><div class="wrap bar"><a class="logo" href="/"><img src="/img/ns-logo.png?v=7" alt="MTÜ Nagu Sina" width="52" height="52"><span>KOMPASS<small>KOOLITUSKESKUS</small>{org}</span></a>
<div class="lb"><button data-l="et">ET</button><button data-l="ru">RU</button></div></div></header>
{both(body)}
<footer><div class="wrap">Mittetulundusühing (MTÜ) NAGU SINA · Reg. 80600369 · Liimi 1, Tallinn · <a href="tel:+37257918599">+372 5791 8599</a> · <a href="mailto:kompasskool@gmail.com">kompasskool@gmail.com</a></div></footer>
<script>
function sl(l){{document.documentElement.setAttribute("data-l",l);document.documentElement.lang=l;try{{localStorage.setItem("l",l)}}catch(e){{}}
document.querySelectorAll(".lb button").forEach(function(b){{b.classList.toggle("on",b.dataset.l===l)}});
document.title=(l==="et"?{c['et']['title']!r}+" — {L['et']['titlesuf']}":{c['ru']['title']!r}+" — {L['ru']['titlesuf']}")+" | Kompass"}}
document.querySelectorAll(".lb button").forEach(function(b){{b.onclick=function(){{sl(b.dataset.l)}}}});
sl(document.documentElement.getAttribute("data-l"));
</script>
</body></html>"""

for c in C:
    d = os.path.join(OUT, "kursus", c["id"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(c))
    print(c["id"], sum(h for _, h in c["ru"]["mod"]), sum(h for _, h in c["et"]["mod"]))
