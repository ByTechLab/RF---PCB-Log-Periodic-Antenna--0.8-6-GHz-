import re
import matplotlib.pyplot as plt
import skrf as rf

FILE1 = r'MEAS_LOG_PERIODIC_COAX_FEED_WITH_CASE.s1p'
FILE2 = r'MEAS_LOG_PERIODIC_COAX_FEED_WITHOUT_CASE.s1p'
FILE3 = r'SIM_LOG_PERIODIC_COAX_FEED_WITH_CASE.s1p'
FILE4 = r'SIM_LOG_PERIODIC_COAX_FEED_WITHOUT_CASE.s1p'
FILE5 = r'SIM_LOG_PERIODIC_SIMPLIFIED_FEED_WITHOUT_CASE.s1p'

for file in [FILE1, FILE2,FILE3,FILE4,FILE5]:
    with open(file, encoding='cp1252') as f:
        for line in f:
            print(line.rstrip())
            if re.search('#', line):
                break
            else:
                pass
    print('\n')

sedat_1 = rf.Network(FILE1)
sedat_2 = rf.Network(FILE2)
sedat_3 = rf.Network(FILE3)
sedat_4 = rf.Network(FILE4)
sedat_5 = rf.Network(FILE5)

# sedat_1.plot_s_db(m=0,n=0) #S11
# sedat_2.plot_s_db(m=0,n=0) #S11
sedat_3.plot_s_db(m=0,n=0,linestyle = '--',linewidth = 3) #S11
sedat_4.plot_s_db(m=0,n=0,linestyle = '--',linewidth = 3) #S11
sedat_5.plot_s_db(m=0,n=0,linestyle = '--',linewidth = 3) #S11

plt.minorticks_on()
plt.grid(visible=True, which='major', color='black', linestyle='-')
plt.grid(visible=True, which='minor', color='grey', linestyle='--')
plt.show()

# sedat_1.plot_s_smith(m=0,n=0) #S11
sedat_2.plot_s_smith(m=0,n=0) #S11
# sedat_3.plot_s_smith(m=0,n=0,linestyle = '--',linewidth = 3) #S11
sedat_4.plot_s_smith(m=0,n=0,linestyle = '--',linewidth = 3) #S11
# sedat_5.plot_s_smith(m=0,n=0,linestyle = '--',linewidth = 3) #S11

plt.minorticks_on()
plt.grid(visible=True, which='major', color='black', linestyle='-')
plt.grid(visible=True, which='minor', color='grey', linestyle='--')
plt.show()



