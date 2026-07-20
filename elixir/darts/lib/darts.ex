defmodule Darts do
  @type position :: {number, number}

  @doc """
  Calculate the score of a single dart hitting a target
  """
  @spec score(position) :: integer
  def score({x, y}) do
    sq_dist = x ** 2 + y ** 2
    cond do
      sq_dist <= 1 -> 10
      sq_dist <= 25 -> 5
      sq_dist <= 100 -> 1
      true -> 0
    end
  end
end
