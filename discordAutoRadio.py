import pyautogui, time, configparser, sys, os.path, os
config = configparser.ConfigParser()
def pywrite(text):
    time.sleep(0.15)
    pyautogui.write(config.get("discord", "prefix") + text, interval=0.05)
    for i in range(0, 3): pyautogui.press('enter')
def findImage(img): return pyautogui.locateOnScreen(config.get("files", img)) is not None
def fileAsArray(): return open(os.getcwd() + "\\\\" + config.get("files", "list"), "r").read().splitlines()
def doOnceFound(img, func):
    for i in range(0, 50):
        if findImage(img):
            func()
            break
        time.sleep(0.01)
def validateSettings(settingsFile):
    setts = open(settingsFile, "r").read().splitlines()
    return len(setts) == 7 and setts[0] == "[discord]" and "prefix" in setts[1] and "cPlay" in setts[2] and setts[3] == "[files]" and "list" in setts[4] and "img1" in setts[5] and "img2" in setts[6]
def escribirCancion(song): pywrite(config.get("discord", "cPlay") + " " +  song)
def vomitarCanciones(songs):
    for song in songs: doOnceFound("img1", lambda : escribirCancion(song))
def main():
    print("<<< __/\\__ Automatizador hecho por: 'daniT45pro' __/\\__ >>>")
    if len(sys.argv) != 1 or not os.path.isfile(sys.argv[0].split('.')[0] + ".cfg") or not validateSettings(sys.argv[0].split('.')[0]+".cfg"): sys.exit("Archivo de configuracion no valido...")
    config.read(sys.argv[0].split('.')[0] + ".cfg")
    doOnceFound("img1", lambda : doOnceFound("img2", lambda : vomitarCanciones(fileAsArray())))
    print("¿Esto es un adios?")
if __name__ == '__main__': main()
