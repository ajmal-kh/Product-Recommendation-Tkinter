

import pandas as pd
from sklearn.decomposition import TruncatedSVD

#read dataset
products = pd.read_csv('dataset.csv')
print(products.head())
ratings = pd.DataFrame(products,columns=['userID','productID','ratings'])

print(ratings.head())

print("Description of the dataset")

print(ratings.info())

print(ratings.shape)

#___sum of ratings
popular = ratings.groupby('productID').sum().reset_index()
print(popular)
#_____first 10 popular
most_popular = pd.DataFrame(popular.sort_values(by = 'ratings', ascending=False).head(10))
print(most_popular)


#____avg of ratings
high_rated = (ratings.groupby('productID').sum() / ratings.groupby('productID').count()).reset_index()
high_rated.drop('userID', axis=1,inplace =True)
#_____first 10 high rated
most_highly_rated = pd.DataFrame(high_rated.sort_values(by = 'ratings', ascending=False).head(10))
print(most_highly_rated)


## _______join with products table to get others features of product
most_pop_products = pd.merge(most_popular, products, how='inner', on=['productID'])
most_pop_products = most_pop_products.drop_duplicates('productID')
print(most_pop_products)

most_highRated_products = pd.merge(most_highly_rated, products, how='inner', on=['productID'])
most_highRated_products = most_highRated_products.drop_duplicates('productID')
print(most_highRated_products)  


#_______Storing top 10 popular products into list with the columns  prodNAME, Price and imageurl
top_10_popular = most_pop_products[['name','prices.amountMax','imageURLs']]
print(top_10_popular)
top_10_popular = top_10_popular.values.tolist()

#_______Storing top 10 high rated products into list with the columns  prodNAME, Price and imageurl
top_10_rated = most_highRated_products[['name','prices.amountMax','imageURLs']]
print(top_10_rated)
top_10_rated = top_10_rated.values.tolist()


from tkinter import *

from PIL import ImageTk, Image
root = Tk()
root.title("Home")
root.geometry("400x300")  
root.configure(background='white')

#_____popular product window
def popularProduct():

    newWindow = Toplevel(root)
    newWindow.configure(background='white')
    # sets the title of the
    # Toplevel widget
    newWindow.title("Popular Products")
  
    # sets the geometry of toplevel
    newWindow.geometry("1280x960")
  
    # A Label widget to show in toplevel
    
  
    # sets the geometry of toplevel
    
    Label(newWindow, text="Top 10 Popular Products", font="Helvetica 15 bold", bg='white', pady=30).grid(row=0,column=1)
    r=3
    c=0
    count=0 
    for prodName, price, imgURL in top_10_popular:
        path = imgURL

        img = Image.open(path)
        img = img.resize((70, 80), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(img)
        label = Label(newWindow, image = photo)
        label.image = photo
        label.grid(row=r-1,column=c)
        
        # 2 img
        # 3 text
        # 4 i
        # 5 t
        # 6 i
        # 7 t
        Label(newWindow, text="%s\nPrice: %d Rs\n\n"%(prodName,price),border=1, bg="white").grid(row=r,column=c)
        count+=1
        c+=1
        if(count%3 == 0):
            r+=2
        if(c>2):
            c=0

#____high rated product window
def highRated():
      
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.configure(background='white')
    # sets the title of the
    # Toplevel widget
    newWindow.title("High rated products")
  
    # sets the geometry of toplevel
    newWindow.geometry("1280x960")
  
    # A Label widget to show in toplevel
    

    Label(newWindow, text="Top 10 High Rated Products", font="Helvetica 15 bold", bg="white", pady=30).grid(row=0,column=1)
    r=3
    c=0
    count=0
    for prodName, price, imgURL in top_10_rated:
        path = imgURL

        img = Image.open(path)
        img = img.resize((70, 80), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(img)
        label = Label(newWindow, image = photo)
        label.image = photo
        label.grid(row=r-1,column=c)
        

        # print(prodId, prodName, price);
        Label(newWindow, text="%s\nPrice: %d Rs\n\n"%(prodName,price),border=1,bg="white").grid(row=r,column=c)
        
        count+=1
        c+=1
        if(count%3 == 0):
            r+=2
        if(c>=3):
            c=0



Label(root, text="Product Recommendation System", bg="white", font='Helvetica 15 bold').pack(pady=30)
btn = Button(root, 
             text ="Click here to see Most Popular Products", 
             command = popularProduct).pack(pady=10)
2
btn1 = Button(root, 
             text ="Click here to see High Rated Products", 
             command = highRated).pack(pady=10)


root.mainloop()


