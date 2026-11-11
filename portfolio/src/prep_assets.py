"""Builds web-sized assets for the portfolio carousel. Run once; sources are the DANAG STUDIO folder (staged copy)
and the v1 renders (for images kept from v1). Output: src/assets/*.jpg (max 2000px long side)."""
from PIL import Image
import pathlib, sys
Image.MAX_IMAGE_PIXELS = None
U = pathlib.Path('/mnt/user-data/uploads/DANAG STUDIO'); A = pathlib.Path(__file__).parent / 'assets'; V1 = pathlib.Path(sys.argv[1])
T = pathlib.Path('/tmp/claude-tool-results/11cfef29-aa45-5b25-bea0-b998ef2d7b19')
def save(im, name, mx=2000):
    im = im.convert('RGB'); im.thumbnail((mx, mx), Image.LANCZOS); im.save(A / f'{name}.jpg', quality=92, subsampling=0); print(name, im.size)
# kept from v1 (cropped out of the 2160x2700 renders, inset to drop the card edge)
def v1(n, box, name, inset=10):
    x0, y0, x1, y1 = box; save(Image.open(V1 / f'{n}.jpg').crop((x0+inset, y0+inset, x1-inset, y1-inset)), name)
v1('01', (168, 922, 1162, 2442), 'my-horse'); v1('01', (1198, 922, 1990, 1662), 'tf-castle')
v1('02', (1198, 844, 1990, 1626), 'my-wood'); v1('02', (1198, 1662, 1990, 2442), 'my-sand')
v1('05', (168, 870, 1162, 2468), 'tf-left'); v1('05', (1198, 870, 1990, 1652), 'tf-arch')
src = {
 'my-apex': 'Maison Yusif/M.Y. - APEX.png', 'my-blackex': 'Maison Yusif/M.Y. AI PERFUME PHOTOGRAPHS/BLACK EXCELLENCE.webp',
 'my-100k': 'Maison Yusif/M.Y. 100K FOLLOWERS POSTER.png', 'my-dallas': 'Maison Yusif/M.Y. EXHIBITION FLYER.png', 'my-exclyusif': 'Maison Yusif/M.Y. EXCLYUSIF.png',
 'ss-086': 'Scent and Spice/SNSXGB 086.png', 'ss-076': 'Scent and Spice/SNSXGB 076.png', 'ss-084': 'Scent and Spice/SNSXGB 084.png', 'ss-080': 'Scent and Spice/SNSXGB 080.png',
 'tf-wig': 'Treadfix/WRAPPED IN GRATITUDE/BLUE/W.I.G. FRONT SHOT 2.png',
 'wk-011': 'MY PERSONAL PROJECTS/WarriorKing Watches/WK WATCHES 011.png', 'wk-015': 'MY PERSONAL PROJECTS/WarriorKing Watches/WK WATCHES 015.png', 'cmw-13': 'MY PERSONAL PROJECTS/CAVEMAN WATCHES/CMW 13.png',
 'fl-wss': "Women's Program Design.png", 'fl-jehovah': 'MY PERSONAL PROJECTS/Jehovah Is My Friend Provisions & Cold Store Design.png',
 'fl-signature': 'SIGNATURE 3.png', 'fl-wealth': 'GLOBAL CARTEL/WEALTH CREATORS FLYER DESIGN.jpg',
 'pk-tombrown': 'MY PERSONAL PROJECTS/The Most Wanted Tombrown.png', 'pk-tombrown2': 'MY PERSONAL PROJECTS/The Most Wanted Tombrown 2.png', 'pk-jeksal': 'Ms. Adeline/Ms. Adel.png',
 'lg-bea': 'Ms. Lawson/BEA ROYALE 3D LOGO 2.png', 'lg-gc': 'GLOBAL CARTEL/GLOBAL CARTEL LOGO (3).jpg',
 'lg-ayara1': 'Ayara Launch Post Slides/SLIDE 10.png', 'lg-ayara2': 'Ayara Launch Post Slides/SLIDE 15.png',
}
for k, v in src.items(): save(Image.open(U / v), k, 3000 if k == 'pk-tombrown' else 2000)
# website screenshots (cloud browser, 1440x900 desktop / 500x992 mobile); trim the scrollbar
def shot(f, name, box): save(Image.open(T / f).crop(box), name)
shot('mcp-remote-browser-blob-1794376464168-6emhdj-803d697e.png', 'web-ss-desktop', (0, 0, 1370, 868))
shot('mcp-remote-browser-blob-1794376443179-3h914g-4abf520c.png', 'web-cc-desktop', (8, 8, 1366, 868))
shot('mcp-remote-browser-blob-1794376500423-83ozq6-ac4199fc.png', 'web-ss-mobile', (0, 0, 484, 992))
shot('mcp-remote-browser-blob-1794376487827-uo3fy9-a673cec1.png', 'web-cc-mobile', (8, 8, 476, 992))
