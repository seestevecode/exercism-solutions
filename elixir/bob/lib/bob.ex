defmodule Bob do
  @spec hey(String.t()) :: String.t()
  def hey(input) do
    trimmed = String.trim(input)
    cond do
      shouting?(trimmed) and question?(trimmed) -> "Calm down, I know what I'm doing!"
      silence?(trimmed) -> "Fine. Be that way!"
      question?(trimmed) -> "Sure."
      shouting?(trimmed) -> "Whoa, chill out!"
      true -> "Whatever."
    end
  end

  defp shouting?(input), do: String.upcase(input) == input and String.downcase(input) != input

  defp question?(input), do: String.ends_with?(input, "?")

  defp silence?(input), do: String.trim(input) == ""
end
