import sys, urllib.parse, pathlib
from playwright.sync_api import sync_playwright
# usage: render.py out.png key=value ...
out = sys.argv[1]
params = dict(a.split('=', 1) for a in sys.argv[2:])
url = pathlib.Path(__file__).with_name('template.html').resolve().as_uri() + '?' + urllib.parse.urlencode(params)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(url); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(300)
    pg.evaluate('document.fonts.ready')
    pg.screenshot(path=out)
    b.close()
print(out)
