import json
import os
from datetime import datetime
import pdb

def count_overlapping_substrings(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i+1)
        if i == -1:
            return count
        count += 1


def create_json_set():
    data = {"sett":
            [{"board":"an","count":0},
             {"board":"b","count":0},
             {"board":"d","count":0},
             {"board":"f","count":0},
             {"board":"hb","count":0},
             {"board":"i2p","count":0},
             {"board":"j","count":0},
             {"board":"k","count":0},
             {"board":"l","count":0},
             {"board":"m","count":0},
             {"board":"p","count":0},
             {"board":"ph","count":0},
             {"board":"prn","count":0},
             {"board":"psy","count":0},
             {"board":"s","count":0},
             {"board":"wr","count":0},
             {"board":"z","count":0}]
            }

    with open('sett.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def get_post_info(path, msg_index):
#def get_post_info(path):
    with open(path + '0.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    #info_list = []
    try:
        sun = data_json['threads'][0]['posts'][0]['sub']
    except KeyError:
        sun = 'Subject not set!'
    
    try:
        msg = data_json['threads'][0]['posts'][msg_index]['com']
    except KeyError:
        msg = 'Message not set!'

    time_post = datetime.utcfromtimestamp(data_json['threads'][0]['posts'][0]['time']).strftime('%Y-%m-%d %H:%M:%S')
    print('--- POST INFO --- ')    
    print('sub: ', sun)
    print('Last post: ',msg)
    #timeboard set MSK, add localtile machime for bot
    print(time_post)
    print('--- --- --- --- ---')    
    print('')


def read_0(path):
    with open(path + '0.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)
    
    try:
        s_temp = str(data_json['threads'][0]['posts'])
        count_no = count_overlapping_substrings(s_temp, "'no'")        
        no_dict = []

        for i in range(count_no):
            no_dict.append(data_json['threads'][0]['posts'][i]['no'])
            #[24, 28, 35, 64, 65, 66]
            #first = tread, last = allert
        return(no_dict)

    except TypeError:
        no_dict = []
    
    return(no_dict)


def get_dir_list(path):
    elem = os.listdir(path)
    res_list_dir = []
    
    for i in elem:
        if os.path.isdir(os.path.join(path, i)):
            res_list_dir.append(i)

    return(res_list_dir)


def allert():
    path = '/home/s300/PythonSource/tg_borda_alert/borda/'
    global sett_count_board

    with open('sett.json', 'r') as file:
        sett_json = json.load(file)
    
    #for debug
    print('All board list = ', get_dir_list(path))
    print('')

    for borda in get_dir_list(path): 
        allmes= read_0(path + borda + '/')
        print('### Curelt board = ',borda,'###')
        print('')
     
        try:            
            tread = allmes[0]
            last_mess = allmes[-1]

            #get cont messages in sett_json
            for borda_sett in range(len(sett_json['sett'])):
                #print ('DEBUG:', borda_sett)
                
                if borda == sett_json['sett'][borda_sett]['board']:
                    sett_count_board = sett_json['sett'][borda_sett]['count']
                    print('borda found ', borda, '(Number in list = ', borda_sett,') = count in sett file', sett_count_board)
                    
                    if last_mess > sett_count_board:
                        print('Board ',borda,' - has messages = ' , read_0(path + borda + '/'))
                        print('After processing - [TreadIndex=', tread, 'LastMess=',last_mess)
                        print('LastMessIndex =', read_0(path + borda + '/').index(last_mess))
                        print('A new message has been detected! Count = ', sett_count_board)
                        # pdb.set_trace()
                        get_post_info(path + borda + '/', read_0(path + borda + '/').index(last_mess))
                        print('')
                        print('')

                        #update new count
                        sett_json['sett'][borda_sett]['count'] = last_mess

                        with open('sett.json', 'w', encoding='utf-8') as file:
                              json.dump(sett_json, file, indent=2)

        except IndexError:
            print('Shit happened! Fuck!')
            continue


#-----
allert()
