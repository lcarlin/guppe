from multiprocessing import Pool
import time

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador // 2])
    r2 = pool.apply_async(contagem_regressiva, [contador // 2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Temp em Segundos :-> {fim - inicio}')
    ## Temp em Segundos :-> 1.482658863067627
