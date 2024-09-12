import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    items = dict(config.items('DEFAULT'))
    for key in items:
        try:
            items[key] = eval(items[key])
        except:
            pass
    return items

if __name__ == '__main__':
    print(get_config())