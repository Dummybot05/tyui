import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

class AudioServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # When the website asks for playlist.json, generate it on the fly
        if self.path == '/playlist.json':
            tracks = []
            # Scan all sub-folders for .m4a files
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.lower().endswith('.m4a'):
                        # Create a clean relative path (e.g., Folder/Song.m4a)
                        rel_path = os.path.relpath(os.path.join(root, file), '.')
                        rel_path = rel_path.replace('\\', '/') # Fix for Windows if needed
                        tracks.append(rel_path)
            
            tracks.sort() # Sort alphabetically
            
            # Send the list back to the browser
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(tracks).encode())
        else:
            # For all other requests (like index.html or the actual .m4a files), serve normally
            super().do_GET()

print("Starting M4A Server on port 8080...")
HTTPServer(('', 8080), AudioServer).serve_forever()
