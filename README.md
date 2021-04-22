# realEstateReporting
This is a repo for sharing info about national real estate market

### How is the data gathered?
Well, it's _borrowed_ from a popular web site for (paid) real estate advertisments.  
I wouldn't share complete python script publicly, since I don't want everybody to make traffic to the website. _Let's be fair to the advertiser._  

### What is the data about?
Data is stored in tab separated format. The dot(.) is a thousands delimiter for price, and decimal delimiter for number of rooms.
Don't be mad for mixture of languages. Take care that there are duplicate ads, some inputs might be missing or misleading - 
i.e. advertisers sometimes put price per square meter instead of total price, there is another example when investors advertise _whole_ builidings 
instead of separate unitsand therefore prices are expressed in millions. 


Address | Area	|Floors	|LastChanged	|Link	|Municipality	|Ogasivac	|Price	|PricePerSpace	|Rooms	|Space|
--------|-------|-------|-------------|-----|-------------|---------|-------|---------------|-------|-----|
Street name and number   |Name of the neighbourhood, sometimes missing   | Storey type, storey(roman)/total numer of storeys(arabic)   |Date of ad creation or update   |Used as ID   |Administrative unit   |Advertiser (investor, agency or owner)   |Total price in EUR  |Price per square meter in EUR   |Number of rooms   |Space in square meters|
Majdanska Čukarica 6   |Banovo brdo   |V/5   |21.04.2021.   |20210421id/novogradnja-penthouse-kod-hipodroma/5425636363796?kid=4   |Opština Čukarica   |Investitor   |298.500   |2.017   |4.0   |148
Vojvode Stepe   |Bioskop Voždovac   |II/2   |07.04.2021.   |20210421id/vozdovac-bioskop-vozdovac-vojvode-stepe-2-5-6/5425636403017?kid=4   |Opština Voždovac   |Agencija   |105.900   |1.629   |2.5   |65


### The .pbix file?

It's a Power BI report - Microsoft tool for data visualisations.  
<a href="https://app.powerbi.com/view?r=eyJrIjoiNDFmZWVmZmYtZDhlNy00ZDljLTljMDAtZGEyOTQxMGUyYTFmIiwidCI6IjI1YTU0OWE5LWZhNGQtNGU3ZS04MGQ2LWQ0NjIzOWQwNmM5OSIsImMiOjl9">
  <img border="0" alt="Online report here" src="https://github.com/iakovpetrovich/realEstateReporting/blob/master/BelgradeRealEstate20210227.png">
</a>
