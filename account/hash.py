'''
회원이 투자금을 입금하기 전 입금 거래 정보를 서버에 등록할 때 계좌번호와 구매량을 해시한다.
'''
hash_table = list([None for i in range(1000)]) #해시 테이블 크기는 0~999

def get_key(data): #데이터를 hash값으로
    return hash(data)

def hash_function(key): #hash값 리턴
    return key % 1000

def save_data_hash_table(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 같은 hash_address가 있는 경우
    if hash_table[hash_address] != None:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
        hash_table[hash_address].append([index_key, value])
        return hash_address 
    else:
        hash_table[hash_address] = [[index_key, value]]
        return hash_address

def get_data_hash_table(data, hash_address):
    index_key = get_key(data)
    if hash_address == hash_function(index_key):
        if hash_table[hash_address] != None:
            for index in range(len(hash_table[hash_address])):
                if hash_table[hash_address][index][0] == index_key:
                    return hash_table[hash_address][index][1]
    else:
        return "invalid data"
