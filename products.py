import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續，跳過這一迴
            name, price = line.strip().split(',') # split()結果為清單，分別存入name與price
            products.append([name, price])
    print(products)
    return products


# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if name == 'q':
            break
        price = input('請輸入商品價格： ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products


# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])


# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


# 主程式(進入點)
def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('找到檔案了！')
        products = read_file(filename)
    else:
        print('找不到檔案...')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)


if __name__ == '__main__': # 如果這個檔案是自己執行不是被import，才執行main()
    main()