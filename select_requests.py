import sqlalchemy

engine = sqlalchemy.create_engine(
    'postgresql+psycopg2://py48user1:12345@localhost:5432/py48db1'
)
connection = engine.connect()
print(engine)


def select_name_year():
    sel = connection.execute("""SELECT name, year_of_release FROM albums
    WHERE year_of_release BETWEEN '2018-01-01' AND '2018-12-31';
    """).fetchmany(10)
    print(sel)


def select_name_duration_max():
    sel = connection.execute("""SELECT name, duration FROM tracks
    WHERE duration = (SELECT MAX(duration) FROM tracks);
    """).fetchmany(10)
    print(sel)


def select_name_duration_nevertheless():
    sel = connection.execute("""SELECT name, duration FROM tracks
    WHERE duration > 3.5;
    """).fetchmany(10)
    print(sel)


def select_name_collection_():
    sel = connection.execute("""SELECT name FROM collections
    WHERE collection_release_year BETWEEN 2018 AND 2020;
    """).fetchmany(10)
    print(sel)


def select_performers_name_1():
    sel = connection.execute("""SELECT name FROM performers
    WHERE NOT name LIKE '%% %%';
    """).fetchmany(10)
    print(sel)


def select_name_track_my():
    sel = connection.execute("""SELECT name FROM tracks
    WHERE LOWER(name) LIKE '%%my%%';
    """).fetchmany(10)
    print(sel)


select_name_year()
select_name_duration_max()
select_name_duration_nevertheless()
select_name_collection_()
select_performers_name_1()
select_name_track_my()
