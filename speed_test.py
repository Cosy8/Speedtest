import speedtest

s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()

st = s.results.dict()
print('Ping:\t\t%6.2f ms' % st['ping'])   
print('Download:\t%6.2f mbps' % (st['download'] / 10**6)) 
print('Upload:\t\t%6.2f mbps' % (st['upload'] / 10**6))