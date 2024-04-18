---
toc: true
comments: true
layout: post
title: Data Structures Write Up
description: A Write Up for the data structures project
type: tangibles
courses: { compsci: {week: 32} }
---

<br>

### Intro: 

- The CPT project includes implementation of algorithms and data structures. Throughout my project I used algorithms and data structures to create a real estate project. 

- To complete the CPT we had many tools to use such as vscode, github, and our teachers and teammates to help us create this unique project. 

- I use lists, dictionaries, sets, trees, and many more things in my CPT to be able to make the best out of it. Examples may include my data set with the 1100+ houses. 

- Overall, the CPT project helps us align our computer science skills and apply them all together with the abilities and knowledge of others to create something with true meaning and effort. 

- The data structures project helped me learn integrate various projects into one. It helped me collaborate and fix errors with my team and improve my features, overall giving me a good experience throughout this trimester. 


#### Collections:
- In my project, I use a database to manage the limited amount of houses I have in my data set. I can manually delete houses I know have been sold, or edit information about certain houses. I added this feature since these houses were on sale somewhere in December. I used a redfin API to gather the houses, and then a google API to attach an image to each house that matches it. Each house has its own page displaying its image and information such as beds, baths, etc. Each page has the address of the house encoded into the URL using a special key.

<br>

![]({{site.baseurl}}/images/ds.png)

<br>

- Here is the code I used to initialize. The schema includes the price of the house as well as the beds, baths, address, latitute, longitude, square feet, and an image link. The initialization enables all of these attributes, but not all are displayed and available for user use such as lat/long. 

<br>

![]({{site.baseurl}}/images/ds2.png) 

<br>

#### Lists/Dictionaries
- When setting a breakpoint in my type "1" variable I am able to debug and look at my python objects as a list. The list includes: lat, long, beds, baths, sqfeet, etc. 

<br>

![]({{site.baseurl}}/images/ds3.png) 

<br>

- As you can see here, I created two random dictionaries and set breakpoints on them. It paused once It got to those dictionaries where I then stepped over to see the python object, aka the information inside the dictionaries (the keys and the values). 

<br>

![]({{site.baseurl}}/images/ds4.png) 

<br>

#### API's and JSON:
- The post method is used to handle POST requests. It retrieves JSON data from the request body and creates a new House object based on the provided data. It then attempts to add the house to the database and returns the resulting JSON data or an error message.

- The get method is used to handle GET requests. It first prints information about the request (method, type, address, and distance). Then, based on the type parameter provided in the request, it either searches for houses within a specified distance of the given address or retrieves information about a specific house by its address.

- The put method is used to handle PUT requests. It first checks if the user making the request is an admin by verifying the JWT token. If the user is an admin, it updates the details of a house specified by the provided address.

- The delete method is used to handle DELETE requests. Similar to the put method, it checks if the user making the request is an admin. If so, it deletes the house specified by the provided address.

- Combined, these different request methods make up my real estate project. 

