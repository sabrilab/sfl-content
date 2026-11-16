import * as THREE from 'three';
import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { mergeVertices } from 'three/examples/jsm/utils/BufferGeometryUtils.js';
import D from './d.txt?raw';
const W=1600,H=900;
const r=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true,alpha:false});
r.setSize(W,H); r.setPixelRatio(1); r.toneMapping=THREE.ACESFilmicToneMapping; r.outputColorSpace=THREE.SRGBColorSpace;
document.body.appendChild(r.domElement);
const pm=new THREE.PMREMGenerator(r);
function geo(depth,bevel,bs){
  const svg=new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 735 237"><path d="${D}"/></svg>`);
  const shapes=svg.paths.flatMap(p=>SVGLoader.createShapes(p));
  const g=new THREE.ExtrudeGeometry(shapes,{depth,bevelEnabled:true,bevelThickness:bevel,bevelSize:bs,bevelSegments:12,curveSegments:24});
  g.center(); g.scale(1,-1,1); g.computeVertexNormals(); return g;
}
function scene(variant){
  const s=new THREE.Scene(); s.background=new THREE.Color(0x050505);
  const env=pm.fromScene(new RoomEnvironment(),0.04).texture; s.environment=env;
  const cam=new THREE.PerspectiveCamera(30,W/H,1,5000); cam.position.set(-110,-120,1000); cam.lookAt(0,0,0);
  let g,m;
  if(variant==='verre'){ g=geo(70,14,8);
    m=new THREE.MeshPhysicalMaterial({color:0xffffff,metalness:0,roughness:0.02,transmission:1,thickness:90,ior:1.7,iridescence:1,iridescenceIOR:2.0,iridescenceThicknessRange:[100,1200],clearcoat:1,dispersion:12,attenuationColor:new THREE.Color(0xf4fbff),attenuationDistance:900,envMapIntensity:2.6,specularIntensity:1});
    for(const [c,x,y] of [[0xff3df2,-500,300],[0x3dd8ff,500,-200],[0xfff1a8,0,600]]){const l=new THREE.PointLight(c,4e5,0,2); l.position.set(x,y,400); s.add(l);}
    const back=new THREE.Mesh(new THREE.PlaneGeometry(3000,1600),new THREE.MeshBasicMaterial({map:stripes()})); back.position.z=-300; s.add(back);
  } else if(variant==='chrome'){ g=geo(80,12,6);
    m=new THREE.MeshPhysicalMaterial({color:0xcfd3d6,metalness:1,roughness:0.22,clearcoat:.4,anisotropy:.9,envMapIntensity:.9});
    s.environment=pm.fromScene(studio(),0).texture;
  } else { g=geo(40,46,30);
    m=new THREE.MeshPhysicalMaterial({color:0x0b6e2c,metalness:0,roughness:0.2,clearcoat:1,clearcoatRoughness:0.02,envMapIntensity:.35});
  }
  const mesh=new THREE.Mesh(g,m); mesh.rotation.set(-0.18,0.32,0.02); s.add(mesh);
  const k=new THREE.DirectionalLight(0xffffff,2.2); k.position.set(-400,600,800); s.add(k);
  const rim=new THREE.DirectionalLight(0x9cc5a6,1.6); rim.position.set(600,-200,-300); s.add(rim);
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(4000,4000),new THREE.ShadowMaterial({opacity:.5}));
  return {s,cam};
}
function studio(){ const sc=new THREE.Scene(); const box=new THREE.Mesh(new THREE.BoxGeometry(10,10,10),new THREE.MeshBasicMaterial({color:0x050505,side:THREE.BackSide})); sc.add(box);
  for(const [x,y,z,w,h,i] of [[0,4.8,0,6,.6,6],[-4.8,1,1,.4,6,3],[4.8,-1,-1,.4,4,2],[0,-2,4.8,8,.3,1.5]]){const p=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({color:new THREE.Color(i,i,i)})); p.position.set(x,y,z); p.lookAt(0,0,0); sc.add(p);} return sc; }
function stripes(){ const c=document.createElement('canvas'); c.width=512;c.height=256; const x=c.getContext('2d'); x.fillStyle='#050505'; x.fillRect(0,0,512,256);
  const gr=x.createRadialGradient(256,128,10,256,128,240); gr.addColorStop(0,'#0f2219'); gr.addColorStop(1,'#050505'); x.fillStyle=gr; x.fillRect(0,0,512,256); x.fillStyle='#e9fff0'; x.font='900 120px sans-serif'; 
  for(let i=0;i<40;i++){x.fillStyle=`rgba(255,255,255,${Math.random()*.08})`; x.fillRect(Math.random()*512,0,1+Math.random()*2,256);} const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; return t; }
const out={};
for(const v of ['verre','chrome','gonfle']){ const {s,cam}=scene(v); r.render(s,cam); out[v]=r.domElement.toDataURL('image/png'); }
window.__out=out; document.body.dataset.ok='1';
