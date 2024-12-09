const jsonServer = require("json-server"); 
const server = jsonServer.create();
const router = jsonServer.router("adjudicaciones_fixed.json"); 
const middlewares = jsonserver.defaults(); 
const port = process. env.PORT || 361; 

server.use(middlewares); 
server.use(router);

server. listen(port);