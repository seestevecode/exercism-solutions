defmodule PigLatin do
  @doc """
  Given a `phrase`, translate it a word at a time to Pig Latin.
  """
  @spec translate(phrase :: String.t()) :: String.t()
  def translate(phrase), do:
    phrase |> String.split() |> Enum.map(&translate_word/1) |> Enum.join(" ")

  defp translate_word(word) do
    cond do
      Regex.match?(~r/^[aeiou]|^xr|^yt/, word) -> word <> "ay"
      match_cons_qu = Regex.run(~r/^([^aeiou]*qu)(.*)$/, word) -> rearrange(match_cons_qu)
      match_cons_y = Regex.run(~r/^([^aeiou]+)y(.*)$/, word) -> "y" <> rearrange(match_cons_y)
      match_cons = Regex.run(~r/^([^aeiou]+)(.*)$/, word) -> rearrange(match_cons)
      true -> word
    end
  end

  defp rearrange([_, matched, rest]), do: rest <> matched <> "ay"
end
