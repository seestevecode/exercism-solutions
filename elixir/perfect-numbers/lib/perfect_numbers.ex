defmodule PerfectNumbers do
  @doc """
  Determine the aliquot sum of the given `number`, by summing all the factors
  of `number`, aside from `number` itself.

  Based on this sum, classify the number as:

  :perfect if the aliquot sum is equal to `number`
  :abundant if the aliquot sum is greater than `number`
  :deficient if the aliquot sum is less than `number`
  """
  @spec classify(number :: integer) :: {:ok, atom} | {:error, String.t()}
  def classify(1), do: {:ok, :deficient}
  def classify(number) when is_integer(number) and number > 1 do
    aliquot = number |> factors() |> Enum.sum()
    cond do
      number == aliquot -> {:ok, :perfect}
      number < aliquot -> {:ok, :abundant}
      number > aliquot -> {:ok, :deficient}
    end
  end
  def classify(_), do: {:error, "Classification is only possible for natural numbers."}

  defp factors(number), do: 1..number - 1 |> Enum.filter(& rem(number, &1) == 0)
end
