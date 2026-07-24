defmodule IsbnVerifier do
  @doc """
    Checks if a string is a valid ISBN-10 identifier

    ## Examples

      iex> IsbnVerifier.isbn?("3-598-21507-X")
      true

      iex> IsbnVerifier.isbn?("3-598-2K507-0")
      false

  """
  @spec isbn?(String.t()) :: boolean
  def isbn?(isbn) do
    cleaned = String.replace(isbn, "-", "")
    if Regex.match?(~r/^\d{9}[\dX]$/, cleaned) do
      checksum = 
        cleaned
        |> String.graphemes()
        |> Enum.map(& if &1 == "X", do: 10, else: String.to_integer(&1))
        |> Enum.with_index(fn value, index -> value * (10 - index) end)
        |> Enum.sum()
      rem(checksum, 11) == 0
    else
      :false
    end
  end
end
