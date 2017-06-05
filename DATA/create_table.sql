
CREATE TABLE hygdata0(
  "id" int,
  "hip" int,
  "hd" int,
  "hr" int,
  "gl" int,
  "bf" TEXT,
  "proper" TEXT,
  "ra" TEXT,
  "dec" TEXT,
  "dist" real,
  "pmra" TEXT,
  "pmdec" TEXT,
  "rv" TEXT,
  "mag" TEXT,
  "absmag" TEXT,
  "spect" TEXT,
  "ci" TEXT,
  "x" int,
  "y" int,
  "z" int,
  "vx" real,
  "vy" real,
  "vz" real,
  "rarad" TEXT,
  "decrad" TEXT,
  "pmrarad" TEXT,
  "pmdecrad" TEXT,
  "bayer" TEXT,
  "flam" TEXT,
  "con" TEXT,
  "comp" TEXT,
  "comp_primary" TEXT,
  "base" TEXT,
  "lum" TEXT,
  "var" TEXT,
  "var_min" TEXT,
  "var_max" TEXT
);
.mode csv
.import hygdata_v3.csv hygdata0
.tables
.mode column
select * from hygdata0 limit 2 ;
