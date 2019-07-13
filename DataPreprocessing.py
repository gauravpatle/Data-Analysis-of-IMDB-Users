#import the data set (u_item_cleaned.txt -> it is u.item file  converted  from '|' to TAB delimited)

import pandas as pd
data=pd.read_csv('u_item_cleaned.txt',sep='\t',encoding = 'unicode_escape',header=None)

#extract the encoded genres and name the columns
genre=data.iloc[:,4:23]
genre.columns= ["unknown","Action","Adventure","Animation","Children","Comedy","Crime","Documentary","Drama","Fantasy","Film_Noir","Horror","Musical","Mystery","Romance","Sci_Fi","Thriller","War","Western"]

#iterate over the encoded genres
res=""
data_part1=data
genre['GENRE']=""
for index,row in genre.iterrows():
    res=""
    print(index)
    if(row['unknown']==1):
        res=res+",unknown"
    if(row['Action']==1):
        res=res+",Action"
    if(row['Adventure']==1):
        res=res+",Adventure"
    if(row['Animation']==1):
        res=res+",Animation"
    if(row['Children']==1):
        res=res+",Children"
    if(row['Comedy']==1):
        res=res+",Comedy"
    if(row['Crime']==1):
        res=res+",Crime"
    if(row['Documentary']==1):
        res=res+",Documentary"
    if(row['Drama']==1):
        res=res+",Drama" 
    if(row['Fantasy']==1):
        res=res+",Fantasy"
    if(row['Film_Noir']==1):
        res=res+",Film_Noir"
    if(row['Horror']==1):
        res=res+",Horror"
    if(row['Musical']==1):
        res=res+",Musical"
    if(row['Mystery']==1):
        res=res+",Mystery"
    if(row['Romance']==1):
        res=res+",Romance"
    if(row['Sci_Fi']==1):
        res=res+",Sci_Fi"
    if(row['Thriller']==1):
        res=res+",Thriller"
    if(row['War']==1):
        res=res+",War"
    if(row['Western']==1):
        res=res+",Western"
    print(res)
    genre.at[index,'GENRE']=res[1:]
    
    
    
    
#Take only first 3 column from u.item
data_part1=data.iloc[:,0:3]

#Take the labeled genres
data_part2=genre.iloc[:,-1]  


#export this concatenated table to CSV
final_genre=pd.concat([data_part1,data_part2],axis=1)

final_genre.to_csv('movie_details.csv',sep='\t',index=None,header=None)
