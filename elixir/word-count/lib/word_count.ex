defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    sentence
    |> String.downcase()
    |> then(&Regex.scan(~r/[a-z0-9]+(?:'[a-z0-9]+)?/, &1))
    |> Enum.map(fn [word] -> word end)
    |> Enum.frequencies()
  end
end
