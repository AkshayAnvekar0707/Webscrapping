from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=aa9a72f8-faaf-423f-8f0b-c688f2c24344&as-searchtext=iphone'

uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_bs = bs(page_html,"html.parser")

containers = page_bs.findAll("div", {"class":"_1UoZlX"})
#print(len(containers)) # 24 mobile phone in 1st tab

#print(bs.prettify(containers[0]))
#Prettify beautifies the 1st mobiles html code into readble format
#As the first phone is apple-iphone-se-white-64-gb all its related information html is bought to structure format
#print(bs.prettify(containers[1]))
#So container has data of 24 phones, container[0] means 1st phone data is beautified

# Using only 1 phone data
container = containers[0]
print(container.div.img["alt"])
# this title alt must be written in square bracket

# To find price of product
price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
print(price[0].text) # This line is used to get only the price value which is 42,500

#inoreder to print all price related values
#price = container.findAll("div", {"class":"col col-5-12 _2o7WAb"}) # Give te main div class
#print(price[0].text)

# To find rating of product
rating = container.findAll("div", {"class":"niH0FQ"}) # Given the main div class
print(rating[0].text)
# 4.6 product rating along with 2,527 customers rating and 303 reviews are shown
# Inorder to to get only product rating which is 4.6
rating = container.findAll("div", {"class":"hGSR34"}) # Given the main div class
print(rating[0].text)

# import info in csv file
filename = "Products.csv"
f = open(filename,"w")

headers = "Product_name,Price,Rating\n"
f.write((headers))

# For loop to enter all 24 phone details to file
for x in containers:
    Product_name = x.div.img["alt"]
    price = x.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    Price = price[0].text.strip() # Strip removes unnecessary commas, spacing
    rating = x.findAll("div", {"class":"hGSR34"})
    Rating = rating[0].text
    print(Product_name.replace(",", "|") + "," + Price + "," + Rating + "\n")
    f.write(Product_name.replace(",", "|") + "," + Price + "," + Rating +"\n")
    #print("Product_name : " + Product_name)
    #print("Price :" + Price)
    #print("Rating : " + Rating)
    # We have to change the format inorder to make 3 columns for the info
    #print(Product_name.replace(",", "|") + "," + Price + "," + Rating + "\n")
    #f.write(Product_name.replace(",", "|") + "," + Price + "," + Rating + "\n")

f.close()