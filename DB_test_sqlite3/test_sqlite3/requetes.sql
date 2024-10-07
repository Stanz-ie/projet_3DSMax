-- SQLite

/*
CREATE TABLE assets (
    project VARCHAR(100),
    asset_name VARCHAR(150),
    task VARCHAR(50),
    scene_name VARCHAR(150),
    path TEXT,
    status VARCHAR(10)
    
);
*/

/*
INSERT INTO assets (
    project,
    asset_name,
    task,
    scene_name,
    status
) VALUES (
    "La_symphonie_des_bananes",
    "banane_bleue",
    "shading",
    "banane_bleue_shading_001.max",
    "to_check"
);
*/

/*
DELETE FROM assets
WHERE project = "La symphonie des bananes"
*/

/*
UPDATE assets 
SET project = "L'homme_qui_rétrécit"
WHERE project = "L'homme qui rétrécit"
*/

/*
SELECT * FROM assets
*/

/*
SELECT asset_name 
FROM assets
*/

/*
SELECT asset_name 
FROM assets
WHERE status = "to_do"
*/

/*
SELECT *
FROM assets
WHERE status = "WIP"
OR task = "modeling"
AND scene_name = "ours_modeling_001.max"
*/

/*
DROP TABLE IF EXISTS assets
*/
