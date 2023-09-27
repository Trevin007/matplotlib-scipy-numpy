#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib.widgets import Slider


# In[4]:


x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]


# In[5]:


plt.plot(x,y)
plt.show()


# In[43]:


#initial function
x=np.linspace(0,10,30)
y=np.sin(0.5*x)*np.sin(x*np.random.randn(30))

#spine interpolaton
spline=UnivariateSpline(x,y,s=6)
x_spline=np.linspace(0,10,1000)
y_spline=spline(x_spline)

fig=plt.figure()
ax=fig.subplots()
plt.subplots_adjust(bottom=0.25)
p=ax.plot(x,y)
p,=ax.plot(x_spline,y_spline,'g')


axcolor = 'lightgoldenrodyellow'
ax_s = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor=axcolor)
s_fav = Slider(ax_s, 'Smoothing', 0.1, 10.0, valinit=6.0)

# Function to update the spline and plot
def update(val):
    current_v = s_fav.val
    spline = UnivariateSpline(x, y, s=current_v)
    y_spline = spline(x_spline)
    p.set_ydata(y_spline)  # Update the plot data with the new spline
    fig.canvas.draw()

# Attach the update function to the slider's event
s_fav.on_changed(update)

plt.show()
    









plt.show()








# In[ ]:





# In[ ]:




