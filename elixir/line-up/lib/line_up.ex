defmodule LineUp do
  @doc """
  Formats a full ticket sentence for the given name and number, including
  the person's name, the ordinal form of the number, and fixed descriptive text.
  """
  @spec format(name :: String.t(), number :: pos_integer()) :: String.t()
  def format(name, number) do
    numstr = to_string(number)
    ordinal_suffix =
      cond do
        String.ends_with?(numstr, "1") and not String.ends_with?(numstr, "11") -> "st"
        String.ends_with?(numstr, "2") and not String.ends_with?(numstr, "12") -> "nd"
        String.ends_with?(numstr, "3") and not String.ends_with?(numstr, "13") -> "rd"
        true -> "th"
      end
    "#{name}, you are the #{number}#{ordinal_suffix} customer we serve today. Thank you!"
  end
end
