import typer
import os
app = typer.Typer()

@app.command()
def ls():
    path = os.getcwd()
    files = os.listdir(path)
    for file in files:
    	print(file)
@app.command()
def mkdir():
	folder_name = input("Folder : ")
	os.mkdir(folder_name)
@app.command()
def mkfile(file_name: str):
	file = open(file_name, 'w')
	file.write("")
	file.close()
@app.command()
def delete():
	try:
		file_folder = input("File folder name : ")
		os.remove(file_folder)
	except:
		print("Cannot delete the File-Folder please type --help to see why.")
@app.command()
def echo(word: str):
	print(word)
@app.command()
def write(file: str):
	file_name = open(file, 'r')
	cntnt = file_name.read()
	file_name.close()
	write = open(file, 'w')
	content = input("write >>> ")
	final = cntnt+content
	write.write(final)
	write.close()
@app.command()
def cd(dir: str):
	os.chdir(dir)
@app.command()
def path():
	print(os.getcwd())
if __name__ == "__main__":
    app()

