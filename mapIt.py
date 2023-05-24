import webbrowser, sys, pyperclip



if (len(sys.argv) > 1):
    # get address from arg
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)