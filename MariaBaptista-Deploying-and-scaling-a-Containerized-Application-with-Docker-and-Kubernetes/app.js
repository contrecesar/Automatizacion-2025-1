const http = require('http');
const os = require('os');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end(`Hello! This is a Node.js app running in Kubernetes\nHostname: ${os.hostname()}\n`);
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
