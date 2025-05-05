CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog

CREATE TABLE size_of_dogs AS
  SELECT dogs.name, sizes.size
    FROM dogs, sizes
   WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent

CREATE TABLE by_parent_height AS
  SELECT child
    FROM parents
         JOIN dogs ON parents.parent = dogs.name
   ORDER BY dogs.height DESC;

-- Filling out this helper table is optional

CREATE TABLE siblings AS
  SELECT
    CASE WHEN c1.child < c2.child THEN c1.child ELSE c2.child END AS sib1,
    CASE WHEN c1.child < c2.child THEN c2.child ELSE c1.child END AS sib2,
    c1.parent
  FROM parents AS c1
  JOIN parents AS c2
    ON c1.parent = c2.parent AND c1.child < c2.child;

-- Sentences about siblings that are the same size

CREATE TABLE sentences AS
  SELECT
    "The two siblings, " || siblings.sib1 || " plus " || siblings.sib2 ||
    " have the same size: " || size_of_dogs.size AS sentence
  FROM siblings
  JOIN size_of_dogs AS s1 ON siblings.sib1 = s1.name
  JOIN size_of_dogs AS s2 ON siblings.sib2 = s2.name
  WHERE s1.size = s2.size;

