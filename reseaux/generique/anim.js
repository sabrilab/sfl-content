import * as THREE from 'three';
import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
import D from './d.txt?raw';
const W=1280,H=720,FR=120;
const r=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true}); r.setSize(W,H); r.setPixelRatio(1); r.outputColorSpace=THREE.SRGBColorSpace; document.body.appendChild(r.domElement);
function face(sweep){ const c=document.createElement('canvas'); c.width=512; c.height=1024; const x=c.getContext('2d'); const g=x.createLinearGradient(0,0,0,1024);
  g.addColorStop(0,'#5e656b'); g.addColorStop(.12,'#ffffff'); g.addColorStop(.42,'#dfe3e6'); g.addColorStop(.5,'#8a9198'); g.addColorStop(.53,'#1a1d20'); g.addColorStop(.62,'#4a5157'); g.addColorStop(.86,'#e7eaec'); g.addColorStop(1,'#9aa1a7');
  x.fillStyle=g; x.fillRect(0,0,512,1024); const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; t.flipY=false; return t; }
function bandTex(){ const c=document.createElement('canvas'); c.width=1024; c.height=64; const x=c.getContext('2d'); const g=x.createLinearGradient(0,0,1024,0); g.addColorStop(0,'rgba(255,255,255,0)'); g.addColorStop(.47,'rgba(255,255,255,0)'); g.addColorStop(.5,'rgba(255,255,255,1)'); g.addColorStop(.53,'rgba(255,255,255,0)'); g.addColorStop(1,'rgba(255,255,255,0)'); x.fillStyle=g; x.fillRect(0,0,1024,64); const t=new THREE.CanvasTexture(c); t.wrapS=THREE.ClampToEdgeWrapping; return t; }
function lineTex(){ const c=document.createElement('canvas'); c.width=1024; c.height=32; const x=c.getContext('2d'); const g=x.createLinearGradient(0,0,1024,0); g.addColorStop(0,'rgba(255,255,255,0)'); g.addColorStop(.5,'rgba(255,255,255,1)'); g.addColorStop(1,'rgba(255,255,255,0)'); x.fillStyle=g; x.fillRect(0,0,1024,32); const v=x.createLinearGradient(0,0,0,32); return new THREE.CanvasTexture(c); }
function matcap(){ const N=512,c=document.createElement('canvas'); c.width=c.height=N; const x=c.getContext('2d'); x.beginPath(); x.arc(N/2,N/2,N/2,0,7); x.clip();
  const g=x.createLinearGradient(0,0,0,N); g.addColorStop(0,'#2b2f33'); g.addColorStop(.18,'#f4f6f8'); g.addColorStop(.42,'#fff'); g.addColorStop(.47,'#8c939a'); g.addColorStop(.5,'#0d0f11'); g.addColorStop(.58,'#3a4046'); g.addColorStop(.8,'#c9ced3'); g.addColorStop(1,'#5b6268'); x.fillStyle=g; x.fillRect(0,0,N,N);
  const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; return t; }
const svg=new SVGLoader().parse(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 735 237"><path d="${D}"/></svg>`);
const g=new THREE.ExtrudeGeometry(svg.paths.flatMap(p=>SVGLoader.createShapes(p)),{depth:110,bevelEnabled:true,bevelThickness:16,bevelSize:10,bevelSegments:12,curveSegments:24});
g.computeBoundingBox(); const bb=g.boundingBox, uv=g.attributes.uv, pos=g.attributes.position; for(let i=0;i<uv.count;i++) uv.setXY(i,.5,(pos.getY(i)-bb.min.y)/(bb.max.y-bb.min.y));
g.center(); g.rotateX(Math.PI); g.computeVertexNormals();
const s=new THREE.Scene(); s.background=new THREE.Color(0x030303);
const g2=g.clone(); { const p=g2.attributes.position, u=g2.attributes.uv; g2.computeBoundingBox(); const b=g2.boundingBox; for(let i=0;i<u.count;i++) u.setXY(i,(p.getX(i)-b.min.x)/(b.max.x-b.min.x)+(p.getY(i)-b.min.y)/(b.max.y-b.min.y)*0.25,0.5); }
const bt=bandTex(); const shineMat=new THREE.MeshBasicMaterial({map:bt,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false,opacity:0});
const mesh=new THREE.Mesh(g,[new THREE.MeshBasicMaterial({map:face()}),new THREE.MeshMatcapMaterial({matcap:matcap()})]);
const shine=new THREE.Mesh(g2,shineMat); shine.scale.setScalar(1.002); mesh.add(shine); s.add(mesh);
// trait de lumière qui balaie

const streak=new THREE.Mesh(new THREE.PlaneGeometry(2600,5),new THREE.MeshBasicMaterial({map:lineTex(),transparent:true,opacity:0,blending:THREE.AdditiveBlending})); streak.position.z=-80; s.add(streak);
const cam=new THREE.PerspectiveCamera(26,W/H,1,10000);
const ease=t=>1-Math.pow(1-t,3);
const frames=[];
for(let f=0;f<FR;f++){ const t=f/(FR-1);
  const a=ease(Math.min(1,t/0.55));
  mesh.rotation.set(-0.06*(1-a),(-1.25)*(1-a)-0.18*a+0.04*Math.sin(t*3),0);
  cam.position.set(0,0,2600-900*a); cam.lookAt(0,0,0);
  const sw=Math.min(1,Math.max(0,(t-0.5)/0.32)); bt.offset.x=0.75-1.6*sw; shineMat.opacity=sw>0&&sw<1?0.9:0;
  streak.material.opacity=Math.max(0,Math.min(1,(t-0.55)/0.15))*0.7; streak.scale.x=0.2+0.8*Math.min(1,Math.max(0,(t-0.55)/0.2));
  r.render(s,cam); frames.push(r.domElement.toDataURL('image/jpeg',0.92)); }
window.__out=Object.fromEntries(frames.map((v,i)=>['f'+String(i).padStart(3,'0'),v])); document.body.dataset.ok='1';
