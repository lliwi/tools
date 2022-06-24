#update 
sudo apt update && sudo apt upgrade

#go lang
sudo apt install -y golang

echo  "# golang env" >> /home/kali/.zshrc
echo "export GOROOT=/usr/lib/go" >> /home/kali/.zshrc
echo "export GOPATH=$HOME/go" >> /home/kali/.zshrc
echo "export PATH=$GOPATH/bin:$GOROOT/bin:$PATH" >> /home/kali/.zshrc

source /home/kali/.zshrc

#CarbonCopyexport GOROOT=/usr/lib/go
sudo apt install osslsigncode -y
pip3 install pyopenssl

#impacket
cd /opt/tools/ldap/impacket
pip3 install -r requirements.txt
python3 -m pip install impacket
python3 -m pip install .
sudo python3 setup.py install

#kerbrute
cd /opt/tools/ldap/kerbrute
pip3 install -r requirements.txt
sudo python3 setup.py install

#koroni
cd /opt/tools/mobile/koroni/
chmod +x koroni

#bettercap
/opt/tools/network/bettercap
make build
sudo make install

#sslstript
cd /opt/tools/network/
sudo cp sslstrip /usr/lib/go/src
cd /usr/lib/go/src/sslstrip/cli 
go build main.go

#Vxscan
cd /opt/tools/network/Vxscan
pip3 install -r requirements.txt

#hotspot bypass
sudo apt install sipcalc -y

#gau 
cd /opt/tools/web/gau
go build .
sudo cp gau /usr/bin

#dirsearch
cd /opt/tools/web/dirsearch
pip3 install -r requirements.txt

#gobuster
cd /opt/tools/web/gobuster
go get && go build
sudo cp gobuster /usr/bin/

#httprobe
cd /opt/tools/web/httprobe
go build main.go 
mv main httprobe
sudo cp httprobe /usr/bin

#nuclei
cd /opt/tools/web/nuclei
sudo apt install nuclei















