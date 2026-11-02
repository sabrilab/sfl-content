export default {
  root: '/tmp/sflv/coupes', base: './', logLevel: 'warn',
  resolve: { alias: [
    { find: /^three\/examples\/jsm\/(.*)$/, replacement: '/home/user/bola-site/node_modules/three/examples/jsm/$1' },
    { find: /^three$/, replacement: '/home/user/bola-site/node_modules/three/build/three.module.js' },
    { find: /^@\//, replacement: '/home/user/SFL/src/' },
  ] },
  build: { outDir: '/tmp/sflv/coupes/dist', emptyOutDir: true, minify: false },
}
