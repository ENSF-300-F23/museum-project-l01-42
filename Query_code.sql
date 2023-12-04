-- QUERY CODE:
-- Question 1:
SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'museum' AND REFERENCED_TABLE_NAME IS NOT NULL;
-- Explanation: 
-- ART_OBJECT is a kind of parent table and it references the COLLECTION table, the ARTIST table, and the EXHIBITION table using the foreign keys: 
-- CFK, AFK, and EIDFK respectively. Each of these uses obj_ID as a primary key in their table and they all reference obj_ID in ART_OBJECT.
-- Then comes the specification tables that categorize each art object into four tables: STATUE, SCULPTURE, PAINTING, and OTHER. 
-- They each have foreign keys STFK, SCFK, PFK, OFK that use their own obj_ID to reference the ART_OBJECT(obj_ID). Another parent collection is
-- COLLECTIONS and this table is referenced in BORROWED_COLLECTION and PERMANENT_COLLECTION using the foreign keys: BCFK, PCFK respectively. Both of 
-- them use collection_name in COLLECTIONS as a foreign key to refer their primary keys so that is borrowed_from for BORROWED_COLLECTION and 
-- collection_name for PERMANENT_COLLECTION. 

-- Question 2: 
-- A basic retrieval query regarding all the art object created in the Renaissance period.
select title, descript, year_created
from art_object
where epoch='Renaissance';

-- Question 3:
-- An ordered query that displays the title of the art object and the year it was created from oldest to newest
select title, year_created
from art_object
order by year_created asc;

-- Question 4: 
-- A nested query to find the exhibit name, start and end date for when the 'The Statue of Eren' will be showcased
select Ename, start_date, end_date
from exhibition
where exhibit_ID in (
			select exhibit_ID
			from art_object
			where title='The Statue of Eren');
            
-- Query 5: 
-- A query that displays the cost of the Brown Collection by going through the ART_OBJECT table and joining it with the PERMANENT_COLLECTION table. 
select distinct cost
from art_object as AO, permanent_collection as P
where AO.collection_name=P.collection_name and AO.collection_name='Brown Collection';
