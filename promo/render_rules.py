"""Design Tip 06: '5 design rules I never break' (guide: TOF carousel, 2026-11-14). Navy, no glow.
Usage: python3 promo/render_rules.py OUTDIR
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
OUT = os.path.abspath(sys.argv[1]); os.makedirs(OUT, exist_ok=True)
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'
PEN = pathlib.Path(f'{R}/assets-hero/pen-cut.png').as_uri()
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:52px;width:auto;display:block"', 1)
DOT = f'<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.04em"></span>'
CSS = f"""@font-face{{font-family:M;font-weight:400;src:url({F}montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
@font-face{{font-family:GB;src:url({R}/book-flyer/fonts/Gobold.otf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;
 background:linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)}}
.a{{position:absolute}} .g{{color:{G}}}
.card{{position:absolute;width:400px;height:500px;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.45)}}
.tag{{position:absolute;font-weight:900;font-size:18px;letter-spacing:5px}}"""
MARK = f'<svg class="a" viewBox="252 255 749 664" style="right:-200px;bottom:-80px;width:620px;opacity:.035"><path fill="#fff" fill-rule="evenodd" d="{rb.MK["nodot"]}"/><path fill="#fff" d="{rb.MK["dot"]}"/></svg>'
GRAIN = f'<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>'

def page(body, n=None, swipe=True):
    foot = f'<div class="a" style="left:90px;bottom:70px;font-weight:600;font-size:20px;color:rgba(255,255,255,.7)">@thedanagstudio</div>'
    if swipe: foot += f'<div class="a" style="right:90px;bottom:68px;font-weight:900;font-size:20px;letter-spacing:4px;color:{G}">SWIPE &gt;&gt;</div>'
    num = f'<div class="a" style="right:90px;top:84px;font-weight:900;font-size:22px;letter-spacing:4px;color:{G}">{n}/05</div>' if n else ''
    return f'<html><head><style>{CSS}</style></head><body>{MARK}<div class="a" style="left:90px;top:76px">{logo}</div>{num}{body}{foot}{GRAIN}<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>'

# ---------- mock cards (400x500) ----------
def c(bg, inner): return f'<div style="width:400px;height:500px;position:relative;overflow:hidden;font-family:M;background:{bg}">{inner}</div>'
def ab(x, y, s, t): return f'<div style="position:absolute;left:{x}px;top:{y}px;{s}">{t}</div>'
MOCK = {
 'loud_b': c('#fff3d6', ab(0,22,'width:400px;text-align:center;color:#d62828;font-weight:900;font-size:56px;line-height:.95','MEGA<br>SALE!!!')
   + ab(22,150,'background:#d62828;color:#fff;font-weight:900;font-size:22px;padding:6px 12px;transform:rotate(-6deg)','50% OFF')
   + ab(220,160,'background:#1d3557;color:#ffd166;font-weight:900;font-size:20px;padding:8px 12px;border-radius:50%;width:120px;height:120px;text-align:center;padding-top:36px','BUY 1<br>GET 1')
   + ab(24,240,'color:#d62828;font-weight:900;font-size:30px','KENTE • LACE • BATIK')
   + ab(24,290,'color:#1d3557;font-weight:900;font-size:26px;text-decoration:underline','FREE DELIVERY!!')
   + ab(24,340,'color:#e76f51;font-weight:900;font-size:24px','LIMITED TIME ONLY')
   + ab(24,384,'color:#d62828;font-weight:700;font-size:20px','HURRY HURRY HURRY')
   + ab(0,440,'width:400px;text-align:center;background:#d62828;color:#fff;font-weight:900;font-size:22px;padding:12px 0','CALL NOW 000 000 0000')),
 'loud_a': c('linear-gradient(170deg,#1b1f3b,#0d1024)', ab(32,36,'color:#ffd166;font-weight:700;font-size:14px;letter-spacing:4px','ADEPA FABRICS · MAKOLA')
   + ab(28,86,'color:#fff;font-weight:900;font-size:120px;line-height:.85;letter-spacing:-5px','50%<br><span style="color:#ffd166">OFF</span>')
   + ab(32,320,'color:#c9cbe0;font-weight:500;font-size:18px;line-height:1.5','Kente, lace and batik.<br>This weekend only.')
   + ab(32,420,'background:#ffd166;color:#0d1024;font-weight:900;font-size:16px;padding:11px 20px;border-radius:30px','Call 000 000 0000')),
 'type_b': c('#f2efe9', ab(0,70,'width:400px;text-align:center;font-family:SC;color:#7b2cbf;font-size:64px;line-height:1','Grand')
   + ab(0,140,'width:400px;text-align:center;font-family:serif;font-style:italic;color:#e63946;font-size:52px;font-weight:700','Opening')
   + ab(0,230,'width:400px;text-align:center;font-family:"Courier New";color:#2a9d8f;font-size:26px;font-weight:700','Ama\'s Kitchen')
   + ab(0,290,'width:400px;text-align:center;font-family:Impact,sans-serif;color:#f4a261;font-size:30px','SATURDAY 10AM')
   + ab(0,360,'width:400px;text-align:center;font-family:serif;color:#264653;font-size:20px','Free drinks for the first 50 guests')
   + ab(0,430,'width:400px;text-align:center;font-family:"Comic Sans MS",cursive;color:#7b2cbf;font-size:18px','Osu, Accra')),
 'type_a': c('linear-gradient(165deg,#2b1408,#120804)', ab(30,40,'color:#f4a261;font-weight:700;font-size:14px;letter-spacing:5px','AMA\'S KITCHEN · OSU')
   + ab(30,84,'',rb.line('GRAND',96,'#ffffff')) + ab(30,196,'',rb.line('OPENING',96,'#f4a261'))
   + ab(30,310,'color:#fff;font-weight:900;font-size:26px','Saturday, 10am')
   + ab(30,350,'color:#d9c3b0;font-weight:400;font-size:17px;line-height:1.5','Free drinks for the<br>first 50 guests.')
   + ab(30,446,'color:#f4a261;font-weight:700;font-size:15px','Osu, Accra · 000 000 0000')),
 'space_b': c('#ffffff', ab(16,14,'color:#0b6e4f;font-weight:900;font-size:40px;line-height:1','Glow Skin Studio')
   + ab(16,60,'color:#333;font-weight:500;font-size:15px;line-height:1.3','Facials · Waxing · Brows · Lashes · Nails · Massage · Make-up')
   + ab(16,108,'color:#0b6e4f;font-weight:900;font-size:22px','Book: 000 000 0000 · East Legon')
   + ab(16,140,'width:368px;height:2px;background:#0b6e4f','')),
 'space_a': c('linear-gradient(180deg,#f3fbf7,#ffffff)', ab(36,48,'color:#0b6e4f;font-weight:700;font-size:13px;letter-spacing:5px','GLOW SKIN STUDIO')
   + ab(34,96,'color:#083d2c;font-weight:900;font-size:58px;line-height:.95;letter-spacing:-2px','Skin that<br>glows.')
   + ab(36,250,'color:#41594f;font-weight:500;font-size:17px;line-height:1.75','Facials · Brows · Lashes<br>Nails · Massage')
   + ab(36,370,'width:60px;height:3px;background:#0b6e4f','')
   + ab(36,396,'color:#083d2c;font-weight:900;font-size:19px','Book: 000 000 0000')
   + ab(36,428,'color:#41594f;font-weight:500;font-size:15px','East Legon, Accra')),
 'deco_b': c('#14213d', ''.join(ab(x,y,f'width:{s}px;height:{s}px;border-radius:50%;border:3px solid {col}','') for x,y,s,col in [(260,20,90,'#fca311'),(20,300,60,'#e5e5e5'),(300,330,110,'#fca311'),(150,170,40,'#e63946')])
   + ab(30,40,'color:#fca311;font-size:40px','★ ★ ★') + ab(250,250,'color:#e63946;font-size:34px','✦')
   + ab(30,110,'color:#fff;font-weight:900;font-size:44px;line-height:1;text-shadow:3px 3px 0 #e63946','Kojo Fit<br>Gym')
   + ab(30,230,'width:200px;height:4px;background:repeating-linear-gradient(90deg,#fca311 0 10px,transparent 10px 18px)','')
   + ab(30,260,'color:#e5e5e5;font-weight:500;font-size:17px','Join today. First week free.')
   + ab(30,440,'color:#fca311;font-weight:700;font-size:16px','000 000 0000')),
 'deco_a': c('linear-gradient(165deg,#14213d,#0a1022)', ab(34,46,'color:#fca311;font-weight:700;font-size:13px;letter-spacing:5px','KOJO FIT GYM · SPINTEX')
   + ab(32,90,'color:#fff;font-weight:900;font-size:64px;line-height:.92;letter-spacing:-2px','First<br>week<br><span style="color:#fca311">free.</span>')
   + ab(46,300,'width:3px;height:110px;background:#fca311','')
   + ab(32,420,'background:#fca311;color:#14213d;font-weight:900;font-size:16px;padding:11px 20px;border-radius:30px','Join: 000 000 0000')),
 'idea_b': c('#ffffff', ab(30,40,'color:#333;font-weight:700;font-size:34px','Fresh Juice')
   + ab(30,90,'color:#666;font-weight:400;font-size:17px;line-height:1.5','We sell orange, pineapple,<br>watermelon and mixed juice.')
   + ab(30,180,'width:340px;height:170px;border-radius:12px;background:#eee;display:flex;align-items:center;justify-content:center;color:#aaa;font-size:16px','[ photo of juice ]')
   + ab(30,380,'color:#333;font-weight:700;font-size:18px','GH₵ 15 per bottle')
   + ab(30,430,'color:#666;font-size:16px','Call 000 000 0000')),
 'idea_a': c('linear-gradient(170deg,#ff9f1c,#f77f00)', ab(150,140,'width:420px;height:420px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#ffd166,#fcbf49 60%,#f4a000);box-shadow:inset -20px -20px 60px rgba(0,0,0,.15)','')
   + ''.join(ab(360,350,f'width:180px;height:4px;background:rgba(255,255,255,.55);transform-origin:0 0;transform:rotate({a}deg)','') for a in range(150,260,20))
   + ab(30,40,'color:#fff;font-weight:700;font-size:13px;letter-spacing:5px','SUNNY JUICE BAR')
   + ab(26,74,'color:#fff;font-weight:900;font-size:64px;line-height:.9;letter-spacing:-2px','Squeeze<br>the day.')
   + ab(30,420,'background:#fff;color:#f77f00;font-weight:900;font-size:16px;padding:11px 20px;border-radius:30px','GH₵ 15 · 000 000 0000')),
}
RULES = [
 ('If everything shouts,', 'nothing is heard', 'Stop trying to make every element pop. One hero, everything else supports it.', 'loud'),
 ('Good type beats', 'fancy graphics', 'Bad type kills great ideas. Great type can carry a simple one.', 'type'),
 ('Space is not', 'empty space', 'If your design feels empty or cramped, your spacing is the problem, not the content.', 'space'),
 ('Design for attention,', 'not decoration', "If it doesn't guide the eye or add meaning, take it out.", 'deco'),
 ('Idea first,', 'style later', 'A weak idea cannot be saved by colours, effects or mockups.', 'idea'),
]

def rule(i, a, b, sub, k):
    cards = ''
    for j, (lab, key, col) in enumerate([('BEFORE', k + '_b', 'rgba(255,255,255,.55)'), ('AFTER', k + '_a', G)]):
        x = 110 + j * 460
        cards += f'<div class="tag" style="left:{x}px;top:600px;color:{col}">{lab}</div><div class="card" style="left:{x}px;top:640px;{"outline:3px solid " + G + ";outline-offset:6px" if j else ""}">{MOCK[key]}</div>'
    return page(f'''<div class="a" style="left:90px;top:236px;right:90px">
 <div style="font-weight:900;font-size:68px;line-height:1.04;letter-spacing:-2px">{a}<br><span class="g">{b}</span>{DOT}</div>
 <div style="font-weight:400;font-size:30px;line-height:1.4;margin-top:26px;color:#dfe5f1;max-width:860px">{sub}</div></div>{cards}''', n=i)

slides = []
slides.append(page(f'''<div class="a" style="left:470px;top:560px;width:520px;height:520px;border-radius:50%;background:{G}"></div>
<img class="a" src="{PEN}" style="left:520px;top:300px;width:560px;filter:grayscale(1) contrast(1.15) drop-shadow(0 40px 50px rgba(0,0,0,.5))">
<div class="a" style="left:78px;top:200px;font-weight:900;font-size:560px;line-height:.8;letter-spacing:-20px;color:{G}">5</div>
<div class="a" style="left:430px;top:236px;font-weight:900;font-size:92px;line-height:.98;letter-spacing:-3px;color:{G}">Design<br>Rules</div>
<div class="a" style="left:432px;top:430px;font-weight:400;font-size:78px;line-height:1;letter-spacing:-2px">I never<br>break{DOT}</div>
<div class="a" style="left:90px;top:1060px;font-weight:700;font-size:20px;letter-spacing:6px;color:{G}">DESIGN TIP 06</div>''', swipe=True))
for i, r in enumerate(RULES, 1): slides.append(rule(i, *r))
slides.append(page(f'''<div class="a" style="left:120px;top:470px;right:120px">
 <div style="font-weight:900;font-size:76px;line-height:1.08;letter-spacing:-2px"><span class="g">Break these rules</span><br><span style="font-weight:400">only when you<br>understand them{DOT}</span></div>
 <div style="font-weight:500;font-size:26px;line-height:1.5;margin-top:44px;color:#dfe5f1">Save this for your next design.<br>Need a designer who follows them? <b class="g">+233 (0)50 332 0548</b></div></div>''', swipe=False))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for i, h in enumerate(slides, 1):
        t = f'/tmp/_rule{i}.html'; open(t, 'w').write(h)
        pg.goto(pathlib.Path(t).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(250)
        pg.screenshot(path='/tmp/_r.png')
        im = Image.open('/tmp/_r.png').convert('RGB'); im.save(f'{OUT}/{i:02d}.jpg', quality=93, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/{i:02d}-1080.jpg', quality=93)
    b.close()
print('ok', len(slides))
