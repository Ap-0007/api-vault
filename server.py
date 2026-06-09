import http.server
import socketserver
import json
import os

PORT = 8000
ENV_FILES = [
    "/Users/amogh/git_helper/.env",
    "/Users/amogh/gfg/gfg_bot/.env",
    "/Users/amogh/dalal/.env"
]

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/auto-import':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            imported_keys = []
            
            for file_path in ENV_FILES:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r') as f:
                            for line in f:
                                line = line.strip()
                                if not line or line.startswith('#'):
                                    continue
                                
                                if '=' in line:
                                    name, val = line.split('=', 1)
                                    name = name.strip()
                                    val = val.strip()
                                    
                                    # Strip quotes
                                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                                        val = val[1:-1]
                                    
                                    imported_keys.append({
                                        "name": name,
                                        "value": val,
                                        "source": os.path.basename(os.path.dirname(file_path)) + "/" + os.path.basename(file_path)
                                    })
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
            
            self.wfile.write(json.dumps(imported_keys).encode())
            return
        
        # Default behavior: serve static files
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("", PORT), handler_object)
print(f"Server started at http://localhost:{PORT}")
print("Exposing /auto-import endpoint with local .env files")

try:
    my_server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    my_server.server_close()
