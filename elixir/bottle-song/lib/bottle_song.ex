defmodule BottleSong do
  @moduledoc """
  Handles lyrics of the popular children song: Ten Green Bottles
  """

  @numbers %{2 => "two", 3 => "three", 4 => "four", 5 => "five",
             6 => "six", 7 => "seven", 8 => "eight", 9 => "nine", 10 => "ten"}

  @spec recite(pos_integer, pos_integer) :: String.t()
  def recite(start_bottle, take_down) do
    finish_bottle = start_bottle - take_down + 1
    start_bottle..finish_bottle//-1 
    |> Enum.map(&recite_verse/1) 
    |> Enum.join("\n") 
    |> String.trim()
  end

  defp recite_verse(verse_num) do
    bottle_string = bottles(verse_num)
    fallen_bottle_string = bottles(verse_num - 1)
    
    """
    #{String.capitalize(bottle_string)} hanging on the wall,
    #{String.capitalize(bottle_string)} hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be #{fallen_bottle_string} hanging on the wall.
    """
  end

  defp bottles(0), do: "no green bottles"
  defp bottles(1), do: "one green bottle"
  defp bottles(n) when n >= 2 and n <= 10, do: "#{@numbers[n]} green bottles"
end
