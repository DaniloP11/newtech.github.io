import sqlite3

#Abrir la base de datos, en caso de que no exista, la crea automaticamente
conn = sqlite3.connect('database.db')

#Crear las tablas users, productskart, categories
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios 
		(userId INTEGER PRIMARY KEY AUTOINCREMENT, 
		nombres TEXT,
		apellidos TEXT,
		celular TEXT,
		email TEXT,
		password TEXT,
        tipoUser TEXT
		)''')

conn.execute('''CREATE TABLE IF NOT EXISTS productos
		(productId INTEGER PRIMARY KEY AUTOINCREMENT,
		nombre TEXT,
		precio REAL,
		descripcion TEXT,
		imagen TEXT,
		cantidad INTEGER,
		categoria TEXT
		)''')
# conn.execute('''DROP TABLE kart''')
conn.execute('''CREATE TABLE IF NOT EXISTS kart
		(kartId INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER,
		productId INTEGER,
		productCantidad INTEGER,
		precio REAL,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE IF NOT EXISTS compras
		(compraId INTEGER PRIMARY KEY AUTOINCREMENT,
        factura TEXT,
        userId INTEGER,
		lista_productos TEXT,
		cantidad_productos TEXT,
        total REAL,
        fecha TEXT,
        direccion TEXT,
        metodo_pago TEXT,
		FOREIGN KEY(userId) REFERENCES users(userId)
		)''')

conn.execute("DELETE FROM compras")
conn.execute("DELETE FROM productos")
conn.execute("DELETE FROM usuarios")
conn.execute("DELETE FROM kart")

conn.execute("INSERT INTO usuarios VALUES(1,'Nombres','Apellidos','3219876540','mail@mail.com','1234','administrador')")
conn.commit()

conn.execute("INSERT INTO productos VALUES(1,'Royal Canin x 2kg Edad +8',259000,'Alimento completo para perros maduros de razas pequeñas','https://www.doggysmarket.com.co/wp-content/uploads/2019/08/ROYAL-CANIN-MINI-ADULT-MATURE-8-2022-NEW.png',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(2,'Hills Adulto Small Paws 4.5lb',89300,'Fácil de digerir diseñada para razas pequeñas y miniatura','https://www.doggysmarket.com.co/wp-content/uploads/2019/06/Hills-Adulto-Raza-Mini-amp-Pequena-De-Cordero-amp-Arroz-2021.png',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(3,'Nupec x2kg raza mediana-grande',61980,'Comida seca, recomendada para perro cachorro.','https://chilax.es/wp-content/uploads/2020/02/NUPEC-CACHORRO.jpeg',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(4,'Diamond Naturals 2.73 Kg',80000,'Para perro cachorro, comida seca para raza grande.','https://i0.wp.com/www.petmall.com.co/wp-content/uploads/2022/04/DIAMOND-NATURALS-PERRO-CACHORRO-RAZA-GRANDE-NEW-2022.png?fit=1080%2C1080&ssl=1',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(5,'Gatsy x 17Kg',180000,'Comida seca para gato adulto sabor: Pescado/Arroz/Espinaca','https://production-img.croper.com/Images/vpmPKN6F-70_oQjCGZegW.jfif',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(6,'DonKat x1 Kg',10200,'Comida seca para gato adulto, buena carga nutricional','https://jumbocolombiaio.vtexassets.com/arquivos/ids/205581/7702084057163.jpg?v=637814200411300000',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(7,'Hills 4 Lb',92400,'Comida seca para gato adulto, 1-6 años','https://www.hillspet.es/content/dam/pim/hills/es_es/sd/dry/sp-feline-science-plan-adult-optimal-care-chicken-dry-productShot_zoom.jpg',100,'laptops')")
conn.execute("INSERT INTO productos VALUES(8,'Monello 1kg',27200,'Sabor: Pollo/Salmón/Cereales integrales/Vegetales','https://www.agrocampo.com.co/media/catalog/product/cache/d51e0dc10c379a6229d70d752fc46d83/_/1/_1_1_111103300.jpg',100,'laptops')")

conn.execute("INSERT INTO productos VALUES(9,'Pechera- arnés',60000,'Acolchada sin correa, costuras reflectantes luminosas','https://cdn.shopify.com/s/files/1/0583/0334/8894/products/10_ef67491d-7c6b-4338-8b9d-d0acc2cb69d0_1024x1024.png?v=1646429804',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(10,'Collares para cachorros',14400,'Elegante collar con Campana, modelo leopardo','https://cf.shopee.com.co/file/sg-11134201-22120-oudi5nruselv23',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(11,'Corbata formal',80000,'>Material cómodo, decorado con lazos, suave y ligero','https://m.media-amazon.com/images/I/61kL4PAIlxL._AC_UF894,1000_QL80_.jpg',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(12,'Chaqueta gruesa',45000,'Abrigos, chaquetas y ropa de abrigo, material: poliester','https://sc04.alicdn.com/kf/H3e65f810637740ea89b824b931a4cdc0s.jpg',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(13,'Gafas de sol',18000,'Redondas, estilo vintage, de reflexion para gatos','https://cf.shopee.com.co/file/53add46a94195654ac0bc0b5d5b9e00f',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(14,'Mochila para mascota',120000,'Bolso transportador de mascotas tipo astronauta','https://exitocol.vtexassets.com/arquivos/ids/7049795/mochila-para-gato-o-perro-bolso-maleta-mascota-rosa-panoramica.jpg?v=637514529573130000',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(15,'Peluca León',45000,'Melena para cosplay de León.','https://http2.mlstatic.com/D_NQ_NP_629097-MCO51813736324_102022-O.jpg',100,'pcescritorio')")
conn.execute("INSERT INTO productos VALUES(16,'Arnés con correa',20900,'Pechera para gatos tipo chaleco.','https://i.linio.com/p/811e6cc2da31c6cf81c87073975372c7-product.jpg',100,'pcescritorio')")

conn.execute("INSERT INTO productos VALUES(17,'Shampoo Petys',20500,'Producto para perros y gatos, protege y cuida el pelo de tus mascotas','https://cdn.shopify.com/s/files/1/1782/2391/products/Shampoo-Limpieza-y-Suavidad-Petys.jpg?v=1618547592',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(18,'Bolfo 20g',6500,'Sobre de polvo antipulgas para perro y gato','https://http2.mlstatic.com/D_NQ_NP_820542-MCO31053309509_062019-O.jpg',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(19,'Toallas humedas x50 Petys',12400,'Paños húmedos extrasuaves','https://lh3.googleusercontent.com/r0-lK6FNByqLk1qhPiQ1aMi3AtAmK02zamr65bKfJ1MPzPzN9EQ6MZYtUo3xZxvpOM2J6GnYW0hURFYrMw8AVyyw6Y0cakwiQ0mYJuxq3kwulEqy=s360',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(20,'Shampoo seco 100g',19900,'Para gatos marca Petra, garanriza limpieza e higiene','https://s.cornershopapp.com/product-images/1132027.jpg?versionId=Ipqq4S1bg9FHP3No5VBuc1m1BTFnt71g',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(21,'Cepillo para perros y gatos',23800,'Producto de plástico para peinar perros cachorros y gatos','https://cf.shopee.com.co/file/31b0e0d075669a355f956702e4d86316',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(22,'Peine para masaje',18200,'Producto masajeador dispensador de shampoo','https://snoki.com/wp-content/uploads/2022/03/152308-4bdc09.jpg',100,'celulares')")
conn.execute("INSERT INTO productos VALUES(23,'Maya de celulares Gatos',21900,'Facilita el baño y previene heridas por rasguños','https://http2.mlstatic.com/D_NQ_NP_897897-MCO48654922803_122021-O.jpg',100,'celulares')")

conn.execute("INSERT INTO productos VALUES(24,'Tengdee',18700,'Juguete para el aburrimiento, para liberar estres','https://m.media-amazon.com/images/I/71-a5KAC0mL._AC_SL1500_.jpg',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(25,'TurnWard',49200,'Juguete giratorio sin relleno. Para cachorros','https://cf.shopee.com.co/file/sg-11134201-22120-t2qljf34zmlv3a',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(26,'Hoopet',24400,'Juguete interactivo, productos para morder.','https://ae01.alicdn.com/kf/HTB1_w_SNNTpK1RjSZFMq6zG_VXae/Hoopet-relojs-interactivos-para-perros-peque-os-y-grandes-productos-para-morder-productos-de-entrenamiento.jpg_Q90.jpg_.webp',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(27,'Pollo chillón',23000,'Al apretar o presionar, emitirá un sonido.','https://www.holospet.cl/wp-content/uploads/2021/08/Pollo-Chillon-1-1.jpg',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(28,'Pez eléctrico',23500,'Con un toque se activará y empezará a mover su cola.','https://cdn.shopify.com/s/files/1/0534/5725/6623/products/juguete-pez-electrico-interactivo-para-gatos-793599_1024x1024_2x_a1e6bdd3-0d13-4361-a145-e58bc04bb160.jpg?v=1653491753',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(29,'Juguete Ratón',13750,'Bonito, pequeño, ligero, divertido. No tóxico.','https://cf.shopee.com.co/file/54b17609284d5fbef567d1c436a30f82',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(30,'Gigwi Ratón interactivo',60400,'Diseño realista con control remoto.','https://m.media-amazon.com/images/I/81F37If9vFL.jpg',100,'relojs')")
conn.execute("INSERT INTO productos VALUES(31,'Serpiente a control remoto',75900,'Con batería recargable integrada.','https://ae01.alicdn.com/kf/HTB1UxdzXWL7gK0jSZFBq6xZZpXat/Juguete-de-serpiente-con-Control-remoto-para-gatos-con-bater-a-recargable-integrada-divertido-juguete-para.jpg',100,'relojs')")

conn.execute("INSERT INTO productos VALUES(32,'Renalof Pets 150ml',84900,'Solución oral, suplemento nutricional, elimina calculos renales','https://shaly.co/wp-content/uploads/2021/08/VECREN001.png',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(33,'Meloxicam 2 mg x10 Tabletas',259000,'Analgésico y antinflamatorio para perros','https://www.agrocampo.com.co/media/catalog/product/cache/d51e0dc10c379a6229d70d752fc46d83/5/3/5353153115311060088-min.jpg',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(34,'Metronid oral 100ml',20100,'Compuesto antiparasitario interno para perros y gatos.','https://www.maximascotas.com.co/img/uploaded/productos/58221236790769.jpg',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(35,'Simparica x Tableta',35500,'Para el tratamiento de las infestaciones por garrapatas.','https://animalsveterinaria.vteximg.com.br/arquivos/ids/156160-1000-1000/HOLSIM004.png?v=638045749541300000',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(36,'Drontal gatos 2 Tabletas',22500,'Antiparasitario interno, protege de Nematodos y cestodos','https://animalstop.com.co/wp-content/uploads/2019/04/DRONTAL-GATO.jpg',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(37,'Drontal Perros x1 Tableta',27500,'Protege de Nematodos y la acumulación de protozoos y cestodos.','https://animalstop.com.co/wp-content/uploads/2019/04/DRONTAL-35KG..jpg',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(38,'MeloxiPet gotas',13000,'Antiinflamatorio no esteroidal, fácil administración, agradable sabor.','https://veterinariaelcountry.com/wp-content/uploads/2022/08/meloxipet-gotas.jpg',100,'medicamentos')")
conn.execute("INSERT INTO productos VALUES(39,'Aciflux Tabletas (20 Comprimidos)',26300,'Tratamiento de úlceras esofágicas, gástricas y duodenales.','https://cdn.shopify.com/s/files/1/1782/2391/products/ACIFLUX-TABLETAS.jpg?v=1616288236',100,'medicamentos')")

conn.execute("INSERT INTO productos VALUES(40,'Moquillo y parvovirosis',18800,'Para perros cachorros','https://www.zooplus.es/magazine/wp-content/uploads/2019/02/accesorios-para-perros-768x512.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(41,'Hepatitis infecciosa',32100,'Aplicar de 6-8 semanas','http://doggysvet.com/wp-content/uploads/2016/11/vacunacion-perro-doggysvet.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(42,'Moquillo (panleucopenia)',27000,'Aplicar a los 6 meses de edad','https://segurossura.com/content/uploads/sites/10/2022/03/seguros-sura-decide-accesorios-mascotas.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(43,'Tos de las perreras',25000,'Aplicar alrededor de las 6 semanas','https://www.dogtorscat.com/wp-content/uploads/2019/08/%C3%A1rticulo-3.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(44,'Gripe felina',45200,'Aplicar de 6-12 semanas','https://mivet.com/hubfs/shutterstock_1773921254.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(45,'Leucemia felina (leucosis)',44800,'Aplicar de 6-12 semanas','https://www.petdarling.com/wp-content/uploads/2014/05/accesorios-para-gatos.jpg',100,'accesorios')")
conn.execute("INSERT INTO productos VALUES(46,'Peritonitis infecciosa felina (PIF)',32800,'Aplicar apartir de 1 año','https://www.cuidandotumascota.com/blog/posts/que-accesorios-debe-tener-tu-gato/1.jpg',100,'accesorios')")



conn.commit()

#debemos cerrar la conexion a la base de datos
conn.close()

