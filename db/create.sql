DROP TABLE IF EXISTS furniture;
DROP TABLE IF EXISTS component;


CREATE TABLE furniture (
	id INTEGER PRIMARY KEY,
	category TEXT NOT NULL,
	name TEXT UNIQUE NOT NULL,
	color TEXT NOT NULL,
	location TEXT NOT NULL,
	material TEXT NOT NULL,
	width INTEGER NOT NULL,
	height INTEGER NOT NULL
);


CREATE TABLE component (
	id INTEGER PRIMARY KEY,
	furniture_id INTEGER,
	name TEXT UNIQUE NOT NULL,
	price INTEGER NOT NULL,
	FOREIGN KEY(furniture_id) REFERENCES furniture(id)
);

-- Insert into component
insert into Component (id, furniture_id, name, price) values (1, 1, 'Flurazepam Hydrochloride', 1);
insert into Component (id, furniture_id, name, price) values (2, 1, 'SILICEA', 2);
insert into Component (id, furniture_id, name, price) values (3, 1, 'ARSENIC TRIOXIDE', 3);
insert into Component (id, furniture_id, name, price) values (4, 2, 'Methylphenidate Hydrochloride', 4);
insert into Component (id, furniture_id, name, price) values (5, 2, 'GRANISETRON HYDROCHLORIDE', 5);

-- Insert into furniture
insert into Furniture (id, category, name, color, location, material, width, height) values (1, 'chair', 'Omeprazole', 'Purple', 'Beloyarskiy', 'Vinyl', 1, 1);
insert into Furniture (id, category, name, color, location, material, width, height) values (2, 'chair', 'Salicylic Acid', 'Red', 'Sakaidechō', 'Aluminum', 2, 2);
insert into Furniture (id, category, name, color, location, material, width, height) values (3, 'chair', 'DEXTROMETHORPHAN', 'Blue', 'Tapada das Mercês', 'Steel', 3, 3);
insert into Furniture (id, category, name, color, location, material, width, height) values (4, 'chair', 'TRAMETES', 'Teal', 'Hässelby', 'Aluminum', 4, 4);
insert into Furniture (id, category, name, color, location, material, width, height) values (5, 'chair', 'CEFPODOXIME', 'Khaki', 'Claveria', 'Rubber', 5, 5);
insert into Furniture (id, category, name, color, location, material, width, height) values (6, 'chairNikita', 'CEFPODONikitaXIME', 'Nikita', 'ClaveriaNikita', 'Nikita', 6, 6);
