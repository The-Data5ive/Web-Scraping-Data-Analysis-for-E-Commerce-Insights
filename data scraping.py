#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np



# In[8]:


df = pd.read_csv("books_data.csv")

df.head()


# In[9]:


df = df.dropna(subset=["Product Name", "Price"])
df.shape


# In[10]:


df = df.drop_duplicates(subset=["Product Name"])
df.shape


# In[11]:


# Remove weird characters and convert price to float
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
    .astype(float)
)

df["Price"].head()


# In[12]:


df["Price"].dtype


# In[13]:


df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Rating"].unique()


# In[14]:


df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Rating"].unique()


# In[15]:


Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df["Price"] >= lower_bound) & (df["Price"] <= upper_bound)]
df.shape


# In[16]:


df.to_csv("books_data_cleaned.csv", index=False)

print("Cleaned dataset saved as books_data_cleaned.csv")


# In[26]:


import matplotlib.pyplot as plt


# In[19]:


plt.figure()
plt.hist(df["Price"], bins=20)
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.title("Distribution of Book Prices")
plt.show()


# In[20]:


top_rated = df[df["Rating"] == df["Rating"].max()]

top_rated[["Product Name", "Price", "Rating"]]


# In[21]:


df.sort_values(["Rating", "Price"], ascending=[False, False]).head(10)


# In[31]:


correlation = df["Price"].corr(df["Rating"])
correlation



# In[23]:


plt.figure()
plt.scatter(df["Price"], df["Rating"])
plt.xlabel("Price")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.show()


# In[32]:


# Create price ranges
df["Price Range"] = pd.cut(
    df["Price"],
    bins=[0, 20, 40, 60, 100],
    labels=["Low", "Medium", "High", "Very High"]
)

# Calculate average rating per price range
avg_rating_by_price = df.groupby("Price Range")["Rating"].mean()
avg_rating_by_price


# In[33]:


plt.figure(figsize=(6,4))
avg_rating_by_price.plot(kind="bar", color="skyblue")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.title("Average Rating by Price Range")
plt.ylim(0,5)
plt.show()


# In[34]:


avg_price = df["Price"].mean()
avg_price


# In[35]:


plt.figure()
plt.hist(df["Price"], bins=20, color="lightgreen")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.title("Distribution of Product Prices")
plt.show()



# In[36]:


# Create price ranges
df["Price Range"] = pd.cut(
    df["Price"],
    bins=[0, 20, 40, 60, 100],
    labels=["Low", "Medium", "High", "Very High"]
)

# Average rating per price range
avg_rating_by_price = df.groupby("Price Range")["Rating"].mean()
avg_rating_by_price


# In[37]:


plt.figure(figsize=(6,4))
avg_rating_by_price.plot(kind="bar", color="skyblue")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.title("Average Rating by Price Range")
plt.ylim(0,5)
plt.show()


# In[38]:


# Example if 'Date Added' column existed
# df['Month'] = pd.to_datetime(df['Date Added']).dt.month
# monthly_avg_price = df.groupby('Month')['Price'].mean()
# monthly_avg_price.plot(kind='line')
# plt.title("Average Price by Month")
# plt.show()


# In[39]:


Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]
outliers[["Product Name", "Price"]]


# In[ ]:




