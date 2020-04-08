#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
file = "Resources/purchase_data.csv"
df = pd.read_csv(file)


# In[2]:


unique_SN = df['SN'].value_counts()
unique = unique_SN.count()

df_total_players = pd.DataFrame(
    {"Total Players": [unique]})

df_total_players


# In[3]:


unique_items = df['Item ID'].value_counts()
unique2 = unique_items.count()
price_avg = round(df['Price'].mean(),2)
total_purchases = df['Price'].count()
total_rev = df['Price'].sum()

purchasing_analysis = pd.DataFrame({
    "Number of Unique Items" : [unique2],
    "Average Price" : [price_avg],
    "Number of Purchases" : [total_purchases],
    "Total Revenue" : [total_rev]
})

purchasing_analysis["Average Price"] = purchasing_analysis['Average Price'].map('${:,.2f}'.format)
purchasing_analysis["Total Revenue"] = purchasing_analysis['Total Revenue'].map('${:,.2f}'.format)
purchasing_analysis


# In[4]:


un_gen = df.groupby(['Gender'])
un_sn_gen = un_gen['SN'].nunique()
un_sn_gen_per = un_sn_gen / unique * 100

df_un_sn_gen = pd.DataFrame({
    "Total Count": un_sn_gen,
    "Percentage of Players": un_sn_gen_per
})

df_un_sn_gen.index.name = None

df_un_sn_gen = df_un_sn_gen.sort_values(['Total Count'],ascending=False).style.format({'Percentage of Players':"{:.2f}%"})

df_un_sn_gen


# In[5]:


grouped_gen = df.groupby(['Gender'])

pur_an_gen = pd.DataFrame({
    "Purchase Count": grouped_gen['Purchase ID'].count(),
    "Average Purchase Price": grouped_gen['Price'].mean(),
    "Total Purchase Value": grouped_gen['Price'].sum(),
    "Avg Total Purchase per Person": grouped_gen['Price'].sum()/grouped_gen['SN'].nunique()
})

pur_an_gen = pur_an_gen.style.format({'Average Purchase Price':'${:.2f}',
                                     'Total Purchase Value':'${:.2f}',
                                     'Avg Total Purchase per Person':'${:.2f}'})

pur_an_gen


# In[6]:


bins = [0,9,14,19,24,29,34,39,100]
group_labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']

df['Age Ranges'] = pd.cut(df['Age'], bins, labels=group_labels)

df_bins = df.groupby('Age Ranges')
bins_un = df_bins['SN'].nunique()
bins_pec = bins_un / unique * 100

age_demographics = pd.DataFrame({
    'Total Count': bins_un,
    'Percentage of Players': bins_pec
})

age_demographics.index.name = None

age_demographics = age_demographics.style.format({"Percentage of Players":"{:.2f}%"})

age_demographics


# In[7]:


age_purchase_count = df_bins['SN'].count()
age_ave_purchase_price = df_bins['Price'].mean()
age_total_value = df_bins['Price'].sum()
age_av_total_purchase = df_bins['Price'].sum()/bins_un

pur_an_age = pd.DataFrame({
    "Purchase Count": age_purchase_count,
    "Average Purchase Price": age_ave_purchase_price,
    "Total Purchase Value": age_total_value,
    "Avg Total Purchase per Person": age_av_total_purchase
})

pur_an_age = pur_an_age.style.format({
    "Average Purchase Price": "${:.2f}",
    "Total Purchase Value": "${:.2f}",
    "Avg Total Purchase per Person": "${:.2f}"
})

pur_an_age


# In[8]:


df_sn = df.groupby('SN')

purchase_count = df_sn['SN'].count()
avg_purchase_price = df_sn['Price'].mean()
total_purchase_price = df_sn['Price'].sum()

top_spenders = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Average Purchase Price": avg_purchase_price,
    "Total Purchase Value": total_purchase_price
})

top_spenders = top_spenders.sort_values(['Total Purchase Value'], ascending=False).head()
top_spenders.style.format({
    "Average Purchase Price": "${:.2f}",
    "Total Purchase Value": "${:.2f}"
})


# In[9]:


df_popular = df.groupby(['Item ID','Item Name'])
item_count = df_popular['Price'].count()
total_price = df_popular['Price'].sum()
price_per_item = total_price/item_count

most_popular_items = pd.DataFrame({
    "Purchase Count": item_count,
    "Item Price": price_per_item,
    "Total Purchase Value": total_price
})

formatted_items = most_popular_items.sort_values("Purchase Count", ascending=False).head()
formatted_items.style.format({
    "Item Price": "${:.2f}",
    "Total Purchase Value": "${:.2f}"
})


# In[10]:


most_profitable_items = most_popular_items
format_items = most_profitable_items.sort_values("Total Purchase Value", ascending= False).head()
format_items.style.format({
    "Item Price": "${:.2f}",
    "Total Purchase Value": "${:.2f}"
})

