import matplotlib.pyplot as py
time = ['Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.']
Taipei = [80 ,60 ,70 ,30 ,30 ,40 ,30]
Taichung = [60 ,50 ,30 ,10 ,20 ,10 ,40]
Tainan = [20, 10, 0, 10, 10, 20, 30]
py.plot(time, Taipei,'b', label = 'Taipei')
py.plot(time, Taichung,'r', label = 'Taichung')
py.plot(time, Tainan,'g', label = 'Tainan')
py.legend(loc = 'upper right')
py.title('Probability of raining')
py.xlabel('Day')
py.ylabel('Probability(%)')
py.ylim(0, 100)
py.show()