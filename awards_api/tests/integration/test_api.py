

def test_awards_list(client_app, award_factory):
    award_factory.create_batch(size=10)
    response = client_app.get("/api/awards/")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_awards_post(client_app, movie_factory):
    movie = movie_factory()
    response = client_app.post("/api/awards/", json={"year": 2022, "movie_id": movie.id, "winner": True})
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") is not None
    assert data.get("movie", {}).get("id") == movie.id


def test_awards_put(client_app, award_factory, movie_factory):
    award = award_factory(year=1990, winner=False)
    movie = movie_factory()
    data = {"year": 2022, "movie_id": movie.id, "winner": True}
    response = client_app.put(f"/api/awards/{award.id}", json=data)
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == award.id
    assert data.get("year") == data.get("year")
    assert data.get("winner") == data.get("winner")
    assert data.get("movie", {}).get("id") == movie.id


def test_winner_route(client_app):
    response = client_app.get("/api/awards/winners/")
    assert response.status_code == 200
    assert response.json() == {"min": [], "max": []}


def test_winner_route_a(client_app, producer_factory, award_factory):
    producer_1 = producer_factory()
    producer_2 = producer_factory()

    award_factory(movie__producers=[producer_1], year=1980, winner=True)
    award_factory(movie__producers=[producer_1], year=1982, winner=True)
    award_factory(movie__producers=[producer_1, producer_2], year=1983, winner=True)
    award_factory(movie__producers=[producer_1], year=1985, winner=True)
    award_factory(movie__producers=[producer_1], year=1988, winner=True)

    award_factory(movie__producers=[producer_2], year=1978, winner=True)
    award_factory(movie__producers=[producer_factory()], year=1979, winner=True)
    award_factory(movie__producers=[producer_2, producer_factory()], year=1984, winner=True)
    award_factory(movie__producers=[producer_2, producer_1], year=1990, winner=True)

    response = client_app.get("/api/awards/winners/")
    assert response.status_code == 200
    assert response.json() == {
        "min": [
            {
                "producer": "Producer 1",
                "interval": 1,
                "previousWin": 1982,
                "followingWin": 1983
            },
            {
                "producer": "Producer 2",
                "interval": 1,
                "previousWin": 1983,
                "followingWin": 1984
            }
            ],
        "max": [
            {
                "producer": "Producer 2",
                "interval": 6,
                "previousWin": 1984,
                "followingWin": 1990
            }
        ]
    }
