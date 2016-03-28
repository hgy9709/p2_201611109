
# coding: utf-8

# In[1]:

mydir = get_ipython().magic(u'pwd')


# In[2]:

mydir


# In[3]:

import os


# In[4]:

myplantdir=os.path.join(mydir,'lib')


# In[5]:

myplantdir


# In[6]:

get_ipython().magic(u'cd {myplantdir}')


# In[7]:

mydot="C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"


# In[8]:

import glob


# In[9]:

get_ipython().magic(u'cd {myplantdir}')


# In[10]:

glob.glob(r'./*.jar')


# In[11]:

import os


# In[12]:

os.environ['GRAPHVIZ_DOT']=mydot


# In[13]:

print os.environ['GRAPHVIZ_DOT']


# In[14]:

get_ipython().system(u'java -jar {myplantdir}/plantuml.jar -testdot')


# In[18]:

get_ipython().magic(u'install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py')


# In[16]:

get_ipython().magic(u'load_ext plantuml_magics')


# In[17]:

get_ipython().run_cell_magic(u'plantuml', u'', u'@startuml\nstart\n\n:fd 100;\n:right 90;\n:fd 100;\n:right 90;\n:fd 100;\n:right 90;\n:fd 100;\n:right 90;\nstop\n@enduml')


# In[ ]:




# In[ ]:




# In[ ]:



