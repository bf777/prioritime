drop table if exists courses_table;
create table courses_table (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
