import sys
import modified_stddraw as stddraw
# import stddraw


for i in range(int(sys.argv[1])):
    stddraw.square(0.3+0.1*i,0.3+0.1*i,0.22)
stddraw.show()