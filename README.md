# Inventory-Autoupdate

ENGLISH

# Initial idea
This program was made to help streamline the inventory update process of my friend's small bussiness. This process consisted of manually searching the product code in the distributor's webpage, entering the price found (buying price) into the Google Sheets spreadsheet and then adding the extra value (sell price). As the amount of products is generally around 400, this became a very time consuming task to do by hand once a week (13 hours if we count 2 minutes per product).

# Maintenance
To keep this program working the Chrome webdriver needs to be re-downloaded to the current Chrome version as it updates.

# Why I chose this technology
The reason why I chose Selenium for this program is it's ease of use y how practical it makes the DOM manipulation.

# How it works
I started by connecting Chrome's webdriver to the distributor's page and entering the username and password storaged as an environment variable in my computer to login. Then I used the Google Sheets API to access the spreadsheet where the products data is stored.
The API takes the product's code and introduces it into the web page's search field through Selenium. Taking into account that sometimes products are deleted from the distributor's page I decided to create a try catch block to avoid the progam from stopping in case the price cannot be found, however it does not delete the product from the spreadsheet as many times this products get back on the page after some weeks. If the product exists then it extracts it's price and enters it into the spreadsheet, if it's not found then a 0 is entered as price.
Once the scraping is done, it starts calculating the sell price of the product, to do this the buying price gets multiplied by the desired number according to the product's original price, and then it's entered into the sales price column. This way, the process is finished in an average of 20 minutes.

ESPAÑOL

# Idea inicial
Este programa fue hecho para ayudar a agilizar el proceso de actualización de inventario del pequeño negocio de mi amiga. Este proceso consistía de buscar manualmente el código del producto en la página web del distribuidor, ingresar el precio encontrado (precio de compra) dentro de la hoja de cálculo de Google Sheets y luego añadir el margen de ganancia (precio de venta). Siendo que la cantidad de productos generalmente rondaba los 400, esto se volvió una tarea que requería mucho tiempo para hacerse a mano una vez por semana (13 horas si contamos 2 minutos por producto).

# Mantenimiento
Para mantener funcionando este programa el webdriver de Chrome debe ser descargado nuevamente con la versión nueva de Chrome cada vez que se actualiza.

# Porqué elegí esta tecnología
La razón por la que elegí Selenium para este programa es su fácilidad de uso y la practicidad con la que permite manipular el DOM de la página.

# Cómo funciona
Comencé por conectar el webdriver de Chrome a la página del distribuidor e ingresando el usuario y contraseña almacenados en una variable de entorno en mi computadora para iniciar sesión. Luego utilicé la API de Google Sheets para acceder a la hoja de cálculo donde se almacenan los datos relevantes a los productos. 
Con la API se toma el código del producto y se introduce con Selenium en el campo de busqueda de la página web. Teniendo en cuenta que a veces los productos son eliminados de la página del distribuidor decidí crear un try catch para evitar que el programa se detenga si no puede encontrarlo, sin embargo no elimina el producto de la hoja de cálculo ya que muchas veces los productos vuelven a aparecer en la página después de algunas semanas. Si el producto existe, extrae su precio y lo ingresa en la hoja de cálculo, si no logra encontrarlo ingresa 0 como precio.
Una vez finalizado el scraping, pasa a calcular el precio de venta que tendrá el producto, para esto el precio de compra se multiplica por el número deseado según el precio original del producto, y se ingresa en la columna de precios de venta. Así se da por terminado el proceso en un promedio de 20 minutos.
