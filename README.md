# https-github.com-shalinihari-ProdRecomm
## An e-commerce company has captured a huge market share in many fields, and it sells the products in various categories. To become a major leader in the market because it has to compete with the Market Leaders.
The concept of recommendations has been around since Market Leaders first added “top picks for you” to its website.
A report on personalization from Segment assessed how it impacts shoppers1. Findings show that 40% of consumers have purchased something more expensive than they had originally set out for. Moreover, nearly half (49%) of the shoppers made an impulse purchase after they received a personalized recommendation and a majority (85%) of them were very happy with their decision.
It would be impossible to keep recommendations relevant to each customer in real-time without using a scalable data science model that works well for your business. Data science helps automate customer recommendations to not only make them relevant to each user but also to consider the dynamic changes that occur along the way.
Engagement with Product Recommendations in the e-commerce can generate recommendations unique to each user.
For our Analysis, we have the Data with 30000 reviews on different products are collected.
The steps to be performed for the first task are given below.

    >>  Exploratory data analysis
    >>  Data cleaning
    >>  Text preprocessing
    >>  Feature extraction
    >>  Training a text classification model
    >>  Building a recommendation system
    >>  Improving the recommendations using the sentiment analysis model
    
Collaborative Filtering:
The most popular of all product recommender methods, the collaborative filtering technique relies solely on how other customers and users have previously rated a product they purchased.
Idea: 
    If a person X likes items 1, 2, 3 and Y like 2, 3, 4 then they have similar interests and X should like item 4 and Y should like item 1.
    This makes it one of the most commonly used algorithm and is not dependent on any additional 
information.

Basic assumptions:
    >>  Customers who had similar tastes in the past, will have similar tastes in the future
    >>  Users give ratings to catalog items (implicitly or explicitly)
User-User collaborative filtering
A better approach to this method is to take your large database and learn those ratings from their behavior.
User-User Filter:
    >>  User A rates a product with 4 stars.
    >>  B rates the same product with 4 stars.
    >>  User A then likes a product and gives 5 stars to it.
    >>  B will be recommended the same product that user A has rated with 5 stars since it assumes that user B will also like it.
    >>  …
    
Item-Item Filter:

With the item-to-item personalization method, products within a single user’s profile are interconnected without relying on other shoppers.
For instance, if you previously bought cookware from one brand, you’ll be recommended more cooking items from that same company.

