DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS payment_order;
DROP TABLE IF EXISTS cart_item;
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS component;
DROP TABLE IF EXISTS furniture;

CREATE TABLE furniture (
	id INTEGER PRIMARY KEY,
	category TEXT NOT NULL,
	name TEXT UNIQUE NOT NULL,
	color TEXT NOT NULL,
	location TEXT NOT NULL,
	material TEXT NOT NULL,
	width INTEGER NOT NULL,
	height INTEGER NOT NULL,
	article varchar(64)
);


CREATE TABLE component (
	id INTEGER PRIMARY KEY,
	furniture_id INTEGER,
	product_id INTEGER,
	name TEXT UNIQUE NOT NULL,
	price INTEGER NOT NULL,
	article varchar(64) not null,
	dimension_eu varchar(128),
	dimension_us varchar(128),
	FOREIGN KEY(furniture_id) REFERENCES furniture(id)
);


CREATE TABLE cart (
    id INTEGER PRIMARY KEY autoincrement,
    total_price float
);


CREATE TABLE cart_item (
    id INTEGER PRIMARY KEY autoincrement,
    price float,
    quantity integer,
    cart_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY(cart_id) REFERENCES cart(id),
    FOREIGN KEY(item_id) REFERENCES component(id)
);


CREATE TABLE payment_order (
    id INTEGER PRIMARY KEY autoincrement,
    total_price float,
    name varchar(64),
    surname varchar(64),
    email varchar(64),
    address varchar(256),
    telephone varchar(20)
);

CREATE TABLE order_item (
    id INTEGER PRIMARY KEY autoincrement,
    price float,
    order_id INTEGER,
    cart_item_id INTEGER,
    FOREIGN KEY(order_id) REFERENCES payment_order(id),
    FOREIGN KEY(cart_item_id) REFERENCES cart_item(id)
);


-- Insert into furniture
insert into Furniture (id, category, name, color, location, material, width, height, article) values (1, 'chair', 'Omeprazole', 'Purple', 'Beloyarskiy', 'Vinyl', 1, 1, '502.400.31');
insert into Furniture (id, category, name, color, location, material, width, height, article) values (2, 'chair', 'Salicylic Acid', 'Red', 'Sakaidechō', 'Aluminum', 2, 2, '502.400.32');
insert into Furniture (id, category, name, color, location, material, width, height, article) values (3, 'chair', 'DEXTROMETHORPHAN', 'Blue', 'Tapada das Mercês', 'Steel', 3, 3, '502.400.33');
insert into Furniture (id, category, name, color, location, material, width, height, article) values (4, 'chair', 'TRAMETES', 'Teal', 'Hässelby', 'Aluminum', 4, 4, '502.400.34');
insert into Furniture (id, category, name, color, location, material, width, height, article) values (5, 'chair', 'CEFPODOXIME', 'Khaki', 'Claveria', 'Rubber', 5, 5, '502.400.35');


-- Insert into component
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (1, 1, 100001, 'Allen Key', 3.91, '502.400.31', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (2, 1, 115988, 'Black Base Leveler', 3.41, '502.400.32', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (3, 1, 1106300, 'Cam Lock Nut', 1.21, '502.400.33', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (4, 1, 118331, 'Cam Lock Screw', 7.81, '502.400.34', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (5, 1, 103091, 'Drawel rail', 4.61, '502.400.35', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');

insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (6, 1, 100365, 'Cam Lock Nut Angle Pin', 2.73, '502.400.36', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (7, 1, 113281, 'Drawer Front', 4.91, '502.400.37', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (8, 1, 117793, 'Rod Clip White', 3.62, '502.400.38', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (9, 1, 110525, 'Self Pins', 4.23, '502.400.39', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');
insert into Component (id, furniture_id, product_id, name, price, article, dimension_eu, dimension_us) values (10, 1, 101350, 'Wood Dowel', 4.56, '502.400.31', '0.09 cm (L) x 0.06 cm (W) x 0.0 cm (D)', '0.03 in (L) x 0.02 in (W) x 0.0 in (D)');


insert into cart (id, total_price) values (1, 0.0);
