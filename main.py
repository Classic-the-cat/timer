import time
def cli():
    while True:
        print('Нажмите Enter чтобы запустить таймер на 10 секунд')
        input()
        time.sleep(10)
        print('10 секунд прошло')

if __name__ == '__main__':
    cli()
