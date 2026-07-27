defmodule RotationalCipher do  
  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) do
    text 
    |> String.to_charlist()
    |> Enum.map(&rotate_codepoint(&1, shift))
    |> List.to_string()
  end

  defp rotate_codepoint(cp, shift) when cp in ?a..?z, do: ?a + Integer.mod(cp - ?a + shift, 26)
  defp rotate_codepoint(cp, shift) when cp in ?A..?Z, do: ?A + Integer.mod(cp - ?A + shift, 26)
  defp rotate_codepoint(cp, _shift), do: cp
end
