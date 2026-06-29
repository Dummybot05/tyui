import os, json

tracks = []
# Scan the current directory and all subfolders
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.lower().endswith('.m4a'):
            # Get the path relative to the current folder
            rel_path = os.path.relpath(os.path.join(root, file), '.')
            folder = os.path.dirname(rel_path)
            
            tracks.append({
                'name': file,
                'path': rel_path,
                'folder': folder if folder else 'Root'
            })

# Sort alphabetically by path
tracks.sort(key=lambda x: x['path'])

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f, indent=2)

print(f"Done! Found {len(tracks)} M4A files and saved to tracks.json")
