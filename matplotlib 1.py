"""import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([0,6])
ypoints=np.array([0,250])

plt.plot(xpoints,ypoints)

plt.show()
"""
'''
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints,)
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])

plt.plot(ypoints)
plt.show()

'''

'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])

plt.plot(ypoints, marker= 'o')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])

plt.plot(ypoints, marker= '*')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])

plt.plot(ypoints, marker= 'h')
plt.show()

'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])

plt.plot(ypoints, marker= 'd')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o:r')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o-.b')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o-.c')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o:y')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o-.b', ms =20)

plt.show()
'''
'''

import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o-.b', ms =20, mec='r')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
 
ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints, 'o-.b', ms =20, mec='r', mfc='y')

plt.show()
'''
'''

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints,linestyle='--')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints,ls=':',color='b')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints,ls=':',color='red')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10,7,15,8,7])
plt.plot(ypoints,linewidth=15)
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
y1=np.array([3,8,1,10,7,15,8,7])
y2=np.array([2,4,6,3,7,4,6,3,8])

plt.plot(y1)
plt.plot(y2)
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([1,4,9,16])
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([1,4,9,16])
plt.plot(x,y)
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

'''