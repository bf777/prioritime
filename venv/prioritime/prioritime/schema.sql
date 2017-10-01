create table courses_table (
  id integer primary key autoincrement,
  'yearlevel' integer not null,
  'courseno' integer not null,
  'coursename' text not null,
  'whichdays' text not null,
  'classlength' integer not null);
