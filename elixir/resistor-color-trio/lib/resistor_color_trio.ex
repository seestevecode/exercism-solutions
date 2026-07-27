defmodule ResistorColorTrio do
  @bands %{
    black: 0, brown: 1, red: 2, orange: 3, yellow: 4,
    green: 5, blue: 6, violet: 7, grey: 8, white: 9
  }

  @labels %{ gigaohms: 10 ** 9, megaohms: 10 ** 6, kiloohms: 10 ** 3, ohms: 1 }

  @doc """
  Calculate the resistance value in ohms from resistor colors
  """
  @spec label(colors :: [atom]) :: {number, :ohms | :kiloohms | :megaohms | :gigaohms}
  def label([tens, units, exponent | _rest]) do
    actual_ohms = (10 * @bands[tens] + @bands[units]) * Integer.pow(10, @bands[exponent])
    label_atom = label_atom(actual_ohms)
    label_ohms = div(actual_ohms, @labels[label_atom])
    {label_ohms, label_atom}
  end

  defp label_atom(resistance) when resistance > 1_000_000_000, do: :gigaohms
  defp label_atom(resistance) when resistance > 1_000_000, do: :megaohms
  defp label_atom(resistance) when resistance > 1_000, do: :kiloohms
  defp label_atom(_resistance), do: :ohms
end
