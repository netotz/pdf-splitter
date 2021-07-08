pip='pip install pyinstaller'

gen64="pyinstaller -F --distpath dist --workpath build -n pdf-splitter-64 pdf-splitter/main.py"
source venv/Scripts/activate
$pip
$gen64

gen32="pyinstaller -F --distpath dist32 --workpath build32 -n pdf-splitter-32 pdf-splitter/main.py"
source venv32/Scripts/activate
$pip
$gen32
