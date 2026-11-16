export default { root:'/tmp/sflv/l3', base:'./', logLevel:'warn',
 resolve:{alias:[{find:/^three\/examples\/jsm\/(.*)$/,replacement:'/home/user/bola-site/node_modules/three/examples/jsm/$1'},{find:/^three$/,replacement:'/home/user/bola-site/node_modules/three/build/three.module.js'}]},
 build:{outDir:'/tmp/sflv/l3/dist',emptyOutDir:true} }
