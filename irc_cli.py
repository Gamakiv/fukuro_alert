import subprocess
import sh
import re

def check_install_ii():
    runer = subprocess.check_output(['apt', 'list', 'ii'])
    match = re.findall(r"\[(.*?)\]", runer.decode('utf-8'))

    if len(match) > 0:
        print(match[0])
        print('ii intall. Ok.')
        return True
    else:
        print('ii not install. Use: apt install ii!')
        return False


def run_ii_client():
    # need run
    # ii -i /tmp -s 127.0.0.1 -p 6668 -n fosa
    # -n = nickname
    if check_install_ii():
        ii_cli_bg = sh.ii("-i" ,"/tmp", "-s", "127.0.0.1", "-p", "6668", "-n", "fosak", _bg=True)


