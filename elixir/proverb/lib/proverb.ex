defmodule Proverb do
  @doc """
  Generate a proverb from a list of strings.
  """
  @spec recite(strings :: [String.t()]) :: String.t()
  def recite([]), do: ""
  def recite([first | _rest] = strings), do:
    strings
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.map(fn [want, lost] -> "For want of a #{want} the #{lost} was lost.\n" end)
    |> Enum.join()
    |> Kernel.<>("And all for the want of a #{first}.\n")
end
