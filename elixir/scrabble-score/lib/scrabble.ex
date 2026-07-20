defmodule Scrabble do
  @doc """
  Calculate the scrabble score for the word.
  """

  @spec score(String.t()) :: non_neg_integer
  def score(word), do:
    word
    |> String.upcase()
    |> to_charlist()
    |> Enum.map(&score_letter/1)
    |> Enum.sum()

  defp score_letter(letter) when letter in ~c"AEIOULNRST", do: 1
  defp score_letter(letter) when letter in ~c"DG", do: 2
  defp score_letter(letter) when letter in ~c"BCMP", do: 3
  defp score_letter(letter) when letter in ~c"FHVWY", do: 4
  defp score_letter(letter) when letter in ~c"K", do: 5
  defp score_letter(letter) when letter in ~c"JX", do: 8
  defp score_letter(letter) when letter in ~c"QZ", do: 10
  defp score_letter(_letter), do: 0
end