<br>


            def post(self):
            body = request.get_json()
            price = body.get("price")
            beds = body.get("beds")
            baths = body.get("baths")
            address = body.get("address")
            lat = body.get("lat")
            long = body.get("long")
            sqfeet = body.get("sqfeet")
            ho = House (price, beds, baths, address, lat, long, sqfeet)
            ''' #2: Key Code block to add user to database '''
            # create player in database
            house = ho.create()
            # success returns json of player
            if house:
                return jsonify(house.read())
            # failure returns error
            return {'message': f'Error'}, 210
        
        def get(self):
            print('GET:', request.method)
            type_value = request.args.get('type')
            address_value = request.args.get('address')
            distance_value = request.args.get('distance')
            print('Type:', type_value)
            print('Address:', address_value)
            print('Distance:', distance_value)
            t = request.args.get('type')
            if t == "1":
                address = request.args.get('address')
                distance = int(request.args.get('distance'))
                json_ready = []
                url = createURL(address)
                response = requests.get(url)
                if response.status_code == 200:
                    response_json = response.json()
                    results = response_json.get('results')
                    if results and len(results) > 0:
                        first_result = results[0]
                        lon = first_result.get('lon')
                        lat = first_result.get('lat')
                        coord = (lat, lon)
                        house = House.query.all()
                        temp = [house.read() for house in house]
                        repeats = set() 
                        for h in temp:
                            hcoord = (h["lat"], h["long"])
                            dist = geodesic(coord, hcoord).miles
                            if dist <= distance and h["address"] not in repeats:
                                repeats.add(h["address"])
                                json_ready.append(h)
                return jsonify(json_ready)
            elif t == "2":
                address = request.args.get('address')
                for house in House.query.all():
                    if house.address == address:
                        return jsonify([house.read()])
                else:
                    return "err"
        
        @token_required
        def put(self):
            token = request.cookies.get("jwt")
            if not token:
                return {
                    "message": "Authentication Token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            try:
                data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                if data["role"] == "Admin":
                    body = request.get_json()
                    address = body.get('address')
                    price = body.get('price')
                    beds = body.get('beds')
                    baths = body.get('baths')
                    sqft = body.get('sqft')
                    houses = House.query.all()
                    for house in houses:
                        if house.address == address:
                            house.update(price = price if price else "", beds = beds if beds else "", baths = baths if baths else "", sqft = sqft if sqft else "")
                            return f"Updated {address}"
                    return f"house not found"
                else: 
                    return {
                    "message": "Not an admin!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "data": None,
                    "error": str(e)
                }, 500
        
        @token_required
        def delete(self):
            token = request.cookies.get("jwt")
            print(token)
            if not token:
                return {
                    "message": "Authentication Token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            try:
                data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                if data["role"] == "Admin":
                    body = request.get_json()
                    print(body)
                    address = body.get('address')
                    houses = House.query.all()
                    count = 1
                    for house in houses:
                        print(house.address,address)
                        if house.address == address:
                            house.delete()
                            count+=1
                            if count == 2:
                                return f"{house.read()} Has been deleted"
                else: 
                    return {
                    "message": "Not an admin!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "data": None,
                    "error": str(e)
                }, 500

<br>

**Postman**:
>- GET Request:
   - URL: Enter the URL of your API endpoint.
   - Method: Select GET.
   - Parameters: Add the required parameters (type, address, distance) as key-value pairs in the Params section.
   - Send the request.
   - 200 Status is returned

<br>

![]({{site.baseurl}}/images/pm.png) 

<br>


>- POST Request:
   - URL: Enter the URL of your API endpoint.
   - Method: Select POST.
   - Body: Select the raw option and choose JSON from the dropdown menu. Then, enter the JSON body with the required fields (price, beds, baths, address, lat, long, sqfeet).
   - Send the request.
   - 200 Status is returned

<br>

![]({{site.baseurl}}/images/pm2.png) 

<br>

- Here's an example of a 400 error due to a mistype or incorrect JSON body format

<br>

![]({{site.baseurl}}/images/pm5.png) 

<br>

- PUT Request:
   - URL: Enter the URL of your API endpoint.
   - Method: Select PUT.
   - Body: Select the raw option and choose JSON from the dropdown menu. Then, enter the JSON body with the fields you want to update (price, beds, baths, sqfeet).
   - Send the request.
   - 200 Status is returned

<br>

![]({{site.baseurl}}/images/pm3.png) 

<br>

>- DELETE Request:
   - URL: Enter the URL of your API endpoint.
   - Method: Select DELETE.
   - Parameters: Add any required parameters, such as the ID of the resource you want to delete.
   - Send the request.
   - 200 Status is returned

<br>

![]({{site.baseurl}}/images/pm4.png) 

<br>

#### Frontend: 
- Here, I send a GET request to find houses on SALE within 2 miles of the inputted address. The image shows the GET request with a 200 SUCCESS. The response tab includes the information output as a JSON object. 

<br>

![]({{site.baseurl}}/images/pm6.png) 

<br>

- Once the GET request is sent, the response tab includes the houses nearby as a JSON object. 

<br>

![]({{site.baseurl}}/images/pm8.png) 

<br>

- Here I sent a PUT request to change the price of the house from 504$ to 800,000$. Once pressed "Update" it sends a PUT request with a 200 SUCCESS. The response includes the address of the house being updated. 

<br>

![]({{site.baseurl}}/images/pm7.png) 

<br>

- This is the javascript fetch being sent and the JSON object seen through the console. It includes the house address, beds, baths, and square feet, as well as additional information not seen in the frontend, yet specific to the house. 

<br>

![]({{site.baseurl}}/images/pm9.png) 

<br>

- Here, this shows how my javascript iterates over the JSON data and formats it into HTML for it to be displayed for the user in the frontend. The table displays that information about the house. 

<br>

![]({{site.baseurl}}/images/pm10.png) 

<br>

- Instead of error handling, the admin has full freedom in entering whatever they'd like into each house. However, if the user isn't admin they will simply not be authorized to change the house's information. 

<br>

![]({{site.baseurl}}/images/pm11.png) 

<br>

- My javascript code shows a 200 success through its data display on the table. The line that specifically results to that is this one. If the fetch and inputted data is succesfully received, the new house information (if using the PUT option) will be updated. 

<br>

resultContainer.innerHTML = JSON.stringify(data);

<br>

#### ML/Extras:

>- Cleaning, Encoding, and One-hot Encoding:
   - In the backend code, the House function reads data from a CSV file, handles missing values with dropna, and converts categorical variables to numerical format using pd.to_numeric.
   - It scales the data using StandardScaler
   - The algorithm then calculates the Euclidean distance between the input data and the dataset to find the top 3 closest matches.

<br>

>- Algorithms and Preparation for Predictions:
   - The frontend provides a form for users to input house details (beds, baths, square feet, and price) and sends this data to the Flask backend via a POST request.
   - Upon receiving the data, the backend processes it using the House function, which predicts the top 3 closest matched houses based on the input features.
   - The predictions are then sent back to the frontend as a JSON response.

<br>

>- Understanding of Linear Regression Algorithms:
   - My code doesn't specifically use linear regression but it uses a similar approach to predict house data based on input features.
   - Linear Regression assumes a linear relationship between independent and dependent variables, but my code uses a distance-based approach instead.

<br>

>- Understanding of Decision Tree Analysis Algorithms:
   - My code doesn't exactly use Decision TRees, but it attempts to find the closest matched house based on the similarities and can be relayed to decision tree concepts, whereas each split in the tree divides the data based on its feature values. 

<br>

    
    haus_api = Blueprint('haus_api', __name__, url_prefix='/api/haus')
api = Api(haus_api)
class HouseAPI:
    class _CRUD(Resource):
        def post(self):
            body = request.get_json()
            square_feet = body.get("sqft")  # Corrected field name
            price = body.get("price")
            beds = body.get("beds")
            baths = body.get("baths")
            result = House(square_feet, price, beds, baths)
            return {'message': result}, 200
    api.add_resource(_CRUD, '/')
def House(sqft, price, beds, baths):
    houseData = pd.read_csv('housesdata.csv')

    newHouse = pd.DataFrame({
        'SQUARE FEET': [sqft],
        'PRICE': [price],
        'BEDS': [beds],
        'BATHS': [baths]
    })
    houseData['SQUARE FEET'] = pd.to_numeric(houseData['SQUARE FEET'], errors='coerce')
    houseData['PRICE'] = pd.to_numeric(houseData['PRICE'], errors='coerce')
    houseData['BEDS'] = pd.to_numeric(houseData['BEDS'], errors='coerce')
    houseData['BATHS'] = pd.to_numeric(houseData['BATHS'], errors='coerce')
    houseData = houseData.dropna(subset=['SQUARE FEET', 'PRICE', 'BEDS', 'BATHS'])
    scaler = StandardScaler()
    houseDataScaled = scaler.fit_transform(houseData[['SQUARE FEET', 'PRICE', 'BEDS', 'BATHS']])
    newHouseScaled = scaler.transform(newHouse)
    distances = np.sqrt(np.sum((houseDataScaled - newHouseScaled)**2, axis=1))
    top3_indices = np.argsort(distances)[:3]
    top3_distances = distances[top3_indices]
    mostSimilar = []
    max_distance = np.max(distances)
    for i in range(3):
        address = houseData.iloc[top3_indices[i]]['ADDRESS']
        closeness = 1 - (top3_distances[i] / max_distance)
        if np.isnan(closeness):
            probability = None
        else:
            probability = closeness  # Using closeness as probability
        mostSimilar.append({'address': address, 'probability': probability})
    return mostSimilar  

<br>

- Here is my frontend view of the ML project
- Once the users inputs the selected data (beds, baths, square feet, price) through my ML model, I provide a relatively close prediction to a house that would match those parameters. The top 3 houses are in order of closeness, and all are inside my built-in data set. 
- This is all handled through a POST request. 

<br>

![]({{site.baseurl}}/images/pm12.png)

<br>















