module MagicianInTraining exposing (..)

import Array exposing (Array)


getCard : Int -> Array Int -> Maybe Int
getCard index deck =
    Array.get index deck


setCard : Int -> Int -> Array Int -> Array Int
setCard index newCard deck =
    Array.set index newCard deck


addCard : Int -> Array Int -> Array Int
addCard newCard deck =
    Array.push newCard deck


removeCard : Int -> Array Int -> Array Int
removeCard index deck =
    if Array.get index deck == Nothing then
        deck
    else
        Array.append 
            (Array.slice 0 index deck) 
            (Array.slice (index + 1) (Array.length deck) deck)


evenCardCount : Array Int -> Int
evenCardCount deck =
    Array.length (Array.filter (\card -> modBy 2 card == 0) deck)
