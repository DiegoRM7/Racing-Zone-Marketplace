# Creator Info:
  * Name: Diego Millan</li>
  * Email: <a href="diego1millan@gmail.com">Diego1millan@gmail.com</a>
  * GitHub repo link: <a href="https://github.com/DiegoRM7/Racing-Zone-Marketplace">Racing-Zone-Marketplace</a>

# Project
<h1 align="center">Racing Zone Marketplace</h1>

### Description:
> Marketplace to post a sports or super car to sell or buy one at the current sellers marketplace to add to your garage. Inspiration was from a game called Gran Turismo where we used to not be able to have a marketplace to sell or trade our cars even when we customized them.

<h1 align="center">MVP :</h1>

### Stack:
  * Python
  * Flask
  * Bootstrap

### **API’s:**
  * Cars data API
  * AFTER MVP: Map data API to view where the car is at when viewing the cars details page

## Feature list / Page’s:
  * Have a page to register an account and another page to login to an existing account.
  
  * Users start with a certain amount of money in order to buy straight from the marketplace if they don’t want to create a car.
  
  * Once bought from the marketplace, money is gone based on the seller's price.
  
  * A create page to create a car post that the user is selling and edit info from the selling stand point.

  * You pick a sports / supercar to create from API: each have a certain amount of hp and weight  
    * Mclaren
    * Lamborghini
    * Ferrari
    * Porsche
    * Mercedes benz
    * etc…
    * F1 car (nobody could buy until they make enough money for it)
  
  * A page that shows the current logged in user’s info (money, name, etc.) and the car that they have in their garage.
  * A marketplace page displaying all the cars that are being sold at the moment.
  * An individual car viewing page where when you click on viewing the car through the user's garage or the marketplace then the user can see all the details of the car and the person selling it.
  * An update page where the user that owns that vehicle can update the info.


### CRUD implementation:
  * Since i need a create version of CRUD all the beginning steps to create a car it need to be in one page and i need to hide all the rest of the details with js jquery to open and close a section of the form with a button to not overwhelm the user with too much pictures or details in one form page.

    * Default from api:
        * Stock Hp
        * Stock Weight
        * Recommended description
  
    * Add on create:
      * Contact info
      * Selling price (would show recommended selling price filled)
      * AFTER MVP: Location: integrate map data api to show where the vehicle is located (views details page).

## Todo's List / Documentation:
  - [x] FE & BE for register page
  - [x] FE & BE for login page
  - [x] connect login/register pages to mySQL DB
  - [x] Add .gitignore file (with only python selected)
  - [x] Update .gitignore file (added Flask to selection)
  - [x] Create FE Home/Dashboard Page (no vehicle data from DB on page)
  - [ ] Create BE Home/Dashboard Page
  - [ ] Create FE Create Listing Page (everything implemented so that it can be populated on the Home page right away)
  - [ ] Create BE for create listing (to connect to Home page)
  - [ ] Create Update Listing page (everything implemented)
  - [ ] Create BE for update listing
  - [ ] Create Account & Garage page FE
  - [ ] Create  BE for Account & Garage
  - [ ] Add bootstrap hover effect to nav links on top right

# Product Backlog Features :
  * Users details page displayed to other users wanting to connect/chat
    * Largest purchase from user
    * Description of user
    * Car brands interests of user
      
  * Another page to view one seller's garage and purchase straight from that page and have a rating on the sellers from a 5 star scale. To access it there would be a button named “sellers garage” on each listing details page.
  
  * You can buy another car with that money or buy mods for it that each give a certain number of hp extra. (have tires that have the same hp just different looks so that we could have a update feature for CRUD still)
    * Tires
    * Supercharger
    * Turbo
    * Tune up

  * Set up a request to trade feature and if the user has cars that have a lower selling price then they can offer money along with the car trade to come to an agreement.

  * Create an “interested” button that can be toggled on and off in the vehicle details page and a list of users that are interested.
    * Later on: Based on the amount of interested users, suggest to the buyer (that doesn’t own the car) that the price could increase by 10% for 1 interested user and 20% for 2 interested users.

  * In order to create a car in the beginning the user starts with a certain amount(i.e 100k) and has to balance how much they buy the car for and what upgrades to put on it.

  * Later on make a page where you could have a catalog of races and a percentage of winning each race depending on the ratio of hp/weight for your vehicle. If a user wins a race (based on randomization on the percentage scale) then the user wins a certain amount of money based on the difficulty.

  * AJAX & Django in the future???
