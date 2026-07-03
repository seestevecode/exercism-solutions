pub type Approval {
  Yes
  No
  Maybe
}

pub type Cuisine {
  Korean
  Turkish
}

pub type Genre {
  Crime
  Horror
  Romance
  Thriller
}

pub type Activity {
  BoardGame
  Chill
  Movie(Genre)
  Restaurant(Cuisine)
  Walk(Int)
}

pub fn rate_activity(activity: Activity) -> Approval {
  case activity {
    Movie(Romance) | Restaurant(Korean) -> Yes
    Restaurant(Turkish) -> Maybe
    Walk(dist_km) if dist_km > 11 -> Yes
    Walk(dist_km) if dist_km > 6 -> Maybe
    _ -> No
  }
}
