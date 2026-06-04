module RolePlayingGame exposing (Player, castSpell, introduce, revive)


type alias Player =
    { name : Maybe String
    , level : Int
    , health : Int
    , mana : Maybe Int
    }


introduce : Player -> String
introduce { name } =
    Maybe.withDefault "Mighty Magician" name


revive : Player -> Maybe Player
revive player =
    if player.health == 0 then
        if player.level >= 10 then
            Just (Player player.name player.level 100 (Just 100))
        else
            Just (Player player.name player.level 100 Nothing)
    else
        Nothing
        

castSpell : Int -> Player -> ( Player, Int )
castSpell manaCost player =
    case player.mana of
        Just m ->
            if m >= manaCost then
                ( { player | mana = Just (m - manaCost) }, manaCost * 2 )
            else
                ( player, 0 )
        Nothing ->
            ( { player | health = max 0 (player.health - manaCost)}, 0 )
