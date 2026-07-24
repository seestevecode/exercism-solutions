defmodule SumOfMultiples do
  @doc """
  Adds up all numbers from 1 to a given end number that are multiples of the factors provided.
  """
  @spec to(non_neg_integer, [non_neg_integer]) :: non_neg_integer
  def to(limit, factors) do
    factors
    |> Enum.map(fn factor -> if factor == 0, do: [0], else: factor..limit - 1//factor end)
    |> Enum.flat_map(&Enum.to_list/1)
    |> Enum.uniq()
    |> Enum.sum()
  end
end
