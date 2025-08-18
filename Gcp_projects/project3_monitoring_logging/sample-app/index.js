const http = require('http');
const port = process.env.PORT || 8080;
setInterval(()=>console.log('heartbeat ' + new Date().toISOString()),5000);
const server = http.createServer((req,res)=>{
  res.end('ok');
});
server.listen(port,()=>console.log('listening'));
