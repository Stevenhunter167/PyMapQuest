## MapQuest module demo
1. get total distance
2. get total time
3. get step-by-step direction
4. get point of interests near a location


```python
from MapQuest import MapQuest
import time
```


```python
client = MapQuest("Enter your API key") # use your key from MapQuest API key Official Website
```


```python
locations = ['3750 barranca pkwy, Irvine, CA 92606', 
             '4143 Campus Dr, Irvine, CA 92612', 
             '3333 Bristol St, Costa Mesa, CA']

res = client.totalDistance(locations) # get total distance in kilometer
print(res, "km")
```

    10.318 km
    


```python
res = client.totalTime(locations) # get total time in seconds
print(res, 'seconds')
```

    946 seconds
    


```python
locations=['4533 Campus Dr, Irvine, CA',
           '1111 Figueroa St, Los Angeles, CA',
           '3799 S Las Vegas Blvd, Las Vegas, NV']

res = MapQuest("9vZ9zYUCDMtMlMwxcyL9AnewGOV9Q0Gm").directions(locations) # get step-by-step direction in a list

for step in res:
    print(step)
```

    Total Evaluation Time 0.6798205375671387
    Start out going northwest on Campus Dr toward Carlson Ave.
    Turn right onto Jamboree Rd.
    Merge onto I-405/San Diego Fwy.
    Merge onto I-110/Harbor Fwy via EXIT 37A.
    Take the Adams Boulevard exit, EXIT 20C.
    Turn left onto W Adams Blvd.
    Turn right onto ramp.
    Merge onto Figueroa St.
    FIGUEROA STREET.
    Start out going northeast on Figueroa St toward 9th St.
    Turn left onto 8th St.
    Merge onto CA-110/Pasadena Fwy.
    Take the US-101/I-5 exit, EXIT 24A.
    Merge onto US-101/Santa Ana Fwy.
    Stay straight to go onto San Bernardino Fwy.
    Merge onto I-15 E via EXIT 58A toward Barstow/Las Vegas (Crossing into Nevada).
    Merge onto NV-159 via EXIT 41A toward Charleston Blvd East.
    Turn left onto S Las Vegas Blvd.
    S Las Vegas Blvd becomes Las Vegas Blvd N.
    SOUTH LAS VEGAS BOULEVARD.
    


```python
res = client.pointOfInterest('4143 Campus Dr, Irvine, CA 92612', 'gas station', 10) # get all gas stations near 4143 Campus Dr

for result in res:
    print(result)
```

    R & M Pacific Rim Inc, 4601 Campus Dr, Irvine, CA 92612
    CHEVRON #96698, 18002 Culver Dr, Irvine, CA 92612
    ExtraMile, 18002 Culver Dr, Irvine, CA 92612
    Culver Auto Spa, 18011 Culver Dr, Irvine, CA 92612
    Chevron Station, 1240 Bison Ave, Newport Beach, CA 92660
    76, 2690 San Miguel Dr, Newport Beach, CA 92660
    Newport Hills 76, 2690 San Miguel Dr, Newport Beach, CA 92660
    J R Enterprises, 4299 Macarthur Blvd, Newport Beach, CA 92660
    R & M Shell, 3090 Main St, Irvine, CA 92614
    Chevron USA Inc, 2121 SE Bristol St, Newport Beach, CA 92660
    


```python

```
