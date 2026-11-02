# Matières SFL dessinées en code (filtres SVG) : aucune image générée.
import re
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
PAL={'bordeaux':'#5E1A24','bouteille':'#1E3B2C','emeraude':'#0F5A43','olive':'#6B6A34','terre':'#A65A34','pelouse':'#4C7A35','sable':'#EEE6D3','or':'#C9A03A','encre':'#16130F','ciel':'#CFE0FF'}
n=[0]
def uid(): n[0]+=1; return f'u{n[0]}'
def cuir(col,w,h,seed=3):
    i=uid(); return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><filter id="{i}" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="{seed}" result="g"/>
<feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="{seed+7}" result="p"/>
<feComposite in="g" in2="p" operator="arithmetic" k2="0.7" k3="0.5" result="h"/>
<feDiffuseLighting in="h" surfaceScale="2.2" lighting-color="#fff" result="l"><feDistantLight azimuth="235" elevation="58"/></feDiffuseLighting>
<feFlood flood-color="{col}"/><feBlend in2="l" mode="multiply"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<rect width="{w}" height="{h}" filter="url(#{i})"/></svg>'''
def tissu(col,w,h):
    i=uid(); p=uid(); return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><defs><pattern id="{p}" width="3.2" height="3.2" patternUnits="userSpaceOnUse">
<rect width="3.2" height="3.2" fill="#000"/><ellipse cx="0.8" cy="1.6" rx=".65" ry="1.3" fill="#fff"/><ellipse cx="2.4" cy="0" rx=".65" ry="1.3" fill="#fff"/><ellipse cx="2.4" cy="3.2" rx=".65" ry="1.3" fill="#fff"/></pattern>
<filter id="{i}" x="0" y="0" width="100%" height="100%"><feGaussianBlur stdDeviation="0.5" result="b0"/><feColorMatrix in="b0" type="luminanceToAlpha" result="b"/>
<feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="9" result="pl"/><feComposite in="b" in2="pl" operator="arithmetic" k2="1" k3="0.35" result="h"/>
<feDiffuseLighting in="h" surfaceScale="1.3" lighting-color="#fff" result="l"><feDistantLight azimuth="225" elevation="62"/></feDiffuseLighting>
<feFlood flood-color="{col}"/><feBlend in2="l" mode="multiply"/></filter></defs>
<rect width="{w}" height="{h}" fill="url(#{p})" filter="url(#{i})"/></svg>'''
def pelouse(w,h,bands=6):
    i=uid(); st=''.join(f'<rect x="0" y="{k*h/bands}" width="{w}" height="{h/bands}" fill="#fff" opacity="{0.07 if k%2 else 0}"/>' for k in range(bands))
    return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><filter id="{i}" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="0.9 0.06" numOctaves="3" seed="4" result="g"/>
<feDiffuseLighting in="g" surfaceScale="2.4" lighting-color="#fff" result="l"><feDistantLight azimuth="270" elevation="50"/></feDiffuseLighting>
<feFlood flood-color="{PAL['pelouse']}"/><feBlend in2="l" mode="multiply"/></filter><rect width="{w}" height="{h}" filter="url(#{i})"/>{st}</svg>'''
def terre(w,h):
    i=uid(); return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><filter id="{i}" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed="12" result="g"/><feTurbulence type="turbulence" baseFrequency="0.03" numOctaves="3" seed="2" result="t"/>
<feComposite in="g" in2="t" operator="arithmetic" k2="0.6" k3="0.6" result="h"/>
<feDiffuseLighting in="h" surfaceScale="1.6" lighting-color="#fff" result="l"><feDistantLight azimuth="240" elevation="60"/></feDiffuseLighting>
<feFlood flood-color="{PAL['terre']}"/><feBlend in2="l" mode="multiply"/></filter><rect width="{w}" height="{h}" filter="url(#{i})"/></svg>'''
def papier(w,h,col=PAL['sable']):
    i=uid(); return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><filter id="{i}" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="2" seed="5" result="g"/>
<feDiffuseLighting in="g" surfaceScale="0.6" lighting-color="#fff" result="l"><feDistantLight azimuth="235" elevation="70"/></feDiffuseLighting>
<feFlood flood-color="{col}"/><feBlend in2="l" mode="multiply"/></filter><rect width="{w}" height="{h}" filter="url(#{i})"/></svg>'''
def brode(fil,h,ombre=True):
    # le sigle en point satin : hachures fines + relief + contour en point arrière
    i=uid(); p=uid(); m=uid()
    return f'''<svg viewBox="0 0 735 237" style="height:{h};width:auto;display:block;overflow:visible"><defs>
