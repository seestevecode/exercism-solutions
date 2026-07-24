defmodule Isogram do
  @doc """
  Determines if a word or sentence is an isogram
  """
  @spec isogram?(String.t()) :: boolean
  def isogram?(sentence) do
    cleaned = sentence |> String.downcase() |> String.replace(~r/[^a-z]/, "")
    String.length(cleaned) == cleaned |> to_charlist() |> MapSet.new() |> MapSet.size()
  end
end
