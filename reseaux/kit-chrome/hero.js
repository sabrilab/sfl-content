import * as THREE from 'three';
import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
import D from './d.txt?raw';
const W=3200,H=1800;
const r=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true,alpha:true}); r.setClearColor(0x000000,0);
r.setSize(W,H); r.setPixelRatio(1); r.toneMapping=THREE.NoToneMapping; r.outputColorSpace=THREE.SRGBColorSpace;
document.body.appendChild(r.domElement);
const pm=new THREE.PMREMGenerator(r);
function studio(){ const c=document.createElement('canvas'); c.width=2048; c.height=1024; const x=c.getContext('2d');
  const g=x.createLinearGradient(0,0,0,1024); g.addColorStop(0,'#1a1c1e'); g.addColorStop(.3,'#6d7277'); g.addColorStop(.46,'#ffffff'); g.addColorStop(.5,'#f0f2f3'); g.addColorStop(.53,'#16191b'); g.addColorStop(.7,'#0b0f0d'); g.addColorStop(1,'#26332b');
  x.fillStyle=g; x.fillRect(0,0,2048,1024);
  for(const [cx,w] of [[200,60],[520,30],[880,90],[1240,40],[1500,120],[1900,50]]){ x.fillStyle='rgba(0,0,0,.85)'; x.fillRect(cx,380,w,200); }
  x.fillStyle='rgba(156,197,166,.9)'; x.fillRect(1350,560,300,40);
  const t=new THREE.CanvasTexture(c); t.mapping=THREE.EquirectangularReflectionMapping; t.colorSpace=THREE.SRGBColorSpace;
  return pm.fromEquirectangular(t).texture; }
function matcap(kind){ const N=1024,c=document.createElement('canvas'); c.width=c.height=N; const x=c.getContext('2d');
  x.fillStyle='#000'; x.fillRect(0,0,N,N); x.save(); x.beginPath(); x.arc(N/2,N/2,N/2,0,7); x.clip();
  const g=x.createLinearGradient(0,0,0,N);
  if(kind==='chrome'){ g.addColorStop(0,'#2b2f33'); g.addColorStop(.18,'#f4f6f8'); g.addColorStop(.42,'#ffffff'); g.addColorStop(.47,'#8c939a'); g.addColorStop(.5,'#0d0f11'); g.addColorStop(.58,'#3a4046'); g.addColorStop(.8,'#c9ced3'); g.addColorStop(1,'#5b6268'); }
  else { g.addColorStop(0,'#0a2e17'); g.addColorStop(.25,'#2fae5c'); g.addColorStop(.55,'#167a39'); g.addColorStop(.85,'#0b4a22'); g.addColorStop(1,'#04190c'); }
  x.fillStyle=g; x.fillRect(0,0,N,N);
  const rg=x.createRadialGradient(N/2,N/2,N*.3,N/2,N/2,N/2); rg.addColorStop(0,'rgba(0,0,0,0)'); rg.addColorStop(1,kind==='chrome'?'rgba(0,0,0,.45)':'rgba(0,0,0,.6)'); x.fillStyle=rg; x.fillRect(0,0,N,N);
  const hl=(cx,cy,rx,ry,a)=>{ const h=x.createRadialGradient(cx,cy,0,cx,cy,rx); h.addColorStop(0,`rgba(255,255,255,${a})`); h.addColorStop(1,'rgba(255,255,255,0)'); x.save(); x.translate(cx,cy); x.scale(1,ry/rx); x.translate(-cx,-cy); x.fillStyle=h; x.beginPath(); x.arc(cx,cy,rx,0,7); x.fill(); x.restore(); };
  if(kind==='chrome'){ hl(N*.32,N*.28,N*.22,N*.08,.9); hl(N*.7,N*.78,N*.18,N*.05,.5); }
  else { hl(N*.34,N*.27,N*.2,N*.1,.95); hl(N*.62,N*.8,N*.22,N*.06,.35); }
  if(kind==='chrome'){ x.fillStyle='rgba(156,197,166,.35)'; x.fillRect(0,N*.55,N,N*.04); }
  x.restore(); const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; return t; }
