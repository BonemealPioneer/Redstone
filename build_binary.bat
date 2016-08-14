@Echo off
cd ./
echo Compiling Redstone as executable binary, please wait...
nuitka --standalone --recurse-all --python-version=2.7 main.py