import json,os
IC=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons.json")))
def contacts(fg,circle,txt,size,phone=True):
    def ic(k): return f'<span style="width:{size}px;height:{size}px;border-radius:50%;background:{circle};display:inline-flex;align-items:center;justify-content:center;flex:none"><svg viewBox="0 0 24 24" width="{int(size*.55)}" height="{int(size*.55)}" style="color:{fg}">{IC[k]}</svg></span>'
    g=lambda ks,t: f'<span style="display:inline-flex;align-items:center;gap:6px">{"".join(ic(k) for k in ks)}<span style="margin-left:6px">{t}</span></span>'
    return f'<div class="ct" style="display:flex;align-items:center;gap:26px;color:{txt}">{g(["IG","TT","X"],"@thedanagstudio")}{g(["SC"],"@realdanag")}{g(["PH"],"+233 (0)50 332 0548") if phone else ""}</div>'
