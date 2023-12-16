# Creator Info:
  * Name: Diego Millan</li>
  * Email: <a href="diego1millan@gmail.com">Diego1millan@gmail.com</a>
  * GitHub repo link: <a href="https://github.com/DiegoRM7/Racing-Zone-Marketplace">Racing-Zone-Marketplace</a>

# Project Name:
<h1 align="center">Racing Zone Marketplace</h1>

### Description:
> Marketplace to post a sports or super car to sell or buy one at the current sellers marketplace to add to your garage. Inspiration was from a game called Gran Turismo where we used to not be able to have a marketplace to sell or trade our cars even when we customized them.

<h1 align="center">MVP :</h1>

### Technology Stack:
  * Python
  * MySQL
  * Flask
  * CSS/HTML
  * Javascript
  * Bootstrap

### **API’s (after MVP):**
  * Cars data API (get universal data about all type of cars that have been made/sold in the US)
  * Map data API (See in what state/country the car is located when viewing details page)

## Feature list / Page’s:
  * Have a page to register an account and another page to login to an existing account.
  * A create page to create a car post that the user is selling and edit info from the selling stand point.
  * A page that shows the current logged in user’s info (money, name, etc.) and the car that they have in their garage.
  * A marketplace page displaying all the cars that are being sold at the moment.
  * An individual car viewing page where when you click on viewing the car through the user's garage or the marketplace then the user can see all the details of the car and the person selling it.
  * An update page where the user that owns that vehicle can update the info.
  
  * (after MVP) Users start with a certain amount of money in order to buy straight from the marketplace if they don’t want to create a car.
  * (after MVP) Once bought from the marketplace, money is gone based on the seller's price.
  * (after MVP) You pick a sports / super car to create from API: each have a certain amount of hp and weight  
    * Mclaren
    * Lamborghini
    * Ferrari
    * Porsche
    * Mercedes benz
    * etc…
    * F1 car (nobody could buy until they make enough money for it)


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
  - [x] Create MVP FE Home/Dashboard Page (no vehicle data from DB on page)
  - [x] Fix FE Home/Dashboard Page spacing between listing cards
  - [x] Create BE Home/Dashboard Page (to connect to DB of saved object cars)
  - [x] Create MVP FE Create Listing Page
  - [x] Create BE for create listing (make sure it can save to database using medium BLOB)
  - [x] Create Account & Garage page FE
  - [x] Set Up a Logout button on account page
  - [x] Create BE for Account & Garage
  - [x] Create Front End for View Listing Page
  - [x] Create Back End for View Listing Page (missing to retrieve image from DB)
  - [x] Update Back End for View Listing Page: the jinja2 if statement to not show edit or delete buttons to people that aren't logged in.
  - [x] Create Front End jinja if statement for purchase button on view listing page (only show if car isn't owned by the viewer)
  - [x] Create Back End for purchase button (move object to user who purchased)
  - [x] Create Validations for all the inputs of creating a listing
  - [x] Create FE Update Listing page (everything implemented)
  - [x] Create BE Update listing page (DB is able to be queried to update)
  - [x] Fix the folder setup for static: individual css & js folders with respective files in them.
  - [x] Fix the linking path to the javascript and css on all html templates.
  - [x] Update car back end controller to be able to save image files. Reference this youtube video https://youtu.be/GQLRVhXnZkE?si=yv3HtOLKAnZzGN5L to get a step by step break down. Includes validations and security.
  - [x] Update car BE controller to retrieve and then show the image files onto the home page.
  - [ ] Update BUG in Account & Garage page BE to make query start with the user data instead of the car data (reversed) so that user data can still show even if they don't have a car in garage.
  - [ ] Update create listing page transmission input on html from a text type into a selection/option type which will have drop down options of either: empty (will throw a flash error), automatic, or manual type.

                        BACKLOG FEATURE'S TODO'S

  - [ ] Create Back End FEATURE for purchase button (alter user's credit amount based on purchase price of car listing)
  - [ ] set up CSS hover feature to not only be set for the class hover-shadow but recreate it to be applied smaller shadows into all tags that include the class btn so that all btn's have a pre-built small shadow on them. Then remove the bootstrap shadow class on btn's, or apply the small shadow on top of the pre-existing bootstrap class "shadow".
  - [ ] Create FE Page for Editing User Profile Data (accessed by the acc/garage page button)
  - [ ] Update FE of Home page to have jinja format the price text to include $$$ sign and comas ,,, after 3 digits
  - [x] Add bootstrap hover-shadow effect just created into all buttons and cards
  - [ ] Figure out how to correctly deploy app into github pages using docker or other deployer(delete the index.html page)(i have a reference video saved on my YT history of examples of this for docker and the other software)
  - [ ] setup sass css or SCSS in the static folder/files

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

### Presentation features that work:
  * User can purchase/move ownership of car listings and then the "amount of vehicles" number in account details with change accordingly.