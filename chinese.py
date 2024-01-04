#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('python -m venv myenv')


# In[2]:


get_ipython().system('myenv\\Scripts\\activate')


# In[18]:


get_ipython().system('pip install pandas googletrans==4.0.0-rc1')


# In[29]:


import pandas as pd
from googletrans import Translator
from googletrans import LANGUAGES
import time


# In[20]:


pip install translate


# In[21]:


pip install openpyxl


# In[27]:


import pandas as pd
from googletrans import Translator

# Start time for performance measurement
start_time = time.time()

def translate_column(column):
    translator = Translator()
    translated_column = []

    for text in column:
        if isinstance(text, str) and text.strip(): 
            try:
                translated_text = translator.translate(str(text), src='zh-cn', dest='en').text
                translated_column.append(translated_text)
            except Exception as e:
                print(f"Error translating: {text}. Error: {e}")
                translated_column.append(None)
        elif isinstance(text, (int, float)):
            translated_column.append(text)
        else:
            translated_column.append(None)

    return translated_column

def translate_dataframe(dataframe):
    translated_dataframe = pd.DataFrame()

    for column in dataframe.columns:
        translated_column_name = translate_column([column])[0]
        translated_column_name = translated_column_name if translated_column_name is not None else column
        translated_dataframe[translated_column_name + '_translated'] = translate_column(dataframe[column])

    return translated_dataframe

if __name__ == "__main__":
    # Replace 'Order Export.xls' with your actual file path
    file_path = 'C:/Users/Dell/chinese/Order Export.xls'
    data = pd.read_excel(file_path)

    data_translated = translate_dataframe(data)

    # Save the translated DataFrame to a new Excel file
    data_translated.to_excel('C:/Users/Dell/chinese/Order final.xls', index=False, engine='openpyxl')

    
    # End time and calculate duration
    end_time = time.time()
    duration = end_time - start_time

# Print the time taken for translation and saving
print(f"Translation and saving completed in {duration:.2f} seconds.")


# In[ ]:





# In[23]:


df


# In[15]:


df.info


# In[33]:


data_translated 


# In[ ]:




