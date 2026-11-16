import re,pathlib
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
def logo3d(h,face=('#FFFFFF','#CFE3D5'),side=('#2F7D4E','#0C1F16'),depth=48):
    layers=''.join(f'<path d="{D}" fill="url(#side)" transform="translate({k*.45},{k*.75})"/>' for k in range(depth,0,-1))
    return f'''<svg viewBox="-20 -20 800 300" style="height:{h}px;width:auto;display:block;overflow:visible"><defs>
<linearGradient id="face" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{face[0]}"/><stop offset=".55" stop-color="{face[0]}"/><stop offset="1" stop-color="{face[1]}"/></linearGradient>
<linearGradient id="side" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{side[0]}"/><stop offset="1" stop-color="{side[1]}"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="28" stdDeviation="18" flood-color="#000" flood-opacity=".8"/></filter>
<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".45" stop-color="#fff" stop-opacity=".75"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cp"><path d="{D}"/></clipPath></defs>
<g filter="url(#sh)">{layers}<path d="{D}" fill="url(#face)"/>
<g clip-path="url(#cp)"><rect x="80" y="-40" width="140" height="340" fill="url(#shine)" transform="skewX(-22)"/></g>
<path d="{D}" fill="none" stroke="#fff" stroke-width="2.5" stroke-opacity=".9"/></g></svg>'''
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&display=block">'
grain='<svg style="position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="3" seed="9"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .25"/></feComponentTransfer></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
glow='<div style="position:absolute;left:50%;top:50%;width:60%;height:70%;transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(47,125,78,.35),transparent)"></div>'
def page(w,h,inner): return f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>*{{margin:0;box-sizing:border-box}}</style></head><body style="width:{w}px;height:{h}px"><div style="position:relative;width:{w}px;height:{h}px;background:#050505;overflow:hidden">{glow}{inner}{grain}</div></body></html>'
# YouTube 2560x1440 : logo 3D dans la zone sûre (1546x423 au centre)
pathlib.Path('yt.html').write_text(page(2560,1440,f'''<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:70px">{logo3d(250)}
<div style="font-family:Anton;font-size:110px;line-height:.86;color:#fff;text-transform:uppercase;letter-spacing:.01em">Sunday<br>Five League</div></div>'''))
pathlib.Path('pp.html').write_text(page(1080,1080,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{logo3d(280)}</div>'))
pathlib.Path('solo.html').write_text(page(1600,900,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{logo3d(380)}</div>'))
