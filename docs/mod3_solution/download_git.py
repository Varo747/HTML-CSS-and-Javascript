import requests, zipfile, io, os, shutil

repo = "jhu-ep-coursera/fullstack-course4"
branch = "master"
folder = "examples/Lecture25"
output = "Lecture25"

url = f"https://github.com/{repo}/archive/refs/heads/{branch}.zip"
print("Downloading zip file...")
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))

base_path = f"{repo.split('/')[1]}-{branch}/{folder}/"
members = [f for f in z.namelist() if f.startswith(base_path)]

print("Extracting folder...")
z.extractall(members=members)

if os.path.exists(output):
    shutil.rmtree(output)
os.rename(base_path, output)
shutil.rmtree(f"{repo.split('/')[1]}-{branch}")
print(f"✅ Done! Folder '{output}' is ready.")