<pattern id="{p}" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-62)"><rect width="7" height="7" fill="{fil}"/><rect width="7" height="1.6" fill="#000" opacity=".28"/><rect y="3.5" width="7" height=".8" fill="#fff" opacity=".18"/></pattern>
<filter id="{i}" x="-10%" y="-20%" width="120%" height="140%"><feGaussianBlur in="SourceAlpha" stdDeviation="5" result="b"/>
<feSpecularLighting in="b" surfaceScale="6" specularConstant=".9" specularExponent="18" lighting-color="#fff" result="s"><feDistantLight azimuth="225" elevation="48"/></feSpecularLighting>
<feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/><feComposite in="SourceGraphic" in2="s2" operator="arithmetic" k2="1" k3=".28" result="lit"/>
{'<feDropShadow dx="3" dy="5" stdDeviation="3" flood-opacity=".55"/>' if ombre else ''}</filter></defs>
<g filter="url(#{i})"><path d="{D}" fill="url(#{p})" stroke="{fil}" stroke-width="7"/><path d="{D}" fill="none" stroke="#000" stroke-opacity=".35" stroke-width="2.2" stroke-dasharray="7 4"/></g></svg>'''
def couture(col='#EEE6D3',inset=6,r=8):
    return f'<div style="position:absolute;inset:{inset}px;border:1.4px dashed {col};border-radius:{r}px;opacity:.75;pointer-events:none"></div>'

# --- Métaux nobles et pierres (V2 gravé)
METAUX={'or':('#F6E3A1','#C9A03A','#8A6A1E','#4A3608'),'argent':('#F4F4F2','#C9CBCC','#8E9194','#3E4144'),'bronze':('#E9B98C','#A86A3C','#6E4120','#3A200E'),'noir':('#5A5A5A','#2A2A2A','#141414','#000000')}
def metal(kind,w,h,r=3):
    a,b,c,d=METAUX[kind]; g=uid(); f=uid()
    return f'''<svg class="tx" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><defs><linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{a}"/><stop offset=".35" stop-color="{b}"/><stop offset=".55" stop-color="{a}"/><stop offset=".8" stop-color="{c}"/><stop offset="1" stop-color="{b}"/></linearGradient>
<filter id="{f}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.004 0.9" numOctaves="2" seed="4" result="n"/>
<feColorMatrix in="n" type="saturate" values="0" result="ng"/><feBlend in="SourceGraphic" in2="ng" mode="soft-light"/></filter></defs>
<rect width="{w}" height="{h}" rx="{r}" fill="url(#{g})" filter="url(#{f})"/>
<rect x=".6" y=".6" width="{w-1.2}" height="{h-1.2}" rx="{r}" fill="none" stroke="{d}" stroke-opacity=".55" stroke-width="1.2"/>
<rect x="1.8" y="1.8" width="{w-3.6}" height="{h-3.6}" rx="{max(r-1,0)}" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width=".6"/></svg>'''
def grave(txt,kind,size,stretch=110,weight=900,family='Archivo',italic=False,anchor='start'):
    # lettre gravée : creux sombre + lèvre claire décalée vers le bas
    a,b,c,d=METAUX[kind]
    st=f"font-family:{family};font-weight:{weight};font-stretch:{stretch}%;font-size:{size}px;{'font-style:italic;' if italic else ''}text-transform:uppercase;letter-spacing:.02em"
    if family!='Archivo': st=st.replace('text-transform:uppercase;','')
    return f'''<span style="position:relative;display:inline-block;line-height:.9;white-space:nowrap;{st}"><span style="position:absolute;left:0;top:.06em;color:{a};opacity:.9">{txt}</span><span style="position:relative;color:{d};text-shadow:0 -.03em 0 {d}aa">{txt}</span></span>'''
def pierre(kind,s):
    col={'rubis':('#FF6B7A','#B3122E','#4A0510'),'saphir':('#7FB2FF','#1F4FC9','#08174A'),'emeraude':('#7FE0B0','#0F7A4E','#03301E'),'diamant':('#FFFFFF','#CFE3EE','#7C93A3')}[kind]
    g=uid(); return f'''<svg viewBox="0 0 20 20" style="width:{s}px;height:{s}px;display:inline-block;vertical-align:middle;filter:drop-shadow(0 .6px .8px rgba(0,0,0,.6))"><defs><radialGradient id="{g}" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="{col[0]}"/><stop offset=".45" stop-color="{col[1]}"/><stop offset="1" stop-color="{col[2]}"/></radialGradient></defs>
<circle cx="10" cy="10" r="9.2" fill="#C9A03A"/><circle cx="10" cy="10" r="7.6" fill="url(#{g})"/><path d="M10 2.4 L14 10 L10 17.6 L6 10Z" fill="#fff" opacity=".12"/><ellipse cx="7.4" cy="6.6" rx="2.2" ry="1.3" fill="#fff" opacity=".8" transform="rotate(-30 7.4 6.6)"/></svg>'''