function face(kind){ const c=document.createElement('canvas'); c.width=1024; c.height=1024; const x=c.getContext('2d'); const g=x.createLinearGradient(0,0,0,1024);
  if(kind==='chrome'){ g.addColorStop(0,'#5e656b'); g.addColorStop(.12,'#ffffff'); g.addColorStop(.42,'#dfe3e6'); g.addColorStop(.5,'#8a9198'); g.addColorStop(.53,'#1a1d20'); g.addColorStop(.62,'#4a5157'); g.addColorStop(.86,'#e7eaec'); g.addColorStop(1,'#9aa1a7'); }
  else { g.addColorStop(0,'#7be09a'); g.addColorStop(.18,'#3fbf6a'); g.addColorStop(.6,'#1c8f45'); g.addColorStop(1,'#0e5a29'); }
  x.fillStyle=g; x.fillRect(0,0,1024,1024); const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; t.wrapS=t.wrapT=THREE.ClampToEdgeWrapping; t.flipY=false; return t; }
function geo(depth,bt,bs,seg=16){ const svg=new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 735 237"><path d="${D}"/></svg>`);
  const g=new THREE.ExtrudeGeometry(svg.paths.flatMap(p=>SVGLoader.createShapes(p)),{depth,bevelEnabled:true,bevelThickness:bt,bevelSize:bs,bevelSegments:seg,curveSegments:32});
  g.computeBoundingBox(); const bb=g.boundingBox; const uv=g.attributes.uv, pos=g.attributes.position;
  for(let i=0;i<uv.count;i++){ uv.setXY(i,.5,(pos.getY(i)-bb.min.y)/(bb.max.y-bb.min.y)); }
  g.center(); g.rotateX(Math.PI); g.computeVertexNormals(); return g; }
function shot(kind,transp=false){
  const s=new THREE.Scene(); if(!transp) s.background=new THREE.Color(0x020202);
  let g,m;
  if(kind==='chrome'){ s.environment=studio(); g=geo(110,16,10); m=[new THREE.MeshBasicMaterial({map:face('chrome')}),new THREE.MeshMatcapMaterial({matcap:matcap('chrome')})]; }
  else { s.environment=studio(); g=geo(50,36,20,24); m=[new THREE.MeshBasicMaterial({map:face('gonfle')}),new THREE.MeshMatcapMaterial({matcap:matcap('gonfle')})]; }
  const grp=new THREE.Group(); const mesh=new THREE.Mesh(g,m); grp.add(mesh);
  // reflet au sol : copie retournée, assombrie
  const refl=transp?new THREE.Group():new THREE.Mesh(g,m.map(x=>{const y=x.clone(); y.transparent=true; y.opacity=.18; return y;})); refl.scale.y=-1; refl.position.y=-300; grp.add(refl);
  grp.rotation.set(transp?-0.06:-0.16,transp?-0.2:-0.36,transp?0:0.02); s.add(grp); const k=new THREE.DirectionalLight(0xffffff,3); k.position.set(-300,500,900); s.add(k); const rim=new THREE.DirectionalLight(0x9cc5a6,2.5); rim.position.set(700,200,-400); s.add(rim);
  const fade=new THREE.Mesh(new THREE.PlaneGeometry(6000,1400),new THREE.MeshBasicMaterial({color:0x020202,transparent:true,opacity:.55})); fade.position.set(0,-560,60); fade.rotation.x=-0.02; if(!transp) s.add(fade);
  const cam=new THREE.PerspectiveCamera(24,W/H,1,10000); cam.position.set(60,40,1450); cam.lookAt(0,-40,0);
  r.render(s,cam); return r.domElement.toDataURL('image/png'); }
window.__out={chrome:shot('chrome'),gonfle:shot('gonfle'),chromeT:shot('chrome',true),gonfleT:shot('gonfle',true)}; document.body.dataset.ok='1';
